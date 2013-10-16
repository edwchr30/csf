# Name: Chris Edwards
# Evergreen Login: edwchr30
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

import hw2_test

a = 0
for i in range(hw2_test.n):
    a = a + i
print a + hw2_test.n


###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

for b in range(2,10):
    print 1.0/b
    



###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

c = 10
triangular = 0
for i in range(c):
    triangular = triangular + i
triangular = triangular + c
print "Triangular number", c, "via loop:", triangular
print "Triangular number", c, "via formula:", c*(c+1)/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

#Use a for loop to compute 10!, the factorial of 10. Recall that the factorial of n is 1*2*3*...*n.
#The first line of your solution will be n = 10. After that, your solution should not use 10 again, though your solution will use n. In other words, your code (after the n = 10 line) should work for any value of n.
#Hint: Your answer will be similar to your answer to "Problem 3: Triangular numbers".

d = 10
import math
print math.factorial(d)

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

#Write code to print the first 10 factorials, in reverse order. In other words, write code that prints 10!, then prints 9!, then prints 8!, ..., then prints 1!. 
#The first line of your solution should assign a variable numlines to 10, and then the rest of your solution must not use 10 anywhere.
#Use two nested for loops.
#The outer loop sets the value of n to the values numlines, numlines-1, numlines-2, ..., 1, in succession.
#Then, the body of that loop is itself a loop - exactly your solution to Problem 4 without the first line n = 10 that hard-codes the value of n.

e = 10
for i in range(e):
    print math.factorial(e)
    e = e - 1
    

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

#Compute the following value:
#1 + 1/1! + 1/2! + 1/3! + 1/4! + ... + 1/10!
#The value should be close to e (~ 2.71828), the base of the natural logarithms.
#Hint: The easiest way to solve this is with two nested for loops. It is possible, but tricky, to compute this using only one for loop. That is not necessary for this assignment.
#Hint: Copy your solution to "Problem 5: Multiple factorials", then modify it. Rather than printing the factorials, you will add their reciprocals to a running total, then print that total at the end.
#Hint: don't try to work the very first "1 +" into your loop; do it outside the loops (either at the very beginning or the very end of the outer loop).

f = 10
g = 0
h = 0
for i in range(f):
    g = 1.0/math.factorial(f)
    f = f - 1
    h = h + g
print h + 1
    

###
### Collaboration
###

# https://wiki.python.org/moin/
# http://docs.python.org/2.7/
# http://nzmaths.co.nz/resource/triangular-numbers?parent_node=

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
