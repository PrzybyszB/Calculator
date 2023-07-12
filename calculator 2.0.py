from tkinter import *
import math
import parser_libraries


def button_press(numbers):
    global operator
    operator = operator +str(numbers)
    txtInput.set(operator)

def Clear():
    global operator
    operator= ""
    txtInput.set("")

def Equal():
    global operator
    summ = str(eval(operator))
    txtInput.set(summ)
    operator = ""

 
window = Tk()
window.geometry('241x395')
window.title("Calculator")
operator = ""
txtInput = StringVar()

txtEntry = Entry(window, font=('Arial',38), justify=LEFT, bg = 'white',width = 8, textvariable=txtInput)
txtEntry.grid(column = 0, row = 0, columnspan=6)





'''======================================================BUTTONS==============================================================================================='''


button = Button(window,text = "0", font = ('Arial', 30), command = lambda: button_press(0), height=1, width = 2, bd =4)
button.grid(row= 4, column = 2)

button1 = Button(window, text = "1", font = ('Arial', 30),  command = lambda: button_press(1), height = 1, width = 2, bd =4)
button1.grid(row=3, column = 1)

button2 = Button(window, text = "2", font = ('Arial', 30), command = lambda: button_press(2), height = 1, width = 2, bd =4)
button2.grid(row=3 , column= 2)

button3 = Button(window, text = "3", font = ('Arial', 30),  command = lambda: button_press(3), height = 1, width = 2, bd =4)
button3.grid(row = 3, column= 3)

button4 = Button(window, text = "4", font = ('Arial', 30),  command = lambda: button_press(4), height = 1, width = 2, bd =4)
button4.grid(row = 2, column= 1)

button5 = Button(window, text = "5", font = ('Arial', 30), command = lambda: button_press(5), height = 1, width = 2, bd =4)
button5.grid(row = 2, column= 2)

button6 = Button(window, text = "6", font = ('Arial', 30),  command = lambda: button_press(6), height = 1, width = 2, bd =4)
button6.grid(row = 2, column= 3)

button7 = Button(window, text = "7", font = ('Arial', 30),  command = lambda: button_press(7), height = 1, width = 2, bd =4)
button7.grid(row = 1, column= 1)

button8 = Button(window, text = "8", font = ('Arial', 30), command = lambda: button_press(8), height = 1, width = 2, bd =4)
button8.grid(row = 1, column= 2)

button9 = Button(window, text = "9", font = ('Arial', 30), command = lambda: button_press(9), height = 1, width = 2, bd =4)
button9.grid(row = 1, column= 3)

button_add = Button(window, text = "+", font = ('Arial', 30), command = lambda: button_press('+'), height = 1, width = 2, bd =4)
button_add.grid(row =3, column= 4)

c = Button(window, text = "C", font = ('Arial', 30), command = Clear, height = 1, width = 2, bd =4)
c.grid(row = 4, column= 1)

button_equal = Button(window, text = "=", font = ('Arial', 30), command = lambda: Equal(), height = 1, width = 2, bd =4)
button_equal.grid(row =4, column= 3)

button_multiply = Button(window, text = "x", font = ('Arial', 30), command = lambda: button_press("*"), height = 1, width = 2, bd =4)
button_multiply.grid(row = 1, column= 4)

button_minus = Button(window, text = "-", font = ('Arial', 30),  command = lambda: button_press("-"), height = 1, width = 2, bd =4)
button_minus.grid(row = 2, column= 4)

button_divide = Button(window, text = "/", font = ('Arial', 30), command = lambda: button_press("/"), height = 1, width = 2, bd =4)
button_divide.grid(row = 4, column= 4)


window.mainloop()