import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def tri_par_bulles(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            yield arr

def tri_par_insertion(l):
    N = len(l)
    for i in range(1,N):
        cle = l[i]
        j = i-1
        while j>=0 and l[j] > cle:
            l[j+1] = l[j]
            j = j-1
            yield l

        l[j+1] = cle
        yield l

def tri_rapide(arr, low, high):
    if low < high:
        pi = yield from partition(arr, low, high) 
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
    gauche = arr[left:mid + 1]
    droite = arr[mid + 1:right + 1]
    i = j = 0
    k = left
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            arr[k] = gauche[i]
            i += 1
        else:
            arr[k] = droite[j]
            j += 1
        k += 1
        yield arr
    while i < len(gauche):
        arr[k] = gauche[i]
        i += 1
        k += 1
        yield arr
    while j < len(droite):
        arr[k] = droite[j]
        j += 1
        k += 1
        yield arr

def Visualisation(arr):
    fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)
    global bars1 ,bars2,bars3,bars4
    bars1 = ax1.bar(range(len(arr)),arr,color = 'green')
    bars2 = ax2.bar(range(len(arr)),arr,color = 'orange')
    bars3 = ax3.bar(range(len(arr)),arr,color = 'yellow')
    bars4 = ax4.bar(range(len(arr)),arr,color = 'pink')


    def update(arr):
        for bar,height in zip(bars1,arr):
            bar.set_height(height)
        ax1.set_title(f'Tri bulles - nb Itérations: {count1}')
        plt.pause(0.01)
    def update2(arr):
        for bar,height in zip(bars2,arr):
            bar.set_height(height)
        ax2.set_title(f'Tri insertion - nb Itérations: {count2}')
        plt.pause(0.01)
    def update3(arr):
        for bar,height in zip(bars3,arr):
            bar.set_height(height)
        ax3.set_title(f'Tri rapide - nb Itérations: {count3}')
        plt.pause(0.01)
    def update4(arr):
        for bar,height in zip(bars4,arr):
            bar.set_height(height)
        ax4.set_title(f'Tri fusion- nb Itérations: {count4}')
        plt.pause(0.01)
    
    arr_bulles=arr.copy()
    arr_inser=arr.copy()
    arr_rapid=arr.copy()
    arr_fusion=arr.copy()

    bubble_gen=tri_par_bulles(arr_bulles)
    insertion_gen=tri_par_insertion(arr_inser)
    rapid_gen=tri_rapide(arr_rapid,0,len(arr_rapid)-1)
    fusion_gen=tri_fusion(arr_fusion,0,len(arr_fusion)-1)

    global count1,count2,count3,count4
    count1=0
    count2=0
    count3=0
    count4=0
    v1=True
    v2=True
    v3=True
    v4=True


    while v1==True or v2==True or v3==True or v4==True:
        
        try:
            arr=next(bubble_gen)
            count1+=1
            update(arr)  
        except StopIteration:
            v1=False
            pass
        try:
            arr=next(insertion_gen)
            count2+=1
            update2(arr)  
        except StopIteration:
            v2=False
            pass
        try:
            arr=next(rapid_gen)
            count3+=1
            update3(arr)  
        except StopIteration:
            v2=False
            pass
        try:
            arr=next(fusion_gen)
            count4+=1
            update4(arr)  
        except StopIteration:
            v2=False
            pass

        
        

    plt.show()

random_values = [random.randint(0, 125) for _ in range(50)]

Visualisation(random_values)

