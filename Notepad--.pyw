import tkinter
from tkinter import messagebox, scrolledtext, filedialog, font, colorchooser, ttk
from tkinter import font as tkFont


# ZDROJ: https://www.bitforestinfo.com/2017/01/how-to-create-font-chooser-using_9.html
# FONT CHOOSER - vyberanie fontu písma (nie je implementované v tkinteri)


class Font_wm(tkinter.Toplevel):
    def __init__(self, Font=None):

        tkinter.Toplevel.__init__(self)
        self.mainfont = Font
        self.title("Písmo")

        # Variable
        self.var = tkinter.StringVar()  # For Font Face
        self.var.set(self.mainfont.actual("family"))
        self.var1 = tkinter.IntVar()  # for Font Size
        self.var1.set(self.mainfont.actual("size"))
        self.var2 = tkinter.StringVar()  # For Bold
        self.var2.set(self.mainfont.actual("weight"))
        self.var3 = tkinter.StringVar()  # For Italic
        self.var3.set(self.mainfont.actual("slant"))
        self.var4 = tkinter.IntVar()  # For Underline
        self.var4.set(self.mainfont.actual("underline"))
        self.var5 = tkinter.IntVar()  # For Overstrike
        self.var5.set(self.mainfont.actual("overstrike"))

        # Font Sample
        self.font_1 = tkFont.Font()
        for i in ["family", "weight", "slant", "overstrike", "underline", "size"]:
            self.font_1[i] = self.mainfont.actual(i)

        # Function
        def checkface(event):
            try:
                self.var.set(str(self.listbox.get(self.listbox.curselection())))
                self.font_1.config(
                    family=self.var.get(),
                    size=self.var1.get(),
                    weight=self.var2.get(),
                    slant=self.var3.get(),
                    underline=self.var4.get(),
                    overstrike=self.var5.get(),
                )
            except:
                pass

        def checksize(event):
            try:
                self.var1.set(int(self.size.get(self.size.curselection())))
                self.font_1.config(
                    family=self.var.get(),
                    size=self.var1.get(),
                    weight=self.var2.get(),
                    slant=self.var3.get(),
                    underline=self.var4.get(),
                    overstrike=self.var5.get(),
                )
            except:
                pass

        def applied():
            self.result = (
                self.var.get(),
                self.var1.get(),
                self.var2.get(),
                self.var3.get(),
                self.var4.get(),
                self.var5.get(),
            )
            self.mainfont["family"] = self.var.get()
            self.mainfont["size"] = self.var1.get()
            self.mainfont["weight"] = self.var2.get()
            self.mainfont["slant"] = self.var3.get()
            self.mainfont["underline"] = self.var4.get()
            self.mainfont["overstrike"] = self.var5.get()

        ##            text.config(font=self.font_1)
        def out():
            self.result = (
                self.var.get(),
                self.var1.get(),
                self.var2.get(),
                self.var3.get(),
                self.var4.get(),
                self.var5.get(),
            )
            self.mainfont["family"] = self.var.get()
            self.mainfont["size"] = self.var1.get()
            self.mainfont["weight"] = self.var2.get()
            self.mainfont["slant"] = self.var3.get()
            self.mainfont["underline"] = self.var4.get()
            self.mainfont["overstrike"] = self.var5.get()
            self.destroy()

        def end():
            self.result = None
            self.destroy()

        # Main window Frame
        self.mainwindow = ttk.Frame(self)
        self.mainwindow.pack(padx=10, pady=10)
        # Main LabelFrame
        self.mainframe = ttk.Frame(self.mainwindow)
        self.mainframe.pack(side="top", ipady=30, ipadx=30, expand="no", fill="both")
        self.mainframe0 = ttk.Frame(self.mainwindow)
        self.mainframe0.pack(side="top", expand="yes", fill="x", padx=10, pady=10)
        self.mainframe1 = ttk.Frame(self.mainwindow)
        self.mainframe1.pack(side="top", expand="no", fill="both")
        self.mainframe2 = ttk.Frame(self.mainwindow)
        self.mainframe2.pack(side="top", expand="yes", fill="x", padx=10, pady=10)
        # Frame in [  main frame]
        self.frame = ttk.LabelFrame(self.mainframe, text="Select Font Face")
        self.frame.pack(
            side="left", padx=10, pady=10, ipadx=20, ipady=20, expand="yes", fill="both"
        )
        self.frame1 = ttk.LabelFrame(self.mainframe, text="Select Font size")
        self.frame1.pack(
            side="left", padx=10, pady=10, ipadx=20, ipady=20, expand="yes", fill="both"
        )
        ttk.Entry(self.frame, textvariable=self.var).pack(
            side="top", padx=5, pady=5, expand="yes", fill="x"
        )
        self.listbox = tkinter.Listbox(self.frame, bg="gray70")
        self.listbox.pack(side="top", padx=5, pady=5, expand="yes", fill="both")
        for i in tkFont.families():
            self.listbox.insert(tkinter.END, i)

        # Frame in [ 0. mainframe]
        self.bold = ttk.Checkbutton(
            self.mainframe0,
            text="Bold",
            onvalue="bold",
            offvalue="normal",
            variable=self.var2,
        )
        self.bold.pack(side="left", expand="yes", fill="x")
        self.italic = ttk.Checkbutton(
            self.mainframe0,
            text="Italic",
            onvalue="italic",
            offvalue="roman",
            variable=self.var3,
        )
        self.italic.pack(side="left", expand="yes", fill="x")
        self.underline = ttk.Checkbutton(
            self.mainframe0, text="Underline", onvalue=1, offvalue=0, variable=self.var4
        )
        self.underline.pack(side="left", expand="yes", fill="x")
        self.overstrike = ttk.Checkbutton(
            self.mainframe0,
            text="Overstrike",
            onvalue=1,
            offvalue=0,
            variable=self.var5,
        )
        self.overstrike.pack(side="left", expand="yes", fill="x")

        # Frame in [ 1. main frame]
        ttk.Entry(self.frame1, textvariable=self.var1).pack(
            side="top", padx=5, pady=5, expand="yes", fill="x"
        )
        self.size = tkinter.Listbox(self.frame1, bg="gray70")
        self.size.pack(side="top", padx=5, pady=5, expand="yes", fill="both")
        for i in range(30):
            self.size.insert(tkinter.END, i)

        tkinter.Label(
            self.mainframe1, bg="white", text="""ABCDEabcde12345""", font=self.font_1
        ).pack(expand="no", padx=10, pady=10)

        # Frame in [ 2. mainframe]
        ttk.Button(self.mainframe2, text="   OK   ", command=out).pack(
            side="left", expand="yes", fill="x", padx=5, pady=5
        )
        ttk.Button(self.mainframe2, text=" Cancel ", command=end).pack(
            side="left", expand="yes", fill="x", padx=5, pady=5
        )
        ttk.Button(self.mainframe2, text=" Apply  ", command=applied).pack(
            side="left", expand="yes", fill="x", padx=5, pady=5
        )

        self.listbox.bind("<<ListboxSelect>>", checkface)
        self.size.bind("<<ListboxSelect>>", checksize)


"""TO DO LIST

testovanie
priblíženie?
//nastavenia

"""

# informácie o aktuálnom súbore
class Aktualny:
    path = ""      # kam uložiť
    ulozeny_text = ""      # text, ktorý bol uložený/načítaný


# FUNKCIE

class Subor:
    def novy():
        # ak nie je aktuálny súbor uložený, opýtať sa na uloženie
        if Aktualny.ulozeny_text != text.get(1.0, tkinter.END):
            mb = messagebox.askyesno(
                "Notepad--",
                "Aktuálny súbor nie je uložený. Chcete súbor uložiť?",
                icon="warning",
            )

            if mb:
                Subor.ulozit()

        # zmazanie textu -> ako keby vytvorenie nového súboru
        text.delete(1.0, tkinter.END)
        Aktualny.path = ""
        Aktualny.ulozeny_text = text.get(1.0, tkinter.END)

    def otvorit():
        # ak nie je aktuálny súbor uložený, opýtať sa na uloženie
        if Aktualny.ulozeny_text != text.get(1.0, tkinter.END):
            mb = messagebox.askyesno(
                "Notepad--",
                "Aktuálny súbor nie je uložený. Chcete súbor uložiť?",
                icon="warning",
            )

            if mb:
                Subor.ulozit()

        # otvorenie súboru (ak sa podarí)
        path = filedialog.askopenfilename(title="Otvoriť")
        try:
            file = open(path, "r")
            text.delete(1.0, tkinter.END)
            for riadok in file:
                text.insert(tkinter.END, riadok)

            file.close()
            Aktualny.ulozeny_text = text.get(1.0, tkinter.END)
            Aktualny.path = path
        except Exception:
            messagebox.askokcancel(
                "Notepad--",
                "Nastala chyba. Súbor sa nepodarilo otvoriť.",
                icon="error",
            )

    # uloženie na miesto, z ktorého sa otváralo/na ktoré sa už ukladalo
    def ulozit(destroy=False):
        # destroy - vypnúť po uložení program či nie?
        if Aktualny.path:
            try:
                file = open(Aktualny.path, "w")
                file.write(text.get(1.0, tkinter.END))
                file.close()
                Aktualny.ulozeny_text = text.get(1.0, tkinter.END)
                if destroy:
                    root.destroy()
            except Exception:
                messagebox.askokcancel(
                    "Notepad--",
                    "Nastala chyba. Súbor sa nepodarilo otvoriť.",
                    icon="error",
                )

        # v prípade že nie je známa adresa aktuálneho súboru spustiť uložiť ako
        else:
            Subor.ulozit_ako(destroy)

    # uloženie súboru vyberaním úložiska
    def ulozit_ako(destroy=False):
        # destroy - vypnúť po uložení program či nie?
        try:
            files = [('All Files', '*.*'),
                     ('Text Document', '*.txt')]
            path = filedialog.asksaveasfilename(
                filetypes=files, defaultextension=".txt", title="Uložiť ako",
                parent=root, initialfile="*.txt"
            )

            file = open(path, "w")
            file.write(text.get(1.0, tkinter.END))
            file.close()
            Aktualny.path = path
            Aktualny.ulozeny_text = text.get(1.0, tkinter.END)
            if destroy:
                root.destroy()
        except Exception:
            pass

    # funkcia spustená pri zatvorení aplikácie
    def zatvorenie():
        # uložiť súbor ak nie je uložený
        if Aktualny.ulozeny_text != text.get(1.0, tkinter.END):
            mb = messagebox.askyesno(
                "Notepad--", "Aktuálny súbor nie je uložený. Chcete súbor uložiť?"
            )

            if mb:
                Subor.ulozit(True)
            else:
                root.destroy()

        else:
            root.destroy()


class Upravy:
    # zobrazí menu pri kliknutí pravým tlačidlom
    def show_menu(event):
        menu_upravy.post(event.x_root, event.y_root)

    # vrátenie späť
    def undo():
        text.edit_undo()

    # vrátiť späť vrátenie späť
    def redo():
        text.edit_redo()

    # hľadanie textu v texte
    def najst():
        def find():
            try:
                pozice = text.search(entry.get(), "1.0", stopindex=tkinter.END)
                dlzka = float(len(entry.get()))
                koniec = str(round(float(pozice) + dlzka / 10, 2))

                text.focus_set()
                text.tag_add(tkinter.SEL, pozice, koniec)
                okno.destroy()
            except Exception:
                label3.config(text="Text nenájdený")

        def pocet():
            pocetnost = len(text.get(1.0, tkinter.END)) - len(
                text.get(1.0, tkinter.END).replace(entry.get(), "")
            )
            label2.config(text=str(pocetnost // len(entry.get())))

        okno = tkinter.Toplevel()
        okno.focus_force()
        okno.title("Notepad--")

        label1 = tkinter.Label(okno, text="Aký text vyhľadať?")
        label1.grid(row=0)

        label3 = tkinter.Label(okno)
        label3.grid(row=1, column=1)

        entry = tkinter.Entry(okno)
        entry.focus()
        entry.grid(row=0, column=1)

        button1 = tkinter.Button(okno, text="Vyhľadaj", command=find)
        button1.grid(row=1, column=0)

        button3 = tkinter.Button(okno, text="Počet výskytu", command=pocet)
        button3.grid(row=2, column=0)

        label2 = tkinter.Label(okno, text="")
        label2.grid(row=2, column=1)

        okno.mainloop()

    # nahradenie textu textom
    def nahradit():
        def hotovo():
            text.replace(
                "1.0",
                tkinter.END,
                text.get("1.0", tkinter.END).replace(entry.get(), entry2.get()),
            )

            okno.destroy()

        okno = tkinter.Toplevel()
        okno.focus_force()
        okno.title("Notepad--")

        label1 = tkinter.Label(okno, text="Aký text nahradiť?")
        label1.grid(row=0)

        label2 = tkinter.Label(okno, text="Čím ho nahradiť?")
        label2.grid(row=1)

        entry = tkinter.Entry(okno)
        entry.focus()
        entry.grid(row=0, column=1)

        entry2 = tkinter.Entry(okno)
        entry2.grid(row=1, column=1)

        button1 = tkinter.Button(okno, text="Nahraď", command=hotovo)
        button1.grid(row=2, column=1)

        okno.mainloop()

    # vybrať celý text
    def select_all():
        text.tag_add(tkinter.SEL, "1.0", tkinter.END)
        text.mark_set(tkinter.INSERT, "1.0")
        text.see(tkinter.INSERT)


class Zobrazenie:
    # výber fontu pre text
    def font():
        Font_wm(Font=font1)

    # výber farby pozadia
    def pozadie():
        farba = colorchooser.askcolor(title="Notepad--")[1]
        try:
            text.config(bg=farba)
        except Exception:
            print("Error: farba neznáma")


# zobrazenie "nápovedy"
def napoveda():
    messagebox.showerror(
        "Notepad--",
        "Nápoveda neexistuje!\n\nAutor si "
        + "(asi mylne) myslel, že používateľ tento "
        + "program zvládne používať aj bez nápovedy.",
    )


# základné informácie o programe - vyskakovacie okno
def o_programe():
    messagebox.showinfo("Notepad--", "Verzia alpha 1.0\n\n©2020 Jakub Judiny")


# ZAČIATOK KÓDU
root = tkinter.Tk()
root.title("Notepad--")
root.state("zoomed")


# event pri zatvorení aplikácie spustí funkciu Subor.zatvorenie
root.protocol("WM_DELETE_WINDOW", Subor.zatvorenie)


# ikona aplikácie - ak ju program nájde v zložke notepadu
try:
    root.iconbitmap(r"icon.ico")
except Exception:
    print("chyba (icon)")


# font písma použitý v texte
font1 = tkFont.Font(family="Arial", size=12)


# hlavné textové pole
text = scrolledtext.ScrolledText(
    width=root.winfo_screenwidth(), height=root.winfo_screenheight(), font=font1
)
text.pack()
text.focus_set()
Aktualny.ulozeny_text = text.get(1.0, tkinter.END)


# založenie menu
hl_menu = tkinter.Menu(root)

menu_subor = tkinter.Menu(hl_menu)
menu_subor.add_command(label="Nový súbor", command=Subor.novy)
menu_subor.add_command(label="Otvoriť súbor", command=Subor.otvorit)
menu_subor.add_command(label="Uložiť", command=Subor.ulozit)
menu_subor.add_command(label="Uložiť ako", command=Subor.ulozit_ako)
menu_subor.add_command(label="Zavrieť", command=Subor.zatvorenie)
hl_menu.add_cascade(label="Súbor", menu=menu_subor)

menu_upravy = tkinter.Menu(hl_menu)
menu_upravy.add_command(label="Späť", command=Upravy.undo)
menu_upravy.add_command(label="Vrátiť späťvzatie", command=Upravy.redo)
menu_upravy.add_command(label="Nájsť", command=Upravy.najst)
menu_upravy.add_command(label="Nahradiť", command=Upravy.nahradit)
menu_upravy.add_command(label="Vybrať všetko", command=Upravy.select_all)
hl_menu.add_cascade(label="Úpravy", menu=menu_upravy)

# spustiť menu úprav pri stlačení pravého tlačidla myši
text.bind("<Button-3>", Upravy.show_menu)

menu_zobrazenie = tkinter.Menu(hl_menu)
menu_zobrazenie.add_command(label="Písmo", command=Zobrazenie.font)
## menu_zobrazenie.add_command(label="Zväčšenie")
menu_zobrazenie.add_command(label="Farba pozadia", command=Zobrazenie.pozadie)
## menu_zobrazenie.add_command(label="Trvalé nastavenia")
hl_menu.add_cascade(label="Zobrazenie", menu=menu_zobrazenie)

hl_menu.add_command(label="Nápoveda", command=napoveda)

hl_menu.add_command(label="O programe", command=o_programe)

root.config(menu=hl_menu)


# koniec kódu
root.mainloop()
