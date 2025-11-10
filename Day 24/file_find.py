
with open("/Users/satya/OneDrive/Desktop/data.txt") as absolute_file_path :
    content = absolute_file_path.read()
    print(content)

# with open(".../data.txt") as relative_file_path :
#     content = relative_file_path.read()
#     print(content)

# [... are not applicable because of In Python,
# "..." is just a string of three dots, not a path shortcut.
#  Unlike "../" (which means go up one folder), "..." means literally “a folder named ...”.]

with open("../../../Desktop/data.txt") as relative_file_path :
    content = relative_file_path.read()
    print(content)