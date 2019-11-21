#!/usr/bin/env bash

pushd bowser

pwd

echo "Running all unit tests..."

# Save entire output as string because apparently it won't `exit 1` and trigger Travis to detect that it has failed
IFS=
output=$(pipenv run coverage run --source=. -m unittest discover 2>&1)

echo $output

# If FAILED in output,
if echo "${output}" | grep -q FAILED; then
    echo "FAILED in output!"
    exit 1 # Fail the entire build
fi

ls -la .coverage

popd