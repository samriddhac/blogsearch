const cheerio = require("cheerio");
const request = require("tinyreq");
const _ = require('lodash');
const uuidv5 = require('uuid/v5');
const webshot = require('webshot');

var numRequest = 0;

module.exports = {
	scrapeSite: async function(index, url, exclusionPattern, pageIndexTextItems, int_min, int_max, outputPath, successCallBack, errCallback) {
		try {
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
			pageIndexTextItem =  {
				blog_index:index,
				page_index:url.trim(),
				page_uuid:pageUUID,
				text_paragraph:textContentPara,
				text_small:textContentSmall,
				text_links:textContentLinks
			};
			pageIndexTextItems.push(pageIndexTextItem);
			takeWebShot(pageUUID,url, outputPath);
			let filteredLinks = filterLinks(links, url, exclusionPattern);
			if(filteredLinks!==undefined && filteredLinks!==null && filteredLinks.length>0) {
				for(let i=0; i<filteredLinks.length; i++) {
					let pageLink = filteredLinks[i];
					await scrapePages(index, url, pageLink, exclusionPattern, pageIndexTextItems, int_min, int_max, outputPath);
				}
			}
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

async function scrapePages(index, url, pageLink, exclusionPattern, pageIndexTextItems, int_min, int_max, outputPath) {
	let isEligible = isEligibleForScrape(pageLink, pageIndexTextItems);
	if(isEligible === true) {
		try {
			if(pageLink!==undefined && pageLink!==null && isURL(pageLink) === true) {
				console.log('Scraping page ', pageLink, ' numRequest ',numRequest);
				if(numRequest%10 == 0 ) {
					await sleep(getRandomInt(int_max,(Number(int_max)+20))*100);
				}
				else {
					await sleep(getRandomInt(int_min,(Number(int_min)+10))*100);
				}
				let body = await request(pageLink);
				numRequest++;
				let $ = cheerio.load(body);
				let links = [];
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
				takeWebShot(pageUUID,pageLink, outputPath);
				let filteredLinks = filterLinks(links, url, exclusionPattern);
				if(filteredLinks!==undefined && filteredLinks!==null && filteredLinks.length>0) {
					for(let i=0; i<filteredLinks.length; i++) {
						let nestedPageLink = filteredLinks[i];
						await scrapePages(index, url, nestedPageLink, exclusionPattern, pageIndexTextItems, int_min, int_max, outputPath);
					}
				}
			}
		}
		catch(e) {
			console.error('Execution failed with error ', e);
		}
	}

}

function takeWebShot(uuid, url, outputPath){
	webshot(url, outputPath+uuid+'.png', function(err) {
		if(err!==undefined && err!==null) {
			console.log('Webshot error ',err);
		}
	});
}

function isEligibleForScrape(pageLink, pageIndexTextItems) {
	let isEligible = true;
	let item = _.find(pageIndexTextItems, {page_index:pageLink});
	if(item!==undefined && item!==null) {
		isEligible = false;
	}
	return isEligible;
}

function textContentsParagraph(Jquery){
	let output = '';
	let pText = Jquery('p').contents().text();
	if(pText!==undefined && pText!==null) {
		pText = pText.trim();
	}
	output = pText;
	return output;
}

function textContentsSpan(Jquery){
	let output = '';
	let spanText = Jquery('span').contents().text();
	if(spanText!==undefined && spanText!==null) {
		spanText = spanText.trim();
	}
	output = spanText;
	return output;
}

function textContentsLinks(Jquery){
	let output = '';
	let aText = Jquery('a').contents().text();
	if(aText!==undefined && aText!==null) {
		aText = aText.trim();
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
  	sleep = 40000;
  }
  console.log('Sleep time ', (sleep/1000));
  return new Promise(resolve => setTimeout(resolve, sleep));
}

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}