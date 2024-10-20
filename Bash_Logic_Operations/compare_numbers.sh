#!/bin/bash
#input numbers
number1=$1
number2=$2
#comparing numbers
if [ "$number1" -gt "$number2" ]; then 
  echo "$number1 is greater than $number2."
elif [ "$number1" -lt "$number2" ]; then
echo "$number1 is less than $number2."
else
echo "$number1 is equall to $number2."
fi