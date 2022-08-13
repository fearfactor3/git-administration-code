#!/usr/bin/bash

pwd=$(pwd);

# Script is designed to be ran from .git-hooks/ dir
if [[ "$pwd" == *".git-hooks"* ]]; then
    files=$(ls | grep -v -e '.*\.');

    while read -r file; do
        chmod +x $file
        ln -s -f ../../.git-hooks/$file ../.git/hooks/
        echo "Linked $file -> ../.git/hooks/$file"
    done <<< "$files";

else
    echo "";
    echo "ERROR: ";
    echo "You must be within the .git-hooks/ dir to run this command";
    exit 1;
fi
