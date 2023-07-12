import tkinter

window = tkinter.Tk()
window.title("lOL")
window.geometry('800x100')



sample_text = tkinter.Entry(window)
sample_text.pack()

def set_text_by_button():
    
    sample_text.delete(0,'end')

    sample_text.insert(0, set_up_button.text)

set_up_button = tkinter.Button(window,
                               height=1,
                               width= 10,
                               text = 0,
                               command = set_text_by_button)

set_up_button.text
set_up_button.pack()


set_up_button1 = tkinter.Button(window,
                               height=1,
                               width= 10,
                               text = 1,
                               command = set_text_by_button)

set_up_button1.pack()

window.mainloop()


