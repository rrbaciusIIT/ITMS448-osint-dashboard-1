#!/usr/bin/env bash

if [[ ! -v ${FREEMYIP_TOKEN} ]]; then
    echo "You must set FREEMYIP_TOKEN environment variable!"
    exit 1
fi

curl -v "https://freemyip.com/update?token=${FREEMYIP_TOKEN}&domain=bowser-web-app.freemyip.com"