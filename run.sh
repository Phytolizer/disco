#!/bin/sh

pushd "$(dirname "$0")" >/dev/null

poetry run python -m disco

popd >/dev/null
