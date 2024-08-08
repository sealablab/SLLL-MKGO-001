#!/bin/bash
##echo "## Activating moku conda env"
##conda init
##conda activate moku

export MOKU_CLI_PATH=`pwd`/mokucli
echo "## Setting the mokucli path to: " $MOKU_CLI_PATH

export PATH=$PATH:$MOKU_CLI_PATH
echo "## Listing available moku's with mokucli.."
mokucli list

