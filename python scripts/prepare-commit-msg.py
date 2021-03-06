#!/usr/bin/python

import sys, subprocess

commitMessage = sys.argv[1]
jiraTicket = subprocess.Popen("git rev-parse --abbrev-ref HEAD | grep -Eo '(\w+[-])?[0-9]+' | tr \"[lower:]\" \"[:upper:]\"", shell=True, stdout=subprocess.PIPE).stdout.read().strip().decode('utf-8')

with open(commitMessage, "+r") as f:
    commitMsg = f.read()
    f.seek(0,0) # correctly positions issue_number when writing commit message
    f.write(f"[{jiraTicket}] {commitMsg}")