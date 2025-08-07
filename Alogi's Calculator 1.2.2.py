from tkinter import *
from webbrowser import open_new

tk = Tk()
tk.title("Alogi's Calculator 1.2.1")
tk.config(padx=200, pady=50, bg = 'azure2')

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()

num1 = []
num2 = []
change = None
joinnum1 = None
joinnum2 = None
numlist1 = None
numlist2 = None
result = None
operator = None
color = 'azure2'

def clickcolor():
    global color
    if color == 'azure2':
        color = 'grey17'
        tk.config(padx=200, pady=50, bg = 'grey17')
    elif color == 'grey17':
        color = 'azure2'
        tk.config(padx=200, pady=50, bg = 'azure2')

def click1():
    if change:
        d = ""
        num2.append('1')
        numlist2 = map(str, num2)
        joinnum2 = d.join(numlist2)
        var3.set(joinnum2)
    else:
        num1.append('1')
        d = ""
        numlist1 = map(str, num1)
        joinnum1 = d.join(numlist1)
        var1.set(joinnum1)

def click2():
    if change:
        d = ""
        num2.append('2')
        numlist2 = map(str, num2)
        joinnum2 = d.join(numlist2)
        var3.set(joinnum2)
    else:
        num1.append('2')
        d = ""
        numlist1 = map(str, num1)
        joinnum1 = d.join(numlist1)
        var1.set(joinnum1)

def click3():
    if change:
        d = ""
        num2.append('3')
        numlist2 = map(str, num2)
        joinnum2 = d.join(numlist2)
        var3.set(joinnum2)
    else:
        num1.append('3')
        d = ""
        numlist1 = map(str, num1)
        joinnum1 = d.join(numlist1)
        var1.set(joinnum1)

def click4():
    if change:
        d = ""
        num2.append('4')
        numlist2 = map(str, num2)
        joinnum2 = d.join(numlist2)
        var3.set(joinnum2)
    else:
        num1.append('4')
        d = ""
        numlist1 = map(str, num1)
        joinnum1 = d.join(numlist1)
        var1.set(joinnum1)

def click5():
    if change:
        d = ""
        num2.append('5')
        numlist2 = map(str, num2)
        joinnum2 = d.join(numlist2)
        var3.set(joinnum2)
    else:
        num1.append('5')
        d = ""
        numlist1 = map(str, num1)
        joinnum1 = d.join(numlist1)
        var1.set(joinnum1)

def click6():
    if change:
        d = ""
        num2.append('6')
        numlist2 = map(str, num2)
        joinnum2 = d.join(numlist2)
        var3.set(joinnum2)
    else:
        num1.append('6')
        d = ""
        numlist1 = map(str, num1)
        joinnum1 = d.join(numlist1)
        var1.set(joinnum1)

def click7():
    if change:
        d = ""
        num2.append('7')
        numlist2 = map(str, num2)
        joinnum2 = d.join(numlist2)
        var3.set(joinnum2)
    else:
        num1.append('7')
        d = ""
        numlist1 = map(str, num1)
        joinnum1 = d.join(numlist1)
        var1.set(joinnum1)

def click8():
    if change:
        d = ""
        num2.append('8')
        numlist2 = map(str, num2)
        joinnum2 = d.join(numlist2)
        var3.set(joinnum2)
    else:
        num1.append('8')
        d = ""
        numlist1 = map(str, num1)
        joinnum1 = d.join(numlist1)
        var1.set(joinnum1)

def click9():
    if change:
        d = ""
        num2.append('9')
        numlist2 = map(str, num2)
        joinnum2 = d.join(numlist2)
        var3.set(joinnum2)
    else:
        num1.append('9')
        d = ""
        numlist1 = map(str, num1)
        joinnum1 = d.join(numlist1)
        var1.set(joinnum1)

def click0():
    if change:
        d = ""
        num2.append('0')
        numlist2 = map(str, num2)
        joinnum2 = d.join(numlist2)
        var3.set(joinnum2)
    else:
        num1.append('0')
        d = ""
        numlist1 = map(str, num1)
        joinnum1 = d.join(numlist1)
        var1.set(joinnum1)


def click00():
    if change:
        d = ""
        num2.append('00')
        numlist2 = map(str, num2)
        joinnum2 = d.join(numlist2)
        var3.set(joinnum2)
    else:
        num1.append('00')
        d = ""
        numlist1 = map(str, num1)
        joinnum1 = d.join(numlist1)
        var1.set(joinnum1)

def clickp(): 
    global change
    global operator
    change = True
    operator = "+"
    var2.set(operator)

def clickm(): 
    global change
    global operator
    change = True
    operator = "-"
    var2.set(operator)

def clickr(): 
    global change
    global operator
    change = True
    operator = "*"
    var2.set(operator)

def clickd(): 
    global change
    global operator
    change = True
    operator = "/"
    var2.set(operator)

def clickpp():
    global change
    global operator
    change = True
    operator = "**"
    var2.set(operator)

def clickC():
    global num1
    global num2
    global change
    global joinnum1
    global joinnum2
    global numlist1
    global numlist2
    global result
    global operator
    num1 = []
    num2 = []
    change = None
    joinnum1 = None
    joinnum2 = None
    numlist1 = None
    numlist2 = None
    result = None
    operator = None
    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")

def clickprint():
    d = ""
    numlist1 = map(str, num1)
    joinnum1 = d.join(numlist1)
    numlist2 = map(str, num2)
    joinnum2 = d.join(numlist2)
    
    if operator == "+" :
        result = int(joinnum1) + int(joinnum2)
        var4.set(result)
    elif operator == "-" :
        result = int(joinnum1) - int(joinnum2)
        var4.set(result)
    elif operator == "*":
        result = int(joinnum1) * int(joinnum2)
        var4.set(result)
    elif operator == "**":
        result = int(joinnum1) ** int(joinnum2)
        var4.set(result)
    elif operator == "/":
        try:
            result = int(joinnum1) / int(joinnum2)
            var4.set(result)
        except ZeroDivisionError:
            var4.set("Error!")

button1 = Button(tk, width = 3, height = 3, text = "1", command = lambda: click1(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button1.grid(column = 1, row = 2)

button2 = Button(tk, width = 3, height = 3, text = "2", command = lambda: click2(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button2.grid(column = 1, row = 3)

button3 = Button(tk, width = 3, height = 3, text = "3", command = lambda: click3(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button3.grid(column = 1, row = 4)

button4 = Button(tk, width = 3, height = 3, text = "4", command = lambda: click4(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button4.grid(column = 2, row = 2)

button5 = Button(tk, width = 3, height = 3, text = "5", command = lambda: click5(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button5.grid(column = 2, row = 3)

button6 = Button(tk, width = 3, height = 3, text = "6", command = lambda: click6(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button6.grid(column = 2, row = 4)

button7 = Button(tk, width = 3, height = 3, text = "7", command = lambda: click7(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button7.grid(column = 3, row = 2)

button8 = Button(tk, width = 3, height = 3, text = "8", command = lambda: click8(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button8.grid(column = 3, row = 3)

button9 = Button(tk, width = 3, height = 3, text = "9", command = lambda: click9(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button9.grid(column = 3, row = 4)

button0 = Button(tk, width = 3, height = 3, text = "0", command = lambda: click0(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button0.grid(column = 2, row = 5)

button00 = Button(tk, width = 3, height = 3, text = "00", command = lambda: click00(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
button00.grid(column = 3, row = 5)

buttonplus = Button(tk, width = 6, height = 3, text = "+", command = lambda: clickp(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonplus.grid(column = 4, row = 3)

buttonminus = Button(tk, width = 6, height = 3, text = "-", command = lambda: clickm(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonminus.grid(column = 4, row = 4)

buttonmulti = Button(tk, width = 6, height = 3, text = "*", command = lambda: clickr(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonmulti.grid(column = 5, row = 2)

buttondiv = Button(tk, width = 6, height = 3, text = "/", command = lambda: clickd(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttondiv.grid(column = 5, row = 3)

buttonpower = Button(tk, width = 6, height = 3, text = "**", command = lambda: clickpp(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonpower.grid(column = 5, row = 4)

buttonC = Button(tk, width = 6, height = 3, text = "C", command = lambda: clickC(), bg = 'slate gray', fg = 'light blue', activebackground = 'red')
buttonC.grid(column = 6, row = 2)

buttonend = Button(tk, width = 6, height = 3, text = "=", command = lambda: clickprint(), bg = 'slate gray', fg = 'light blue', activebackground = 'light slate gray')
buttonend.grid(column = 4, row = 2)

label1 = Label(tk, textvariable = var1, width = 7, height = 2)
label1.place(x = 45, y = -40)

label2 = Label(tk, textvariable = var2, width = 1, height = 2)
label2.place(x = 100, y = -40)

label3 = Label(tk, textvariable = var3, width = 7, height = 2)
label3.place(x = 110, y = -40)

label4 = Label(tk, text = "=", width = 1, height = 2)
label4.place(x = 155, y = -40)

label5 = Label(tk, textvariable = var4, width = 6, height = 2)
label5.place(x = 165, y = -40)

menu = Menu(tk)
tk.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "Menu", menu = filemenu)
filemenu.add_command(label = 'Exit', command = tk.quit)
filemenu.add_command(label = 'Color mode', command = lambda: clickcolor())
filemenu.add_command(label = 'About me', command = lambda: open_new('https://github.com/AlogiLupiee'))

mainloop()

# change log 1.2.1:
# - (1.2) error handlin from if to try
# - (1.2.1) updated change log and app title
# To do:
# - small cosmetic changes
# - major code improvement