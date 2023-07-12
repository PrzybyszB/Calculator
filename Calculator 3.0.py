from tkinter import *




window = Tk()
window.geometry('241x478')
window.title("Calculator")


calculator = Frame(window)
calculator.grid()

class Calculator:
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
       
    def entry(self, value):
        txtEntry.delete(0,END)
        txtEntry.insert(0,value)

    def valid_fuction(self):
        if self.op == "addition":
            self.total += self.current
        if self.op == "substract":
            self.total -= self.current
        if self.op == "multiply":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.input_value = True
        self.check_sum = False
        self.entry(self.total)
    
    def operation (self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_fuction()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def button_press(self,num):
        self.result = False
        firstnum = txtEntry.get()
        secondnum= str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum =='.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.entry(self.current)
    
    def ClearEntry(self):
        self.result = False
        self.current = '0'
        self.entry(0)
        self.input_value = True

    def Clear(self):
        self.ClearEntry()
        self.total = '0'

    def Equal(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_fuction()
        else:
            self.total = float(txtEntry.get())


added_value = Calculator()



txtEntry = Entry(calculator, font=('Arial',38), justify=LEFT, bg = 'white',width = 8)
txtEntry.grid(column = 0, row = 0, columnspan=6)
# txtEntry.insert(0,'0')







'''======================================================BUTTONS==============================================================================================='''


button = Button(calculator,text = "0", font = ('Arial', 30), command = lambda: added_value.button_press(0), height=1, width = 2, bd =4)
button.grid(row= 5, column = 2)

button1 = Button(calculator, text = "1", font = ('Arial', 30),  command = lambda: added_value.button_press(1), height = 1, width = 2, bd =4)
button1.grid(row=4, column = 1)

button2 = Button(calculator, text = "2", font = ('Arial', 30), command = lambda: added_value.button_press(2), height = 1, width = 2, bd =4)
button2.grid(row=4 , column= 2)

button3 = Button(calculator, text = "3", font = ('Arial', 30),  command = lambda: added_value.button_press(3), height = 1, width = 2, bd =4)
button3.grid(row = 4, column= 3)

button4 = Button(calculator, text = "4", font = ('Arial', 30),  command = lambda: added_value.button_press(4), height = 1, width = 2, bd =4)
button4.grid(row = 3, column= 1)

button5 = Button(calculator, text = "5", font = ('Arial', 30), command = lambda: added_value.button_press(5), height = 1, width = 2, bd =4)
button5.grid(row = 3, column= 2)

button6 = Button(calculator, text = "6", font = ('Arial', 30),  command = lambda: added_value.button_press(6), height = 1, width = 2, bd =4)
button6.grid(row = 3, column= 3)

button7 = Button(calculator, text = "7", font = ('Arial', 30),  command = lambda: added_value.button_press(7), height = 1, width = 2, bd =4)
button7.grid(row = 2, column= 1)

button8 = Button(calculator, text = "8", font = ('Arial', 30), command = lambda: added_value.button_press(8), height = 1, width = 2, bd =4)
button8.grid(row = 2, column= 2)

button9 = Button(calculator, text = "9", font = ('Arial', 30), command = lambda: added_value.button_press(9), height = 1, width = 2, bd =4)
button9.grid(row = 2, column= 3)

button_add = Button(calculator, text = "+", font = ('Arial', 30), command = lambda: added_value.operation("addition"), height = 1, width = 2, bd =4)
button_add.grid(row =4, column= 4)

button_point = Button(calculator, text = ".", font = ('Arial', 30), command = lambda: added_value.button_press("."), height = 1, width = 2, bd =4)
button_point.grid(row = 5, column= 1)

button_equal = Button(calculator, text = "=", font = ('Arial', 30), command = added_value.Equal, height = 1, width = 2, bd =4)
button_equal.grid(row =5, column= 3)

c = Button(calculator, text = "C", font = ('Arial', 30), command= added_value.Clear, padx = 25, bd =4)
c.grid(row= 1,column = 1, columnspan= 2)

button_multiply = Button(calculator, text = "x", font = ('Arial', 30), command = lambda: added_value.operation("multiply"), height = 1, width = 2, bd =4)
button_multiply.grid(row = 2, column= 4)

button_minus = Button(calculator, text = "-", font = ('Arial', 30),  command = lambda: added_value.operation("substract"), height = 1, width = 2, bd =4)
button_minus.grid(row = 3, column= 4)

button_divide = Button(calculator, text = "/", font = ('Arial', 30), command = lambda: added_value.operation("divide"), height = 1, width = 2, bd =4)
button_divide.grid(row = 5, column= 4)

ce = Button(calculator, text = "CE", font = ('Arial', 30), command = added_value.ClearEntry, padx=14, bd =3)
ce.grid(row= 1, column= 3, columnspan= 2)


window.mainloop()







# Oto szczegółowe wyjaśnienie, jak ten kod działa:

# Importowanie modułów:

# from tkinter import * importuje wszystkie elementy z modułu tkinter, który jest wykorzystywany do tworzenia interfejsu graficznego.
# import math importuje moduł math, który zawiera funkcje matematyczne.
# Tworzenie okna:

# window = Tk() tworzy nowe okno główne.
# window.geometry('241x478') ustawia rozmiar okna na 241 pikseli szerokości i 478 pikseli wysokości.
# window.title("Calculator") ustawia tytuł okna na "Calculator".
# Tworzenie ramki dla kalkulatora:

# calculator = Frame(window) tworzy ramkę (kontener) dla elementów interfejsu kalkulatora.
# calculator.grid() umieszcza ramkę w oknie głównym.
# Tworzenie klasy Calculator:

# Klasa Calculator zawiera logikę kalkulatora i funkcje obsługujące operacje matematyczne oraz wyświetlanie wyników.

# def __init__(self): to metoda inicjalizacyjna (konstruktor) klasy. Inicjalizuje zmienne, takie jak total (aktualny wynik), current (aktualnie wprowadzana liczba), input_value (czy aktualnie wprowadzana wartość jest nową liczbą), check_sum (czy przeprowadzono operację), op (typ ostatniej operacji), result (czy wynik jest już dostępny).

# def entry(self, value): metoda ta służy do aktualizacji pola wprowadzania (Entry) z podaną wartością.

# def valid_function(self): metoda ta wykonuje odpowiednią operację matematyczną (dodawanie, odejmowanie, mnożenie, dzielenie) na podstawie wartości op i current. Aktualizuje również total i wywołuje metodę entry() w celu aktualizacji pola wprowadzania.

# def operation(self, op): metoda ta jest wywoływana po naciśnięciu przycisku operacji (+, -, *, /). Konwertuje current na liczbę zmiennoprzecinkową, a następnie wywołuje valid_function() lub aktualizuje total i input_value w zależności od wcześniejszych operacji.

# def button_press(self, num): metoda ta jest wywoływana po naciśnięciu przycisku liczby (0-9) lub kropki. W zależności od stanu input_value, aktualizuje current i wywołuje entry().

# def clear_entry(self): metoda ta czyści wprowadzoną wartość (current) i wywołuje entry().

# def clear(self): metoda ta czyści wszystkie wartości (ustawia current i total na 0) oraz wywołuje clear_entry().

# def equal(self): metoda ta jest wywoływana po naciśnięciu przycisku równości (=). Konwertuje current na liczbę zmiennoprzecinkową i wykonuje operację matematyczną, wywołując valid_function() lub aktualizując total w zależności od wcześniejszych operacji.

# Tworzenie instancji klasy Calculator:

# added_value = Calculator() tworzy instancję klasy Calculator o nazwie added_value. Ta instancja przechowuje stan kalkulatora i obsługuje operacje.
# Tworzenie pola wprowadzania (Entry):

# txtEntry = Entry(calculator, font=('Arial', 38), justify=LEFT, bg='white', width=8) tworzy pole wprowadzania (Entry) w ramce calculator z określonymi parametrami, takimi jak czcionka, justowanie tekstu, kolor tła i szerokość.
# Tworzenie przycisków:

# Przykład dla przycisku "0":
# button = Button(calculator, text="0", font=('Arial', 30), command=lambda: added_value.button_press(0), height=1, width=2, bd=4) tworzy przycisk z etykietą "0" i określonymi parametrami, takimi jak czcionka, rozmiar, funkcja obsługująca (button_press) i inne.
# Umieszczanie przycisków w ramce:

# button.grid(row=5, column=2) umieszcza przycisk w określonym wierszu i kolumnie w ramce calculator.
# Tworzenie przycisków i umieszczanie ich w ramce odbywa się dla wszystkich przycisków liczbowych, kropki, operacji matematycznych (+, -, *, /), przycisku równości (=) oraz przycisków czyszczenia (C, CE).

# Uruchamianie pętli głównej:

# window.mainloop() uruchamia główną pętlę programu, która obsługuje zdarzenia i utrzymuje interfejs kalkulatora w trybie pracy, dopóki użytkownik nie zamknie okna.
# To jest ogólny opis działania tego kodu. Każda metoda w klasie Calculator obsługuje odpowiednie zdarzenia i aktualizuje interfejs kalkulatora w zależności od wprowadzanych danych i wykonywanych operacji matematycznych.
# #