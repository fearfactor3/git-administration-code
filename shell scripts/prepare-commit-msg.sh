#!/bin/sh

MESSAGE=$(cat $1)
TICKET=[$(git rev-parse --abbrev-ref HEAD | grep -Eo '^(\w+/)?(\w+[-_])?[0-9]+' | grep -Eo '(\w+[-])?[0-9]+' | tr "[:lower:]" "[:upper:]")]

if [[ "$MESSAGE" == *"$TICKET"* ]]; then
    echo "Ticket found in commit message.  Skipping..."
    exit 0
fi

echo "$TICKET $MESSAGE" > $1 