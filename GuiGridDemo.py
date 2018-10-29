import tkinter as tk 
#Importing your 'toolbox'
#tkinter is a module that holds all the functions, that lets us easily use GUI elements
root = tk.Tk()
#creates main window. To do this, we need to call Tk() function
#root.mainloop()
#THIS IS HOW YOU OPEN A SECOND WINDOW
 

label = tk.Label(root, text = "Welcome to Concentration")
label.grid(row = 0 ,column = 0, columnspan=2)



btn1 = tk.Button(root, text = "1")
btn1.config(width=5,height=5,)
btn1.grid(row = 1, column = 0, sticky="NESW")

btn2 = tk.Button(root, text = "2")
btn2.config(width=5,height=5,)
btn2.grid(row = 1, column=1, sticky="NESW")

btn3 = tk.Button(root, text = "3")
btn3.config(width=5,height=5,)
btn3.grid(row = 2, column=0, sticky = "NESW")

btn4 = tk.Button(root, text = "4")
btn4.config(width=5,height=5)
btn4.grid(row=2, column=1, sticky = "NESW")

if"btn1"p print("Hi")

root.mainloop()