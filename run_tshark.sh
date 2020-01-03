#!/bin/bash

DIRECTORY="data"

if [ ! -d "$DIRECTORY" ]; then
    echo "Created $DIRECTORY"
    mkdir $DIRECTORY
fi

tshark -i wlo1 -w $DIRECTORY/out.pcapng -b duration:30