#John Paul Lee
#Problem Sheet for Week 7 of Programming and Scripting

#open the file in read mode
with open('moby-dick.txt', 'r') as f:

#read all the contents of the file and store it as e_count
    e_count = f.read()

#find the number of "e's" in the file both higher and lower case
#for each "e" character found add to the count
    e = 0
    for i in e_count:
        if(i=='E' or i=='e'):
            e +=1
#print the number of "e's" found in the file
print("The number of e's in this file is", e) 

#references: https://easycodebook.com/python-text-file-program-to-count-vowels/
#https://stackoverflow.com/questions/22694244/counting-specific-letters-or-symbols-in-a-text-file-in-python
#https://docs.python.org/3/tutorial/inputoutput.html