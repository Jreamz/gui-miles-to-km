from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=250)
window.config(padx=50, pady=50)


def button_calc():
    gui_conversion["text"] = round((int(input.get()) * 1.609), 2)

#Label
gui_miles = Label(text="Miles", font=("Arial", 14))
gui_miles.grid(column=2, row=0)

gui_text_equal = Label(text="is equal to", font=("Arial", 14))
gui_text_equal.grid(column=0, row=1)

#
gui_text_km = Label(text="Km", font=("Arial", 14))
gui_text_km.grid(column=2, row=1)

#text answer appears after input and calculate
gui_conversion = Label(font=("Arial", 14))
gui_conversion.grid(column=1, row=1)

#calculate button
button_one = Button(text="Calculate", command=button_calc)
button_one.grid(column=1, row=2)

#User entry input
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()
