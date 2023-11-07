my_dict = {}
b = input("How many items are in this dictionary? ")
b = int(b)

for a in range(b):
    key = input("Enter Key: ")
    val = input("Enter Value: ")
    my_dict[key] = val

print("Dictionary:", my_dict)
