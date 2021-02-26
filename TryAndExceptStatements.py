#Try and Except statements

#Example 1
def div42by(divideBy):
    try: 
        return 42/divideBy
    except ZeroDivisionError:
        print("Error:you tried to divide by zero")

print (div42by(2))
print (div42by(12))
print (div42by(0)) 
# Como la división por cero da error, python se enoja y no ejecuta el código que queda por debajo.
#Para evitarlo, puedo usar 'except' statement. Si no aclaro el tipo de error, se aplica a cualquier error que aparezca
print (div42by(1))

#Example 2

def how_many_cats():
    print("How many cats do you have?")
    number = input()
    try:
        if int(number) >= 4:
            print("You have a lot of cats!")
        else:
            print("That is not many cats")
    except ValueError:
        print("Please enter a number, no letters allowed")
#por qué aparece 'None' al final?

print(how_many_cats())