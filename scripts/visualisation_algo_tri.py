import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Tri à bulles
def tri_par_bulles_animation(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            yield arr
        if not swapped:
            break

# Tri par insertion
def tri_par_insertion_animation(arr):
    for i in range(1, len(arr)):
        cle = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > cle:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr
        arr[j + 1] = cle
        yield arr

# Tri rapide
def tri_rapid_animation(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot = yield from partition(arr, low, high)
        yield from tri_rapid_animation(arr, low, pivot - 1)
        yield from tri_rapid_animation(arr, pivot + 1, high)
    yield arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[i], arr[j]
        yield arr
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr
    return i + 1

# Tri fusion
def merge_sort_animation(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    yield from merge_sort_animation(left)
    yield from merge_sort_animation(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        yield arr

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        yield arr

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        yield arr

# Fonction pour afficher les animations
def visualize_sorts():
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    ax1, ax2, ax3, ax4 = axes.flatten()

    N = 50
    array = [random.randint(1, 100) for _ in range(N)]
    arrays = [array.copy() for _ in range(4)]  # Copies des tableaux pour chaque tri

    ax1.set_title("Tri à bulles")
    ax2.set_title("Tri par insertion")
    ax3.set_title("Tri rapide")
    ax4.set_title("Tri fusion")

    plots = [ax1, ax2, ax3, ax4]
    bars = []

    # Initialisation des barres et du texte pour les itérations
    iteration_texts = []
    for ax in plots:
        bar = ax.bar(range(len(array)), arrays[plots.index(ax)], color="blue")
        bars.append(bar)
        iteration_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, ha="left")
        iteration_texts.append(iteration_text)

    iteration_counts = [0] * 4  # Compteurs d'itérations pour chaque algorithme
    completed = [False] * 4  # Indicateurs pour savoir si le tri est terminé pour chaque algorithme

    def update(frames):
        for i, bar in enumerate(bars):
            if completed[i]:
                continue  # Si l'algorithme est terminé, ne pas mettre à jour

            array = frames[i]
            if array is None:
                completed[i] = True  # Marquer l'algorithme comme terminé
                continue

            for rect, val in zip(bar, array):
                rect.set_height(val)

            # Mettre à jour le texte avec le nombre d'itérations
            iteration_counts[i] += 1
            iteration_texts[i].set_text(f"Iterations: {iteration_counts[i]}")

        return bars + iteration_texts

    # Générateurs des algorithmes
    anims = [
        tri_par_bulles_animation(arrays[0]),
        tri_par_insertion_animation(arrays[1]),
        tri_rapid_animation(arrays[2]),
        merge_sort_animation(arrays[3]),
    ]

    # Fonction pour générer les frames pour tous les algorithmes
    def frames_gen():
        while True:
            frames = []
            all_completed = True
            for i, anim in enumerate(anims):
                try:
                    frame = next(anim)
                    frames.append(frame)
                    all_completed = False  # Au moins un algorithme n'a pas terminé
                except StopIteration:
                    frames.append(None)  # Cet algorithme est terminé
            if all_completed:
                break
            yield frames

    ani = animation.FuncAnimation(
        fig,
        update,
        frames=frames_gen,
        interval=1,
        repeat=False,
        blit=False  # blit=False car on a plusieurs subplots à mettre à jour
    )

    plt.tight_layout()
    plt.show()

# Appeler la fonction pour visualiser les algorithmes de tri
visualize_sorts()
