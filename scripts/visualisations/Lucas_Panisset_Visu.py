import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation



def rechercheBinaire(list,n):
    g=0
    d=len(list)-1
    m=(g+d)//2
    while g<=d :
        yield m
        if list[m]==n:
                return m
        elif list[m]>n:
            d=m-1
        else:
            g=m +1
        m=(g+d)//2
    return None
        
def visualize_recherche_linaire(l:list[int], cible:int):
    l.sort()
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
    
    def update(i):
        for bar in bars:
            bar.set_color("blue")
        bars[i].set_color("red")
        return bars
    
    ani = animation.FuncAnimation(
        fig,
        update,
        frames= rechercheBinaire(l,cible),
        init_func= init,
        interval = 100,
        repeat = False
        
    )

    plt.show()


random_values = [random.randint(0, 100) for _ in range(50)]
visualize_recherche_linaire(random_values, 25)