#! /bin/bash

COMMAND=$1

if [[ "$COMMAND" = "move" ]]; then
    python3 ./command.py "move" $2 $3 

elif [[ "$COMMAND" = "status" ]]; then
    python3 ./command.py "status"

elif [[ "$COMMAND" = "end" ]]; then
    python3 ./command.py "end"

else
    echo "Wrong Command"
fi

