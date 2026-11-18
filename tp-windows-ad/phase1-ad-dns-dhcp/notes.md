# Phase 1 : Active Directory et DNS (création du domaine)

TP Intégrateur : Administration Système et Réseau sous Windows
Domaine : `batiplus.local` · Serveur : `SRV-AD01` (`172.21.211.200`)

## 1. Objectif

Promouvoir la VM Windows Server en **contrôleur de domaine** `batiplus.local`. Cette étape crée l'annuaire central de l'entreprise fictive BatiPlus et installe en même temps le service DNS dont il dépend.

## 2. La logique : qui fait quoi ?

| Service | Rôle | Pourquoi on en a besoin |
|---|---|---|
| **AD DS** (Active Directory Domain Services) | Annuaire central : comptes, groupes, ordinateurs, règles | Un seul endroit pour gérer les utilisateurs et leurs droits |
| **DNS** | Traduit les noms en adresses IP | AD l'utilise pour localiser le contrôleur de domaine et ouvrir une session |

Active Directory **dépend du DNS** : sans DNS fonctionnel, pas de domaine. C'est pourquoi le serveur a une IP fixe et utilise sa propre adresse comme serveur DNS (voir Phase 0).

## 3. Étapes réalisées

### 3.1 Installation des rôles

```powershell
Install-WindowsFeature AD-Domain-Services, DHCP -IncludeManagementTools
```

Installe le rôle annuaire et le rôle DHCP, avec leurs outils de gestion. (Le DHCP sera configuré dans la suite de la phase.)

### 3.2 Mot de passe de l'administrateur local

La promotion exige que le compte administrateur local ait un mot de passe conforme à la politique de complexité (majuscule, minuscule, chiffre, symbole).

```powershell
net user Administrateur "<mot_de_passe_complexe>"
```

Le compte s'appelle `Administrateur` car le serveur est en français.

### 3.3 Promotion en contrôleur de domaine (création de la forêt)

```powershell
Install-ADDSForest -DomainName "batiplus.local" -DomainNetbiosName "BATIPLUS" -InstallDns -SafeModeAdministratorPassword (ConvertTo-SecureString "<mot_de_passe_dsrm>" -AsPlainText -Force) -Force
```

| Paramètre | Signification |
|---|---|
| `-DomainName` | Nom DNS complet du domaine |
| `-DomainNetbiosName` | Nom court (`BATIPLUS`), utilisé à la connexion (`BATIPLUS\utilisateur`) |
| `-InstallDns` | Installe le rôle DNS en même temps |
| `-SafeModeAdministratorPassword` | Mot de passe DSRM, pour restaurer l'annuaire en mode sans échec |

Résultat obtenu : `L'opération s'est déroulée avec succès`, `Status : Success`. La VM redémarre ensuite toute seule.

Les avertissements affichés sont normaux :
- *Délégation DNS impossible* : il n'existe pas de zone parente (`.local` n'est pas géré par un serveur DNS public). Aucune action requise.
- *Algorithmes compatibles Windows NT 4.0* : information de sécurité par défaut de Windows Server 2022.

## 4. Validation

| Test | Résultat | Statut |
|---|---|---|
| Forêt `batiplus.local` créée | `Status : Success` | [x] |

## 5. Captures d'écran

<!-- Renomme les fichiers selon tes captures -->
![Promotion réussie](images/phase1-promotion-succes.jpg)

## 6. Problèmes rencontrés

| Problème | Cause | Solution |
|---|---|---|
| Le Gestionnaire de serveur se fermait en cliquant sur « Ajouter une nouvelle forêt » | Plantage de l'assistant graphique | Promotion en ligne de commande avec `Install-ADDSForest` |
| `Le nom d'utilisateur est introuvable` (`net user Administrator`) | Le serveur est en français : le compte s'appelle `Administrateur` | Utiliser `Administrateur` |
| `Impossible de trouver un paramètre « SafeModeAdministrateurPassword »` | Nom du paramètre francisé par erreur | Le paramètre est en anglais : `-SafeModeAdministratorPassword` |

## 7. Ce que j'en retiens

- Active Directory **dépend du DNS**.
- Les noms de commandes et de paramètres PowerShell restent en **anglais**, même sur un système en français, alors que les noms de comptes et de groupes sont localisés.
- Une erreur de saisie se lit : le message d'erreur nomme le paramètre fautif, c'est le premier indice.
