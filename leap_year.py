#CS 362 HW 3 Question 4
#Jacob Gillette
#1/29/21

print("Enter a year to check whether it is a leap year or not")
#Get user input
user_in = input()

#type cast into integer
user_in = int(user_in)

if user_in % 4 == 0:
    if user_in % 100 == 0:
        if user_in % 400 == 0:
            print("{0} is a leap year!".format(user_in))
        else:
            print("{0} is not a leap year!".format(user_in))
    else:
        print("{0} is a leap year!".format(user_in))
else:
    print("{0} is not a leap year!".format(user_in))
