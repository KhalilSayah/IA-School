
from matplotlib.animation import FuncAnimation
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
#TAILLE DE LA GRILLE

n = 15
m = 15

# CREATION DE LA GRILLE
grid_data = np.array([
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

start = (0,0) 
finish = (n - 1, m - 1)


fig,ax = plt.subplots(figsize = (6,6) )
im = ax.imshow(grid_data, cmap='gray_r')

ax.scatter(start[1], start[0], color='magenta', s=100, label='Start')
ax.scatter(finish[1], finish[0], color='red', s=100, label='End')
ax.legend()
plt.show()
"""
# Afficher la matrice sous forme de grille

plt.grid(visible=True)  # Afficher la grille de l'axe
plt.matshow(grid_data, cmap='grey')  # 'coolwarm' est une autre palette de couleurs


"""