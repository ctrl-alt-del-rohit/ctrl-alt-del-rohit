from tkinter import *
from datetime import date

def calculate_age():
    birth_year = int(input_field.get())
    current_year = date.today().year
    age = current_year - birth_year
    age_label.config(text=f"Your age is {age} years.")

win = Tk()
win.title("Age Calculator")
win.geometry('400x280')
win.resizable(0, 0)

canvas = Canvas(win, width=150, height=30, bg="green")
canvas.create_text(70, 15, text="Enter birth year", font=("Arial Bold", 13, "bold"))
canvas.pack(side=TOP)

input_field = Entry(win, font=("Microsoft Sans Serif", 18), width=10, justify=LEFT)
input_field.pack(pady=10)
input_field.focus()

age_button = Button(win, text="Age", width=35, height=2, font=("Arial", 12, "bold"), command=calculate_age)
age_button.pack(pady=10)

age_label = Label(win, text="", font=("Arial", 14, "bold"), fg="green")
age_label.pack(pady=10)

input_field.bind('<Return>', lambda event: calculate_age())

win.mainloop()
