#John Paul Lee
#Problem Sheet for Week 6 of Programming and Scripting
import math 

#ask user to input a positive floating-point number 
n = float(input("Please enter a positive number: "))

# Function which that returns square root of a number with precision upto 5 decimal places 
def Square(n, i, j): 
# 3 inputs; n = user input, i = iteration starting = 1, j = iteration also starting = 1
    mid = (i + j) / 2; 
    mul = mid * mid; 
    # If mid itself is the square root, 
    # return mid 
    if ((mul == n) or (abs(mul - n) < 0.00001)): 
        return mid; 
    # If mul is less than n, recur second half 
    elif (mul < n): 
        return Square(n, mid, j); 
    # Else recur first half 
    else: 
        return Square(n, i, mid); 
# Function to find the square root of n 
def findSqrt(n): 
    i = 1; 
    # While the square root is not found 
    found = False; 
    while (found == False): 
        # If n is a perfect square 
        if (i * i == n): 
            print("The square root of", n, "is approx.", i); 
            found = True; 
        elif (i * i > n): 
            # Square root will lie in the 
            # interval i-1 and i 
            res = Square(n, i - 1, i); 
            print ("The square root of", n, "is approx.", "{0:.5f}".format(res))  
            found = True
        i += 1; 
# Driver code for program 
if __name__ == '__main__': 
    findSqrt(n); 

#The approach to the above is as follows:
#   Start iterating from i = 1. If i * i = n, then print i as n is a perfect square whose square root is i.
#   Else find the smallest i for which i * i is strictly greater than n.
#   Now we know square root of n lies in the interval i – 1 and i and we can use Binary Search algorithm to find the square root.
#   Find mid of i – 1 and i and compare mid * mid with n, with precision upto 5 decimal places.
#       If mid * mid = n then return mid.
#       If mid * mid < n then recur for the second half.
#       If mid * mid > n then recur for the first half.   

# References:
# "Defining and Using Functions" section of A Whirlwind Tour of Python by Jake Vanderplas.
# https://www.geeksforgeeks.org/square-root-of-a-number-without-using-sqrt-function/
# https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf
# https://www.math.upenn.edu/~kazdan/202F09/sqrt.pdf
# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo