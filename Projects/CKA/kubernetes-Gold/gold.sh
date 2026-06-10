#!/usr/bin/env bash

# Make sure we are in the directory of the script
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"

# Run python CLI
python3 "${DIR}/gold.py" "$@"
