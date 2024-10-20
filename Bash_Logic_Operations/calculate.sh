#!/bin/bash
#input numbers
number1=$1
number2=$2
number3=$3
#the sum of first two numbers
sum=$((number1 + number2)) 
#the product of the sum with the third number
product=$((sum * number3)) 
echo "The sum of $number1 and $number2 is: $sum"
echo "Multiplying the sum by $number3 gives: $product"