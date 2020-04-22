#!/bin/bash



SITE_PACKAGES=`cat ~/.site-packages.env`
export PYTHONPATH=./src:$SITE_PACKAGES:$PYTHONPATH

python3 cli/Server.py run


