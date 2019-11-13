#!/usr/bin/env bash

pushd bowser

IFS=
output=$(pipenv run coverage run --source=. -m unittest discover 2>&1)

echo $output

if echo "${output}" | grep -q FAILED; then
    echo "FAILED in output!"
    exit 1
fi

ls -la .coverage

popd