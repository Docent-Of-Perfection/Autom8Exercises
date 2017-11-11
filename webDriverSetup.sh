#!/bin/bash
pip3 install selenium &&  wget -O /usr/bin/geckoZip geckodriver-v0.19.1-linux64.tar.gz https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz && cd /usr/bin && tar xvf geckoZip && rm geckoZip
