#!/bin/bash
sudo apt-get update -y
sudo apt-get install nfs-common -y
sudo apt-get install libfontconfig -y
sudo apt install awscli -y
mkdir tmp
cd tmp
curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt-get install nodejs
sudo apt-get install build-essential -y
cd ../
git clone https://samriddhac@github.com/samriddhac/blogsearch.git
cd blogsearch/jobs/web-scrapper
chmod 777 *.sh
npm install
mkdir -p /home/ubuntu/shared
sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2 fs-fc378d55.efs.us-west-2.amazonaws.com:/ /home/ubuntu/shared