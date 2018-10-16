import tkinter as tk
from tkinter import ttk

class Display:
	#A constructor is a special method only called once 
	#when we create an object
	#A class is a blueprint to make an object
	def __init__(self):

		self.root = tk.Tk()
		self.root.title("Calculator")

		self.tabControl = ttk.Notebook(self.root)	

		self.tab1= ttk.Frame(self.tabControl)
		self.tabControl.add(self.tab1,text="Tab1")
		

		self.tab2= ttk.Frame(self.tabControl)
		self.tabControl.add(self.tab2,text="Tab2")
		
		self.tabControl.pack(expand=3, fill="both")

		self.et1 = tk.Entry(self.tab1)
		self.et1.pack()
		self.btnt1 = tk.Button(self.tab1, text = "Submit", command = self.btn1Pressed)
		self.btnt1.pack()


		self.et2 = tk.Entry(self.tab2)
		self.et2.pack()
		self.btnt2 = tk.Button(self.tab2, text = "Submit", command = self.btn1Pressed)
		self.btnt2.pack()




		self.root.mainloop()

	def btn1Pressed(self):
			print("2")
			print(self.et1.get())

display=Display()