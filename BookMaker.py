contents = ['Security', 'Privacy', 'Compliance']

df = {}
definitions = []

for term in contents:
    define = input(f"Definition of '{term}': ")
    definitions.append(define)

df = dict.fromkeys(contents)
for i, term in enumerate(df):
    df[term] = definitions[i]

print(df)
