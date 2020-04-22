#!/bin/bash

DIR_NAME=$( dirname "${BASH_SOURCE[0]}" )

SITE_PACKAGES=`cat ~/.site-packages.env`
export PYTHONPATH=$DIR_NAME/src:$SITE_PACKAGES:$PYTHONPATH

python3 cli/Server.py run


