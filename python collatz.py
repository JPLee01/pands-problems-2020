#John Paul Lee
#Problem Sheet for Week 4 of Programming and Scripting

#ask user to input a positive integer
n = int(input("Please enter a positive integer: "))

#if the current value is even divide it by 2
def collatz(n):
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            yield(n)
#if the current value is odd, mulitiply it by 3 and add 1
        else:
            n = n * 3 + 1
            yield(n)

a = list(collatz(n))
#print the results when the current value is 1
print(n, a)

# References:
# "Control Flow" section of A Whirlwind Tour of Python by Jake Vanderplas.
#https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
#https://www.geeksforgeeks.org/program-to-print-collatz-sequence/
