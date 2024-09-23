
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation




def bubble_tri(l:list,update):
    n = len(l)  # Nombre d'éléments dans le l

    # Boucle pour parcourir le l entier
    for i in range(n):
        # Derniers i éléments sont déjà triés, on les ignore
        for j in range(0, n - i - 1):
            # Si l'élément courant est plus grand que le suivant, on les échange
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

                update(l,1)
                yield 

    


def tri_par_insertion(l,update):
    N = len(l)
    for i in range(1,N):
        cle = l[i]
        j = i-1

        while j>=0 and l[j] > cle:
            l[j+1] = l[j]
            j = j-1
            update(l,2)
            yield

        l[j+1] = cle
        update(l,2)
        yield
    



"""
def visualize_tri_bulle(l:list[int]):
    fig,ax = plt.subplots()

    bars = ax.bar(
        range(len(l)),
        l,
        color = 'blue'
    )

    def init():
        for bar in bars:
            bar.set_color("blue")
        return bars
    
    def update(l):
        for i in range(len(l)):
            bars[i].set_height(l[i])
        return bars 
        
    
    ani = animation.FuncAnimation(
        fig,
        update,
        frames= bubble_tri(l),
        init_func= init,
        interval = 100,
        repeat = False
        
    )

    plt.show()
"""
random_values = [random.randint(0, 100) for _ in range(50)]

#visualize_tri_bulle(random_values)


def tri_rapide(arr, low, high):
    if low < high:
        pi = yield from partition(arr, low, high)  # partition doit être itérable
        yield from tri_rapide(arr, low, pi - 1)
        yield from tri_rapide(arr, pi + 1, high)
    yield arr
    

def partition(arr, low, high,update):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        yield arr
        update(arr,3)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]


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
                
            update(arr,4)
            yield
        update(arr,4)
        yield
            
        
        result.extend(left[i:])
        result.extend(right[j:])
        update(arr,4)
        yield

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid],update)
    right_half = merge_sort(arr[mid:],update)
    return merge(left_half, right_half)





def visualize_tri(l:list[int]):
    fig,((ax1, ax2,ax3,ax4)) = plt.subplots(4)
    bars1 = ax1.bar(
        range(len(l)),
        l,
        color = 'blue'
    )


    bars2 = ax2.bar(
        range(len(l)),
        l,
        color = 'blue'
    )

    bars3 = ax3.bar(
        range(len(l)),
        l,
        color = 'blue'
    )
    bars4 = ax4.bar(
        range(len(l)),
        l,
        color = 'blue'
    )

    def init():
        for bar in bars1:
            bar.set_color("blue")
        for bar in bars2:
            bar.set_color("blue")

        for bar in bars3:
            bar.set_color("blue")
        
        for bar in bars4:
            bar.set_color("blue")
        return bars1,bars2,bars3,bars4
    
    def update(l,num):
        if num == 1:
            for i in range(len(l)):
                bars1[i].set_height(l[i])
               
        elif num == 2:
            for i in range(len(l)):
                bars2[i].set_height(l[i])
        elif num == 3:
            for i in range(len(l)):
                bars3[i].set_height(l[i])
        else:
                for i in range(len(l)):
                    bars4[i].set_height(l[i])

                
            

    l1 = l.copy()
    l2 = l.copy()
    l3 = l.copy()
    l4 = l.copy()

    bubble_gen = bubble_tri(l1,update)
    insertion_gen = tri_par_insertion(l2,update)
    tri_rapid_gen = tri_rapide(l3,0,len(l3),update)
    merge_gen = merge_sort(l4,update)
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
            next(tri_rapid_gen)
        except StopIteration:
            break


        try:
            next(merge_gen)
        except StopIteration:
            break
        plt.pause(0.01) 
        

    
    

    plt.show()

random_values = [random.randint(0, 100) for _ in range(50)]

visualize_tri(random_values)