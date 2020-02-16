#John Paul Lee
#Problem Sheet for Week 5 of Programming and Scripting

#import datetime to calaulate the date
import datetime

#have now = todays date
now = datetime.datetime.now()

#have n = what day of the week it is
n = datetime.datetime.today().weekday()

#if it is a weekday print Yes, unfortunately today is a weekday
if n <= 4:
    print("Yes, unfortunately today is a weekday")

#if it is the weekend print It is the weekend, yay!
else:
    print("It is the weekend, yay!")

