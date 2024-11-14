import numpy as np

def calculate_cross_sum(grid, x, y):
    center = grid[y][x]
    up = grid[y-1][x]
    down = grid[y+1][x]
    left = grid[y][x-1]
    right = grid[y][x+1]
    total = center + up + down + left + right
    print(f"\nPosition testée ({x},{y}):")
    print(f"     {up}")
    print(f"{left}  {center}  {right}")
    print(f"     {down}")
    print(f"Somme: {total}\n")
    return total

def find_best_cross(grid):
    height = len(grid)
    width = len(grid[0])
    max_sum = 0
    best_x = 0
    best_y = 0
    
    for y in range(1, height-1):
        for x in range(1, width-1):
            current_sum = calculate_cross_sum(grid, x, y)
            if current_sum > max_sum:
                max_sum = current_sum
                best_x = x
                best_y = y
                print(f"Nouvelle meilleure somme trouvée!")
                print("-" * 30)

    return best_x, best_y, int(max_sum)

# Charger les données
grid = np.loadtxt('carte_brest.csv', delimiter=',')

# Trouver la meilleure position
x, y, total = find_best_cross(grid)

# Afficher le résultat final avec visualisation de la croix
print("\nRésultat final:")
print(f"Position: {x};{y};{total}")
print(f"Valeurs de la croix:")
print(f"     {grid[y-1][x]}")
print(f"{grid[y][x-1]}  {grid[y][x]}  {grid[y][x+1]}")
print(f"     {grid[y+1][x]}")