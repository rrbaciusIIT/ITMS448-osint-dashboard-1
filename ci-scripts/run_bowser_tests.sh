#!/usr/bin/env bash

cd bowser

pipenv run coverage run --source=. -m unittest discover

ls -la .coverage