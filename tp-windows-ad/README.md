# TP intégrateur : Administration système et réseau sous Windows

Déploiement d'un domaine Active Directory (`batiplus.local`) sur une VM Windows Server (VirtualBox, hébergée sur Ubuntu), avec un poste client Windows 11 Pro. Ce dépôt contient mes notes, mes commandes expliquées et mes captures, phase par phase.

## Architecture

| Machine | Rôle | Adresse |
|---|---|---|
| Routeur de poche MTN (sans SIM) | Réseau local, passerelle | 192.168.1.1 |
| SRV-AD01 (VM Windows Server, accès par pont) | AD DS, DNS, DHCP, fichiers | 192.168.1.250 |
| PC Windows 11 Pro | Client du domaine | DHCP (192.168.1.210 à 220) |

Le DHCP du routeur est désactivé : c'est SRV-AD01 qui distribue les adresses.

## Avancement

| Phase | Contenu | État |
|---|---|---|
| 0 | Réseau VirtualBox et liaison entre les 2 PC | Terminée |
| 1 | Active Directory, DNS, DHCP | En cours |
| 2 | OU, groupes, utilisateurs, jonction au domaine | À faire |
| 3 | Dossiers partagés et permissions NTFS | À faire |
| 4 | GPO, pare-feu, dépannage | À faire |

## Changement de réseau (19/11/2026)

Le TP a démarré sur le point d'accès du téléphone, puis a migré vers un routeur de poche dédié.

| | Avant (hotspot téléphone) | Après (routeur MTN) |
|---|---|---|
| Réseau | 172.21.211.0/24 | 192.168.1.0/24 |
| Passerelle | 172.21.211.95 | 192.168.1.1 |
| SRV-AD01 | 172.21.211.200 | 192.168.1.250 |
| DHCP | celui du téléphone | SRV-AD01 (routeur désactivé) |

**Pourquoi :** le hotspot consommait la connexion limitée du téléphone, et sa plage d'adresses pouvait changer à chaque redémarrage.

**Ce qui a été refait :** l'adresse IP, la passerelle et le DNS du serveur, puis l'enregistrement DNS de SRV-AD01 (`ipconfig /registerdns`) et le plan d'adressage.

**Captures :** `phase0et1reseau/captures/` (ancien réseau, périmé) et `phase0et1reseau/captures/Captures_des_modifications/` (réseau actuel).

## Structure du dépôt

```
tp-windows-ad/
├── README.md
├── docs/
├── phase0et1reseau/
├── phase2/ ... phase4/
```

Les mots de passe du TP ne figurent pas dans ce dépôt.