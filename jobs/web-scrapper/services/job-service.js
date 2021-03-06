const fs = require('fs');
const csv = require('csv-parser');
const scrapeService = require('./scrape-service.js');

module.exports = {
	startJob: async function(inputPath, outputPath) {
		console.log('input path ', inputPath);
		console.log('output path ', outputPath);
		var pageIndexTextItems = [];
		let dataList = [];
		fs.createReadStream(inputPath)
		  .pipe(csv())
		  .on('data', function (data) {
		    console.log('Blog index: %s Blog url: %s', data.blog_index, data.blog_url);
		    dataList.push(data);
		  })
		  .on('end', function() {
		  	console.log('dataList ',dataList);
			if(dataList!==undefined && dataList!==null && dataList.length>0) {
				for(let i=0; i<dataList.length; i++)  {
					let data = dataList[i];
					if(data.execute==='Y') {
						scrapeService.scrapeSite(data.blog_index, data.blog_url, data.exclusion_pattern, pageIndexTextItems,
							data.interval_min, data.interval_max, outputPath, ()=>{
				    	console.log('Job completed with Blog index: %s Blog url: %s', data.blog_index, data.blog_url);
					    }, (err)=>{
					    	console.error('Job failed weith error ', err);
					    });
					}
				}
			}
		  });
	}
}