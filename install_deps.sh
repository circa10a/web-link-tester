#!/bin/bash
file='./requirements.txt'
if [ -f $file ]; then
  if command -v $(which pip) > /dev/null; then
  $(which pip) install -r $file
  else
    echo "Pip not installed."
    exit 1
  fi
else
  echo "Can't find ${file}"
  exit 1
fi
