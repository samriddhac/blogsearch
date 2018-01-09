const fs = require('fs');
const csvWriter = require('csv-write-stream');

module.exports = {

	writeCSVData: function(pageIndexTextItems, outputPath, blogIndex){
		if(pageIndexTextItems!==undefined && pageIndexTextItems!==null && pageIndexTextItems.length>0) {
    		let writer = csvWriter({sendHeaders: false});
    		writer.pipe(fs.createWriteStream(outputPath+'output_'+blogIndex+'.csv', {flags: 'a'}));
    		pageIndexTextItems.forEach((item)=>{
    			writer.write(item);
    		});
    		writer.end();
    	}
	}
}

