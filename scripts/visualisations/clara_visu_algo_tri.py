import random
import matplotlib.pyplot as plt
import time


def tri_par_bulles(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield arr


def tri_par_insertion(arr):
    N = len(arr)
    for i in range(1, N):
        cle = arr[i]
        j = i-1
        while j >= 0 and arr[j] > cle:
            arr[j+1] = arr[j]
            j -= 1
            yield arr
        arr[j+1] = cle
        yield arr


def tri_rapide(arr, low, high):
    if low < high:
        pi = yield from partition(arr, low, high)  # partition doit être itérable
        yield from tri_rapide(arr, low, pi - 1)
        yield from tri_rapide(arr, pi + 1, high)
    yield arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        yield arr
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    yield arr
    return i + 1  


def tri_fusion(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        yield from tri_fusion(arr, left, mid)
        yield from tri_fusion(arr, mid + 1, right)
        yield from fusion(arr, left, mid, right)
    yield arr

def fusion(arr, left, mid, right):
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        yield arr
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
        yield arr
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        yield arr

def update_func(arr, count, bars, ax, title):
    for bar, height in zip(bars, arr):
        bar.set_height(height)
    ax.set_title(f'{title} - Itérations: {count}')
    plt.pause(0.01)


valeurs_aleatoires = [random.randint(0, 100) for _ in range(50)]
arr_bubble = valeurs_aleatoires.copy()
arr_insertion = valeurs_aleatoires.copy()
arr_quick = valeurs_aleatoires.copy()
arr_merge = valeurs_aleatoires.copy()


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 12))
bars1 = ax1.bar(range(len(arr_bubble)), arr_bubble, color='blue')
bars2 = ax2.bar(range(len(arr_insertion)), arr_insertion, color='green')
bars3 = ax3.bar(range(len(arr_quick)), arr_quick, color='red')
bars4 = ax4.bar(range(len(arr_merge)), arr_merge, color='purple')

ax1.set_title('Tri à bulles')
ax2.set_title('Tri par insertion')
ax3.set_title('Tri rapide')
ax4.set_title('Tri fusion')


bubble_gen = tri_par_bulles(arr_bubble)
insertion_gen = tri_par_insertion(arr_insertion)
quick_gen = tri_rapide(arr_quick, 0, len(arr_quick) - 1)
merge_gen = tri_fusion(arr_merge, 0, len(arr_merge) - 1)

count1 = count2 = count3 = count4 = 0
active_generators = [bubble_gen, insertion_gen, quick_gen, merge_gen]
active_counts = [count1, count2, count3, count4]
bars_list = [bars1, bars2, bars3, bars4]
axes_list = [ax1, ax2, ax3, ax4]
titles = ['Tri à bulles', 'Tri par insertion', 'Tri rapide', 'Tri fusion']


while active_generators:
    for i in range(len(active_generators) - 1, -1, -1): 
        try:
            arr = next(active_generators[i])
            active_counts[i] += 1
            update_func(arr, active_counts[i], bars_list[i], axes_list[i], titles[i])
        except StopIteration:
            active_generators.pop(i)  
plt.show()
