#!/usr/bin/env bash

pushd bowser

output=$(pipenv run coverage run --source=. -m unittest discover 2>&1)


if grep -q FAILED "${output}"; then
    echo "FAILED in output!"
    exit 1
fi

ls -la .coverage

popd