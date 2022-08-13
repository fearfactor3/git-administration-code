#!/bin/sh

BRANCH=$(git rev-parse --abbrev-ref HEAD)
REGEX="^(develop|main|release|((feature|task|bugfix|hotfix)\/SRE+(-|_)[0-9]+(-|_).+))$"

if [[ ${#BRANCH} -gt 35 ]]; then
    echo "Your branch name: $BRANCH is too long"
    echo "Please keep your branchname to under 35 characters"
    exit 1
fi

if ! [[ $BRANCH =~ $REGEX ]]; then
    echo "Your commit was rejected due to branching name"
    echo "Please rename your branch with $REGEX syntax"
    echo "To rename your name run the following git command below"
    echo "git branch -m <new_name> e.g feature/SRE-0000-Somework, task/SRE-0000-Somework, bugfix/SRE-0000-Somework, hotfix/SRE-0000-Somework"
    exit 1
else
    echo "The branch name fits within"
    echo "Accepting your branch name into remote git repo once you do the following command below"
    echo "git push origin $BRANCH"
    exit 0
fi
