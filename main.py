from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup as bs
import tkinter
import random


class THT_cekilis(object):
    def __init__(self):
        self.pencere = tkinter.Tk()
        self.pencere.geometry("990x410")
        self.pencere.title(" THT-Çekiliş Programı")



        self.pencere.configure(bg="#1C2D46")
        self.label = tkinter.Label(self.pencere , text="Konu Linki ",bg="#1C2D46", fg="white",font=('Courier New',12)).place(
            x=10,
            y=50
        )
        self.entryKisi = tkinter.Entry(self.pencere, width=35)

        self.entryKisi.place(
            x=120,
            y=53
        )

        self.kazanacakkisiLabel =tkinter.Label(self.pencere , text="Kazanacak: ",bg="#1C2D46", fg="white",font=('Courier New',12)).place(
            x=346,
            y=50
        )

        self.yedekKisiS = tkinter.Label(self.pencere, text="Yedek: ", bg="#1C2D46", fg="white",
                                        font=('Courier New', 12)).place(
            x=566,
            y=50
        )


        self.yedekKisi()

        self.kazanacakkisiSayisi()
        self.Buton()


        self.pencere.mainloop()

    def kazanacakkisiSayisi(self):
        self.st = tkinter.StringVar()
        self.kazanacakkisi = ttk.Combobox(self.pencere, width=12, textvariable=self.st)

        self.kazanacakkisi["values"] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
        self.kazanacakkisi.place(
            x=461,
            y=54
        )
        self.kazanacakkisi.current(0)

    def yedekKisi(self):
        self.sy = tkinter.StringVar()
        self.kazanacakkisiYedek = ttk.Combobox(self.pencere, width=12, textvariable=self.sy,)

        self.kazanacakkisiYedek["values"] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
        self.kazanacakkisiYedek.place(
            x=631,
            y=54
        )
        self.kazanacakkisiYedek.current(0)

    def Buton(self):
        self.btn = tkinter.Button(self.pencere , text="Başla",bd=3, width=20,font=('Comic Sans MS',11),command=self.ButtonCommand).place(
            x=370,
            y=104
        )

    def ButtonCommand(self):
        if self.entryKisi.get() =="":
            messagebox.showwarning("Hata!","Link Alanı Boş olamaz")
        elif self.entryKisi.get():
            self.req = requests.get(self.entryKisi.get()).content
            self.parse = bs(self.req, "lxml").find("a", class_="reactionsBar-link")

            self.user = requests.get("https://www.turkhackteam.org"+str(self.parse.attrs["href"])).content
            self.user_fir = bs(self.user, "lxml")

            self.end = self.user_fir.find_all("h3", class_="contentRow-header")
            try:
                liste = []
                for i in (self.end):
                    liste.append(i.text)
                self.kazanan = random.sample(liste,int(self.kazanacakkisi.get()))
                self.yedek = random.sample(liste,int(self.kazanacakkisiYedek.get()))
                messagebox.showinfo("Kazanan",f"Kazanan:{' | '.join(self.kazanan)}\nYedek: {' | '.join(self.yedek)}")
            except ValueError:
                pass





if __name__ == "__main__":
    THT_cekilis()