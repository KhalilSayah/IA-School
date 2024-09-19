
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