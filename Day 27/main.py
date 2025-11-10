from tkinter import *

window = Tk()
window.title("This is my first GUI project")
window.minsize(500,500)

def change_label() :
    new_text = input_.get()
    my_label.config(text=new_text)

# Label
my_label = Label(text="This is me Satyajit !",font=("Arial",24))
my_label.pack() #expand=True --> get to the center

my_label["text"] = "hello"
my_label.config(text="hell not")

# Entry
input_ = Entry(width=10)
input_.place(x=10,y=100)

# Button
button = Button(command=change_label)
button.config(text="click me")
button.pack()
# button.grid(column=0,row=0) while using the pack we cant use the grid
# this error we occurred _tkinter.TclError: cannot use geometry manager grid inside .
# which already has slaves managed by pack




window.mainloop()
#https://docs.python.org/3/library/tkinter.html#the-packer