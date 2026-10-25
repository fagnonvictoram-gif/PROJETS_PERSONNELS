def ip_to_int(ip_list):
    """Convertit une liste de 4 octets en un entier 32-bit."""
    return (ip_list[0] << 24) + (ip_list[1] << 16) + (ip_list[2] << 8) + ip_list[3]

def int_to_ip(ip_int):
    """Convertit un entier 32-bit en liste de 4 octets."""
    return [
        (ip_int >> 24) & 255,
        (ip_int >> 16) & 255,
        (ip_int >> 8) & 255,
        ip_int & 255
    ]

def fonction_recuperation_d_adresse():
    while True:
        try:
            buffer = input("Entrer l'adresse IP (ex: 192.168.1.0) ---------> ")
            octets = buffer.split('.')
            if len(octets) != 4:
                print("Format invalide. L'adresse doit contenir 4 octets séparés par des points.")
                continue
            
            adresse_final = [int(o) for o in octets]
            if all(0 <= val <= 255 for val in adresse_final):
                return adresse_final
            else:
                print("Chaque octet doit être compris entre 0 et 255.")
        except ValueError:
            print("Saisie incorrecte, veuillez entrer des nombres réels.")

# --- MENU PRINCIPAL ---
while True:
    print("=================================================================")
    print("Copyright by FAGNON VICTOR Abdoul Malik - Cybersécurité (IFRI)")
    print("=================================================================\n")
    print("MENU CLI POUR CALCUL FLSM ET VLSM\n")

    while True:
        try:
            choix_menu = int(input("1-) FLSM \n2-) VLSM \n------> "))
            if choix_menu == 1:
                break
            elif choix_menu == 2:
                print("VLSM EN COURS DE DEVELOPPEMENT...\n")
        except ValueError:
            print("Erreur de saisie ! Entrez 1 ou 2.")

    print("\n----------------- Bienvenue dans le mode FLSM --------------------")
    
    adresse_reseau = fonction_recuperation_d_adresse()
    
    subnetmask_cidr = -1
    while not (0 <= subnetmask_cidr <= 32):
        try:
            subnetmask_cidr = int(input("Entrer le masque initial en CIDR (ex: 24) : "))
            if not (0 <= subnetmask_cidr <= 32):
                print("Le masque doit être entre 0 et 32.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    bits_hote_disponibles = 32 - subnetmask_cidr

    while True:
        try:
            nombre_de_sous_reseau = int(input("Entrer le nombre de sous-réseaux souhaités ------> "))
            if nombre_de_sous_reseau <= 0:
                print("Le nombre doit être supérieur à 0.")
                continue
            break
        except ValueError:
            print("Veuillez entrer un entier valide.")

    # Calcul des bits à emprunter (2^n >= nombre_de_sous_reseau)
    bits_empruntes = 0
    while (2 ** bits_empruntes) < nombre_de_sous_reseau:
        bits_empruntes += 1

    if bits_empruntes > bits_hote_disponibles:
        print(f" Impossible ! Il faut {bits_empruntes} bits, mais il n'en reste que {bits_hote_disponibles}.\n")
        continue

    nouveau_cidr = subnetmask_cidr + bits_empruntes
    taille_sous_reseau = 2 ** (32 - nouveau_cidr)

    print(f"\n Opération réalisable !")
    print(f"Nouveau masque : /{nouveau_cidr}")
    print(f"Nombre de blocs réservés : {2 ** bits_empruntes}")
    print(f"Nombre d'adresses totales par sous-réseau : {taille_sous_reseau}\n")

    # Conversion IP réseau de base en entier
    ip_base_int = ip_to_int(adresse_reseau)

    # Affichage des sous-réseaux
    print(f"{'N°':<5} | {'Adresse Réseau':<16} | {'1ère IP Utilisable':<18} | {'Dernière IP Utilisable':<22} | {'Broadcast':<16}")
    print("-" * 85)

    for i in range(nombre_de_sous_reseau):
        net_int = ip_base_int + (i * taille_sous_reseau)
        first_ip_int = net_int + 1
        last_ip_int = net_int + taille_sous_reseau - 2
        broadcast_int = net_int + taille_sous_reseau - 1

        net_str = ".".join(map(str, int_to_ip(net_int)))
        first_str = ".".join(map(str, int_to_ip(first_ip_int)))
        last_str = ".".join(map(str, int_to_ip(last_ip_int)))
        bcast_str = ".".join(map(str, int_to_ip(broadcast_int)))

        print(f"{i+1:<5} | {net_str:<16} | {first_str:<18} | {last_str:<22} | {bcast_str:<16}")

    print("\n")
    quitter = input("Voulez-vous quitter le programme ? (o/n) ------> ").strip().lower()
    if quitter == 'o':
        print("Merci d'avoir utilisé le programme. À bientôt !")
        break