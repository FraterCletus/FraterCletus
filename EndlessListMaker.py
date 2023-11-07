#This listmaker is rudimentary and will help build more complex code.
#It does not end. Ever. So as long as you have entries to make it will take them.
section = []
a = 0
b = 1
while a <= b:
    entry = input('Enter a string: ')
    section.append(entry)
    print(section)#Prints list contents
    print(len(section))#Prints number of items on list
