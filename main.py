# -*- coding:Utf8 -*-
#############################################
# Chifrement de Vigenere                    #
# auteur : Nasser Ngandu, Lubumbashi, 2023  #
# licence : GPL                             #
#############################################

#############################################
# Imporatation
from tkinter import *
from tkinter import filedialog
from vigenere import CryptageVigenere
import os 
#############################################

class Main():
    url_fichier = None
    url_dossier = None
    option = None
    def __init__(self):
        fenetre = Tk()
        fenetre.title("CHIFFREMENT DE VIGENERE")
        fenetre.geometry("400x230")
        fenetre.minsize(400,230)
        fenetre.maxsize(400,230)

        fenetre.grid_rowconfigure(0, weight=1)
        fenetre.grid_rowconfigure(1, weight=1)
        fenetre.grid_rowconfigure(2, weight=1)
        fenetre.grid_rowconfigure(3, weight=1)
        fenetre.grid_rowconfigure(4, weight=1)
        fenetre.grid_rowconfigure(5, weight=1)
        fenetre.grid_columnconfigure(0, weight=1)
        fenetre.grid_columnconfigure(1, weight=1)
        fenetre.grid_columnconfigure(2, weight=1)

        entree_label = Label(fenetre, text = "ENTREE", font = ("Times", 14))
        entree_label.grid(row = 0, column = 0, sticky = W, padx = 15)
        self.entree = Entry(fenetre, font = ("Times", 14))
        self.entree.grid(row = 0, column = 1)
        entree_bouton = Button(fenetre, text='...', font = ("Times", 14), command = self.ouvrir_fichier)
        entree_bouton.grid(row = 0, column = 2)

        sortie_label = Label(fenetre, text = "SORTIE", font = ("Times", 14))
        sortie_label.grid(row = 1, column = 0, sticky = W, padx = 15)
        self.sortie = Entry(fenetre, font = ("Times", 14))
        self.sortie.grid(row = 1, column = 1)
        sortie_bouton = Button(fenetre, text='...', font = ("Times", 14), command = self.ouvrir_dossier)
        sortie_bouton.grid(row = 1, column = 2)

        option_label = Label(text = "OPTION", font = ("Times", 14))
        option_label.grid(row = 2, column = 0, sticky = W, padx = 15)
    

        self.option = Listbox(fenetre, height = 2, font = ("Times", 14))
        self.option.insert(1,"Cryptage")
        self.option.insert(2,"Decryptage")
        self.option.grid(row = 2, column = 1)

        entree_cle = Label(fenetre, text = 'CLE', font = ("Times", 14))
        entree_cle.grid(row = 3, column = 0, sticky = W, padx = 15)
        self.cle = Entry(fenetre, font = ("Times", 14))
        self.cle.grid(row = 3, column = 1)

        self.message_label = Label(fenetre, text = "", font = ("Times", 12))
        self.message_label.grid(row = 4, column = 0, columnspan = 3)

        valider_bouton = Button(fenetre, text='VALIDER', font = ("Times", 14), command = self.valider)
        valider_bouton.grid(row = 5, column = 0, columnspan = 3, sticky = E, padx = 15)

        fenetre.mainloop()

    def ouvrir_fichier(self):
        self.url_fichier = filedialog.askopenfilename(initialdir = "/",
                                                 title = "Sélectionner le fichier",
                                                 filetypes = (("Fichiers texte", "*.txt"),
                                                              ("Tous les fichiers", "*.*")))
        if self.url_fichier:
            self.entree.delete(0, END)
            self.entree.insert(0, self.url_fichier)

    def ouvrir_dossier(self):
        self.url_dossier = filedialog.askdirectory(initialdir = "/",
                                                      title = "Sélectionner le dossier")
        if self.url_dossier:
            self.sortie.delete(0, END)
            self.sortie.insert(0, self.url_dossier)

    def valider(self):
        #Verification du fichier a crypter
        if not os.path.isfile(self.entree.get()):
            self.message_label.configure(text="Url du fichier a crypté invalide", fg="red")
        #Verification du dossier de destination
        elif not os.path.isdir(self.sortie.get()):
            self.message_label.configure(text="Url du dossier de destination invalide", fg="red")
        #Verification de l'option
        elif not self.option.curselection():
            self.message_label.configure(text="Veuillez selectionner une option", fg="red")
        else: 
            vigerene = CryptageVigenere()
            if not vigerene.main_gnu(self.entree.get(), self.sortie.get(), self.option.curselection()[0], self.cle.get()):
                self.entree.delete(0, END)
                self.sortie.delete(0, END)
                self.cle.delete(0, END)
                if not self.option.curselection()[0]:
                    self.message_label.configure(text="Le cryptage s'est deroulé avec succès", fg="green")
                else:
                    self.message_label.configure(text="Le decryptage s'est deroulé avec succès", fg="green")
                self.option.selection_clear(0, END)
            else :
                self.message_label.configure(text="Une erreur est survenue", fg="red")


if __name__ == '__main__':
    Main()