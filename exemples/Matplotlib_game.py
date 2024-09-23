import matplotlib

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
matplotlib.use('TkAgg')
# Taille du labyrinthe
n, m = 15, 15

# Grille définie manuellement (0 = libre, 1 = obstacle)
grid = np.array([
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
])

# Définir un point de départ et un point d'arrivée
start = (0, 0)  # Coin supérieur gauche
end = (n-1, m-1)  # Coin inférieur droit

# Fonction d'animation
fig, ax = plt.subplots(figsize=(6, 6))
im = ax.imshow(grid, cmap='gray_r')

# Définir le départ et l'arrivée avec des marqueurs
ax.scatter(start[1], start[0], color='green', s=100, label='Start')
ax.scatter(end[1], end[0], color='red', s=100, label='End')
ax.legend()

# Algorithme de Dijkstra sans heapq
def dijkstra_no_heap(grid, start, end):
    n, m = grid.shape
    distances = { (i, j): float('inf') for i in range(n) for j in range(m) }
    distances[start] = 0
    visited = { (i, j): False for i in range(n) for j in range(m) }
    parents = {start: None}
    explored_cells = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Haut, Bas, Gauche, Droite

    while True:
        # Trouver la cellule non visitée avec la plus petite distance
        min_distance = float('inf')
        current_cell = None
        for i in range(n):
            for j in range(m):
                if not visited[(i, j)] and distances[(i, j)] < min_distance:
                    min_distance = distances[(i, j)]
                    current_cell = (i, j)

        # Si on n'a plus de cellules accessibles ou si on a atteint la destination
        if current_cell is None or current_cell == end:
            break

        x, y = current_cell
        visited[current_cell] = True

        # Ajouter la case explorée à la liste pour l'animation
        explored_cells.append(current_cell)

        # Explorer les voisins
        for direction in directions:
            nx, ny = x + direction[0], y + direction[1]

            if 0 <= nx < n and 0 <= ny < m and grid[nx, ny] == 0:  # Si la case est dans la grille et libre
                new_distance = distances[(x, y)] + 1

                if new_distance < distances[(nx, ny)]:
                    distances[(nx, ny)] = new_distance
                    parents[(nx, ny)] = (x, y)

    # Reconstruire le chemin
    path = []
    cell = end
    while cell is not None:
        path.append(cell)
        cell = parents.get(cell)
    
    path.reverse()  # Chemin dans le bon ordre
    return explored_cells, path

# Trouver les étapes d'exploration et le chemin avec Dijkstra sans heapq
explored_cells, path = dijkstra_no_heap(grid, start, end)

# Fonction d'animation mise à jour à chaque étape
def update(num):
    # Réinitialiser l'image
    im.set_data(grid)
    
    # Mettre à jour l'animation pour les cases explorées jusqu'à l'étape num
    if num < len(explored_cells):
        x, y = explored_cells[num]
        grid[x, y] = 0.5  # Marquer comme exploré (grisé)
    
    # Une fois toutes les cases explorées, dessiner le chemin
    if num == len(explored_cells):
        for (x, y) in path:
            grid[x, y] = 0.2  # Chemin trouvé (coloré en bleu clair)
    
    return [im]

# Création de l'animation
ani = FuncAnimation(fig, update, frames=len(explored_cells)+1, interval=200, repeat=False)

plt.show()
