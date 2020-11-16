"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("Madlib Creator")
nf=Frame()

eoutput1 = StringVar()
eoutput2 = StringVar()
eoutput3 = StringVar()


def clickFunction():
    person = e1.get()
    noun = e2.get()
    event = e3.get()
   
    
    entry1.delete(0,END)
    entry1.insert(0,person)
    entry2.delete(0,END)
    entry2.insert(0,noun)
    entry3.delete(0,END)
    entry3.insert(0,event)
  


l1 = Label(window, text="(person)")
e1 = Entry(window, width=10)
l2 = Label(window, text="is too cool for (noun)")
e2 = Entry(window, width=10)
l4 = Label(window, text="class.")
l5 = Label(window, text="Instead, she/he will be attending the (an event)")
e3 = Entry(window, width=10)

label1=Label(window, text="is too cool for")
label2=Label(window, text="class.")
label3=Label(window, text="Instead, she/he will be attending the")
entry1 = Entry(window, width=10, textvariable=eoutput1)
entry2 = Entry(window, width=10, textvariable=eoutput2)
entry3 = Entry(window, width=10, textvariable=eoutput3)

b1 = Button(window, text="Click to create madlib", command=clickFunction)



l1.grid(row=1,column=1)
e1.grid(row=1,column=2)
l2.grid(row=1,column=3)
e2.grid(row=1, column=4)
l4.grid(row=1, column=5)
l5.grid(row=2, column=1)
e3.grid(row=2, column=2)
b1.grid(row=3, column=2)

entry1.grid(row=4, column=1)
label1.grid(row=4, column=2)
entry2.grid(row=4, column=3)
label2.grid(row=4, column=4)
label3.grid(row=5, column=1)
entry3.grid(row=5, column=2)




mainloop()




