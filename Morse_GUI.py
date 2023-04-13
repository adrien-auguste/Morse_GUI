from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time
RPi.GPIO.setmode(RPi.GPIO.BCM)


## Assigning Variable
red = LED(10)

## Defining the GUI


win = Tk()
win.title("Task 5.3- Making GUI - Morse code")
win.geometry('500x300')
myFont = tkinter.font.Font(family ='Arial' ,size = '13', weight = "bold")



## Morse Function - in this program a unit is considered to be half a second

def dot():
	# The function produces a dot
	red.on()
	time.sleep(0.5)
	red.off()
	time.sleep(0.5)

def dash():
	# The function produces a dash
	red.on()
	time.sleep(1.5)
	red.off()
	time.sleep(0.5)	

	
def morse(name):
	# The function contains the morse code data as a dict and execute the input
	morsename = {
		'A': [0,1],'B':[1,0,0,0],'C':[1,0,1,0],'D':[1,0,0],
		'E':[0],'F':[0,0,1,0],'G':[1,1,0],'H':[0,0,0,0],
		'I':[0,0],'J':[0,1,1,1],'K':[1,0,1],'L':[0,1,0,0],'M':[1,1],
		'N':[1,0],'O':[1,1,1],'P':[0,1,1,0],'Q':[1,1,0,1],
		'R':[0,1,0],'S':[0,0,0],'T':[1],'U':[0,0,1],'V':[0,0,0,1],
		'W':[0,1,1],'X':[1,0,0,1],'Y':[1,0,1,1],'Z':[1,1,0,0]	
	}
	for letter in name:
		interpret = morsename[letter]
		for morse_ in interpret:
			if morse_ == 0:
				print(str(morse_))
				dot()
				
			else:
				print(str(morse_))
				dash()
	
def input():
	# the function deals with the user input
	word = e.get()
	
	false_word = Label(win, text='Please enter a word with maximum of 12 letters', bg='red')
	if (not word.isalpha() or len(word) > 13):
		false_word.grid(row = 1, column = 13)
		e.delete(0,END)
		
		false_word.after(1000, lambda: false_word.grid_forget())
				
	else:
		morse(word.upper())
		e.delete(0,END)

def closeProgram():
	# The function closes the program correctly
	RPi.GPIO.cleanup()
	win.destroy()


## Building widgets
# Input from keyboard
e = Entry(win, width = 12)
e.grid(row =1, column = 2)

# Label to prompt the user to input a name or word
label_name= Label(win, text="Enter a word")
label_name.grid(row =1, column = 1)

# Button to execute the translation of the name to morse code
myButton = Button(win, text="Execute Morse Code", command=input, bg ="blue",fg ='white', height=1, width = 20) 
myButton.grid(row=3,column =1)

# Closing the program and clearing the GPIO
exitProgram = Button(win, text= "Close program", command = closeProgram, bg ='red',height = 1, width = 20)
exitProgram.grid(row = 7, column = 1)

win.protocol("WM_DELETE_WINDOW", closeProgram)

win.mainloop()
