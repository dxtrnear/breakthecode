import csv

def lire_armes(fichier_armes):
    armes = {}
    with open(fichier_armes, 'r') as csvfile:
        lecteur = csv.DictReader(csvfile)
        for ligne in lecteur:
            armes[ligne['arme']] = {
                'degat': float(ligne['degat']),
                'precision_courte': float(ligne['precision_courte']),
                'precision_moyenne': float(ligne['precision_moyenne']),
                'precision_longue': float(ligne['precision_longue']),
                'cadence': float(ligne['cadence'])
            }
    return armes

def lire_duels(fichier_duels):
    duels = []
    with open(fichier_duels, 'r') as csvfile:
        lecteur = csv.DictReader(csvfile)
        for ligne in lecteur:
            duels.append({
                'joueur_arme': ligne['joueur_arme'],
                'adversaire_arme': ligne['adversaire_arme'],
                'distance': ligne['distance']
            })
    
    # Vérifier que nous avons bien 1000 duels
    if len(duels) != 1000:
        print(f"Attention : Le fichier contient {len(duels)} duels au lieu des 1000 attendus.")
    
    return duels

def simuler_duel(joueur_arme_info, adversaire_arme_info, distance):
    joueur_vie = 200
    adversaire_vie = 200

    if distance == "courte":
        precision_joueur = joueur_arme_info['precision_courte']
        precision_adversaire = adversaire_arme_info['precision_courte']
    elif distance == "moyenne":
        precision_joueur = joueur_arme_info['precision_moyenne']
        precision_adversaire = adversaire_arme_info['precision_moyenne']
    else:  # longue
        precision_joueur = joueur_arme_info['precision_longue']
        precision_adversaire = adversaire_arme_info['precision_longue']

    degats_joueur = joueur_arme_info['degat'] * precision_joueur
    degats_adversaire = adversaire_arme_info['degat'] * precision_adversaire

    while joueur_vie > 0 and adversaire_vie > 0:
        adversaire_vie -= degats_joueur
        joueur_vie -= degats_adversaire

    if joueur_vie > 0 and adversaire_vie <= 0:
        return 1  # Victoire du joueur
    elif adversaire_vie > 0 and joueur_vie <= 0:
        return 0  # Défaite du joueur
    else:
        return 0.5  # Match nul

def calculer_statistiques(armes, duels):
    total_victoires_pompe = 0
    total_duels_pompe = 0
    total_victoires_longue = 0
    total_duels_longue = 0

    for duel in duels:
        joueur_arme = duel['joueur_arme']
        adversaire_arme = duel['adversaire_arme']
        distance = duel['distance']

        if joueur_arme not in armes or adversaire_arme not in armes:
            print(f"Arme inconnue dans le duel : {duel}")
            continue

        joueur_arme_info = armes[joueur_arme]
        adversaire_arme_info = armes[adversaire_arme]

        resultat = simuler_duel(joueur_arme_info, adversaire_arme_info, distance)

        if joueur_arme == 'Pompe':
            total_duels_pompe += 1
            total_victoires_pompe += resultat

        if distance == 'longue':
            total_duels_longue += 1
            total_victoires_longue += resultat

    pourcentage_victoires_pompe = (total_victoires_pompe / total_duels_pompe * 100) if total_duels_pompe > 0 else 0
    pourcentage_victoires_longue = (total_victoires_longue / total_duels_longue * 100) if total_duels_longue > 0 else 0

    return round(pourcentage_victoires_pompe, 2), round(pourcentage_victoires_longue, 2)

# Exécution complète
def main():
    armes = lire_armes('c:/Users/david/Documents/1 David/break the code/breakthecode/5 - Victory Royale/armes.csv')
    duels = lire_duels('c:/Users/david/Documents/1 David/break the code/breakthecode/5 - Victory Royale/duels_Brest.csv')

    A, B = calculer_statistiques(armes, duels)
    
    # Affichage des résultats
    print(f"{A:.2f} {B:.2f}")

# Lancer le programme principal
if __name__ == "__main__":
    main()
