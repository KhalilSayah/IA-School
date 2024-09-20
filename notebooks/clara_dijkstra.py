import numpy as np
import matplotlib.pyplot as plt
import heapq

directions = [(-1,0), (1,0), (0,-1), (0,1)]

def grille(rows, cols, obstacle_prob=0.2, start=(0, 0), end=None):

    matrix = np.random.choice([0, 1], size=(rows, cols), p=[1 - obstacle_prob, obstacle_prob])

    if end is None:
        end = (rows - 1, cols - 1)

    matrix[start] = 0  
    matrix[end] = 0    

    return matrix, start, end

def tracer(matrix, start, end, path=None, title="Grille avec Départ et Arrivée"):

    plt.figure(figsize=(8, 8))
    plt.imshow(matrix, cmap='Greys', origin='upper')


    if path:
        y_coords, x_coords = zip(*path)
        plt.plot(x_coords, y_coords, color='yellow', linewidth=2, label='Chemin le plus court')


    plt.scatter(start[1], start[0], marker='o', color='green', s=100, label='Départ (A)')


    plt.scatter(end[1], end[0], marker='x', color='red', s=100, label='Arrivée (B)')

    plt.title(title)
    plt.legend(loc='upper right')
    plt.gca().invert_yaxis() 
    plt.grid(True, which='both', color='lightgrey', linewidth=0.5)
    plt.xticks(np.arange(-0.5, matrix.shape[1], 1), [])
    plt.yticks(np.arange(-0.5, matrix.shape[0], 1), [])
    plt.show()

def dijkstra(matrix, start, end):
    rows, cols = matrix.shape
    distance = np.full((rows, cols), np.inf)
    distance[start] = 0
    visited = np.zeros((rows, cols), dtype=bool)
    previous = np.full((rows, cols, 2), -1, dtype=int)

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        current_dist, current = heapq.heappop(heap)
        if visited[current]:
            continue
        visited[current] = True

        if current == end:
            break

        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and 
                matrix[neighbor] == 0 and not visited[neighbor]):
                new_dist = current_dist + 1  
                if new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    previous[neighbor] = current
                    heapq.heappush(heap, (new_dist, neighbor))


    path = []
    if distance[end] != np.inf:
        at = end
        while at != start:
            path.append(at)
            at = tuple(previous[at])
        path.append(start)
        path.reverse()

    return distance[end], path

def main():

    rows, cols = 20, 20  
    obstacle_prob = 0.2    
    start = (0, 0)         
    end = (19, 19)         


    matrix, start, end = grille(rows, cols, obstacle_prob, start, end)

    distance, path = dijkstra(matrix, start, end)
    print(f"Distance minimale de {start} à {end}: {distance}")
    print(f"Chemin le plus court: {path}")

    tracer(matrix, start, end, path, title="Algorithme de Dijkstra")

if __name__ == "__main__":
        main()
