#!/usr/bin/env bash

# This script will set up the python web api on digitalocean.

pwd
sudo apt update
sudo apt install python3-pip
pip3 install pipenv

cd bowser/
python3 -m pipenv install