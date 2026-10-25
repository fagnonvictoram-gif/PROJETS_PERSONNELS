#Pour annalyser le fichier log ligne par ligne et ressortir des mots cles comme echec ou brut force 
from pathlib import Path
chem_dossier = Path(__file__).parent
chem_fichier = chem_dossier/"logs.txt"
chem_fichier_blacklist = chem_dossier/"blacklist.txt"
def fonction_pour_recuperer_les_mots_rouge () :
    liste=[]
    with open(chem_fichier_blacklist,"r",encoding="utf-8") as f  :
        for ligne in f :
            word = (ligne.strip())
            liste.append(word)
    return liste


    
liste_noire=[]
liste_noire = fonction_pour_recuperer_les_mots_rouge()
alerte = False
compteur=0
with open (chem_fichier,"r",encoding="utf-8") as f :
    for ligne in f :
        compteur=compteur+1
        texte_de_la_ligne = ligne.strip() #permet de conserver chaque ligne du fichier log sans le saut de ligne a la fin
        texte_de_la_ligne_min = texte_de_la_ligne.lower()
        for mot in liste_noire :
            if mot in texte_de_la_ligne_min :
                alerte=True
                print(f"Une erreur du type {mot} a ete rencontree a la ligne numero {compteur}")
                continue
            
    if alerte == False : 
        print("L'analyse de logs.txt n'a reveler aucune anomalie --- Fermeture du progaramme .......")
    n=input("Appuyer sur entree pour fermer le terminal")

