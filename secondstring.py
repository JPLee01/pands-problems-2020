#John Paul Lee
#Problem Sheet for Week 3 of Programming and Scripting

#Ask user to input a sentance.
s = str(input("Please enter a sentence: "))

sliced = s[::-1] 
#sliced the sentence in reverse. No input between the colons to allow for unlimited length of sentance.

print(sliced[::2])
#print every second word of the sliced (reversed) sentence .


#how to print evey second word in of the sentence correct order  print(s[0:99:2]).
