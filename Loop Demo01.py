 #Loops are structures used to repeat sections of code


 
 

 #This is a counted loop. Think about "Count Check Change"
 # i =0, 0 < 5, TRUE RUN LOOP= how the computer thinks (repeats all the way to 4)for i in range(4,12,2):

 	#In this case, 0=count, 5=check,=1=change
 	#Anything Tabbed is considered the loop block
 	 
for i in range(2,6,1):
 print(i*2)  
#If you chnge your increment to go in reverse
#te check is always i > check, in this case -1
for i in range(10,-1,-1):
 print(i)
print("Backwards")
print(i)


str = "Monkey"


for i in range(0,6,1):
	print(str[i])
#We can use the loop to go through each index in a stiring to print out each letter
#always indicate the length of a word using function len

print("*********Printing String Characters*********")

"M"
"o"
"n"
"k"
"e"
"y"

print("Moving On")
for i in range(len(str) - 1, -1, -1):
	print (str[i])

print("Every second letter in str staring at index 0")