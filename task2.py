"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""
import math 
import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("Factoring Trinomials")

eoutput1=StringVar()


def clickFunction():
    b=e2.get()
    c=e3.get()

    a=1
    
    b=int(b)
    c=int(c)

    answer1=((-b)+(math.sqrt((b**2)-(4*a*c))))/(2*a)
    answer2=((-b)-(math.sqrt((b**2)-(4*a*c))))/(2*a)
    if (answer1<0 and answer2<0):
        answer1=str(answer1)
        answer2=str(answer2)   
        result=("(x"+answer1+")(x"+answer2+")")

    elif (answer1>0 and answer2>0):
        answer1=str(answer1)
        answer2=str(answer2) 
        result=("(x+"+answer1+")(x+"+answer2+")")

    elif (answer1<0 and answer2>0):
        answer1=str(answer1)
        answer2=str(answer2) 
        result=("(x"+answer1+")(x+"+answer2+")")

    elif (answer1>0 and answer2<0):
        answer1=str(answer1)
        answer2=str(answer2) 
        result=("(x+"+answer1+")(x"+answer2+")")

    entry1.delete(0, END)
    entry1.insert(0,result)
   

l1=Label(window, text='Instructions: Enter a value for a, b, and c in the boxes below,\nthen click the "Factor Trinomial" button to display the answer')
e1=Label(window, text="1", width=2)
e2=Entry(window, width=2)
e3=Entry(window, width=2)
l2=Label(window, text="a:")
l3=Label(window, text="b:")
l4=Label(window, text="c:")

b1=Button(window, text="Factor Trinomial", command=clickFunction)

entry1 = Entry(window, width=12, textvariable=eoutput1)

l1.grid(row=1, column=1)
e1.grid(row=3, column=1, sticky=W)
e2.grid(row=4, column=1, sticky=W)
e3.grid(row=5, column=1, sticky=W)
l2.grid(row=3, column=0)
l3.grid(row=4, column=0)
l4.grid(row=5, column=0)
b1.grid(row=4, column=1)
entry1.grid(row=5, column=1)

mainloop()