"""to-do list:
- zoom funkcia
- orezanie obrázka  (dôležité)
- resize obrázka
- pridať viac objektov
- reorganizovať menu
- otočenie
- súbor: vlastnosti, o programe
- pridať redo(vrátenie vrátenia) - ako?
- vybrať sektor a vyfarbiť ho/vystrihnúť
- zlepšiť rozhranie pre písanie textu
- pridať vyfarbenie objektu/plochy
- vložiť označenie+zmazanie+vyfarbenie
- pridať VLOŽIŤ OBRÁZOK Z CLIPBOARDU
- opraviť scrollovanie
- pridať výber farby
- scrollovanie myšou
- menu pri pravom kliknutí
- preprogramovať celý program cez draw funkciu (namiesto save)   ---WIP---
SPOJIŤ PROGRAM S PYGAME
"""
from PIL import ImageGrab, ImageTk, Image, ImageDraw
import tkinter
from os import getenv, mkdir
from tkinter import colorchooser, simpledialog, filedialog, messagebox

#trieda vlastností
class Vlastnosti:
    hrubka = 4
    farba = "black"
    nastroj = "Ceruzka"
    pozadie = "white"
    vypln = False
    farbavypln = "black"
    poslednaklavesa = ""
    obrazky = []
    #kreslenie
    lastx = -1
    lasty = -1
    image = Image.new("RGB", (0,0))
    draw = ImageDraw.Draw(image)
    #ciara
    firstx = -1
    firsty = -1
    secondx = -1
    secondy = -1
    stav = 0
    #úpravy
    stack = []
    stack_vratene = []
    aktualnytag = 0
    posuvane = 0
    #scrollovanie
    scrollbars = False


#hlavný event kreslenia
def kresli(event):
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)
    if (Vlastnosti.lastx == -1):
        Vlastnosti.lastx = x
        Vlastnosti.lasty = y
    if (Vlastnosti.nastroj == "Ceruzka"):
        canvas.create_line(Vlastnosti.lastx, Vlastnosti.lasty, x, y,fill=Vlastnosti.farba,\
        width=Vlastnosti.hrubka,capstyle="round", smooth="TRUE", tag="n" + str(Vlastnosti.aktualnytag))
    elif (Vlastnosti.nastroj == "Guma"):
        canvas.create_line(Vlastnosti.lastx, Vlastnosti.lasty, x, y, fill=Vlastnosti.pozadie,\
        width=Vlastnosti.hrubka*4,capstyle="round", smooth="TRUE", tag="n" + str(Vlastnosti.aktualnytag))
    Vlastnosti.lastx = x
    Vlastnosti.lasty = y

def stopkreslit(event):
    if (Vlastnosti.nastroj == "Ceruzka" or Vlastnosti.nastroj == "Guma"):
        Vlastnosti.aktualnytag += 1
        Vlastnosti.stack.append("ceruzka" + str(Vlastnosti.aktualnytag))
        Vlastnosti.lastx = -1
        Vlastnosti.lasty = -1

#event iných udalostí než kreslenie
def kliknutie(event):
    if (Vlastnosti.nastroj == "Text"):
        text = simpledialog.askstring("Text", "Zadajte prosím text.")
        pismo = simpledialog.askinteger("Písmo", "Zadajte prosím veľkosť písma")
        farba = colorchooser.askcolor(title="Výber farby písma", parent=canvas)[1]
        x = canvas.create_text(canvas.canvasx(event.x), canvas.canvasy(event.y), text=text, font="arial " + str(pismo), fill=farba)
        Vlastnosti.stack.append(x)
    elif (Vlastnosti.nastroj == "Obdĺžnik"):
        if (Vlastnosti.stav == 0):
            Vlastnosti.firstx = canvas.canvasx(event.x)
            Vlastnosti.firsty = canvas.canvasy(event.y)
            Vlastnosti.stav = 1
        elif (Vlastnosti.stav == 1):
            if(Vlastnosti.vypln):
                x = canvas.create_rectangle(canvas.canvasx(event.x), canvas.canvasy(event.y), Vlastnosti.firstx, Vlastnosti.firsty, \
                outline="", fill=Vlastnosti.farbavypln)
                Vlastnosti.stack.append(x)
            else:
                x = canvas.create_rectangle(canvas.canvasx(event.x), canvas.canvasy(event.y), Vlastnosti.firstx, Vlastnosti.firsty, \
                outline=Vlastnosti.farba, width=Vlastnosti.hrubka)
                Vlastnosti.stack.append(x)
            Vlastnosti.firstx = 0
            Vlastnosti.firsty = 0
            Vlastnosti.stav = 0
    elif (Vlastnosti.nastroj == "Kruh"):
        if (Vlastnosti.stav == 0):
            Vlastnosti.firstx = canvas.canvasx(event.x)
            Vlastnosti.firsty = canvas.canvasy(event.y)
            Vlastnosti.stav = 1
        elif (Vlastnosti.stav == 1):
            if (Vlastnosti.vypln):
                x = canvas.create_oval(canvas.canvasx(event.x), canvas.canvasy(event.y), Vlastnosti.firstx, Vlastnosti.firsty, \
                outline="", fill=Vlastnosti.farbavypln)
                Vlastnosti.stack.append(x)
            else:
                x = canvas.create_oval(canvas.canvasx(event.x), canvas.canvasy(event.y), Vlastnosti.firstx, Vlastnosti.firsty, \
                outline=Vlastnosti.farba, width=Vlastnosti.hrubka)
                Vlastnosti.stack.append(x)
            Vlastnosti.firstx = 0
            Vlastnosti.firsty = 0
            Vlastnosti.stav = 0
    elif (Vlastnosti.nastroj == "Čiara"):
        if (Vlastnosti.stav == 0):
            Vlastnosti.firstx = canvas.canvasx(event.x)
            Vlastnosti.firsty = canvas.canvasy(event.y)
            Vlastnosti.stav = 1
        elif (Vlastnosti.stav == 1):
            x = canvas.create_line(canvas.canvasx(event.x), canvas.canvasy(event.y), Vlastnosti.firstx, Vlastnosti.firsty, \
            fill=Vlastnosti.farba, width=Vlastnosti.hrubka)
            Vlastnosti.stack.append(x)
            Vlastnosti.firstx = 0
            Vlastnosti.firsty = 0
            Vlastnosti.stav = 0
    elif (Vlastnosti.nastroj == "Posúvanie"):
        canvas.delete("nakres")
        x = canvas.find_closest(canvas.canvasx(event.x), canvas.canvasy(event.y))
        Vlastnosti.posuvane = x

#nákresy
def pohyb(event):
    label.config(text="Súradnice: " + str(canvas.canvasx(event.x)) + ", " + str(canvas.canvasy(event.y)) +\
    "                                   "+ "Aktuálny nástroj: " + Vlastnosti.nastroj)
    if (Vlastnosti.stav == 1 and Vlastnosti.nastroj == "Čiara"):
        canvas.delete("nakres")
        canvas.create_line(Vlastnosti.firstx, Vlastnosti.firsty, canvas.canvasx(event.x), canvas.canvasy(event.y), \
        width = Vlastnosti.hrubka, fill = Vlastnosti.farba, tag="nakres")
    elif (Vlastnosti.stav == 1 and Vlastnosti.nastroj == "Obdĺžnik"):
        canvas.delete("nakres")
        if(Vlastnosti.vypln):
            canvas.create_rectangle(canvas.canvasx(event.x), canvas.canvasy(event.y), Vlastnosti.firstx, Vlastnosti.firsty, \
            outline="", fill=Vlastnosti.farbavypln, tag="nakres")
        else:
            canvas.create_rectangle(canvas.canvasx(event.x), canvas.canvasy(event.y), Vlastnosti.firstx, Vlastnosti.firsty, \
            outline=Vlastnosti.farba, width=Vlastnosti.hrubka, tag="nakres")
    elif (Vlastnosti.stav == 1 and Vlastnosti.nastroj == "Kruh"):
        canvas.delete("nakres")
        if (Vlastnosti.vypln):
            canvas.create_oval(canvas.canvasx(event.x), canvas.canvasy(event.y), Vlastnosti.firstx, Vlastnosti.firsty, \
            outline="", fill=Vlastnosti.farbavypln, tag="nakres")
        else:
            canvas.create_oval(canvas.canvasx(event.x), canvas.canvasy(event.y), Vlastnosti.firstx, Vlastnosti.firsty, \
            outline=Vlastnosti.farba, width=Vlastnosti.hrubka, tag="nakres")

#stlačenie klávesnice
def klaves(event):
    if (Vlastnosti.nastroj != "Text" and Vlastnosti.poslednaklavesa == "Control_L"):
        if (event.keysym.lower() == "h"):
            zmenahrubky()
        elif (event.keysym.lower() == "f"):
            zmenafarby()
        elif (event.keysym.lower() == "z"):
            clear()
        elif (event.keysym.lower() == "u" or event.keysym.lower() == "s"):
            save()
        elif (event.keysym.lower() == "c"):
            ceruzka()
        elif (event.keysym.lower() == "g"):
            guma()
        elif (event.keysym.lower() == "b"):
            back()
    elif (Vlastnosti.nastroj == "Posúvanie"):
        if (event.keysym.lower() == "up"):
            canvas.move(Vlastnosti.posuvane, 0, -2)
        elif (event.keysym.lower() == "down"):
            canvas.move(Vlastnosti.posuvane, 0, 2)
        elif (event.keysym.lower() == "right"):
            canvas.move(Vlastnosti.posuvane, 2, 0)
        elif (event.keysym.lower() == "left"):
            canvas.move(Vlastnosti.posuvane, -2, 0)
    Vlastnosti.poslednaklavesa = event.keysym

"""rôzne funkcie, spustené pri kliknutí na menu tlačidlo"""
def zmenahrubky():
    dialog = simpledialog.askinteger("Hrúbka", "Zadajte prosím hrúbku.")
    Vlastnosti.hrubka = dialog
def zmenafarby():
    Vlastnosti.farba = colorchooser.askcolor(title="Farba", parent=canvas)[1]
def vyplntvaru():
    Vlastnosti.vypln = messagebox.askyesno("Výplň", "Chcete objekty vyplniť farbou?")
def farbavypln():
    Vlastnosti.farbavypln = colorchooser.askcolor(title="Farba výplne", parent=canvas)[1]
def clear():
    message = messagebox.askokcancel("Vyprázdnenie", "Skutočne chcete všetko zmazať? Táto akcia nejde vrátiť.")
    if (message):
        canvas.delete("all")
def vyfarbi():
    farba = colorchooser.askcolor(title="Výber farby", parent=canvas)[1]
    canvas.configure(bg=farba)
    Vlastnosti.pozadie = farba

def ceruzka():
    Vlastnosti.nastroj = "Ceruzka"
    label.config(text="Aktuálny nástroj: " + Vlastnosti.nastroj)
def guma():
    Vlastnosti.nastroj = "Guma"
    label.config(text="Aktuálny nástroj: " + Vlastnosti.nastroj)
def text():
    Vlastnosti.nastroj = "Text"
    label.config(text="Aktuálny nástroj: " + Vlastnosti.nastroj)
def obrazok():
    global sirka, vyska
    path = filedialog.askopenfilename(title="Vyber obrázok", filetypes=[("Obrázky", "*.png *.jpg *.gif")])
    obrazok = ImageTk.PhotoImage(file=path)
    Vlastnosti.obrazky.append(obrazok)
    if (int(vyska) < obrazok.height()):
        canvas.configure(height=obrazok.height())
        f.configure(height=obrazok.height())
        vyska = obrazok.height()
    if (int(sirka) < obrazok.width()):
        canvas.configure(width=obrazok.width())
        f.configure(width=obrazok.width())
        sirka = obrazok.width()
    canvas.configure(scrollregion=(0,0,sirka,vyska))
    x = canvas.create_image(obrazok.width()//2, obrazok.height()//2, image=Vlastnosti.obrazky[-1])
    Vlastnosti.stack.append(x)
    scrollbars()
def save():
    global sirka, vyska
    filename = "canvas.png"
    Vlastnosti.image.save(getenv('LOCALAPPDATA') + "\\LepsiSkicar\\" + filename, "PNG")
def saveas():
    global sirka, vyska
    path = filedialog.asksaveasfilename(initialfile="obrazok.png",defaultextension=".png",initialdir = "/",title = "Vyberte zložku",filetypes = (("Obrázok PNG","*.png"),("Obrázok JPG","*.jpg")))
    Vlastnosti.image.save(path, "PNG")
def new():
    global farba, sirka, vyska
    canvas.delete("all")
    canvas.configure(bg=farba)
    canvas.configure(width=sirka, height=vyska, scrollregion=(0,0,sirka,vyska))

def ciara():
    Vlastnosti.nastroj = "Čiara"
    label.config(text="Aktuálny nástroj: " + Vlastnosti.nastroj)
def obdlznik():
    Vlastnosti.nastroj = "Obdĺžnik"
    label.config(text="Aktuálny nástroj: " + Vlastnosti.nastroj)
def kruh():
    Vlastnosti.nastroj = "Kruh"
    label.config(text="Aktuálny nástroj: " + Vlastnosti.nastroj)
def trojuholnik():
    Vlastnosti.nastroj = "Trojuholník"
    label.config(text="Aktuálny nástroj: " + Vlastnosti.nastroj)

def posuvanie():
    Vlastnosti.nastroj = "Posúvanie"
    label.config(text="Aktuálny nástroj: " + Vlastnosti.nastroj)
def velkostplochy():
    global sirka, vyska
    a = simpledialog.askinteger("", "Zadajte šírku strany", initialvalue=sirka)
    b = simpledialog.askinteger("", "Zadajte výšku strany", initialvalue=vyska)
    if (a > 2500 or b > 2500):
        messagebox.askokcancel("Šírka ani výšku nesmie byť väčšia než 2500!")
        velkostplochy()
    elif (a != None and b != None):
        subor = open(getenv('LOCALAPPDATA') + "\\LepsiSkicar\\nastaveniastrana.txt", "w")
        subor.write(str(a) + " " + str(b))
        subor.close()
        canvas.configure(width=a)
        canvas.configure(height=b)
        f.configure(width=a)
        f.configure(height=b)
        sirka = a
        vyska = b
        canvas.configure(scrollregion=(0,0,sirka,vyska))
        Vlastnosti.image = Vlastnosti.image.resize((a,b), Image.ANTIALIAS)
##        scrollbars()

def farbaplochy():
    farba = colorchooser.askcolor(title="Výber farby pozadia")[1]
    subor = open(getenv('LOCALAPPDATA') + "\\LepsiSkicar\\nastaveniafarba.txt", "w")
    subor.write(farba)
    subor.close()
    canvas.configure(bg=farba)
    Vlastnosti.pozadie = farba
def reset():
    mb = messagebox.askyesno("","Skutočne chcete resetovať nastavenia?")
    if (mb):
        subor = open(getenv('LOCALAPPDATA') + "\\LepsiSkicar\\nastaveniastrana.txt", "w")
        subor.write(str(root.winfo_screenwidth()) + " " + str(root.winfo_screenheight()))
        subor.close()
        canvas = tkinter.Canvas(root, height = root.winfo_screenheight(), \
                 width = root.winfo_screenwidth(), bg="white")
        subor2 = open(getenv('LOCALAPPDATA') + "\\LepsiSkicar\\nastaveniafarba.txt", "w")
        subor2.write("white")
        subor2.close()
        ukoncit()
def back():
    canvas.delete("nakres")
    x = Vlastnosti.stack.pop()
    if (type(x) == str):
        if ("ceruzka" in x):
            canvas.delete("n" + str(Vlastnosti.aktualnytag-1))
            Vlastnosti.aktualnytag -= 1
    elif (type(x) == list):
        Vlastnosti.pozadie = x[0]
        canvas.delete(x[1])
    else:
        canvas.delete(x)
    Vlastnosti.stack_vratene.append(x)
def redo():
    x = Vlastnosti.stack_vratene.pop()
##    Vlastnosti.stack.append(x)
##    print(x)
##    canvas._create(x)
def otvorit():
    path = filedialog.askopenfilename(title="Vyber obrázok", filetypes=[("Obrázky", "*.png *.jpg *.gif")])
    obrazok = ImageTk.PhotoImage(file=path)
    root.otvorene = obrazok
    canvas.create_image(obrazok.height()//2+1, obrazok.width()//2+1, image=obrazok)
def ukoncit():
    root.destroy()
    exit()

def scrollbars():
    global sirka, vyska
    if ((int(sirka) > root.winfo_width()-100 and Vlastnosti.scrollbars == False) or\
     (int(vyska) > root.winfo_height()-100 and Vlastnosti.scrollbars == False)):
        hbar.pack(side="bottom",fill="x")
        hbar.config(command=canvas.xview)
        vbar.pack(side="right",fill="y")
        vbar.config(command=canvas.yview)

        canvas.config(yscrollcommand=vbar.set, xscrollcommand=hbar.set)

        Vlastnosti.scrollbars = True
    elif (int(sirka) < root.winfo_width()-50 and int(vyska) < root.winfo_height()-50\
    and Vlastnosti.scrollbars == True):
        hbar.pack_forget()
        vbar.pack_forget()
        Vlastnosti.scrollbars = False
        canvas.config(yscrollcommand=None, xscrollcommand=None)

"""začiatok programu"""
root = tkinter.Tk()
root.title("Lepší skicár [DEV verzia]")
root.state('zoomed')
root.option_add('*Font', 'Arial 10')

#načítavanie údajov z trvalých nastavení
sirka = root.winfo_screenwidth()
vyska = root.winfo_screenheight()
farba = "white"
try:
    subor = open(getenv('LOCALAPPDATA') + "\\LepsiSkicar\\prvykrat.txt")
    riadok = subor.readline()
    subor.close()
except:
    try:
        mkdir(getenv('LOCALAPPDATA') + "\\LepsiSkicar")
    except:
        pass
    subor = open(getenv('LOCALAPPDATA') + "\\LepsiSkicar\\prvykrat.txt", "w")
    subor.write("ano")
    subor.close()
    reset()
try:
    subor = open(getenv('LOCALAPPDATA') + "\\LepsiSkicar\\nastaveniastrana.txt")
    riadok = subor.readline()
    pole = riadok.split(" ")
    sirka = pole[0]
    vyska = pole[1]
    subor.close()
except:
    print("Error pri načítavaní dĺžky strán.")
try:
    subor2 = open(getenv('LOCALAPPDATA') + "\\LepsiSkicar\\nastaveniafarba.txt")
    farba = subor2.readline()
    subor2.close()
except:
    print("Error pri načítavaní farby.")
Vlastnosti.pozadie = farba

label = tkinter.Label(root, text="Aktuálny nástroj: " + Vlastnosti.nastroj, bg="light cyan")
label.pack()
#frame
f=tkinter.Frame(root, width=sirka, height=vyska)
f.pack()

canvas = tkinter.Canvas(f, height = int(vyska), width = int(sirka), bg=farba, scrollregion=(0,0,sirka,vyska))

Vlastnosti.image = Image.new("RGB", (int(sirka), int(vyska)), farba)
Vlastnosti.draw = ImageDraw.Draw(Vlastnosti.image)

#scrolovanie
hbar=tkinter.Scrollbar(f,orient="horizontal")
vbar=tkinter.Scrollbar(f,orient="vertical")
scrollbars()

canvas.pack(expand=True,fill="both")

canvas.bind("<B1-Motion>", kresli)
canvas.bind("<ButtonPress>", kliknutie)
canvas.bind_all("<Key>", klaves)
canvas.bind_all("<ButtonRelease-1>", stopkreslit)
canvas.bind("<Motion>", pohyb)

"""defície menu"""
hlavnemenu = tkinter.Menu(root)

menusubor = tkinter.Menu(hlavnemenu)
menusubor.add_command(label="Nový", command=new)
menusubor.add_command(label="Otvoriť", command=otvorit)
menusubor.add_command(label="Uložiť", command=save)
menusubor.add_command(label="Uložiť ako", command=saveas)
menusubor.add_command(label="Ukončiť", command=ukoncit)
hlavnemenu.add_cascade(label="Súbor", menu=menusubor)

menuupravy = tkinter.Menu(hlavnemenu)
menuupravy.add_command(label="Späť", command=back)
menuupravy.add_command(label="Vrátiť späťvzatie", command=redo)
menuupravy.add_command(label="Posunúť objekt", command=posuvanie)
hlavnemenu.add_cascade(label="Úpravy", menu=menuupravy)

menunastroje = tkinter.Menu(hlavnemenu)
menunastroje.add_command(label="Ceruzka", command=ceruzka)
menunastroje.add_command(label="Guma", command=guma)
menunastroje.add_command(label="Text", command=text)
menunastroje.add_command(label="Obrázok", command=obrazok)
hlavnemenu.add_cascade(label="Nástroje", menu=menunastroje)

menuparametre = tkinter.Menu(hlavnemenu)
menuparametre.add_command(label="Hrúbka", command=zmenahrubky)
menuparametre.add_command(label="Farba", command=zmenafarby)
menuparametre.add_command(label="Vyplniť útvar", command=vyplntvaru)
menuparametre.add_command(label="Farba výplne", command=farbavypln)
hlavnemenu.add_cascade(label="Parametre", menu=menuparametre)

menuobjekty = tkinter.Menu(hlavnemenu)
menuobjekty.add_command(label="Čiara", command=ciara)
menuobjekty.add_command(label="Obdĺžnik", command=obdlznik)
menuobjekty.add_command(label="Kruh", command=kruh)
hlavnemenu.add_cascade(label="Objekty", menu=menuobjekty)

menuakcie = tkinter.Menu(hlavnemenu)
menuakcie.add_command(label="Zmazať všetko", command=clear)
menuakcie.add_command(label="Vyfarbiť plochu", command=vyfarbi)
hlavnemenu.add_cascade(label="Akcie", menu=menuakcie)

menunastavenia = tkinter.Menu(hlavnemenu)
menunastavenia.add_command(label="Veľkosť plochy", command=velkostplochy)
menunastavenia.add_command(label="Farba plochy", command=farbaplochy)
menunastavenia.add_command(label="Reset", command=reset)
hlavnemenu.add_cascade(label="Nastavenia", menu=menunastavenia)

hlavnemenu.config(font=("Verdana", 10))

root.configure(bg="light cyan")

root.iconbitmap("app.ico")

"""koniec"""
root.config(menu=hlavnemenu)

root.mainloop()
