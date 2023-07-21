class CryptageVigenere():
    # La fonction init
    def __init__(self):
        self.lettre_cryptage = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+!@#$%^&*()_-=`~}{/.,<>:;"
        self.tableau_filtre_lettre_index = [[],[]]
        self.TableauVigenere = list()

    # La fonction principale fenetre
    def main_gnu(self, url_entree, url_sortie, option, cle):
        ext = url_entree.split(".")
        ext = ext[len(ext) - 1]
        if option == 0:
            url_sortie = "%s/crypt.%s"%(url_sortie, ext)
        else:
            url_sortie = "%s/decrypt.%s"%(url_sortie, ext)
        cle_filtre = self.filtre_cle(cle)
        try:
            fichier_entree = open(url_entree, 'r')
            fichier_sortie = open(url_sortie, 'w')
        except:
            print("Impossible d'ouvrir l'un des fichiers")
            exit()
        # Generation du tableau de Vigenere
        self.generation_tableau()
        ligne_fichier = fichier_entree.readline()
        while ligne_fichier != "":
            mot_filtre = self.filtre_mot(ligne_fichier)
            if int(option) == 0:
                mot_crypte = self.cryptage(mot_filtre, cle_filtre)
                fichier_sortie.write(self.defiltre_mot(mot_crypte))
            elif int(option) == 1:
                mot_decrypte = self.decryptage(mot_filtre, cle_filtre)
                fichier_sortie.write(self.defiltre_mot(mot_decrypte))
            else:
                print("Erreur option %s invalide"%(option))
                break
            self.tableau_filtre_lettre_index = [[],[]]
            ligne_fichier = fichier_entree.readline()
        
        fichier_entree.close()
        fichier_sortie.close()
        return 0

    # La fonction principale
    def main_console(self):
        option = input("Entrez une option :\n\t1. cryptage\n\t2.decryptage\n>>> ")
        cle = input("Entrez la cle\n>>> ")
        url_entree = input("Entrez l'url du fichier en entree\n>>> ")
        url_sortie = input("Entrez l'url du fichier en sortie\n>>> ")
        cle_filtre = self.filtre_cle(cle)
        try:
            fichier_entree = open(url_entree, 'r')
            fichier_sortie = open(url_sortie, 'w')
        except:
            print("Impossible d'ouvrir l'un des fichiers")
            exit()
        # Generation du tableau de Vigenere
        self.generation_tableau()
        ligne_fichier = fichier_entree.readline()
        while ligne_fichier != "":
            mot_filtre = self.filtre_mot(ligne_fichier)
            if int(option) == 1:
                mot_crypte = self.cryptage(mot_filtre, cle_filtre)
                fichier_sortie.write(self.defiltre_mot(mot_crypte))
            elif int(option) == 2:
                mot_decrypte = self.decryptage(mot_filtre, cle_filtre)
                fichier_sortie.write(self.defiltre_mot(mot_decrypte))
            else:
                print("Erreur option invalide")
                break
            self.tableau_filtre_lettre_index = [[],[]]
            ligne_fichier = fichier_entree.readline()
        
        fichier_entree.close()
        fichier_sortie.close()

    # Generation du tableau de vigenere pour le cryptage
    def generation_tableau(self):
        if not self.TableauVigenere:
            self.TableauVigenere = list()
        self.TableauVigenere.append(self.lettre_cryptage)
        for compteur in range(len(self.lettre_cryptage) - 1):
            premier_element = self.TableauVigenere[len(self.TableauVigenere) - 1][0]
            self.TableauVigenere.append("%s%s"%(self.TableauVigenere[len(self.TableauVigenere) - 1][1:], premier_element))
    
    # Retir des caracteres qui n'existent pas dans le dataset
    def filtre_mot(self, mot):
        mot1 = ""
        for compteur in range(len(mot)):
            if mot[compteur] not in self.lettre_cryptage:
                self.tableau_filtre_lettre_index[0].append(mot[compteur])
                self.tableau_filtre_lettre_index[1].append(compteur)
            else:    
                mot1 += mot[compteur]
        return mot1
    
    # Remet des caracteres qui n'existent pas dans le dataset
    def defiltre_mot(self, mot):
        mot1 = ""
        lettre_non_chiffre = 0
        for compteur1 in range(len(mot) + len(self.tableau_filtre_lettre_index[1])):
            if compteur1 in self.tableau_filtre_lettre_index[1]:
                indice = self.tableau_filtre_lettre_index[1].index(compteur1)
                mot1 += self.tableau_filtre_lettre_index[0][indice]
                lettre_non_chiffre += 1
            else:
                mot1 += mot[compteur1 - lettre_non_chiffre]
        return mot1

    def filtre_cle(self, cle):
        cle1 = ""
        for compteur in range(len(cle)):
            if cle[compteur] in self.lettre_cryptage:
                cle1 += cle[compteur] 
        cle1 += "NASSER"
        return cle1

    def cryptage(self, mot, cle):
        # Alignement de la cle avec le mot
        mot_cle = [[],[]]
        compteur_cle = 0
        tableau_ligne_colonne = [[],[]]
        retour = ""
        for compteur_mot in range(len(mot)):
            # Ajout d'une lettre du mot
            mot_cle[0].append(mot[compteur_mot])
            
            # Ajout d'une lettre de la cle
            mot_cle[1].append(cle[compteur_cle])
            compteur_cle += 1
            if len(cle) <= compteur_cle:
                compteur_cle = 0

        # Recuperation des numeros de lettres ligne colonne
        for compteur1 in range(len(mot)):
            tableau_ligne_colonne[0].append(self.lettre_cryptage.index(mot_cle[0][compteur1]))
            tableau_ligne_colonne[1].append(self.lettre_cryptage.index(mot_cle[1][compteur1]))

        # Retour cryptage
        for compteur2 in range(len(mot)):
            retour += self.TableauVigenere[tableau_ligne_colonne[0][compteur2]][tableau_ligne_colonne[1][compteur2]]
        return retour
    
    def decryptage(self, mot, cle):
        # Alignement de la cle avec le mot
        mot_cle = [[],[]]
        compteur_cle = 0
        tableau_retour = []
        retour = ""
        for compteur_mot in range(len(mot)):
            # Ajout d'une lettre du mot
            mot_cle[0].append(mot[compteur_mot])
            
            # Ajout d'une lettre de la cle
            mot_cle[1].append(cle[compteur_cle])
            compteur_cle += 1
            if len(cle) <= compteur_cle:
                compteur_cle = 0

        # Recuperation des numeros de lettres ligne colonne
        colonne = 0

        for compteur1 in range(len(mot_cle[1])):
            for compteur2 in range(len(self.TableauVigenere)):
                if mot_cle[1][compteur1] == self.TableauVigenere[compteur2][0]:
                    tableau_retour.append(self.TableauVigenere[compteur2].index(mot_cle[0][colonne]))
                    colonne+=1
                if colonne >= len(mot_cle[1]):
                    break
        # Retour Decryptage
        for compteur in tableau_retour:
            retour += self.lettre_cryptage[compteur]
        return retour        
if __name__ == '__main__': 
    CryptageVigenere().main_console()