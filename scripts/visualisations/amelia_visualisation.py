import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


values = [random.randint(0,100) for _ in range(50)]

""""
def recherche_lineaire_graph(l, cible):
    for i in range(len(l)):
        yield i
        if l[i] == cible:
            return i
        

def visualize_recherche_lineaire(l:list[int], cible:int):
    fig,ax = plt.subplots()
    bars = ax.bar(
        range(len(l)),
        l,
        color = "blue"
    )

    def init():
        for bar in bars:
            bar.set_color("blue")
        return bars
    
    def update(i):
        for bar in bars:
            bar.set_color("blue")
        bars[i].set_color("red")
        return bars
    
    ani = animation.FuncAnimation(
        fig,
        update,
        frames = recherche_lineaire_graph(l,cible),
        init_func= init,
        interval = 100,
        repeat = False
    )

    plt.show()

visualize_recherche_lineaire(values,83)
"""

def recherche_dichotomique_graph(d,target):
    d.sort()
    debut,fin = 0,len(d) -1

    while debut <= fin:
        mid = (debut + fin) // 2
        yield mid

        if d[mid] == target:
            return mid
        elif d[mid] < target:
            debut = mid + 1
        else:
            fin = mid - 1


def visualize_recherche_binaire(l:list[int], cible:int):
    fig,ax = plt.subplots()
    bars = ax.bar(
        range(len(l)),
        l,
        color = "blue"
    )

    def init():
        for bar in bars:
            bar.set_color("blue")
        return bars
    
    def update(i):
        for bar in bars:
            bar.set_color("blue")
        bars[i].set_color("red")
        return bars
    
    ani = animation.FuncAnimation(
        fig,
        update,
        frames = recherche_dichotomique_graph(l,cible),
        init_func= init,
        interval = 100,
        repeat = False
    )

    plt.show()

visualize_recherche_binaire(values,83)