import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def recherche_binaire_graph(l: list[int], cible: int):
    steps = []
    gauche, droite = 0, len(l) - 1
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        steps.append((gauche, milieu, droite))  
        
        if l[milieu] == cible:
            break
        elif l[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1

    return steps

def visualize_recherche_binaire(l: list[int], cible: int):
    l.sort()  
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(l)), l, color="blue")

    def init():
        for bar in bars:
            bar.set_color("blue")
        return bars

    def update(step):
        gauche, milieu, droite = step
        for i, bar in enumerate(bars):
            if gauche <= i <= droite:
                bar.set_color("yellow")  
            else:
                bar.set_color("blue")
        bars[milieu].set_color("red")
        return bars

    steps = recherche_binaire_graph(l, cible)

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=steps,
        init_func=init,
        interval=500,
        repeat=False
    )

    plt.show()

values = [random.randint(0, 100) for _ in range(50)]
visualize_recherche_binaire(values, 83)

#Trie par bulles visualisation : 
def tri_par_bulles_graph(arr):
    n = len(arr)
    steps = []
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            steps.append(list(arr))
    return steps

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Tri par bulle avec visualisation
def tri_par_bulles_graph(arr):
    n = len(arr)
    steps = []
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            steps.append(list(arr))  # Enregistrer l'état après chaque échange
    return steps

# Tri par insertion avec visualisation
def tri_par_insertion_graph(arr):
    N = len(arr)
    steps = []
    for i in range(1, N):
        cle = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > cle:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cle
        steps.append(list(arr))  
    return steps

# Tri rapide avec visualisation
def tri_rapide_graph(arr):
    steps = []

    def tri_rapide_rec(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        sorted_arr = tri_rapide_rec(left) + middle + tri_rapide_rec(right)
        steps.append(list(sorted_arr))
        return sorted_arr

    tri_rapide_rec(arr)
    return steps

def tri_fusion_graph(arr):
    steps = []

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
        steps.append(list(result)) 
        return result

    def tri_fusion_rec(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_half = tri_fusion_rec(arr[:mid])
        right_half = tri_fusion_rec(arr[mid:])
        return merge(left_half, right_half)

    tri_fusion_rec(arr)
    return steps

def visualize_all_sorts(values):
    fig, axs = plt.subplots(2, 2, figsize=(12, 8)) 
    fig.suptitle('Visualisation des algorithmes de tri')

    bars_bulle = axs[0, 0].bar(range(len(values)), values, color="blue")
    axs[0, 0].set_title("Tri par bulle")

    bars_insertion = axs[0, 1].bar(range(len(values)), values, color="blue")
    axs[0, 1].set_title("Tri par insertion")

    bars_rapide = axs[1, 0].bar(range(len(values)), values, color="blue")
    axs[1, 0].set_title("Tri rapide")

    bars_fusion = axs[1, 1].bar(range(len(values)), values, color="blue")
    axs[1, 1].set_title("Tri fusion")

    steps_bulle = tri_par_bulles_graph(list(values))
    steps_insertion = tri_par_insertion_graph(list(values))
    steps_rapide = tri_rapide_graph(list(values))
    steps_fusion = tri_fusion_graph(list(values))

    def init():
        for bars in [bars_bulle, bars_insertion, bars_rapide, bars_fusion]:
            for bar in bars:
                bar.set_color("blue")
        return bars_bulle, bars_insertion, bars_rapide, bars_fusion

    def update(frame):
        if frame < len(steps_bulle):
            for bar, val in zip(bars_bulle, steps_bulle[frame]):
                bar.set_height(val)
        if frame < len(steps_insertion):
            for bar, val in zip(bars_insertion, steps_insertion[frame]):
                bar.set_height(val)
        if frame < len(steps_rapide):
            for bar, val in zip(bars_rapide, steps_rapide[frame]):
                bar.set_height(val)
        if frame < len(steps_fusion):
            for bar, val in zip(bars_fusion, steps_fusion[frame]):
                bar.set_height(val)
        return bars_bulle, bars_insertion, bars_rapide, bars_fusion

    max_frames = max(len(steps_bulle), len(steps_insertion), len(steps_rapide), len(steps_fusion))

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=max_frames,
        init_func=init,
        interval=300, 
        repeat=False
    )

    plt.tight_layout()
    plt.show()

values = [random.randint(0, 100) for _ in range(50)]

visualize_all_sorts(values)


