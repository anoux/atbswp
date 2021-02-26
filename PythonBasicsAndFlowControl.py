# Automate the boring stuff with Python
# FIRST PROGRAM: say hello and ask about me

print ("Hello!")
print ("What's your name?")
myName = input()
print ("It is good to meet you, "+ myName)
print ("The length of your name is:")
print (len(myName))
print ("What is your age?")
myAge = input()
print ("You will be " 
       + str(int (myAge) + 1) 
       + " in a year.")

#%%

city = "Vicente López"
street = "Libertad 4502"

city == "Vicente López" and street == "Libertad 4502"

surname = "Jadur"

#%% IF AND ELIF STATEMENTS

name = "Anoux"

if name == "Anoux":
    print ("Hi Anoux!")
    print ("Wrong name, bitch")

#%% IF AND ELIF STATEMENTS

print ("Type your password")
password = input()
if password == "AJ96":
    print ("acces granted")
else:
    print ("Wrong password")

#%% IF AND ELIF STATEMENTS
name = "Vampire"
age = 500

if name == "Anoux":
    print("Hi Anoux")
elif age > 100:
    print("You are 24, not 25")


#%%
# Falsey values and Trhuthly values. The bool function 
# tells you which is one or other

print(bool(""))
print(bool(" "))
print(bool(0))

#%% WHILE LOOPS --> ejecuta lo que está identado 
# y luego vuelve a la condición. Si sigue siendo True, sigue el loop

spam = 0

while spam < 5:
    print ("Hello World")
    spam = spam + 1

#%% WHILE LOOPS

name = " "

while name != "Lucrecia":
    print ("Type your name")
    name = input()
print ("Thanks")
    
#%% INFINITE LOOPS, condition is always true, so it prints "hey" for ever
while True:    
    print ("Hey")
    break # break stops the infinite loop, so it is executed just once.

#%% FOR LOOPS

print ("My name is")
for i in range(5):
    print ("Anoux " + str(i) + " times")
    
#%% FOR LOOPS looks similar to WHILE LOOPS

print ("My name is")
i = 0
while i < 5:
    print ("Anoux " + str(i) + " times")
    i = i + 1
#%% 

print (range(1000))
print (range(-5))




































    