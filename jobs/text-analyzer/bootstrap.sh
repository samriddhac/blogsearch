#!/bin/bash
sudo apt-get update -y
sudo apt-get install nfs-common -y
sudo apt-get install libfontconfig -y

mkdir tmp
cd tmp
curl -O https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh


