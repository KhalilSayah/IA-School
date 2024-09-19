
def recherche_linaire_graph(l, cible):
    for i in range(len(l)):
        yield i
        if l[i] == cible:
            return i
        

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


