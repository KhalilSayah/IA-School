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

def dijkstra(matrix, start, end):
    n = len(matrix)
    dist = [float('inf')] * n  # Tableau des distances initialisé à l'infini
    dist[start] = 0  # La distance depuis le départ
    visited = [False] * n  # Tableau pour suivre les nœuds visités
    previous = [None] * n  # Pour reconstruire le chemin

    for _ in range(n):
        # Trouver le nœud avec la distance minimale non visité
        min_dist = float('inf')
        min_index = -1
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_index = i

        if min_index == -1:  # Tous les nœuds visités ou inaccessible
            break

        visited[min_index] = True  # Marquer le nœud comme visité

        # Mettre à jour les distances des voisins
        for neighbor in range(n):
            if matrix[min_index][neighbor] > 0:  # Si une arête existe
                new_dist = dist[min_index] + matrix[min_index][neighbor]
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    previous[neighbor] = min_index

    # Reconstruire le chemin
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return dist[end], path 

def update(arr):
    de



#print(dijkstra(grid,0,24))
plt.show()
