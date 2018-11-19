import tkinter as tk 
#imports tkinter as tk, giving it a short name to use
#tkinter is our"tool box that gives us the resources to 
#make GUI elements


root = tk.Tk() #creates main window

#**********************WIDGET 1*********(Organization technique)
#Three stages to build elements/objects
#1 Construct: Build and Configure 
#2 Configure the object: Specify behaviours/settings
#3 Pack the object: Put it in a window
output = tk.Text(root,height = 10, width = 30)#Three parameters, root, height width
#ordered parameters: The order we send them matters (COMMON)
#Named Parameters: Java and Python specific
output.config(state = "disable", background = "turquoise")
output.grid(row = 0, column = 0, rowspan = 5)

#*********************WIDGETS 2-4******************************
labInput1 = tk.Label(root, text = "Input1")
labInput1.grid(row = 5, column = 0)

labInput2 = tk.Label(root, text = "Input 2", font = "impact")
labInput2.grid(row = 6, column = 0)

labInput3 = tk.Label(root, text = "Input3")
labInput3.grid(row = 7, column = 0)
#going to be set up with "Grid Packing Management"
#****************************Widget5,6

# How to check the checkbox state

var1 = tk.IntVar()
var2 = tk.IntVar()

cHC = tk.Checkbutton(root, text="Expand", variable=var1)
cHC.grid(row = 0, column = 1)

cHC = tk.Checkbutton(root, text="Expand", variable=var2)
cHC.grid(row = 1, column = 1)
#Starting an "Event Driven Program"
#Build the GUI, Start it Running, Eait for "EVENT"
root.mainloop() #starts the program