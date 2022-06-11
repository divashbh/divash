from re import sub
from tkinter import*
from tkinter import END, Entry
import tkinter.font as font

root= Tk()
root.iconbitmap("we.ico")
root.title("CALCULATOR")
root.geometry('300x480')
myFont = font.Font(family='Helvetica',)
e= Entry(root,  width=26, borderwidth=10, fg="white",bg="black" ,font= myFont)

e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current= e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number=e.get()
    global result
    result= "add"
    global f_num
    f_num =int(first_number)
    e.delete(0,END)

def button_subtract():
    global result
    result= "subtract"
    second_number=e.get()
    global g_num
    g_num= int(second_number)
    e.delete(0,END)

def button_multiply():
    global result
    global m_num
    result="multiply"
    second_number= e.get()
    m_num= int(second_number)
    e.delete(0,END)

def button_divide():
    global result
    global d_num
    result="divide"
    second_number= e.get()
    d_num= int(second_number)
    e.delete(0,END)

def button_modulo():
    global result
    global e_num
    result="modulo"
    second_number= e.get()
    e_num= int(second_number)
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    
    if result =="add":
        e.insert(0, f_num + int(second_number))
    
    elif result== "subtract":
        e.insert(0, g_num-int(second_number) )
    
    elif result== "multiply":
        e.insert(0, m_num*int(second_number) )
    
    elif result== "divide":
        if d_num==0:
            e.insert(0,'ERROR')
        else:
            e.insert(0, d_num/int(second_number) )
    
    elif result== "modulo":
        e.insert(0 , e_num % int(second_number) )
    

# 
button_1= Button(root, text="1", padx=40, pady=20, command = lambda : button_click(1), bg="#e6ffff" ,font= myFont)

button_2= Button(root, text="2", padx=40, pady=20, command = lambda : button_click(2), bg="#e6ffff" ,font= myFont)

button_3= Button(root, text="3", padx=40, pady=20, command = lambda : button_click(3), bg="#e6ffff" ,font= myFont)

button_4= Button(root, text="4", padx=40, pady=20, command = lambda : button_click(4), bg="#e6ffff" ,font= myFont)

button_5= Button(root, text="5", padx=40, pady=20, command = lambda : button_click(5), bg="#e6ffff" ,font= myFont)

button_6= Button(root, text="6", padx=40, pady=20, command = lambda : button_click(6), bg="#e6ffff" ,font= myFont)

button_7= Button(root, text="7", padx=40, pady=20, command = lambda : button_click(7), bg="#e6ffff" ,font= myFont)

button_8= Button(root, text="8", padx=40, pady=20, command = lambda : button_click(8), bg="#e6ffff" ,font= myFont)

button_9= Button(root, text="9", padx=40, pady=20, command = lambda : button_click(9), bg="#e6ffff" ,font= myFont)

button_0= Button(root, text="0", padx=40, pady=20, command = lambda : button_click(0), bg="#e6ffff" ,font= myFont)

button_add= Button(root, text="+", padx=39, pady=20, command = button_add, bg="#e6ffff" ,font= myFont)

button_equal= Button(root, text="=", padx=89, pady=20, command =  button_equal, bg="#e6ffff" ,font= myFont)

button_clear= Button(root, text="AC", padx=34, pady=20, command = button_clear, bg="#e6ffff" ,font= myFont)

button_subtract= Button(root, text="-", padx=40, pady=20, command = button_subtract, bg="#e6ffff" ,font= myFont)

button_multiply= Button(root, text= "X", padx=40, pady=20, command= button_multiply , bg="#e6ffff" ,font= myFont)

button_divide= Button(root, text= "/", padx=40, pady=20, command= button_divide, bg="#e6ffff" ,font= myFont)

button_modulo= Button(root, text= "%", padx=35, pady=20, command= button_modulo, bg="#e6ffff" ,font= myFont)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clear.place(x=101, y=270)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1,columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_modulo.grid(row=4, column=2)
root.mainloop()



