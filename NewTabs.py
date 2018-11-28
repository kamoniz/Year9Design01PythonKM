import tkinter as tk
from tkinter import ttk 
import math 

def rectangle(*args):
	output.delete("1.0",tk.END)
	print ("Submit pressed")
	lt2 = float(entrt2.get())
	wt2 = float(entht2.get())
	
	vt2 = lt2*wt2
	
	outputValuet2= "The area is "+str(vt2)+" units squared"
	output.insert(tk.INSERT,outputValuet2)

def circle(*args):
	output.delete("1.0",tk.END)
	print ("Submit pressed")
	rt3 = float(entrt3.get())

	vt3 = rt3*rt3*3.14159265359

	outputValuet3= "The area is "+str(vt3)+" units squared"
	output.insert(tk.INSERT,outputValuet3) 
	
def rectangularprism(*args):
	output.delete("1.0",tk.END)
	print ("Submit pressed")
	lt4 = float(entrt4.get())
	wt4 = float(entwt4.get())
	ht4 = float(entht4.get())

	vt4 = lt4*wt4*ht4
	
	outputValuet4= "The volume is "+str(vt4)+" units cubed"
	output.insert(tk.INSERT,outputValuet4)

def cylindervolume(*args):

	output.delete("1.0",tk.END)
	print ("Submit pressed")
	
	rt1 = float(entrt1.get())
	ht1 = float(entht1.get())

	vt1 = math.pi*rt1*rt1*ht1
	vt1 = round(vt1,3)
	
	
	
	
	#output.config(state="normal")
	outputValuet1= "Given\nradius:"+str(rt1)+"\nheight:"+str(ht1)+" units\nThe volume is:"+str(vt1)+" units cubed"
	
	output.insert(tk.INSERT,outputValuet1) 
	
	





root = tk.Tk()
root.title("Calculator")


tabControl = ttk.Notebook(root)
output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)




#*****************************************ALL TAB 1 SETUP
tab1 = ttk.Frame(tabControl)
#Step 1: Create or Construct the element
labrt1 = tk.Label(tab1, text="Radius")
#Step 2: configure element/widget/object
labrt1.configure(background="red", font="impact")
#Step 3: Pack the element put it on the window that is displayed
labrt1.pack()

entrt1 = tk.Entry(tab1)
entrt1.pack()

labht1 = tk.Label(tab1, text="Height")
labht1.configure(font="impact", background="red")
labht1.pack()

entht1 = tk.Entry(tab1)
entht1.pack()

#output = tk.Text(tab1, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
#output.config(state="disabled")
#output.pack()
#REMEMBER TO DISABLE OUTPUT BOX!!!!
btnt1 = tk.Button(tab1, text="Submit", font="impact", background="red", command=cylindervolume)
btnt1.pack()


#Put widgets into tab1 instead of root
#******************************************************

#***********************************ALL TAB 2

tab2 = ttk.Frame(tabControl)
#Step 1: Create or Construct the element
labrt2 = tk.Label(tab2, text="Length")
#Step 2: configure element/widget/object
labrt2.configure(background="red",font= "impact")
#Step 3: Pack the element put it on the window that is displayed
labrt2.pack()

entrt2 = tk.Entry(tab2)
entrt2.pack()

labht2 = tk.Label(tab2, text="Width")
labht2.configure(background="red", font="impact")
labht2.pack()

entht2 = tk.Entry(tab2)
entht2.pack()

#output = tk.Text(tab2, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
#output.config(state="disabled")
#output.pack()


btnt2 = tk.Button(tab2, text="Submit", font="impact",background="red",command=rectangle)
btnt2.pack()


#***************************TAB THREE**************************
tab3 = ttk.Frame(tabControl)

labrt3 = tk.Label(tab3, text="Radius")
labrt3.configure(background="red",font="impact")
labrt3.pack()

entrt3 = tk.Entry(tab3)
entrt3.pack()

#output = tk.Text(tab3, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
#output.pack()

btnt3 = tk.Button(tab3, text="Submit", font="impact", background="red", command=circle)
#REMEMBER TO ASSIGN
btnt3.pack()


#************************TAB FOUR********************************
tab4 = ttk.Frame(tabControl)

#Step 1: Create or Construct the element
labrt4 = tk.Label(tab4, text="Length")
#Step 2: configure element/widget/object
labrt4.configure(background="red",font= "impact")
#Step 3: Pack the element put it on the window that is displayed
labrt4.pack()

entrt4 = tk.Entry(tab4)
entrt4.pack()

labwt4 = tk.Label(tab4, text="Width")
labwt4.configure(background="red", font="impact")
labwt4.pack()

entwt4 = tk.Entry(tab4)
entwt4.pack()

labht4 = tk.Label(tab4, text="Height")
labht4.configure(background="red", font="impact")
labht4.pack()

entht4 = tk.Entry(tab4)
entht4.pack()

#output = tk.Text(tab2, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
#output.config(state="disabled")
#output.pack()


btnt4 = tk.Button(tab4, text="Submit", font="impact",background="red",command=rectangularprism)
btnt4.pack()


#*********PUT TABS INTO TAB CONTROL
tabControl.add(tab1, text="Volume of Cylinder")
tabControl.add(tab2, text="Area of a Rectangle")
tabControl.add(tab3, text="Area of a Circle")
tabControl.add(tab4, text="Volume of a Rectangular Prism")
tabControl.pack()
output.pack()






root.mainloop()