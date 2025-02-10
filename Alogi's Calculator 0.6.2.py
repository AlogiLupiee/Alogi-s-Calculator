from tkinter import *

num1 = []
num2 = []
change = None
joinnum1 = None
joinnum2 = None
numlist1 = None
numlist2 = None
result = None
operator = None
color = 'snow'

def clickcolor():
    global color
    if color == 'snow':
        color = 'black'
        tk.config(padx=200, pady=50, bg = 'black')
    elif color == 'black':
        color = 'snow'
        tk.config(padx=200, pady=50, bg = 'snow')

def click1():
    if change == True:
        num2.append('1')
        print("1")
    else:
        num1.append('1')
        print("1")

def click2():
    if change == True:
        num2.append('2')
        print("2")
    else:
        num1.append('2')
        print("2")

def click3():
    if change == True:
        num2.append('3')
        print("3")
    else:
        num1.append('3')
        print("3")

def click4():
    if change == True:
        num2.append('4')
        print("4")
    else:
        num1.append('4')
        print("4")

def click5():
    if change == True:
        num2.append('5')
        print("5")
    else:
        num1.append('5')
        print("5")

def click6():
    if change == True:
        num2.append('6')
        print("6")
    else:
        num1.append('6')
        print("6")

def click7():
    if change == True:
        num2.append('7')
        print("7")
    else:
        num1.append('7')
        print("7")

def click8():
    if change == True:
        num2.append('8')
        print("8")
    else:
        num1.append('8')
        print("8")

def click9():
    if change == True:
        num2.append('9')
        print("9")
    else:
        num1.append('9')
        print("9")

def click0():
    if change == True:
        num2.append('0')
        print("0")
    else:
        num1.append('0')
        print("0")
 
def clickp(): 
    global change
    global operator
    change = True
    operator = "+"
    print("+")

def clickm(): 
    global change
    global operator
    change = True
    operator = "-"
    print("-")

def clickr(): 
    global change
    global operator
    change = True
    operator = "*"
    print("*")

def clickd(): 
    global change
    global operator
    change = True
    operator = "/"
    print("/")

def clickpp():
    global change
    global operator
    change = True
    operator = "**"
    print("**")

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

def clickexit():
    exit(0)

def clickprint():
    d = ""
    numlist1 = map(str, num1)
    joinnum1 = d.join(numlist1)
    numlist2 = map(str, num2)
    joinnum2 = d.join(numlist2)
    if operator == "+" :
        result = int(joinnum1) + int(joinnum2)
        print("=")
        print(result)
    elif operator == "-" :
        result = int(joinnum1) - int(joinnum2)
        print("=")
        print(result)
    elif operator == "*":
        result = int(joinnum1) * int(joinnum2)
        print("=")
        print(result)
    elif operator == "**":
        result = int(joinnum1) ** int(joinnum2)
        print("=")
        print(result)
    elif operator == "/":
        if int(joinnum2) == 0:
            print("Error! You can't divide by 0.")
        else:
            result = int(joinnum1) / int(joinnum2)
            print("=")
            print(float(result))

tk = Tk()
tk.title("Alogi's Calculator 0.6.2")
tk.config(padx=200, pady=50, bg = 'snow')

button1 = Button(tk, width = 3, height = 3, text = "1", command = lambda: click1())
button1.grid(column = 1, row = 1)

button2 = Button(tk, width = 3, height = 3, text = "2", command = lambda: click2())
button2.grid(column = 1, row = 2)

button3 = Button(tk, width = 3, height = 3, text = "3", command = lambda: click3())
button3.grid(column = 1, row = 3)

button4 = Button(tk, width = 3, height = 3, text = "4", command = lambda: click4())
button4.grid(column = 2, row = 1)

button5 = Button(tk, width = 3, height = 3, text = "5", command = lambda: click5())
button5.grid(column = 2, row = 2)

button6 = Button(tk, width = 3, height = 3, text = "6", command = lambda: click6())
button6.grid(column = 2, row = 3)

button7 = Button(tk, width = 3, height = 3, text = "7", command = lambda: click7())
button7.grid(column = 3, row = 1)

button8 = Button(tk, width = 3, height = 3, text = "8", command = lambda: click8())
button8.grid(column = 3, row = 2)

button8 = Button(tk, width = 3, height = 3, text = "9", command = lambda: click9())
button8.grid(column = 3, row = 3)

button0 = Button(tk, width = 3, height = 3, text = "0", command = lambda: click0())
button0.grid(column = 2, row = 4)

buttonplus = Button(tk, width = 6, height = 3, text = "+", command = lambda: clickp())
buttonplus.grid(column = 4, row = 2)

buttonminus = Button(tk, width = 6, height = 3, text = "-", command = lambda: clickm())
buttonminus.grid(column = 4, row = 3)

buttonmulti = Button(tk, width = 6, height = 3, text = "*", command = lambda: clickr())
buttonmulti.grid(column = 5, row = 1)

buttondiv = Button(tk, width = 6, height = 3, text = "/", command = lambda: clickd())
buttondiv.grid(column = 5, row = 2)

buttonpower = Button(tk, width = 6, height = 3, text = "**", command = lambda: clickpp())
buttonpower.grid(column = 5, row = 3)

buttonC = Button(tk, width = 6, height = 3, text = "C", command = lambda: clickC())
buttonC.grid(column = 6, row = 1)

buttonexit = Button(tk, width = 6, height = 3, text = "Exit", command = lambda: clickexit())
buttonexit.grid(column = 6, row = 2)

buttonend = Button(tk, width = 6, height = 3, text = "=", command = lambda: clickprint())
buttonend.grid(column = 4, row = 1)

buttoncolor = Button(tk, width = 6, height = 3, text = "L/D", command = lambda: clickcolor())
buttoncolor.grid(column = 6, row = 3)


mainloop()

# change log 0.6.2:
# - added light and dark mode (to bo improved)
# To do:
# - add a proper display