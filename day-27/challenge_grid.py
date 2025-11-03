from tkinter import *

window = Tk()
window.title("This is my first GUI project")
window.minsize(500,300)
window.config(padx=200,pady=80)

# Label
my_label = Label(text="This !",font=("Arial",24))
my_label.grid(column=0,row=0)
my_label.config(pady=10,padx=10)

# Entry
input_ = Entry(width=10)
input_.grid(row=2,column=3)

# Button
button = Button()
button.config(text="click me")
button.grid(column=1,row=1)

# new Button
new_button = Button()
new_button.config(text="new button")
new_button.grid(column=2,row=0)


window.mainloop()