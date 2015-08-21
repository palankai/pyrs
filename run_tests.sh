#!/bin/bash

set -e

python -m unittest discover pyrs

./test_set_trace.sh

flake8 pyrs
