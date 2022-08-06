#!/usr/bin/python

"""
This script is designed in order to filter commit messages BEFORE creating a commit
according to specified pattern (i.e. regexp).
"""

import re
import sys

green_color = "\033[1;32m"
red_color = "\033[1;31m"
color_off = "\033[0m"
blue_color = "\033[1;34m"
yellow_color = "\033[1;33m"

commit_msg_filepath = sys.argv[1]

regex = r"Add: |Created: |Fix: |Update: |Rework:"
error_msg = "Commit message format must match regex " + regex

with open(commit_msg_filepath, "r+") as file:
    commit_msg = file.read()
    if re.search(regex, commit_msg):
        print(green_color + "Good Commit!" + color_off)
    else:
        print(red_color + "Bad commit " + blue_color + commit_msg)
        print(yellow_color + error_msg)
        sys.exit(1)