from tkinter import *
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)  # Update every 1 second (1000 milliseconds)

win = Tk()
win.title("Digital Clock")

clock_label = Label(win, font=("Arial", 40), fg="blue", bg="white")
clock_label.pack(padx=20, pady=20)

update_clock()  # Start the clock update loop

win.mainloop()
