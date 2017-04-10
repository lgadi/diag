#!/bin/sh
export PYTHONPATH=`pwd`
echo $PYTHONPATH
nodemon --exec "python " -w ./server server/main.py 