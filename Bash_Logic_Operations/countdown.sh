#!/bin/bash
#getting the input number
Number=$1
while [ $Number -gt 0 ]
do
echo "$Number"
Number=$((Number -1))
done
echo "Countdown completed!"