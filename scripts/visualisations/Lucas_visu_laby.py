import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


grid =np.array([
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,1,0,0],
    [1,0,1,0,1],
    [1,1,1,0,0]
])


start=(0,0)
fin=(4,4)

fig,ax = plt.subplots()
im=ax.imshow(grid,cmap='gray_r')

ax.scatter(start[0],start[1],color="Green",s=150,label="Départ")
ax.scatter(fin[0],fin[1],color="Red",s=150,label="Fin")
plt.title("Grille du labyrinth")
plt.plot(fin[0], fin[1], color='blue', linewidth=2, label='Chemin le plus court')
plt.legend(loc='upper right')

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
        update(path)
        plt.pause(0.2)
        cell = parents.get(cell)
    
    path.reverse()  # Chemin dans le bon ordre
    print( explored_cells, path)

def update(path=None):
    if path:
        y_coords, x_coords = zip(*path)
        plt.plot(x_coords, y_coords, color='blue', linewidth=2, label='Chemin le plus court')
        

update()

print(dijkstra_no_heap(grid,start,fin))

plt.show()
