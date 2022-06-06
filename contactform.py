from tkinter import *
from tkinter import ttk
from tkinter import messagebox

form = Tk()
form.title("contact form")

form.geometry("400x400")

def bams():
    if g1 == "" and g2 == "" and g3 == "":
        messagebox.showerror("ERROR", "inValid")
    else:
        d1 = open("file.txt", "w")
        t1 = g1.get()
        d1.write(t1)
        t2 = g2.get()
        d1.write(t2)
        t3 = g3.get()
        d1.write(t3)
        print("successful....")


g1 = StringVar()
g2 = StringVar()
g3 = StringVar()

a1 = Entry(form, textvariable=g1, bg="grey").grid(row=1, column=1)
a2 = Entry(form, textvariable=g2, bg="grey").grid(row=2, column=1)
a3 = Entry(form, textvariable=g3, bg="grey").grid(row=3, column=1)
a4 = Label(form, text='First Name').grid(row=1, column=0)
a5 = Label(form, text='Last Name').grid(row=2, column=0)
a6 = Label(form, text='Email Address').grid(row=3, column=0)
a8 = Label(form, text="STATE").grid(row=5, column=0)
state = ("Oyo", "Ogun", "lagos", "Ondo", "Kaduna", "Kano")
box = ttk.Combobox(form, values=state).grid(row=5, column=1)
a7 = Button(form, text="Enter", pady=5, padx=5, bg="grey", command=bams).grid(row=6, column=1)

form.mainloop()
