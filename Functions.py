# BUILT IN FUNCTIONS
# for example,
# print(), input(), len()
# To use certain functions we need to import certain libraries
# For example....

import random
print (random.randint(0,10))

# You can also import several libreries like this

import random, sys, os, math

# Or import a specific function from a library

from random import randint

# random.exit() doesn't work here

#%%

import pyperclip
# no tenía pyperclip instalado, fui hasta la terminal

pyperclip.copy ("I am Anoux")
print (pyperclip.paste())

#%%
# WRITING YOU OWN FUNCTION

def hello():
    print("H")
    print("E")
    print("L")
    print("L")
    print("O")
#then, to call the function, type __ hello() __
hello()

#%%

def good_morning(name):
    print ("Good morning " + name)
    print ("Did you sleep well?")

good_morning("Anoux")
good_morning("Bruno")

# name is the parameter of the function. Anoux and Bruno are arguments 

#%%

def plus_one (number):
    return number + 1

new_number = plus_one(3)

print (new_number)

#%% 
# The print() function returns "none value"

print ("spoon", "knife", "fork", sep = "JAJA")

#%% GLOBAL AND LOCAL VARIABLES
# SOME RULES
# Code in the global scope cannot use any local variables
# Code in the local scope can access global variables
# Code in one function's local scope cannot use variables 
# in another local scope
# It can be two different local scopes with "same variable"
# (eggs) but different values. First case is "Hello", second is 44.

































