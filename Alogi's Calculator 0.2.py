from tkinter import *

tk = Tk()
tk.title("Kalkulator")
tk.config(padx=200, pady=50)

liczb1 = []
liczb2 = []
zmiana = None
joinnum1 = None
joinnum2 = None
numlist1 = None
numlist2 = None
wynik = None

def klik1():
    if zmiana == True:
        liczb2.append('1')
        print("1")
    else:
        liczb1.append('1')
        print("1")

def klik2():
    if zmiana == True:
        liczb2.append('2')
        print("2")
    else:
        liczb1.append('2')
        print("2")

def klik3():
    if zmiana == True:
        liczb2.append('3')
        print("3")
    else:
        liczb1.append('3')
        print("3")

def klik4():
    if zmiana == True:
        liczb2.append('4')
        print("4")
    else:
        liczb1.append('4')
        print("4")

def klik5():
    if zmiana == True:
        liczb2.append('5')
        print("5")
    else:
        liczb1.append('5')
        print("5")

def klik6():
    if zmiana == True:
        liczb2.append('6')
        print("6")
    else:
        liczb1.append('6')
        print("6")

def klik7():
    if zmiana == True:
        liczb2.append('7')
        print("7")
    else:
        liczb1.append('7')
        print("7")

def klik8():
    if zmiana == True:
        liczb2.append('8')
        print("8")
    else:
        liczb1.append('8')
        print("8")

def klik9():
    if zmiana == True:
        liczb2.append('9')
        print("9")
    else:
        liczb1.append('9')
        print("9")

def klik0():
    if zmiana == True:
        liczb2.append('0')
        print("0")
    else:
        liczb1.append('0')
        print("0")
 
def klikp(): 
    global zmiana
    zmiana = True
    print("+")

def klikm(): 
    global zmiana
    zmiana = True
    print("+")
 
def klikprint():
    d = ""
    numlist1 = map(str, liczb1)
    joinnum1 = d.join(numlist1)
    numlist2 = map(str, liczb2)
    joinnum2 = d.join(numlist2)
    wynik = int(joinnum1) + int(joinnum2)
    print("=")
    print(wynik)

przycisk1 = Button(tk, width = 3, height = 3, text = "1", command = lambda: klik1())
przycisk1.grid(column = 1, row = 1)

przycisk2 = Button(tk, width = 3, height = 3, text = "2", command = lambda: klik2())
przycisk2.grid(column = 1, row = 2)

przycisk3 = Button(tk, width = 3, height = 3, text = "3", command = lambda: klik3())
przycisk3.grid(column = 1, row = 3)

przycisk4 = Button(tk, width = 3, height = 3, text = "4", command = lambda: klik4())
przycisk4.grid(column = 2, row = 1)

przycisk5 = Button(tk, width = 3, height = 3, text = "5", command = lambda: klik5())
przycisk5.grid(column = 2, row = 2)

przycisk6 = Button(tk, width = 3, height = 3, text = "6", command = lambda: klik6())
przycisk6.grid(column = 2, row = 3)

przycisk7 = Button(tk, width = 3, height = 3, text = "7", command = lambda: klik7())
przycisk7.grid(column = 3, row = 1)

przycisk8 = Button(tk, width = 3, height = 3, text = "8", command = lambda: klik8())
przycisk8.grid(column = 3, row = 2)

przycisk8 = Button(tk, width = 3, height = 3, text = "9", command = lambda: klik9())
przycisk8.grid(column = 3, row = 3)

przycisk0 = Button(tk, width = 3, height = 3, text = "0", command = lambda: klik0())
przycisk0.grid(column = 2, row = 4)

przyciskplus = Button(tk, width = 6, height = 3, text = "+", command = lambda: klikp())
przyciskplus.grid(column = 4, row = 2)

przyciskminus = Button(tk, width = 6, height = 3, text = "-", command = lambda: klikm())
przyciskminus.grid(column = 4, row = 3)

przyciskend = Button(tk, width = 6, height = 3, text = "=", command = lambda: klikprint())
przyciskend.grid(column = 4, row = 1)

mainloop()

#change log 0.2
# - dodano liczby 2, 3, 4, 5, 6, 7, 8, 9, 0
# - z optymalizowano kalkulację wyniku
# - zmieniono pozycje przycisków
#
#
#
#
#
#