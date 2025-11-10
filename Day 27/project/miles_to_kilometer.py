from tkinter import *


window = Tk()
window.minsize(width=400,height=150)
window.title("Mile to Km converter")
window.config(padx=30,pady=20)

# miles entry
miles_input = Entry()
miles_input.grid(row=0,column=1)

# is equal label
equal_label = Label(text="is equal to",font=("Arial",15))
equal_label.config(padx=5,pady=5)
equal_label.grid(row=1,column=0)

# Miles Label
mile_label = Label(text="Miles",font=("Arial",15))
mile_label.config(padx=20,pady=5)
mile_label.grid(row=0,column=2)

# output of KM
output_km = Entry()
output_km.grid(row=1,column=1)
# output_km = Label(text="0",font=("Arial",15))

# km Label
km_label = Label(text="Km",font=("Arial",15))
km_label.config(padx=10,pady=5)
km_label.grid(row=1,column=2)

CONVERSION = 1.60
def calculater():
    miles = miles_input.get()
    km =  float(miles) * CONVERSION
    output_km.insert(END, string=f"{km}")
    # output_km.config(text=f"{km}")

# calculate button
cal = Button(text="calculate")
cal.grid(row=2,column=1)
cal.config(command=calculater)


window.mainloop()