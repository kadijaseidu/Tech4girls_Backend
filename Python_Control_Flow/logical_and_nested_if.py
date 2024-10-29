#!/usr/bin/python
#defining two boolean variables
is_student = True
is_employed = False

if is_student and is_employed:
    print("you are a working student.")
elif is_student and not is_employed:
    print("you are a student.")
elif not is_student and is_employed:
    print("you are employed but ot a student.")

#nested if statement for checking age and driver's license
age = int(input("What is your age?"))

if age >= 18:
    my_license = input("do you have a driver's lincense?(Yes/No)").lower()
    if my_license == "yes":
        print("you are allowed to drive.")
    else:
        print("you need a driver's license to drive.")
else:
        print("you are not old enough to drive")
