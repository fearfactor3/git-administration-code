#!/usr/bin/python

import sys, re
from subprocess import check_output

branch = (check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode("utf-8").strip())
regex = r"^(develop|main|release|((feature|task|bugfix|hotfix)\/SRE+(-|_)[0-9]+(-|_).+))$"

found_obj = re.match(regex, branch)

if found_obj:
    if len(branch) > 35:
        print(f"Your branch name: {branch} is too long.")
        print(f"Please keep your branchname to under 35 characters.")
        sys.exit(1)
    else:
        print(f"The branch name fits within Local Cloud SRE team naming standards.")
        print(f"Accepting your branch name into remote git repo once you run the following git command below.")
        print(f"git push origin {branch}")
        sys.exit(0)
else:
    print(f"Your commit was rejected due to branching name does meet our team naming standards.")
    print(f"Please rename your branch with {regex} syntax.")
    print(f"To rename your branch, run the following git command below.")
    print(f"git branch -m <new_name> e.g feature/SRE-0000-Somework, task/SRE-0000-Somework, bugfix/SRE-0000-Somework, hotfix/SRE-0000-Somework")
    sys.exit(1)