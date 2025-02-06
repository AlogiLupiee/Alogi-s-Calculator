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

def klikend(): 
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

przyciskplus = Button(tk, width = 6, height = 3, text = "+", command = lambda: klikend())
przyciskplus.grid(column = 2, row = 2)

przyciskend = Button(tk, width = 6, height = 3, text = "=", command = lambda: klikprint())
przyciskend.grid(column = 2, row = 1)

mainloop()