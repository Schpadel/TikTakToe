user_input = input()
result = ""

for x in user_input:
    if x.isupper():
        result = result + "_" + x.lower()
    else:
        result = result + x

print(result)
