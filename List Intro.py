#list intro
#this program demonstrates how lists work
#for lists, we use square brackets
#items in lists are separated by commas
#string needs to have speech marks around it
names = ["Max", "Noah"]

#to print a list
print(names)

#to print an individual item from a list, we use
# it's index(position on a list)
print(names[0])

#to add something to the end of a list, use append()
names.append("Neko")
print(names)

#to add something in a specific position, use insert()
names.insert(1, "Dr Evil")
print(names)
# lists are mutable(changeable)
# to change a value of an item in a list we just,
# over-write it
names[1] = "Dr Good"
print(names)

# len(lists) returns the number of items on a list
print(len(names))