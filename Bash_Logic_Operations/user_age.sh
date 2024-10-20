#!/bin/bash
echo "please enter your age:"
read age
if [ "$age" -lt 18 ]; then 
echo "You are a minor."
elif [ "$age" -ge 18 ] && [ "$age" -lt 65 ]; then 
echo "You are an adult."
else
echo "You are a senior."
fi 