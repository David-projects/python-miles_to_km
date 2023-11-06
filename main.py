from tkinter import *

window = Tk()
window.title("Miles to Km")
window.minsize()
window.config(padx=20, pady=20)

#miles to km function
def miles_to_km():
    miles = float(mile_input.get())
    km = round(miles * 1.6, 2)
    km_display_label.config(text=km)

# setup grid
mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

km_equal_to_label = Label(text="is equal to")
km_equal_to_label.grid(column=0, row=1)

km_display_label = Label(text=0)
km_display_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

buttom = Button(text="submit", command=miles_to_km)
buttom.grid(column=1, row=2)



window.mainloop()