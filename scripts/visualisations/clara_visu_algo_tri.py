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


def update_func1(arr, count, bars, ax1):
    for bar, height in zip(bars, arr):
        bar.set_height(height)
    ax1.set_title(f'Tri à bulles - Itérations: {count}')
    plt.pause(0.01)


def update_func2(arr, count, bars, ax2):
    for bar, height in zip(bars, arr):
        bar.set_height(height)
    ax2.set_title(f'Tri par insertion - Itérations: {count}')
    plt.pause(0.01)


valeurs_aleatoires = [random.randint(0, 100) for _ in range(50)]
arr_bubble = valeurs_aleatoires.copy()
arr_insertion = valeurs_aleatoires.copy()


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))
bars1 = ax1.bar(range(len(arr_bubble)), arr_bubble, color='blue')
bars2 = ax2.bar(range(len(arr_insertion)), arr_insertion, color='green')

ax1.set_title('Tri à bulles')
ax2.set_title('Tri par insertion')


bubble_gen = tri_par_bulles(arr_bubble)
insertion_gen = tri_par_insertion(arr_insertion)


count1 = 0
count2 = 0


while True:
    try:
        arr_bubble = next(bubble_gen)
        count1 += 1
        update_func1(arr_bubble, count1, bars1, ax1)
    except StopIteration:
        break

while True:
    try:
        arr_insertion = next(insertion_gen)
        count2 += 1
        update_func2(arr_insertion, count2, bars2, ax2)
    except StopIteration:
        break

plt.show()
