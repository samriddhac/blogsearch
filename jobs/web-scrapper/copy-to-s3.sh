#!/bin/bash
cd /home/ubuntu/shared/opt/jobs/scrape/output/images/
aws s3 mv ./ s3://blog-search-png-bucket/ --recursive --include '*' --acl 'public-read'