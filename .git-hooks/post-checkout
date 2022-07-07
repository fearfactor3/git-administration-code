#!/usr/bin/python

import os, sys, subprocess

dirpath=".git-hooks"

for file in os.listdir(dirpath):
    path = os.path.join(dirpath, file)
    os.chmod(path, 0o755)

# Change to directory where git-hooks are stored and execute shell script there.
os.chdir(dirpath)
print("Activiting git-hooks for repo now.")
subprocess.call(['sh', './install_hooks.sh'])