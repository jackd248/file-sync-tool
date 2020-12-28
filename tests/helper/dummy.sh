#!/bin/sh
#
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

randomFileSize() {
  echo $((RANDOM%100000000))
}

# Creat dummy file
# https://stackoverflow.com/a/9800465
head -c $(randomFileSize) /dev/urandom > ../files/$1/dir1/dummy1.file
head -c $(randomFileSize) /dev/urandom > ../files/$1/dir1/dummy2.file
head -c $(randomFileSize) /dev/urandom > ../files/$1/dir1/dummy3.file
head -c $(randomFileSize) /dev/urandom > ../files/$1/dir2/dummy1.file
head -c $(randomFileSize) /dev/urandom > ../files/$1/dir2/dummy2.file
head -c $(randomFileSize) /dev/urandom > ../files/$1/dir2/dummy3.file

