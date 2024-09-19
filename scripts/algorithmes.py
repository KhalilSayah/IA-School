
def recherche_linaire_graph(l, cible):
    for i in range(len(l)):
        yield i
        if l[i] == cible:
            return i