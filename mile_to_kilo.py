from tkinter import *


# TODO 6. Miles to km funtion

def calculate_m_to_km():
    miles = float(mile.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


# TODO 1. Creating the window

window = Tk()
# TODO 2. Adding title
window.title("Mile-to-Kilometer")
# TODO 3 Mile Input filed
mile = Entry(width=10)
mile.grid(column=1, row=0)

# TODO 4. Creating the label

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

# TODO 5. Creating the Button

calculate_button = Button(text="Calculate", command=calculate_m_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
