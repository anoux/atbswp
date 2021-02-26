# A list is a value that contains values ("items"). It has a sequence, an order
# You use commas to separate the values inside and brackets to delimite the list
# It is like a variable. You can access different items inside the list

salad = ["lettuce", "tomato", "carrot", "avocado", "lemon", "olive oil"]

print(salad)

print(salad[0])

# Also a list can contains two or more list inside
# Separate them with commas, and use another pairs of brackets to delimite them

double_list = [["cat", "dog", "hamster"], [10, 20, 30]]

#then, you need two indexes to acces one element

print(double_list) #gives all the list

print(double_list[0]) #gives the first list inside "double_list", if 1, gives the second

print(double_list[0][1]) #gives the second element of the first list and so on.

# NEGATIVE INDEXES --> goes backwards

print(salad[-1]) # -1 gives the last item of the list

print(double_list[-1][-1])

print("The " + salad[-5] + " is the unique fruit in the salad")
#  salad[-5] is the same that salad[1]

#SLICES: it has two indexes inside.

print(salad[0:3]) #gives items 0,1,2 of the list. NOT 3

# Also you can change items inside the list like the following

salad[0] = "meat" #should change "lettuce" for "meat

print(salad)

# and if you use slices, then it changes s




























