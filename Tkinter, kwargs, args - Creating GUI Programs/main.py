from tkinter import *
import plaground

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I am a Rebel", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "I am a REBEL"

# Entry

input = Entry(width=10)
input.pack()


# Button

def button_clicked():
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

window.mainloop()
