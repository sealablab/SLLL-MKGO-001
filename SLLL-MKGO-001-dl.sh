#!/bin/bash
##echo "Downloading the x64 mokucli tarball" #Optional
mkdir mokucli
cd mokucli
wget https://download.liquidinstruments.com/software/mokucli/linux/mokucli-linux.tar.gz
tar -zxpf ./mokucli-linux.tar.gz
cd ..
