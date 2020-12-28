#!/bin/sh

#
# Starting shell script in helper directory
#
parent_path=$(
  cd "$(dirname "${BASH_SOURCE[0]}")"
  pwd -P
)
cd "$parent_path"
cd ..

VERBOSE="-m"

if [ "$#" -eq "0" ]; then
  sh scenario/receiver/test.sh $VERBOSE
  sh scenario/sender/test.sh $VERBOSE
  sh scenario/proxy/test.sh $VERBOSE
else
  # Default is mute mode
  if [ -z "$2" ]; then
    VERBOSE=""
  else
    VERBOSE=$2
  fi
  sh scenario/$1/test.sh $VERBOSE
fi
