#John Paul Lee
#Problem Sheet for Week 2 of Programming and Scripting

#Ask user to input their weight in kilograms
weight = float(input("Enter Weight in Kilograms: "))

#Ask user to input thier height in centimeters
height = float(input("Enter Height in Centimeters: "))

#BMI calaculated by dividing weight by height (in meters squared)
BMI = weight / (height/100)**2

#Print the result
print("Your BMI is", BMI)

# References:
# Up to page 9 of of A Whirlwind Tour of Python by Jake Vanderplas.