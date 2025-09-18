# the traditional way
file = open("text.txt")
content = file.read()
print(content)
file.close() # you need to close the file because it uses the resources.

# modern way

with open("text.txt") as f:
    cont = f.read()
    print(cont)

# you just don't need to close the file because with as can handle it