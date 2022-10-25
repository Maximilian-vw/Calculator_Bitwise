from tkinter import *
 

#coding untuk logic
expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
 
 
def samadengan():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set(" error ")
        expression = ""
 
 

def hapus():
    global expression
    expression = ""
    equation.set("")
 
 
# coding tampilan
if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light blue")
    gui.title("Vivin_Calculator_GUI")
    gui.geometry("330x160")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=5, ipadx=100)
 
    #coding untuk tombol
    tombol1 = Button(gui, text=' 1 ', fg='black', bg='white',
                    command=lambda: press(1), height=1, width=7)
    tombol1.grid(row=2, column=0)
 
    tombol2 = Button(gui, text=' 2 ', fg='black', bg='white',
                    command=lambda: press(2), height=1, width=7)
    tombol2.grid(row=2, column=1)
 
    tombol3 = Button(gui, text=' 3 ', fg='black', bg='white',
                    command=lambda: press(3), height=1, width=7)
    tombol3.grid(row=2, column=2)
 
    tombol4 = Button(gui, text=' 4 ', fg='black', bg='white',
                    command=lambda: press(4), height=1, width=7)
    tombol4.grid(row=3, column=0)
 
    tombol5 = Button(gui, text=' 5 ', fg='black', bg='white',
                    command=lambda: press(5), height=1, width=7)
    tombol5.grid(row=3, column=1)
 
    tombol6 = Button(gui, text=' 6 ', fg='black', bg='white',
                    command=lambda: press(6), height=1, width=7)
    tombol6.grid(row=3, column=2)
 
    tombol7 = Button(gui, text=' 7 ', fg='black', bg='white',
                    command=lambda: press(7), height=1, width=7)
    tombol7.grid(row=4, column=0)
 
    tombol8 = Button(gui, text=' 8 ', fg='black', bg='white',
                    command=lambda: press(8), height=1, width=7)
    tombol8.grid(row=4, column=1)
 
    tombol9 = Button(gui, text=' 9 ', fg='black', bg='white',
                    command=lambda: press(9), height=1, width=7)
    tombol9.grid(row=4, column=2)
 
    tombol0 = Button(gui, text=' 0 ', fg='black', bg='white',
                    command=lambda: press(0), height=1, width=7)
    tombol0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ', fg='black', bg='seashell2',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='seashell2',
                command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='black', bg='seashell2',
                    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='black', bg='seashell2',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    AND = Button(gui, text=' & ', fg='black', bg='seashell2',
                    command=lambda: press("&"), height=1, width=7)
    AND.grid(row=6, column=0)

    OR = Button(gui, text=' | ', fg='black', bg='seashell2',
                    command=lambda: press("|"), height=1, width=7)
    OR.grid(row=6, column=1)

    NOT = Button(gui, text=' ~ ', fg='black', bg='seashell2',
                    command=lambda: press("~"), height=1, width=7)
    NOT.grid(row=6, column=2)

    XOR = Button(gui, text=' ^ ', fg='black', bg='seashell2',
                    command=lambda: press("^"), height=1, width=7)
    XOR.grid(row=6, column=3)

    Left_Shift = Button(gui, text=' << ', fg='black', bg='seashell2',
                    command=lambda: press("<<"), height=1, width=7)
    Left_Shift.grid(row=3, column=4)

    modulus = Button(gui, text=' % ', fg='black', bg='seashell2',
                    command=lambda: press("%"), height=1, width=7)
    modulus.grid(row=5, column=4)

    Right_Shift = Button(gui, text=' >> ', fg='black', bg='seashell2',
                    command=lambda: press(">>"), height=1, width=7)
    Right_Shift.grid(row=4, column=4)
    
    equal = Button(gui, text=' = ', fg='black', bg='seashell3',
                command=samadengan, height=1, width=7)
    equal.grid(row=6, column=4)
 
    hapus = Button(gui, text='Hapus', fg='black', bg='seashell3',
                command=hapus, height=1, width=7)
    hapus.grid(row=2, column=4)
 
    Decimal= Button(gui, text=',', fg='black', bg='white',
                    command=lambda: press(','), height=1, width=7)
    Decimal.grid(row=5, column=1)

    Decimal= Button(gui, text='.', fg='black', bg='white',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=5, column=2)

    #memulai gui dengan codingan ini 
    gui.mainloop()
