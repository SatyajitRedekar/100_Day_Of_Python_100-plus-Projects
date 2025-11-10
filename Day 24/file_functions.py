with open("func_text.txt", mode="w") as file: # mode mean what you want to perform
                                         # r = read/default, w = write , a = append
    file.write("hi python")

# if file is not available the python will create a new file


with open("func_text.txt", mode="a") as file:
    file.write("\nI am a programmer")

# a will append anything on file not delete

