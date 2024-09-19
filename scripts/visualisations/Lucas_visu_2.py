import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def tri_par_bulles(arr,update):
    n = len(arr)
    count=0
    for i in range(n):
        for j in range(0, n-i-1):
            count+=1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                update(arr.copy(),count)
                yield arr

def tri_par_insertion(l,update):
    N = len(l)
    count=0
    for i in range(1,N):
        cle = l[i]
        j = i-1
        count+=1
        while j>=0 and l[j] > cle:
            l[j+1] = l[j]
            j = j-1
            count+=1
            update(l.copy(),count)
            yield l

        l[j+1] = cle
    return l

def tri_rapid(arr,update):
    if len(arr) <= 1:
        yield arr
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    arr=[left+middle+right]
    update(arr)
    yield arr
    return tri_rapid(left,update) + middle + tri_rapid(right,update)


def merge_sort(arr,update):
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
    left_half = merge_sort(arr[:mid],update)
    right_half = merge_sort(arr[mid:],update)
    r= merge(left_half,right_half)
    yield r
    return merge(left_half, right_half)

def Visualisation(arr):
    fig,(ax1,ax2,ax3,ax4) = plt.subplots(1,4)
    global bars1 ,bars2,bars3,bars4
    bars1 = ax1.bar(range(len(arr)),arr,color = 'green')
    bars2 = ax2.bar(range(len(arr)),arr,color = 'orange')
    bars3 = ax3.bar(range(len(arr)),arr,color = 'yellow')
    bars4 = ax4.bar(range(len(arr)),arr,color = 'pink')


    def update(arr,count):
        for bar,height in zip(bars1,arr):
            bar.set_height(height)
        ax1.set_title(f'Tri bulles - nb Itérations: {count}')
        plt.pause(0.05)
    def update2(arr,count):
        for bar,height in zip(bars2,arr):
            bar.set_height(height)
        ax2.set_title(f'Tri insertion - nb Itérations: {count}')
        plt.pause(0.05)
    def update3(arr):
        for bar,height in zip(bars3,arr):
            bar.set_height(height)
        ax3.set_title(f'Tri insertion - nb Itérations:')
        plt.pause(0.05)
    def update4(arr):
        for bar,height in zip(bars4,arr):
            bar.set_height(height)
        ax4.set_title(f'Tri fusion- nb Itérations:')
        plt.pause(0.05)
    
    arr_bulles=arr.copy()
    arr_inser=arr.copy()
    arr_rapid=arr.copy()
    arr_fusion=arr.copy()

    bubble_gen=tri_par_bulles(arr_bulles,update)
    insertion_gen=tri_par_insertion(arr_inser,update2)
    rapid_gen=tri_rapid(arr_rapid,update3)
    fusion_gen=merge_sort(arr_fusion,update4)

    while True:
        try:
            next(bubble_gen)  
        except StopIteration:
            break

        try:
            next(insertion_gen)  
        except StopIteration:
            break
        try:
            next(rapid_gen)  
        except StopIteration:
            break

    plt.show()

random_values = [random.randint(0, 100) for _ in range(50)]

Visualisation(random_values)

