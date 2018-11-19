import tkinter as tk
from tkinter import ttk
import math

class Display:
	
	def __init__(self):

		self.root = tk.Tk() #Create root window
		self.root.title("Calculator") #Title window

		self.tabControl = ttk.Notebook(self.root) #Create tab control, keeps track of tabs

		#Tab 1
		self.tab1= ttk.Frame(self.tabControl) #Puts frame in tab control
		self.tabControl.add(self.tab1,text="Tab1")

		#Tab 2
		self.tab2= ttk.Frame(self.tabControl)
		self.tabControl.add(self.tab2,text="Tab2")
		
		#Putting Tabs in tabControl
		self.tabControl.pack(expand=3, fill="both")

		#Tab 1
		self.et1 = tk.Entry(self.tab1)
	
		self.labr = tk.Label(self.tab1, text="radius")
		#Step 2: configure element/widget/object
		self.labr.configure(background="red")
		#Step 3: Pack the element put it on the window that is displayed
		self.labr.pack()


		self.entr = tk.Entry(self.tab1)
		self.entr.pack()

		self.labh = tk.Label(self.tab1, text="height")
		self.labh.pack()

		self.enth = tk.Entry(self.tab1)
		self.enth.pack()

		self.btn = tk.Button(self.tab1, text="Submit", command=submit)
		self.btn.pack()

		self.output = tk.Text(self.tab1, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
		self.output.config(state="disabled")
		self.output.pack()


		self.btnt1 = tk.Button(self.tab1, text = "Submit", command = self.btn1Pressed)
		self.btnt1.pack()

		self.root.mainloop()

	def btn1Pressed(self):

		print ("2")
		print(self.et1.get())

	def submit():

		self.print ("Submit pressed")
		self.r = float(entr.get())
		self.h = float(entr.get())

		self.v = math.pi*r*r*h
		self.v = round(v,3)

		self.output.config(state="normal")

		self.outputValue= "Given\nradius:"+str(r)+"\nheight:"+str(h)+" units\nThe volume is:"+str(v)+" units cubed"
		

		self.output.delete(1.0,tk.END)
		
		self.output.insert(tk.INSERT,outputValue)
		self.output.config(state="disabled")



display=Display()