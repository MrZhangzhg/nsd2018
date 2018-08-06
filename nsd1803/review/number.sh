#!/bin/bash

read -p "number: " number

if [[ "$number" =~ ^[0-9]+$ ]]; then
    echo "number"
else
    echo "not number"
fi
