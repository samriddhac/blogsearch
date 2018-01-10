const jobService = require('./services/job-service.js');

if(process.argv.length<4) {
	console.error("Mandatory arguments CSV file path and Output path is missing.");
	return;
}
else {
	let csvPath = process.argv[2];
	let outputPath = process.argv[3];
	jobService.startJob(csvPath, outputPath);
}
process.on('unhandledRejection', up => { 
	console.error("ERR: Promise rejected ",up);
});
process.on('uncaughtException', function (err) {
  console.error((new Date).toUTCString() + ' uncaughtException:', err.message)
  console.error(err.stack)
  process.exit(1);
});
process.on('exit', (code) => {
  console.log(`About to exit with code: ${code}`);
});