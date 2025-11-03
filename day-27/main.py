from tkinter import *

window = Tk()
window.title("This is my first GUI project")
window.minsize(500,500)

# Label
my_label = Label(text="This is me Satyajit !",font=("Arial",24))
my_label.pack() #expand=True

my_label["text"] = "hello"
my_label.config(text="hell not")

# Entry
input_ = Entry(width=10)
input_.pack()

def change_label() :
    new_text = input_.get()
    my_label.config(text=new_text)


# Button
button = Button(command=change_label)
button.config(text="click me")
button.pack()




window.mainloop()
#https://docs.python.org/3/library/tkinter.html#the-packer