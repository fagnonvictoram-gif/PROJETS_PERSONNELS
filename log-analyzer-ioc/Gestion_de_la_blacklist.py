from pathlib import Path
chemin = Path(__file__).parent
file_way  = chemin/"blacklist.txt"
print("Bienvenue dans le menu d'ajout de nouveau mot a une liste ")
choix=int(input("Veuillez entrer votre choix \n 1-) Ajouter un mot\n 2-) Supprimer un mot \n 3-) Afficher les mots de la liste  "))
####################### Ecriture des fonctions  ######################
def fonction_ajout () :
    with open (file_way,"a",encoding="utf-8") as file:
        while True:
            try:
                n_mots_a_enregistrer = int(input("Entrer le nombre de mot que vous souhaiter ajouter a votre liste de mots noir "))
                break
            except ValueError :
                print ("Quelque chose c'est mal passer reprenez XD")
                continue
        for i in range (n_mots_a_enregistrer) :
            mot = input(f"Entrer le mot numero {i+1} : ====> ").lower()
            file.write(f"{mot} \n")
def fonction_supprimer (chemin) :
    if not chemin.exists () :
        print("Le fichier est introuvable")
        return
    n_mots_supprimer = int(input("Entrer le nombre de mots a supprimer "))
    for i in range (n_mots_supprimer) :
        mots_supprimer = input("Entrer le mot a supprimer : ").lower()
        if mots_supprimer in blacklist :
            blacklist.remove(mots_supprimer)
            print("Mots correctement supprimer \n ")
            for i in range (2) : print ("\n")
        else :
            print(f"Le mot {mots_supprimer} est introuvable :) passage au mot suivant \n ")
            for i in range (2) : print("\n")
    with open (chemin,"w",encoding="utf-8") as f :
        with open (chemin,"a",encoding="utf-8") as f_ :
            for i in range (len(blacklist)) :
                f_.write(f"{blacklist[i]} \n")

def fonction_charger_la_blacklist (chemin) :
    mots=[]
    with open(chemin,"r",encoding="utf-8") as file :
     for ligne in file :
          le_mot= ligne.strip()
          if le_mot :
              mots.append(le_mot)
    return mots


def fonction_afficher_les_mots (chemin,mots):
    print("\n-----------Liste des mots sous surveillances----------")
    if not chemin.exists() :
        print("fichier introuvable ou depalcer ")
        return
    for i in range (len(mots)) :
        print(f"===={mots[i]}\n")
        #####n'oubli pas de ramener le bloc de code de la fonction ci-dessus dans une fonction qui va retourner la loste de smots se serait vraiment dommage de tt reecrire 

    


############################### APPLICATION ##############################
blacklist=[]
blacklist = fonction_charger_la_blacklist(file_way)
if (choix == 1) :
    fonction_ajout()
    n=input("Appuyer entree ou toute autre touche pour fermer cette fenetre")
if (choix == 2) :
    fonction_supprimer(file_way)
    n=input("Appuyer entree ou toute autre touche pour fermer cette fenetre")
if (choix == 3) :
    fonction_afficher_les_mots(file_way,blacklist)
    n=input("Appuyer entree ou toute autre touche pour fermer cette fenetre")
