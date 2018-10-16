import tkinter as tk
from tkinter import ttk

class Display:

	def _init_(self):

		self.root = tk.Tk()
		self.root.title("Calculator")

	self.tabControl = ttk.Notebook(self.root)	

	self.tab1= ttk.Frame(self.tabControl)
	self.tabControl.add(self.tab1,text="Tab1")
	self.tabControl.pack(expand=1, fill="both")

	display=Display()