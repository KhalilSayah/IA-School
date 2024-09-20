import numpy as np
import matplotlib.pyplot as plt

def grille(rows, cols, obstacle_prob=0.2, start=(0, 0), end=None):
    
    matrix = np.random.choice([0, 1], size=(rows, cols), p=[1 - obstacle_prob, obstacle_prob])
    
    if end is None:
        end = (rows - 1, cols - 1)
    
    matrix[start] = 0  
    matrix[end] = 0    
    
    return matrix, start, end

def tracer(matrix, start, end, title="Grille avec Départ et Arrivée"):

    plt.figure(figsize=(8, 8))
    plt.imshow(matrix, cmap='Greys', origin='upper')
    
    plt.scatter(start[1], start[0], marker='o', color='green', s=100, label='Départ (A)')
    
    plt.scatter(end[1], end[0], marker='x', color='red', s=100, label='Arrivée (B)')
    
    plt.title(title)
    plt.legend(loc='upper right')
    plt.gca().invert_yaxis()
    plt.grid(True, which='both', color='lightgrey', linewidth=0.5)
    plt.xticks(np.arange(-0.5, matrix.shape[1], 1), [])
    plt.yticks(np.arange(-0.5, matrix.shape[0], 1), [])
    plt.show()

def main():

    rows, cols = 20, 20  
    obstacle_prob = 0.2    
    start = (0, 0)         
    end = (19, 19)       
    
    matrix, start, end = grille(rows, cols, obstacle_prob, start, end)
    
    tracer(matrix, start, end, title="Matrice")
    

main()
