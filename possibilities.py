team = ['Red', 'Yellow', 'Orange', 'Green', 'Blue', 'Purple']
procedure = ['Identify', 'Protect', 'Detect', 'Respond', 'Recover']
for color in team:
    for duty in procedure:
        scanner = f'{color} {duty}'
        print(scanner)
