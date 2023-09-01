import random
from tkinter import *
diceTypes = [2,4,6,8,10,12,20,100]

# Create object
root = Tk()
  
# Adjust size
root.geometry( "200x200" )
  
# Change the label text
def show():
    label.config( text = clicked.get() )

class diceSet:
    def _init_(set, dice):
        set.dice = []

# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( "Select Dice" )
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *diceTypes)
drop.pack()
  
# Create button, it will change label text
button = Button( root , text = "click Me" , command = show ).pack()
  
# Create Label
label = Label( root , text = " " )
label.pack()
  
# Execute tkinter
root.mainloop()
