#!/usr/bin/env bash

# When a new version is released, perform these tasks to ensure the app runs correctly.

git checkout -- . # discard changes
git pull

# refresh pipenv deps
pipenv install

# install npm deps and build web content
pushd client
npm install
npm build
popd