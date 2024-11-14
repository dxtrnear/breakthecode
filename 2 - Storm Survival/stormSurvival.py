import csv

def can_survive(player_safe_distance, player_speed, storm_player_distance, storm_speed):
    # Si déjà dans la zone de sûreté
    if player_safe_distance <= 0:
        return True
        
    # Si déjà touché par la tempête
    if storm_player_distance <= 0:
        return False
    
    # Calculer le temps pour atteindre la zone de sûreté
    time_to_safe = player_safe_distance / player_speed
    
    # Calculer le temps avant que la tempête nous rattrape
    # La tempête doit parcourir storm_player_distance + la distance qu'on parcourt
    distance_storm_must_travel = storm_player_distance + player_safe_distance
    time_until_caught = distance_storm_must_travel / storm_speed
    
    # On survit si on arrive avant la tempête
    return time_to_safe < time_until_caught

# Lire le fichier d'entrée
survivals = 0
with open('storm_survival_brest.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Sauter la ligne d'en-tête
    for row in reader:
        player_safe_distance = float(row[0])
        player_speed = float(row[1])
        storm_player_distance = float(row[2])
        storm_speed = float(row[3])
        
        if can_survive(player_safe_distance, player_speed, storm_player_distance, storm_speed):
            survivals += 1

print(survivals)