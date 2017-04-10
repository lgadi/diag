#!/bin/sh
export PYTHONPATH=`pwd`
echo $PYTHONPATH
nodemon --exec "python " -w ./client client/main.py 