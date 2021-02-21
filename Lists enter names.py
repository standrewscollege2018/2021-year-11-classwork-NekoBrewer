#this code will ask the user to enter three names into a list and the prgram will then print the list

names = []
for i in range (0,3):
    name = input("Please enter a name: ")
    names.append(name)
for n in names:
    print(n)
for i in range(len(names)):
    print(i+1, names[i])