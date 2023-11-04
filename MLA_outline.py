# MLA Outline Builder
# Variables and Lists
#By Frater Cletus 4 November 2023
roman = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X')
caps = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

# Capture more information
title = input('What is the title of your document? ')
I = input('How many points do you need to convey?(Up to 10 permitted) ')
I = int(I)
i = 1
points = []

while i <= I:
    points_input = input('What is your point? ')
    points.append(points_input)
    i = i + 1
    print(points)
    print()

print('It is recommended that you structure your paragraphs with a logical flow')
print('For example:')
print('- Point of interest, story, or quote')
print('- Extract meaning from the point of interest')
print('- Present your fact')
print('- Tie into the overall argument')
print('PLEASE READ THE ABOVE PARAGRAPH BEFORE PROCEEDING')
print()

S = input('How many structural points do you think you will need? ')
S = int(S)
s = 1
section = []

while s <= S:
    section_input = input('What is the next flow? ')
    section.append(section_input)
    s = s + 1
    print(section)
    print()

arab = input('How many detailed points do you need to make? ')
arab = int(arab)
n = 1  # Initialize n to 1

print('Here is your newly scaffolded outline based on the information you have given')
print(title)

# Output Script
for i in range(I):
    print(roman[i] + '. ' + points[i])

    for s in range(S):
        print('    ' + caps[s] + '. ' + section[s])

        for m in range(arab):
            print(f'        {n}. ')
            n += 1
            print('             a.')
            print('             b.')
            print('             c.')
