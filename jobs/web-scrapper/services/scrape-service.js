const cheerio = require("cheerio");
const request = require("tinyreq");
const _ = require('lodash');
const uuidv5 = require('uuid/v5');
const webshot = require('webshot');
const csvWriteService = require('./csv-write-service.js');

var numRequest = 0;
var MAX_RECURSIVE_DEPTH = 20;

module.exports = {
	scrapeSite: async function(index, url, exclusionPattern, pageIndexTextItems, int_min, int_max, outputPath, successCallBack, errCallback) {
		try {
			var visitedLinks = [];
			var maxDepthLinks = [];
			let queuedLinks = [];
			let depth = 1;
			console.log('Scraping page ', url, ' numRequest ',numRequest, ' depth ', depth);
			let body = await request(url);
			numRequest++;
			let $ = cheerio.load(body);
			let links = [];
			$('body').find('a').each(function(i, elem){
				links.push($(elem).attr('href'));
			});
			let pageUUID = uuidv5(url, uuidv5.URL);
			let textContentPara = textContentsParagraph($);
			let textContentSmall = textContentsSpan($);
			let textContentLinks = textContentsLinks($);
			let headerItem =  {
				blog_index:'blog_index',
				page_index:'page_index',
				page_uuid:'page_uuid',
				text_paragraph:'text_paragraph',
				text_small:'text_small',
				text_links:'text_links'
			};
			pageIndexTextItems.push(headerItem);
			pageIndexTextItem =  {
				blog_index:index,
				page_index:url.trim(),
				page_uuid:pageUUID,
				text_paragraph:textContentPara,
				text_small:textContentSmall,
				text_links:textContentLinks
			};
			pageIndexTextItems.push(pageIndexTextItem);
			visitedLinks.push(url.trim());
			queuedLinks.push(url.trim());
			takeWebShot(pageUUID,url, outputPath);
			let filteredLinks = filterLinks(links, url, exclusionPattern);
			queuedLinks.concat(filteredLinks);
			if(filteredLinks!==undefined && filteredLinks!==null && filteredLinks.length>0) {
				await scrapePages(index, url, filteredLinks, exclusionPattern, pageIndexTextItems, visitedLinks, 
						int_min, int_max, outputPath, depth, queuedLinks, maxDepthLinks);
			}
			csvWriteService.writeCSVData(pageIndexTextItems, outputPath, index);
			pageIndexTextItems = [];
			console.log('Total visited links : ', visitedLinks.length);
			console.log('Max depth links : ', maxDepthLinks.length);
			let unvisitedLinks = _.difference(maxDepthLinks,visitedLinks);
			console.log('Un-visited max depth links : ', unvisitedLinks);
			visitedLinks = [];
			maxDepthLinks = [];
			unvisitedLinks = [];
		}
		catch(e) {
			console.error('Execution failed with error ', e);
			if(errCallback!==undefined && errCallback!==null) {
				errCallback(e);
			}
		}
		if(successCallBack!==undefined && successCallBack!==null) {
			successCallBack();
		}
	}
}

async function scrapePages(index, url, filteredLinks, exclusionPattern, pageIndexTextItems, visitedLinks, 
	int_min, int_max, outputPath, depth, queuedLinks, maxDepthLinks) {
	let links = [];
	let currentDepth = depth+1;
	depth = currentDepth; 		
	if(filteredLinks!==undefined && filteredLinks!==null && filteredLinks.length>0) {
		for(let i=0; i<filteredLinks.length; i++) {
			let pageLink = filteredLinks[i];
			let isEligible = isEligibleForScrape(pageLink, visitedLinks);
			if(isEligible === true && currentDepth<=MAX_RECURSIVE_DEPTH) {
				try {
					if(pageLink!==undefined && pageLink!==null && isURL(pageLink) === true) {
						console.log('Scraping page ', pageLink, ' numRequest ',numRequest, ' depth ', depth);
						if(numRequest%10 == 0 ) {
							await sleep(getRandomInt(int_max,(Number(int_max)+20))*100);
						}
						else {
							await sleep(getRandomInt(int_min,(Number(int_min)+10))*100);
						}
						let body = await request(pageLink);
						numRequest++;
						let $ = cheerio.load(body);
						$('body').find('a').each(function(i, elem){
							links.push($(elem).attr('href'));
						});
						let pageUUID = uuidv5(pageLink, uuidv5.URL);
						let textContentPara = textContentsParagraph($);
						let textContentSmall = textContentsSpan($);
						let textContentLinks = textContentsLinks($);
						pageIndexTextItem =  {
							blog_index:index,
							page_index:pageLink.trim(),
							page_uuid:pageUUID,
							text_paragraph:textContentPara,
							text_small:textContentSmall,
							text_links:textContentLinks
						};
						pageIndexTextItems.push(pageIndexTextItem);
						visitedLinks.push(pageLink.trim());
						if(pageIndexTextItems.length > 99) {
							csvWriteService.writeCSVData(pageIndexTextItems, outputPath, index);
							pageIndexTextItems = [];
							console.log('Reached 100 requests , Hence cleaning the memory.');
						}
						takeWebShot(pageUUID,pageLink, outputPath);
					}
				}
				catch(e) {
					console.error('Execution failed with error ', e);
				}
			}
			else {
				if(isEligible === true && currentDepth>MAX_RECURSIVE_DEPTH) {
					if(maxDepthLinks!==undefined && maxDepthLinks!==null) {
						maxDepthLinks.push(pageLink);
					}	
				}
			}
		}
		if(links!==undefined && links!==null && links.length>0) {
			let nestedFilteredLinks = filterLinks(links, url, exclusionPattern);
			if(nestedFilteredLinks!==undefined && nestedFilteredLinks!==null && nestedFilteredLinks.length>0){
				await scrapePages(index, url, nestedFilteredLinks, exclusionPattern, pageIndexTextItems, visitedLinks, 
						int_min, int_max, outputPath, depth, queuedLinks, maxDepthLinks);
			}
		}
	}
}

function takeWebShot(uuid, url, outputPath){
	webshot(url, outputPath+'images/'+uuid+'.png', function(err) {
		if(err!==undefined && err!==null) {
			console.log('Webshot error ',err);
		}
	});
}

function isEligibleForScrape(pageLink, visitedLinks) {
	let isEligible = true;
	if(_.includes(visitedLinks, pageLink)) {
		isEligible = false;
	}
	return isEligible;
}

function textContentsParagraph(Jquery){
	let output = '';
	let pText = Jquery('p').contents().text();
	if(pText!==undefined && pText!==null) {
		pText = pText.trim().replace(/[\r\n]+/g, '\n');
	}
	output = pText;
	return output;
}

function textContentsSpan(Jquery){
	let output = '';
	let spanText = Jquery('span').contents().text();
	if(spanText!==undefined && spanText!==null) {
		spanText = spanText.trim().replace(/[\r\n]+/g, '\n');
	}
	output = spanText;
	return output;
}

function textContentsLinks(Jquery){
	let output = '';
	let aText = Jquery('a').contents().text();
	if(aText!==undefined && aText!==null) {
		aText = aText.trim().replace(/[\r\n]+/g, '\n');
	}
	output = aText;
	return output;
}

function filterLinks(inputLinks, domain, exclusionPattern) {
	let outputLinks = [];
	//Unique filter.
	let uniqueLinks = _.uniq(inputLinks);
	//Same page + Domain filter.
	let exclusionList = exclusionPattern.split('|');
	uniqueLinks.forEach((link)=>{

		if(_.startsWith(link, domain) 
			&& !(link.match(/\.(jpeg|jpg|gif|png|pdf|xls|xlsx|doc|svg|JPEG|JPG|GIF|PNG)$/) != null)){
			outputLinks.push(link.trim());
		}
	});
	if(exclusionList!==undefined && exclusionList!==null && exclusionList.length>0) {
		let delIndex = [];
		outputLinks.forEach((link)=>{
			exclusionList.forEach((pattern)=>{
				if(_.includes(link, pattern)){
					let index = outputLinks.indexOf(link);
					delIndex.push(index);
				}
			});
		});
		if(delIndex!==undefined && delIndex!==null && delIndex.length>0) {
			let uniqueDelIndex = _.uniq(delIndex);
			uniqueDelIndex.forEach((idx)=>{
				delete outputLinks[idx];
			});
		}
		let finalOutput = [];
		outputLinks.forEach((link)=>{
			if(link!==undefined && link!==null) {
				finalOutput.push(link);
			}
		});
		outputLinks = finalOutput;
	}
	return outputLinks;
}

function isURL(str) {
  var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
  '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.?)+[a-z]{2,}|'+ // domain name
  '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
  '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
  '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
  '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
  return pattern.test(str);
}

function sleep(ms) {
  let sleep = ms;
  let sl = (ms/1000);
  if(sl>40) {
  	sleep = 35000;
  }
  console.log('Sleep time ', (sleep/1000));
  return new Promise(resolve => setTimeout(resolve, sleep));
}

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}