def recherche_binaire_graph(liste: list[int], cible: int):
    liste.sort() 
    bas, haut = 0, len(liste) - 1
    
    while bas <= haut:
        milieu = (bas + haut) // 2
        yield milieu 
        
        if liste[milieu] < cible:
            bas = milieu + 1
        elif liste[milieu] > cible:
            haut = milieu - 1
        else:
            return milieu
    return -1


import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def visualiser_recherche_binaire(liste: list[int], cible: int):
    fig, ax = plt.subplots()

    barres = ax.bar(
        range(len(liste)),
        liste,
        color='blue'
    )

    def init():
        for barre in barres:
            barre.set_color("blue")
        return barres

    def mise_a_jour(i):
        for barre in barres:
            barre.set_color("blue")
        barres[i].set_color("red")
        return barres

    ani = animation.FuncAnimation(
        fig,
        mise_a_jour,
        frames=recherche_binaire_graph(liste, cible),
        init_func=init,
        interval=100, 
        repeat=False
    )

    plt.show()

# Test avec des valeurs aléatoires triées
valeurs_aleatoires = sorted([random.randint(0, 100) for _ in range(50)])  # Liste triée nécessaire pour la recherche binaire
visualiser_recherche_binaire(valeurs_aleatoires, 23)


