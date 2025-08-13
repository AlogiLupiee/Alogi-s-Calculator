from tkinter import *
from webbrowser import open_new

tk = Tk()
tk.title("Alogi's Enchanced Calculator 0.3")
tk.config(padx=200, pady=50, bg = 'azure2')

for i in range(8):
    tk.grid_columnconfigure(i, weight = 1)
for i in range(4):
    tk.grid_rowconfigure(i, weight = 1)

var1 = StringVar()
color = 'azure2'
result_str = ""
result = ""

def clickcolor():
    global color
    if color == 'azure2':
        color = 'grey17'
        tk.config(padx=200, pady=50, bg = 'grey17')
        label1.config(bg = 'grey17')
    elif color == 'grey17':
        color = 'azure2'
        tk.config(padx=200, pady=50, bg = 'azure2')
        label1.config(bg = 'azure2')

def click1():
    global result_str
    result_str = f"{result_str}1"
    var1.set(result_str)

def click2():
    global result_str
    result_str = f"{result_str}2"
    var1.set(result_str)

def click3():
    global result_str
    result_str = f"{result_str}3"
    var1.set(result_str)

def click4():
    global result_str
    result_str = f"{result_str}4"
    var1.set(result_str)

def click5():
    global result_str
    result_str = f"{result_str}5"
    var1.set(result_str)

def click6():
    global result_str
    result_str = f"{result_str}6"
    var1.set(result_str)

def click7():
    global result_str
    result_str = f"{result_str}7"
    var1.set(result_str)

def click8():
    global result_str
    result_str = f"{result_str}8"
    var1.set(result_str)

def click9():
    global result_str
    result_str = f"{result_str}9"
    var1.set(result_str)

def click0():
    global result_str
    result_str = f"{result_str}0"
    var1.set(result_str)

def click00():
    global result_str
    result_str = f"{result_str}00"
    var1.set(result_str)

def clickp():
    global result_str
    result_str = f"{result_str}+"
    var1.set(result_str)

def clickm():
    global result_str
    result_str = f"{result_str}-"
    var1.set(result_str)

def clickr():
    global result_str
    result_str = f"{result_str}*"
    var1.set(result_str)

def clickd():
    global result_str
    result_str = f"{result_str}/"
    var1.set(result_str)

def clickpp():
    global result_str
    result_str = f"{result_str}**"
    var1.set(result_str)

def clicksqrt():
    global result_str
    result_str = f"{result_str}**(1/2)"
    var1.set(result_str)

def clickC():
    global result, result_str
    result = ""
    result_str = ""
    var1.set("")

def clickprint():
    try:
        global result, var1
        result = eval(result_str)
        var1.set(f"{result_str}={result}")
    except ZeroDivisionError:
        clickC()
        var1.set("Can't divide by 0")
    except ValueError as e:
        clickC()
        var1.set(f"Error: {e}")
    except Exception as e:
        clickC()
        var1.set(f"Error: {e}")

button1 = Button(tk, width = 6, height = 3, text = "1", command = lambda: click1(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button1.grid(column = 1, row = 1, sticky = "nsew")

button2 = Button(tk, width = 6, height = 3, text = "2", command = lambda: click2(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button2.grid(column = 2, row = 1, sticky = "nsew")

button3 = Button(tk, width = 6, height = 3, text = "3", command = lambda: click3(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button3.grid(column = 3, row = 1, sticky = "nsew")

button4 = Button(tk, width = 6, height = 3, text = "4", command = lambda: click4(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button4.grid(column = 1, row = 2, sticky = "nsew")

button5 = Button(tk, width = 6, height = 3, text = "5", command = lambda: click5(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button5.grid(column = 2, row = 2, sticky = "nsew")

button6 = Button(tk, width = 6, height = 3, text = "6", command = lambda: click6(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button6.grid(column = 3, row = 2, sticky = "nsew")

button7 = Button(tk, width = 6, height = 3, text = "7", command = lambda: click7(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button7.grid(column = 1, row = 3, sticky = "nsew")

button8 = Button(tk, width = 6, height = 3, text = "8", command = lambda: click8(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button8.grid(column = 2, row = 3, sticky = "nsew")

button9 = Button(tk, width = 6, height = 3, text = "9", command = lambda: click9(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button9.grid(column = 3, row = 3, sticky = "nsew")

button0 = Button(tk, width = 6, height = 3, text = "0", command = lambda: click0(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button0.grid(column = 4, row = 2, sticky = "nsew")

button00 = Button(tk, width = 6, height = 3, text = "00", command = lambda: click00(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button00.grid(column = 4, row = 3, sticky = "nsew")

buttonplus = Button(tk, width = 6, height = 3, text = "+", command = lambda: clickp(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonplus.grid(column = 7, row = 1, sticky = "nsew")

buttonminus = Button(tk, width = 6, height = 3, text = "-", command = lambda: clickm(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonminus.grid(column = 6, row = 1, sticky = "nsew")

buttonmulti = Button(tk, width = 6, height = 3, text = "*", command = lambda: clickr(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonmulti.grid(column = 7, row = 2, sticky = "nsew")

buttondiv = Button(tk, width = 6, height = 3, text = "/", command = lambda: clickd(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttondiv.grid(column = 6, row = 2, sticky = "nsew")

buttonpower = Button(tk, width = 6, height = 3, text = "x²", command = lambda: clickpp(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonpower.grid(column = 6, row = 3, sticky = "nsew")

buttonsqrt = Button(tk, width = 6, height = 3, text = "√x", command = lambda: clicksqrt(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonsqrt.grid(column = 7, row = 3, sticky = "nsew")

buttonC = Button(tk, width = 6, height = 3, text = "C", command = lambda: clickC(), bg = 'red3', fg = 'black', activebackground = 'red')
buttonC.grid(column = 4, row = 1, sticky = "nsew")

buttonend = Button(tk, width = 6, height = 11, text = "=", command = lambda: clickprint(), bg = 'green3', fg = 'black', activebackground = 'light slate gray')
buttonend.grid(column = 8, row = 1, rowspan = 3, sticky = "nsew")

label1 = Label(tk, textvariable = var1, bg = "azure2", border = 1, borderwidth = 2, relief = "groove", wraplength = 340)
label1.grid(column = 1, row = 0, columnspan = 8, sticky = 'ew')

menu = Menu(tk)
tk.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "Menu", menu = filemenu)
filemenu.add_command(label = 'Exit', command = tk.quit)
filemenu.add_command(label = 'Color mode', command = lambda: clickcolor())
filemenu.add_command(label = 'About me', command = lambda: open_new('https://github.com/AlogiLupiee'))

mainloop()

# change log 0.3:
# - fixed cosmetic bugs
# - added widget resizing respectfully to the window size
# - fixed the screen
# To do:
# - turn the 5 displays into one ✓
# - multiple operations in one go (main goal) ✓
# - add different modes to the app