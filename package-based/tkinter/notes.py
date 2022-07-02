from tkinter import *

root = Tk()

# Pack System
"""
# Making a 'Label Widget'
label01 = Label(root, text="Hello World")
# Packing label in root
label01.pack()
"""

# Grid System
"""
label01 = Label(root, text="This is Tkinter thingy")
label02 = Label(root, text="A python library")
label01.grid(row=0, column=0)
label02.grid(row=1, column=1)
"""

# Buttons
"""
button = Button(root, text="Download", state=DISABLED) # Disable
button = Button(root, text="Download", padx=30, pady=10) # Padding

# Using button to perform a fuction
def click():
    label = Label(root, text="Starting...")
    label.pack()

button = Button(root, text="Download", command=click)

button = Button(root, text="Click me", fg="red", bg="black") # Color
"""

# Entry/Input
"""
entry = Entry(root)
entry.get() # Get entered value
entry.insert(0, "Pre wrtten text")

"""
e = Entry(borderwidth=5, width=20, fg="#3A3B3C")
e.insert(0, "URL")
e.pack()

def onClick():
    label = Label(root, text=e.get())
    label.pack()
button = Button(root, text="Download", command=onClick)

button.pack()

root.mainloop()
