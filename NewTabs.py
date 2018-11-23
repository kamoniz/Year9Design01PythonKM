import tkinter as tk
from tkinter import ttk 
import math 



def submit(*args):

	print ("Submit pressed")
	rt1 = float(entrt1.get())
	ht1 = float(entht1.get())

	vt1 = math.pi*rt1*rt1*ht1
	vt1 = round(vt1,3)
	
	#output.config(state="normal")
	outputValue= "Given\nradius:"+str(rt1)+"\nheight:"+str(ht1)+" units\nThe volume is:"+str(vt1)+" units cubed"
	
	output.insert(tk.INSERT,outputValue)
	

root = tk.Tk()
root.title("Calculator")


tabControl = ttk.Notebook(root)



#*****************************************ALL TAB 1 SETUP
tab1 = ttk.Frame(tabControl)
#Step 1: Create or Construct the element
labrt1 = tk.Label(tab1, text="radius")
#Step 2: configure element/widget/object
labrt1.configure(background="red")
#Step 3: Pack the element put it on the window that is displayed
labrt1.pack()

entrt1 = tk.Entry(tab1)
entrt1.pack()

labht1 = tk.Label(tab1, text="height")
labht1.pack()

entht1 = tk.Entry(tab1)
entht1.pack()

output = tk.Text(tab1, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
#output.config(state="disabled")
output.pack()

btnt1 = tk.Button(tab1, text="Submit", font="impact", background="red", command=submit)
btnt1.pack()


#Put widgets into tab1 instead of root
#******************************************************

#***********************************ALL TAB 2

tab2 = ttk.Frame(tabControl)
#Step 1: Create or Construct the element
labrt2 = tk.Label(tab2, text="Length")
#Step 2: configure element/widget/object
labrt2.configure(background="red",font= "Impact")
#Step 3: Pack the element put it on the window that is displayed
labrt2.pack()

entrt2 = tk.Entry(tab2)
entrt2.pack()

labht2 = tk.Label(tab2, text="Width")
labht2.configure(background="red", font="impact")
labht2.pack()

entht2 = tk.Entry(tab2)
entht2.pack()

btnt2 = tk.Button(tab2, text="Submit")
btnt2.pack()



#*********PUT TABS INTO TAB CONTROL
tabControl.add(tab1, text="Volume of Cylinder")
tabControl.add(tab2, text="Area of a Rectangle")
tabControl.grid()





root.mainloop()