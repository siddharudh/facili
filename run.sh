#!/bin/bash

export FACILI_HOME=$(dirname "$0")
cd $FACILI_HOME/src
./facili-server
