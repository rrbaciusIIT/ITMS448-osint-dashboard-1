#!/usr/bin/env bash

pushd bowser

pipenv run coverage run --source=. -m unittest discover

ls -la .coverage

popd