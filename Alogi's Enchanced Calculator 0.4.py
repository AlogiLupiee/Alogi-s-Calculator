from tkinter import *
from webbrowser import open_new

# main window properties
tk = Tk()
tk.title("Alogi's Enchanced Calculator 0.4")
tk.config(padx=200, pady=50, bg = 'azure2')

# this allows widget resizing
for i in range(8):
    tk.grid_columnconfigure(i, weight = 1)
for i in range(5):
    tk.grid_rowconfigure(i, weight = 1)

# variables
var1 = StringVar()
color = 'azure2'
result_str = ""
result = ""
mode = "normal"
mode_step = 1
a = None
b = None
h = None
result_r = ""

# changes the color mode
def clickcolor():
    global color
    if color == 'azure2':
        color = 'grey17'
        tk.config(padx=200, pady=50, bg = 'grey17')
        label1.config(bg = 'grey17', fg = 'azure2')
    elif color == 'grey17':
        color = 'azure2'
        tk.config(padx=200, pady=50, bg = 'azure2')
        label1.config(bg = 'azure2', fg = 'black')

# adds char to the end of result_str
def click(char):
    global result_str
    if "=" in var1.get():
        result_str = ""
    result_str = f"{result_str}{char}"
    var1.set(result_str)

# deletes the last character
def del_last():
    global result_str
    if "=" in var1.get():
        result_str = ""
    else:
        result_str = result_str[:-1]
    var1.set(result_str)

# wipes all data and resets the calculator
def clickC():
    global result, result_str, a, b, h, mode_step, result_r
    result = ""
    result_str = ""
    var1.set("")
    a = None
    b = None
    h = None
    mode_step = 1
    result_r = ""
    if mode == "triangle":
        var1.set("input a, then click '=' : ")

# calculates the equation and handles modes
def clickprint():
    global result, result_str, mode_step, a, b, h, result_r, mode
    if mode == "normal":
        # normal eqations
        try:
            result = eval(result_str)
            var1.set(f"{result_str}={result}")
        except ZeroDivisionError:
            clickC()
            var1.set("Can't divide by 0")
        except Exception as e:
            clickC()
            var1.set(f"Error: {e}")
    elif mode == "triangle":
        # calculates the area of a triangle 
        try:
            if mode_step == 1:
                a = result_str
                result_str = ""
                mode_step += 1
                var1.set("input h, then click '=' : ")
            elif mode_step == 2:
                h = result_str
                result_str = ""
                result_r = f"({a})*({h})/2"
                result = eval(result_r)
                var1.set(f"The area of the triangle is: {result}")
                mode = "normal"
        except Exception as e:
            clickC()
            var1.set(f"Error: {e}")
    elif mode == "rectangle":
        # calculates the area of a rectangle; uses a^2 if it detects a square
        try:
            if mode_step == 1:
                a = result_str
                result_str = ""
                mode_step +=1
                var1.set("input b, then click '=' : ")
            elif mode_step == 2:
                b = result_str
                result_str = ""
                if b == a:
                    result_r = f"({a})**2"
                else:
                    result_r = f"({a})*({b})"
                result = eval(result_r)
                var1.set(f"The area of the rectangle is: {result}")
                mode = "normal"
        except Exception as e:
            clickC()
            var1.set(f"Error: {e}")
    elif mode == "trapezoid":
        # calculates the area of a trapezoid
        try:
            if mode_step == 1:
                a = result_str
                result_str = ""
                mode_step += 1
                var1.set("input b, then click '=' : ")
            elif mode_step == 2:
                b = result_str
                result_str = ""
                mode_step += 1
                var1.set("input h, then click '=' : ")
            elif mode_step == 3:
                h = result_str
                result_str = ""
                result_r = f"(({a})+({b}))*({h})/2"
                result = eval(result_r)
                var1.set(f"The area of the trapezoid is: {result}")
                mode = "normal"
        except Exception as e:
            clickC()
            var1.set(f"Error: {e}")

def activ_nrml():
    global mode
    mode = "normal"
    clickC()

def activ_tri():
    global mode
    mode = "triangle"
    clickC()
    var1.set("input a, then click '=' : ")

def activ_rec():
    global mode
    mode = "rectangle"
    clickC()
    var1.set("input a, then click '=' : ")

def activ_tpz():
    global mode
    mode = "Trapezoid"
    clickC()
    var1.set("input a, then click '=' : ")

button1 = Button(tk, width = 6, height = 3, text = "1", command = lambda: click("1"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button1.grid(column = 1, row = 1, sticky = "nsew")

button2 = Button(tk, width = 6, height = 3, text = "2", command = lambda: click("2"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button2.grid(column = 2, row = 1, sticky = "nsew")

button3 = Button(tk, width = 6, height = 3, text = "3", command = lambda: click("3"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button3.grid(column = 3, row = 1, sticky = "nsew")

button4 = Button(tk, width = 6, height = 3, text = "4", command = lambda: click("4"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button4.grid(column = 1, row = 2, sticky = "nsew")

button5 = Button(tk, width = 6, height = 3, text = "5", command = lambda: click("5"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button5.grid(column = 2, row = 2, sticky = "nsew")

button6 = Button(tk, width = 6, height = 3, text = "6", command = lambda: click("6"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button6.grid(column = 3, row = 2, sticky = "nsew")

button7 = Button(tk, width = 6, height = 3, text = "7", command = lambda: click("7"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button7.grid(column = 1, row = 3, sticky = "nsew")

button8 = Button(tk, width = 6, height = 3, text = "8", command = lambda: click("8"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button8.grid(column = 2, row = 3, sticky = "nsew")

button9 = Button(tk, width = 6, height = 3, text = "9", command = lambda: click("9"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button9.grid(column = 3, row = 3, sticky = "nsew")

button0 = Button(tk, width = 6, height = 3, text = "0", command = lambda: click("0"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button0.grid(column = 1, row = 4, sticky = "nsew")

button00 = Button(tk, width = 6, height = 3, text = "00", command = lambda: click("00"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button00.grid(column = 2, row = 4, sticky = "nsew")

button000 = Button(tk, width = 6, height = 3, text = "000", command = lambda: click("000"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button000.grid(column = 3, row = 4, sticky = "nsew")

buttonplus = Button(tk, width = 6, height = 3, text = "+", command = lambda: click("+"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonplus.grid(column = 7, row = 1, sticky = "nsew")

buttonminus = Button(tk, width = 6, height = 3, text = "-", command = lambda: click("-"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonminus.grid(column = 6, row = 1, sticky = "nsew")

buttonmulti = Button(tk, width = 6, height = 3, text = "*", command = lambda: click("*"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonmulti.grid(column = 7, row = 2, sticky = "nsew")

buttondiv = Button(tk, width = 6, height = 3, text = "/", command = lambda: click("/"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttondiv.grid(column = 6, row = 2, sticky = "nsew")

buttonpower = Button(tk, width = 6, height = 3, text = "Xʸ", command = lambda: click("**"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonpower.grid(column = 6, row = 3, sticky = "nsew")

buttonsqrt = Button(tk, width = 6, height = 3, text = "√x", command = lambda: click("**(1/2)"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonsqrt.grid(column = 7, row = 3, sticky = "nsew")

buttoncls = Button(tk, width = 6, height = 3, text = ")", command = lambda: click(")"), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttoncls.grid(column = 5, row = 3, sticky = "nsew")

buttonopn = Button(tk, width = 6, height = 3, text = "(", command = lambda: click("("), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonopn.grid(column = 5, row = 2, sticky = "nsew")

buttonC = Button(tk, width = 6, height = 3, text = "C", command = lambda: clickC(), bg = 'red3', fg = 'black', activebackground = 'red')
buttonC.grid(column = 5, row = 1, sticky = "nsew")

buttondel = Button(tk, width = 6, height = 8, text = "Back", command = lambda: del_last(), bg = 'red3', fg = 'black', activebackground = 'red')
buttondel.grid(column = 0, row = 1, rowspan = 2, sticky = "nsew")

buttonend = Button(tk, width = 6, height = 11, text = "=", command = lambda: clickprint(), bg = 'green3', fg = 'black', activebackground = 'light slate gray')
buttonend.grid(column = 8, row = 1, rowspan = 3, sticky = "nsew")

label1 = Label(tk, textvariable = var1, bg = "azure2", fg = "black", border = 1, borderwidth = 2, relief = "groove", wraplength = 340)
label1.grid(column = 1, row = 0, columnspan = 8, sticky = 'ew')

menu = Menu(tk)
tk.config(menu = menu)
filemenu = Menu(menu)
modemenu = Menu(menu)
menu.add_cascade(label = "Menu", menu = filemenu)
menu.add_cascade(label = "Mode", menu = modemenu)
filemenu.add_command(label = 'Exit', command = tk.quit)
filemenu.add_command(label = 'Color mode', command = lambda: clickcolor())
filemenu.add_command(label = 'About me', command = lambda: open_new('https://github.com/AlogiLupiee'))
modemenu.add_cascade(label = "Normal mode", command = lambda: activ_nrml())
modemenu.add_cascade(label = "Triangle mode", command = lambda: activ_tri())
modemenu.add_cascade(label = "Rectangle mode", command = lambda: activ_rec())
modemenu.add_cascade(label = "Trapezoid mode", command = lambda: activ_tpz())

mainloop()

# change log 0.4:
# - added modes
# - added backspace button
# - optimized the functions for buttons
# To do:
# - turn the 5 displays into one ✓
# - multiple operations in one go (main goal) ✓
# - add different modes to the app ✓