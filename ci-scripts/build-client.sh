#!/usr/bin/env bash

pushd client

npm install

npm run-script build

# Don't run in BG yet -- this may be useless.
## run in bg
#npm start &
#
## this is the server pid
#NPM_SERVER_PID=$!