#!/bin/sh

pushd "$(dirname "$0")" >/dev/null

PYGAME_HIDE_SUPPORT_PROMPT=1 poetry run python -m disco

popd >/dev/null
