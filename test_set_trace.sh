#!/bin/bash

set -e

set_trace_count=`grep -rIn --exclude-dir=\.bzr --exclude-dir=\.git --exclude-dir=\.hg --exclude-dir=\.svn --exclude=tags --exclude-dir=build --exclude-dir=dist --include=*.py  "db\.set_trace()" . | wc -l`
if [ $set_trace_count -ne 0 ]; then
    grep -rIn --exclude-dir=\.bzr --exclude-dir=\.git --exclude-dir=\.hg --exclude-dir=\.svn --exclude=tags --exclude-dir=build --exclude-dir=dist --include=*.py  "db\.set_trace()" .
    echo ""
    echo "WARNING pdb.set_trace() was found"
    exit 1
fi
