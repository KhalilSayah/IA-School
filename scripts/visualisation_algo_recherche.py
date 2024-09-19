import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from algorithmes import recherche_linaire_graph



        
def visualize_recherche_linaire(l:list[int], cible:int):
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
        frames= recherche_linaire_graph(l,cible),
        init_func= init,
        interval = 100,
        repeat = False
        
    )

    plt.show()


random_values = [random.randint(0, 100) for _ in range(50)]
visualize_recherche_linaire(random_values, 23)