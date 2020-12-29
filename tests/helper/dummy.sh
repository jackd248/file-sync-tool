#!/bin/sh
#
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

function randomFileSize {
  echo $((RANDOM%100000000+100000))
}

function createFile {
  # https://stackoverflow.com/a/9800465
  head -c $(randomFileSize) /dev/urandom > ../files/$1/$2/dummy$3.file
}

function createFiles {
  n=0
  while (( $n <= $1 ))
  do
    createFile $2 $3 $n
    n=$(( n+1 ))
  done
}

for i in dir1 dir2
do
  createFiles 20 $1 $i
done