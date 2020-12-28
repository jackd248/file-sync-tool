#!/bin/sh
#
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

# Cleaning up files
rm -rf ../files/www1/dir1/*
rm -rf ../files/www1/dir2/*
rm -rf ../files/www2/dir1/*
rm -rf ../files/www2/dir2/*
