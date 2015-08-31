#!/bin/bash

set -e

python -m unittest discover .

./test_set_trace.sh

flake8 pyrs
