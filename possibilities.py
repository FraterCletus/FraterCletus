#This python list allows you to visually every possible outcome of lists
a = ['a', 'b', 'c', 'd', 'e', 'f']
b = ['1', '2', '3', '4', '5', '6']
c = ['A', 'B', 'C', 'D', 'E', 'F']

for item_a in a: #This nested loop flips through every combination, as opposed to  MLA maker
    for item_b in b:
        for item_c in c:
            print(item_a + '/' + item_b + '/' + item_c)
