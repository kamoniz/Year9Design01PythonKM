import tkinter as tk
from tkinter import ttk 
import math 

def triangle(*args):
	
	output.config(state="normal")
	output.delete("1.0",tk.END)
	print ("Submit pressed")
	lt5 = float(entrt5.get())
	wt5 = float(entht5.get())
	
	vt5 = lt5*wt5/2
	
	outputValuet5= "The area is "+str(vt5)+" units squared"
	output.insert(tk.INSERT,outputValuet5)
	output.config(state="disabled")
	userlog.write(outputValuet5)


def rectangle(*args):
	
	output.config(state="normal")
	output.delete("1.0",tk.END)
	print ("Submit pressed")
	lt2 = float(entrt2.get())
	wt2 = float(entht2.get())
	
	vt2 = lt2*wt2
	
	outputValuet2= "The area is "+str(vt2)+" units squared"
	output.insert(tk.INSERT,outputValuet2)
	output.config(state="disabled")
	userlog.write(outputValuet2)


def circle(*args):
	
	output.config(state="normal")
	output.delete("1.0",tk.END)
	print ("Submit pressed")
	rt3 = float(entrt3.get())

	
	vt3 = rt3*rt3*3.14159265359

	outputValuet3= "The area is "+str(vt3)+" units squared"
	output.insert(tk.INSERT,outputValuet3) 
	output.config(state="disabled")
	userlog.write(outputValuet3)

def rectangularprism(*args):
	
	output.config(state="normal")
	output.delete("1.0",tk.END)
	print ("Submit pressed")
	lt4 = float(entrt4.get())
	wt4 = float(entwt4.get())
	ht4 = float(entht4.get())
	
	vt4 = lt4*wt4*ht4
	
	outputValuet4= "The volume is "+str(vt4)+" units cubed"
	output.insert(tk.INSERT,outputValuet4)
	output.config(state="disabled")
	userlog.write(outputValuet4)


def cylindervolume(*args):

	output.config(state="normal")
	output.delete("1.0",tk.END)
	print ("Submit pressed")
	
	rt1 = float(entrt1.get())
	ht1 = float(entht1.get())
	
	vt1 = math.pi*rt1*rt1*ht1
	vt1 = round(vt1,3)
	
	
	
	#output.config(state="normal")
	outputValuet1= "Given\nradius:"+str(rt1)+"\nheight:"+str(ht1)+" units\nThe volume is:"+str(vt1)+" units cubed"
	
	output.insert(tk.INSERT,outputValuet1) 
	output.config(state="disabled")
	userlog.write(outputValuet1)

def sphere(*args):

	output.config(state="normal")
	output.delete("1.0",tk.END)
	print ("Submit pressed")
	
	rt6 = float(entrt6.get())
	
	

	vt6 = math.pi*rt6*rt6*rt6*4/3
	
	
	
	#output.config(state="normal")
	outputValuet6= "The volume is:"+str(vt6)+" units cubed"
	
	output.insert(tk.INSERT,outputValuet6) 
	output.config(state="disabled")
	userlog.write(outputValuet6)

def trapezoid(*args):

	output.config(state="normal")
	output.delete("1.0",tk.END)
	print ("Submit pressed")
	lt7 = float(entrt7.get())
	wt7 = float(entwt7.get())
	ht7 = float(entht7.get())

	

	vt7 = (lt7+wt7)/2 *ht7
	
	outputValuet7= "The area is "+str(vt7)+" units squared"
	output.insert(tk.INSERT,outputValuet7)
	output.config(state="disabled")
	userlog.write(outputValuet7)

def cone(*args):
	output.config(state="normal")
	output.delete("1.0",tk.END)
	print ("Submit pressed")
	rt8 = float(entrt8.get())
	wt8 = float(entwt8.get())
	

	vt8 = 3.14159265359*rt8*rt8*(wt8/3)
	
	
	outputValuet8= "The volume is "+str(vt8)+" units cubed\n"
	
	
	output.insert(tk.INSERT,outputValuet8)
	output.config(state="disabled")
	userlog.write(outputValuet8)

	output.insert(tk.INSERT,outputValuet8)


def pyramid(*args):

	output.config(state="normal")
	output.delete("1.0",tk.END)
	print ("Submit pressed")
	lt9 = float(entrt9.get())
	wt9 = float(entwt9.get())
	ht9 = float(entht9.get())

	vt9 = (lt9*wt9*ht9)/3
	
	outputValuet9= "The volume is "+str(vt9)+" units cubed\n"
	output.insert(tk.INSERT,outputValuet9)
	output.config(state="disabled")
	userlog.write(outputValuet9)

def circumference(*args):
	output.config(state="normal")
	output.delete("1.0",tk.END)
	print ("Submit pressed")
	
	r = float(entrt10.get())
	
	vt10 = math.pi*r*2
	
	#output.config(state="normal")
	outputValuet10= "The volume is:"+str(vt10)+" units cubed\n"
	
	output.insert(tk.INSERT,outputValuet10) 

	output.config(state="disabled")
	userlog.write(outputValuet10)




userlog = open("log.txt","w") #open a file called log.txt and allow the user to write to it. 
userlog.write("Log file:")

root = tk.Tk()
root.title("Calculator")
root.config(background="#90AFC5")




tabControl = ttk.Notebook(root)
output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")



#*****************************************ALL TAB 1 SETUP
tab1 = ttk.Frame(tabControl)
#Step 1: Create or Construct the element
labrt1 = tk.Label(tab1, text="Radius")
#Step 2: configure element/widget/object
labrt1.configure(background="#90AFC5", font="times")
#Step 3: Pack the element put it on the window that is displayed
labrt1.pack()

entrt1 = tk.Entry(tab1)
entrt1.pack()

labht1 = tk.Label(tab1, text="Height")
labht1.configure(font="times", background="#90AFC5")
labht1.pack()

entht1 = tk.Entry(tab1)
entht1.pack()

#output = tk.Text(tab1, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
#output.config(state="disabled")
#output.pack()
#REMEMBER TO DISABLE OUTPUT BOX!!!!
btnt1 = tk.Button(tab1, text="Submit", font="times", background="#90AFC5", command=cylindervolume)
btnt1.pack()


#Put widgets into tab1 instead of root
#******************************************************

#***********************************ALL TAB 2

tab2 = ttk.Frame(tabControl)
#Step 1: Create or Construct the element
labrt2 = tk.Label(tab2, text="Length")
#Step 2: configure element/widget/object
labrt2.configure(background="#90AFC5",font= "times")
#Step 3: Pack the element put it on the window that is displayed
labrt2.pack()

entrt2 = tk.Entry(tab2)
entrt2.pack()

labht2 = tk.Label(tab2, text="Width")
labht2.configure(background="#90AFC5", font="times")
labht2.pack()

entht2 = tk.Entry(tab2)
entht2.pack()

#output = tk.Text(tab2, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
#output.config(state="disabled")
#output.pack()


btnt2 = tk.Button(tab2, text="Submit", font="times",background="#90AFC5",command=rectangle)
btnt2.pack()


#***************************TAB THREE**************************
tab3 = ttk.Frame(tabControl)

labrt3 = tk.Label(tab3, text="Radius")
labrt3.configure(background="#90AFC5",font="times")
labrt3.pack()

entrt3 = tk.Entry(tab3)
entrt3.pack()

#output = tk.Text(tab3, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
#output.pack()

btnt3 = tk.Button(tab3, text="Submit", font="times", background="#90AFC5", command=circle)
#REMEMBER TO ASSIGN
btnt3.pack()


#************************TAB FOUR********************************
tab4 = ttk.Frame(tabControl)

#Step 1: Create or Construct the element
labrt4 = tk.Label(tab4, text="Length")
#Step 2: configure element/widget/object
labrt4.configure(background="#90AFC5",font= "times")
#Step 3: Pack the element put it on the window that is displayed
labrt4.pack()

entrt4 = tk.Entry(tab4)
entrt4.pack()

labwt4 = tk.Label(tab4, text="Width")
labwt4.configure(background="#90AFC5", font="times")
labwt4.pack()

entwt4 = tk.Entry(tab4)
entwt4.pack()

labht4 = tk.Label(tab4, text="Height")
labht4.configure(background="#90AFC5", font="times")
labht4.pack()

entht4 = tk.Entry(tab4)
entht4.pack()

#output = tk.Text(tab2, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
#output.config(state="disabled")
#output.pack()


btnt4 = tk.Button(tab4, text="Submit", font="times",background="#90AFC5",command=rectangularprism)
btnt4.pack()



#******************************************TAB FIVE*****************
tab5 = ttk.Frame(tabControl)
#Step 1: Create or Construct the element
labrt5 = tk.Label(tab5, text="Base")
#Step 2: configure element/widget/object
labrt5.configure(background="#90AFC5",font= "times")
#Step 3: Pack the element put it on the window that is displayed
labrt5.pack()

entrt5 = tk.Entry(tab5)
entrt5.pack()

labht5 = tk.Label(tab5, text="Height")
labht5.configure(background="#90AFC5", font="times")
labht5.pack()

entht5 = tk.Entry(tab5)
entht5.pack()

#output = tk.Text(tab2, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
#output.config(state="disabled")
#output.pack()


btnt5 = tk.Button(tab5, text="Submit", font="times",background="#90AFC5",command=triangle)
btnt5.pack()


#********************************************TAB SIX************************
tab6 = ttk.Frame(tabControl)
#Step 1: Create or Construct the element
labrt6 = tk.Label(tab6, text="Radius")
#Step 2: configure element/widget/object
labrt6.configure(background="#90AFC5",font= "times")
#Step 3: Pack the element put it on the window that is displayed
labrt6.pack()

entrt6 = tk.Entry(tab6)
entrt6.pack()



btnt6 = tk.Button(tab6, text="Submit", font="times",background="white",command=sphere)
btnt6.pack()


#*****************************************TAB SEVEN**********
tab7 = ttk.Frame(tabControl)

#Step 1: Create or Construct the element
labrt7 = tk.Label(tab7, text="Base a")
#Step 2: configure element/widget/object
labrt7.configure(background="#90AFC5",font= "times")
#Step 3: Pack the element put it on the window that is displayed
labrt7.pack()

entrt7 = tk.Entry(tab7)
entrt7.pack()

labwt7 = tk.Label(tab7, text="Base b")
labwt7.configure(background="#90AFC5", font="times")
labwt7.pack()

entwt7 = tk.Entry(tab7)
entwt7.pack()

labht7 = tk.Label(tab7, text="Height")
labht7.configure(background="#90AFC5", font="times")
labht7.pack()

entht7 = tk.Entry(tab7)
entht7.pack()

#output = tk.Text(tab2, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
#output.config(state="disabled")
#output.pack()


btnt7 = tk.Button(tab7, text="Submit", font="times",background="#90AFC5",command=trapezoid)
btnt7.pack()




#******************************************TAB EIGHT**************

tab8 = ttk.Frame(tabControl)

#Step 1: Create or Construct the element
labrt8 = tk.Label(tab8, text="Radius")
#Step 2: configure element/widget/object
labrt8.configure(background="#90AFC5",font= "times")
#Step 3: Pack the element put it on the window that is displayed
labrt8.pack()

entrt8 = tk.Entry(tab8)
entrt8.pack()

labwt8 = tk.Label(tab8, text="Height")
labwt8.configure(background="#90AFC5", font="times")
labwt8.pack()

entwt8 = tk.Entry(tab8)
entwt8.pack()


#output = tk.Text(tab2, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
#output.config(state="disabled")
#output.pack()


btnt8 = tk.Button(tab8, text="Submit", font="times",background="#90AFC5",command=cone)
btnt8.pack()


#*********************************TAB NINE*******************

tab9 = ttk.Frame(tabControl)

#Step 1: Create or Construct the element
labrt9 = tk.Label(tab9, text="Base Length")
#Step 2: configure element/widget/object
labrt9.configure(background="#90AFC5",font= "times")
#Step 3: Pack the element put it on the window that is displayed
labrt9.pack()

entrt9 = tk.Entry(tab9)
entrt9.pack()

labwt9 = tk.Label(tab9, text="Base Width")
labwt9.configure(background="#90AFC5", font="times")
labwt9.pack()

entwt9 = tk.Entry(tab9)
entwt9.pack()

labht9 = tk.Label(tab9, text="Height")
labht9.configure(background="#90AFC5", font="times")
labht9.pack()

entht9 = tk.Entry(tab9)
entht9.pack()

#output = tk.Text(tab2, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
#output.config(state="disabled")
#output.pack()


btnt9 = tk.Button(tab9, text="Submit", font="times",background="#90AFC5",command=pyramid)
btnt9.pack()

#************************************TAB TEN********************
tab10 = ttk.Frame(tabControl)

labrt10 = tk.Label(tab10, text="Radius")
labrt10.configure(background="#90AFC5",font="times")
labrt10.pack()

entrt10 = tk.Entry(tab10)
entrt10.pack()

#output = tk.Text(tab3, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
#output.pack()

btnt10 = tk.Button(tab10, text="Submit", font="times", background="#90AFC5", command=circumference)

#REMEMBER TO ASSIGN
btnt10.pack()



#*********PUT TABS INTO TAB CONTROL*************************
tabControl.add(tab1, text="Volume of Cylinder")
tabControl.add(tab2, text="Area of a Rectangle")
tabControl.add(tab3, text="Area of a Circle")
tabControl.add(tab4, text="Volume of a Rectangular Prism")
tabControl.add(tab5, text="Area of a Triangle")
tabControl.add(tab6, text="Volume of a Sphere")
tabControl.add(tab7, text="Area of a Trapezoid")
tabControl.add(tab8, text="Volume of a Cone")
tabControl.add(tab9, text="Volume of a Pyramid")
tabControl.add(tab10, text="Circumference of a Circle")
tabControl.pack()


output.config(background="mintcream",borderwidth=3,width=100, font=("Times",20), height=100)
output.pack()






root.mainloop()
userlog.close()

