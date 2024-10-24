Annie = 1997
Jane = 1996

#here are 2 sisters, Annie and Jane, born in 1996 and 1999 respectively.
# They want to know who was born in a leap year. Write an if-else statement to determine who was born in a leap year.

if Annie  % 4 == 0 :
    print("Annie was born in a leap year")
elif Jane % 4 == 0:
    print("Jane was born in a leap year")
else:
    print("None of them were born in a leap year")

# In a school canteen, children under the age of 9 are only given milk porridge for breakfast.
# Children from 10 to 14 are given a sandwich, and children from 15 to 17 are given a burger.
# The canteen master asks the age of the student and gives them breakfast accordingly.
# Sam's age is 10. Use if-else statement to determine what the canteen master will offer to him.

sam_age = 10

if sam_age <= 9:
    print("milk porridge")

elif (sam_age >= 10) and (sam_age <= 14):
    print("sandwich")

elif (sam_age >= 15) and (sam_age <= 17):
    print("hamburger")

else:
    print("you dont receive any food")