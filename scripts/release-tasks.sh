#!/usr/bin/env bash

# When a new version is released, perform these tasks to ensure the app runs correctly.

#git checkout -- . # discard changes
git pull || exit 1

# refresh pipenv deps
pipenv install

# install npm deps and build web content
pushd client
npm install
npm build
popd

# restart web api service
systemctl restart bowser-web-api.service