import random  
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definition des fonctions de tri 

def tri_par_bulles(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr
                

def tri_par_insertion(l):
    N = len(l)
    for i in range(1,N):
        cle = l[i]
        j = i-1

        while j>=0 and l[j] > cle:
            l[j+1] = l[j]
            j = j-1

        l[j+1] = cle
    return l

def tri_rapid(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return tri_rapid(left) + middle + tri_rapid(right)


## Visualition des 3 tris :


def visualiser_tri_par_bulles(arr):
    fig, ax = plt.subplots()
    barres = ax.bar(range(len(arr)), arr, color='blue')

    def mise_a_jour(arr):
        for rect, val in zip(barres, arr):
            rect.set_height(val)

    ani = animation.FuncAnimation(
        fig, mise_a_jour, frames=tri_par_bulles(arr), interval=100, repeat=False
    )
    
    plt.show()


valeurs_aleatoires = [random.randint(0, 100) for _ in range(50)]
visualiser_tri_par_bulles(valeurs_aleatoires)



def visualiser_tri_par_insertion(arr):
    fig, ax = plt.subplots()
    barres = ax.bar(range(len(arr)), arr, color='green')

    def mise_a_jour(arr):
        for rect, val in zip(barres, arr):
            rect.set_height(val)

    ani = animation.FuncAnimation(
        fig, mise_a_jour, frames=tri_par_insertion(arr), interval=100, repeat=False
    )
    
    plt.show()


valeurs_aleatoires = [random.randint(0, 100) for _ in range(50)]
visualiser_tri_par_insertion(valeurs_aleatoires)
                             
                
                             

def partition(arr, debut, fin): #pour le pivot 
    pivot = arr[fin]
    i = debut - 1
    for j in range(debut, fin):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        yield arr  
    arr[i+1], arr[fin] = arr[fin], arr[i+1]
    yield arr  
    return i+1

def visualiser_tri_rapide(arr):
    fig, ax = plt.subplots()
    barres = ax.bar(range(len(arr)), arr, color='red')

    def mise_a_jour(arr):
        for rect, val in zip(barres, arr):
            rect.set_height(val)

    ani = animation.FuncAnimation(
        fig, mise_a_jour, frames=tri_rapid(arr), interval=100, repeat=False
    )
    
    plt.show()


valeurs_aleatoires = [random.randint(0, 100) for _ in range(50)]
visualiser_tri_rapide(valeurs_aleatoires)