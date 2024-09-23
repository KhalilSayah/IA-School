#Gil Elisabeth B2IA Exercice visualisation des algortihme de tri

#recherche lin graph

def recherche_binaire_graph(liste: list[int], cible: int):
    liste.sort() 
    bas, haut = 0, len(liste) - 1
    
    while bas <= haut:
        milieu = (bas + haut) // 2
        yield milieu 
        
        if liste[milieu] < cible:
            bas = milieu + 1
        elif liste[milieu] > cible:
            haut = milieu - 1
        else:
            return milieu
    return -1


import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def visualiser_recherche_binaire(liste: list[int], cible: int):
    fig, ax = plt.subplots()

    barres = ax.bar(
        range(len(liste)),
        liste,
        color='blue'
    )

    def init():
        for barre in barres:
            barre.set_color("blue")
        return barres

    def mise_a_jour(i):
        for barre in barres:
            barre.set_color("blue")
        barres[i].set_color("red")
        return barres

    ani = animation.FuncAnimation(
        fig,
        mise_a_jour,
        frames=recherche_binaire_graph(liste, cible),
        init_func=init,
        interval=100, 
        repeat=False
    )

    plt.show()


valeurs_random = sorted([random.randint(0, 100) for _ in range(50)])  
visualiser_recherche_binaire(valeurs_random, 23)


#tri par bulles

def tri_bulles(liste):
    n = len(liste)
    for i in range(n-1):
        for j in range(n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
                yield liste

def visu_tri_bulles(liste):
    fig, ax = plt.subplots()
    rects = ax.bar(range(len(liste)), liste)
    ax.set_ylim(0, max(liste) * 1.1)
    for i, liste_i in enumerate(tri_bulles(liste)):
        for rect, h in zip(rects, liste_i):
            rect.set_height(h)
        plt.pause(0.1)

    plt.show()

# Test sur liste de 50 entiers aléatoies

liste = [random.randint(1, 100) for _ in range(50)]
visu_tri_bulles(liste)

#Partie 2 ajout d'algoritmes de tri

#tri sélection

def tri_selection(liste):
    n = len(liste)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if liste[j] < liste[min_idx]:
                min_idx = j
        liste[i], liste[min_idx] = liste[min_idx], liste[i]
        yield liste  

def visu_tri_selection(liste):
    fig, ax = plt.subplots()
    rects = ax.bar(range(len(liste)), liste, color='blue')
    ax.set_ylim(0, max(liste) * 1.1)

    def mise_a_jour(liste):
        for rect, val in zip(rects, liste):
            rect.set_height(val)
        return rects

    ani = animation.FuncAnimation(
        fig, mise_a_jour, frames=tri_selection(liste),
        interval=200, repeat=False
    )
    plt.show()

# Test avec une liste de 50 nombres aléatoires
liste = [random.randint(1, 100) for _ in range(50)]
visu_tri_selection(liste)

#tri rapide

def tri_rapid(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return tri_rapid(left) + middle + tri_rapid(right)

def visu_tri_rapide(liste):
    fig, ax = plt.subplots()
    rects = ax.bar(range(len(liste)), liste, color='blue')
    ax.set_ylim(0, max(liste) * 1.1)

    def mise_a_jour(liste):
        for rect, val in zip(rects, liste):
            rect.set_height(val)
        return rects

    ani = animation.FuncAnimation(
        fig, mise_a_jour, frames=tri_rapid(liste),
        interval=200, repeat=False
    )
    plt.show()

#Test avec une liste de 50 nombres aléatoires
liste = [random.randint(1, 100) for _ in range(50)]
visu_tri_rapide(liste)

#tri fusion

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def visu_tri_fusion(liste):
    fig, ax = plt.subplots()
    rects = ax.bar(range(len(liste)), liste, color='blue')
    ax.set_ylim(0, max(liste) * 1.1)

    def mise_a_jour(liste):
        for rect, val in zip(rects, liste):
            rect.set_height(val)
        return rects

    ani = animation.FuncAnimation(
        fig, mise_a_jour, frames=merge_sort(liste),
        interval=200, repeat=False
    )
    plt.show()

#Test avec une liste de 50 nombres aléatoires
liste = [random.randint(1, 100) for _ in range(50)]
visu_tri_fusion(liste)

#tri insetion
def tri_insertion(liste):
    for i in range(1, len(liste)):
        cle = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > cle:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = cle
        yield liste  

def visu_tri_insertion(liste):
    fig, ax = plt.subplots()
    rects = ax.bar(range(len(liste)), liste, color='blue')
    ax.set_ylim(0, max(liste) * 1.1)

    def mise_a_jour(liste):
        for rect, val in zip(rects, liste):
            rect.set_height(val)
        return rects

    ani = animation.FuncAnimation(
        fig, mise_a_jour, frames=tri_insertion(liste),
        interval=200, repeat=False
    )
    plt.show()

#test avec une liste de 50 nombres aléatoires
liste = [random.randint(1, 100) for _ in range(50)]
visu_tri_insertion(liste)

#j'ai fais comme pour tri bulles

#Visualtiosation des algorithmes

def visualize_sorts():
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    ax1, ax2, ax3, ax4 = axes.flatten()

    N = 50
    array = [random.randint(1, 100) for _ in range(N)]
    arrays = [array.copy() for _ in range(4)]  

    ax1.set_title("Tri à bulles")
    ax2.set_title("Tri par insertion")
    ax3.set_title("Tri rapide")
    ax4.set_title("Tri fusion")

    plots = [ax1, ax2, ax3, ax4]
    bars = []

    iteration_texts = []
    for ax in plots:
        bar = ax.bar(range(len(array)), arrays[plots.index(ax)], color="blue")
        bars.append(bar)
        iteration_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, ha="left")
        iteration_texts.append(iteration_text)

    iteration_counts = [0] * 4  
    completed = [False] * 4 

    def update(frames):
        for i, bar in enumerate(bars):
            if completed[i]:
                continue  
            array = frames[i]
            if array is None:
                completed[i] = True  
                continue

            for rect, val in zip(bar, array):
                rect.set_height(val)

            iteration_counts[i] += 1
            iteration_texts[i].set_text(f"Iterations: {iteration_counts[i]}")

        return bars + iteration_texts

    # affichage algo
    anims = [
        visu_tri_bulles(arrays[0]),
        visu_tri_insertion(arrays[1]),
        visu_tri_rapide(arrays[2]),
        visu_tri_fusion(arrays[3]),
    ]

    def frames_gen():
        while True:
            frames = []
            all_completed = True
            for i, anim in enumerate(anims):
                try:
                    frame = next(anim)
                    frames.append(frame)
                    all_completed = False  
                except StopIteration:
                    frames.append(None)  
            if all_completed:
                break
            yield frames

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=frames_gen,
        interval=1,
        repeat=False,
        blit=False 
    )

    plt.tight_layout()
    plt.show()

visualize_sorts()

