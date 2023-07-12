from tkinter import *

'''podziałac klase przycisk z tego zeby mozna bylo wstawiac text przypisany do danego przycisku self.tekst=tekst zeby dalej mozna bylo ogarnac jakos usuniecie evala i zrobic funkcje dodac,odjac,podzielic i pomnozyc'''
window = Tk()
window.title('Calculator')

txtEntry = Entry(window, font = ('Arial', 35), width= 8, bg='white')
txtEntry.grid(row = 0, column= 1, columnspan= 4)


def button_press(number):
    
    current = txtEntry.get()
    txtEntry.delete(0, END)
    txtEntry.insert(0, str(current) + str(number))

def clear():
    txtEntry.delete(0, END)

def back():
    pass

def add():
   first_number = txtEntry.get()
   global f_num
   global math
   math = "addition"
   f_num = int(first_number)
   txtEntry.delete(0, END)

def minus():
   first_number = txtEntry.get()
   global f_num
   global math
   math = "subtraction"
   f_num = int(first_number)
   txtEntry.delete(0, END)

def divide():
   first_number = txtEntry.get()
   global f_num
   global math
   math = "division"
   f_num = int(first_number)
   txtEntry.delete(0, END)

def multiply():
   first_number = txtEntry.get()
   global f_num
   global math
   math = "multiplication"
   f_num = int(first_number)
   txtEntry.delete(0, END)


def equal():
    second_number = txtEntry.get()
    txtEntry.delete(0, END)

    if math == "addition" :
        txtEntry.insert(0, f_num + int(second_number))

    if math == "subtraction" :
        txtEntry.insert(0, f_num - int(second_number))

    if math == "division" :
        txtEntry.insert(0, f_num / int(second_number)) 

    if math == "multiplication" :
        txtEntry.insert(0, f_num * int(second_number))

# BUTTONS

button = Button(window,text = "0", font = ('Arial', 30), command= lambda: button_press(0), height=1, width = 2)
button.grid(row= 5, column = 2)

button1 = Button(window, text = "1", font = ('Arial', 30), command= lambda: button_press(1), height = 1, width = 2)
button1.grid(row=4, column = 1)

button2 = Button(window, text = "2", font = ('Arial', 30), command= lambda: button_press(2), height = 1, width = 2)
button2.grid(row=4 , column= 2)

button3 = Button(window, text = "3", font = ('Arial', 30), command= lambda: button_press(3), height = 1, width = 2)
button3.grid(row = 4, column= 3)

button4 = Button(window, text = "4", font = ('Arial', 30), command= lambda: button_press(4), height = 1, width = 2)
button4.grid(row = 3, column= 1)

button5 = Button(window, text = "5", font = ('Arial', 30), command= lambda: button_press(5), height = 1, width = 2)
button5.grid(row = 3, column= 2)

button6 = Button(window, text = "6", font = ('Arial', 30), command= lambda: button_press(6), height = 1, width = 2)
button6.grid(row = 3, column= 3)

button7 = Button(window, text = "7", font = ('Arial', 30), command= lambda: button_press(7), height = 1, width = 2)
button7.grid(row = 2, column= 1)

button8 = Button(window, text = "8", font = ('Arial', 30), command= lambda: button_press(8), height = 1, width = 2)
button8.grid(row = 2, column= 2)

button9 = Button(window, text = "9", font = ('Arial', 30), command= lambda: button_press(9), height = 1, width = 2)
button9.grid(row = 2, column= 3)

button_add = Button(window, text = "+", font = ('Arial', 30), command= add, height = 1, width = 2)
button_add.grid(row =4, column= 4)

button_point = Button(window, text = ".", font = ('Arial', 30), command= button_press, height = 1, width = 2)
button_point.grid(row = 5, column= 1)

button_equal = Button(window, text = "=", font = ('Arial', 30), command= equal, height = 1, width = 2)
button_equal.grid(row =5, column= 3)

c = Button(window, text = "C", font = ('Arial', 30), command= lambda: clear(), padx = 25, pady=0)
c.grid(row= 1,column = 1, columnspan= 2)

button_multiply = Button(window, text = "x", font = ('Arial', 30), command= multiply, height = 1, width = 2)
button_multiply.grid(row = 2, column= 4)

button_minus = Button(window, text = "-", font = ('Arial', 30), command= minus, height = 1, width = 2)
button_minus.grid(row = 3, column= 4)

button_divide = Button(window, text = "/", font = ('Arial', 30), command= divide, height = 1, width = 2)
button_divide.grid(row = 5, column= 4)

ce = Button(window, text = "CE", font = ('Arial', 30), command= lambda: back(), padx=11, pady= 0)
ce.grid(row= 1, column= 3, columnspan= 2)



window.mainloop()
