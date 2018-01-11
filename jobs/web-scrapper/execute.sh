#!/bin/bash
cd /home/ubuntu/blogsearch/jobs/web-scrapper
git pull
npm install
chmod 777 execute.sh
rm -rf blogs.csv
wget https://s3-us-west-2.amazonaws.com/blogsearch-csv-bucket/blogs.csv
nohup node index.js blogs.csv /home/ubuntu/shared/opt/jobs/scrape/output/ >> /home/ubuntu/shared/opt/jobs/scrape/logs/scrapelog-`date +%Y%m%d%H%M%S`.log &