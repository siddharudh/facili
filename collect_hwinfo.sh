#!/bin/bash

cd $(dirname "$0") 

mkdir -p data
sudo lshw -json > data/lshw.json
sudo dmidecode > data/dmidecode.txt
