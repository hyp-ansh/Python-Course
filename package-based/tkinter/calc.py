from tkinter import *

root = Tk()
root.title("Calculator v1")

inpt = Entry(root, borderwidth=5, width=33, justify="right")
inpt.grid(row=0, column=0, columnspan=3, padx=15, pady=10)

# Fuctions
def fClick(number):
    current = str(inpt.get())
    inpt.delete(0, END)
    inpt.insert(0,current + str(number))

def fClear():
    inpt.delete(0, END)

def fAdd():
    first_num = inpt.get()
    global f_num
    f_num = int(first_num)
    inpt.delete(0, END)

def fResult():
    second_num = int(inpt.get())
    inpt.delete(0, END)
    inpt.insert(0, f_num + second_num)

def fSub():
    return

def fProd():
    return

def fDiv():
    return

# buttons
b0 = Button(root, text="0", fg="white", bg="#060606", 
                padx=33, pady=13, command=lambda: fClick(0))

b1 = Button(root, text="1", fg="white", bg="#060606", 
                padx=33, pady=13, command=lambda: fClick(1))

b2 = Button(root, text="2", fg="white", bg="#060606", 
                padx=33, pady=13, command=lambda: fClick(2))

b3 = Button(root, text="3", fg="white", bg="#060606", 
                padx=33, pady=13, command=lambda: fClick(3))

b4 = Button(root, text="4", fg="white", bg="#060606", 
                padx=33, pady=13, command=lambda: fClick(4))

b5 = Button(root, text="5", fg="white", bg="#060606", 
                padx=33, pady=13, command=lambda: fClick(5))

b6 = Button(root, text="6", fg="white", bg="#060606", 
                padx=33, pady=13, command=lambda: fClick(6))

b7 = Button(root, text="7", fg="white", bg="#060606", 
                padx=33, pady=13, command=lambda: fClick(7))

b8 = Button(root, text="8", fg="white", bg="#060606", 
                padx=33, pady=13, command=lambda: fClick(8))

b9 = Button(root, text="9", fg="white", bg="#060606", 
                padx=33, pady=13, command=lambda: fClick(9))

bAdd = Button(root, text="+", fg="white", bg="#131313", 
                padx=32, pady=13, command=lambda: fAdd())

bSub = Button(root, text="-", fg="white", bg="#131313", 
                padx=33, pady=13, command=lambda: fSub())

bProd = Button(root, text="x", fg="white", bg="#131313", 
                padx=33, pady=13, command=lambda: fProd())

bDiv = Button(root, text="÷", fg="white", bg="#131313", 
                padx=32, pady=13, command=lambda: fDiv())

bEqual = Button(root, text="=", fg="white", bg="#134367", 
                padx=32, pady=13, command=lambda: fResult())

bClear = Button(root, text="Clear", fg="white", bg="#320A0A",
                padx=105, pady=13, command=lambda: fClear())

# Arranging buttons
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)
bAdd.grid(row=4, column=1)
bSub.grid(row=4, column=2)

bEqual.grid(row=5, column=0)
bProd.grid(row=5, column=1)
bDiv.grid(row=5, column=2)

bClear.grid(row=6, column=0, columnspan=3)

root.mainloop()
