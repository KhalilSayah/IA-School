import pygame
from queue import PriorityQueue


pygame.init()

# Taille de la fenêtre et de la grille
ecran_taille = 600  
lignes, cols = 15, 15  
cell_size = ecran_taille // lignes  

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
BLEUE = (0, 0, 255)
VIOLET = (128, 0, 128)
TURQUOISE = (64, 224, 208)

# Fenêtre
ecran = pygame.display.set_mode((ecran_taille, ecran_taille))
pygame.display.set_caption("Visualisation Dijkstra (appuyer entrer)")

# Texte
font = pygame.font.SysFont(None, 20)

# Point de départ et d'arrivée
start = (2, 6)
end = (14, 12)  

# Classe pour chaque nœud de la grille
class Spot:
    def __init__(self, ligne, col, larg):
        self.ligne = ligne
        self.col = col
        self.x = ligne * larg
        self.y = col * larg
        self.color = BLANC
        self.voisins = []
        self.larg = larg
        self.distance = abs(ligne - start[0]) + abs(col - start[1])  # Distance de Manhattan par rapport au point de départ

    def get_pos(self):
        return self.ligne, self.col

    def dessin_grille(self):
        return self.color == NOIR

    def debut(self):
        self.color = VERT

    def fermer(self):
        self.color = TURQUOISE

    def ouverture_voisins(self):
        self.color = BLEUE  

    def arriver(self):
        self.color = ROUGE

    def chemin(self):
        self.color = VIOLET

    def draw(self, e):
        pygame.draw.rect(e, self.color, (self.col * self.larg, self.ligne * self.larg, self.larg, self.larg))
        text = font.render(str(self.distance), True, NOIR)
        e.blit(text, (self.col * self.larg + self.larg // 3, self.ligne * self.larg + self.larg // 3))

    def update_voisins(self, grid):
        self.voisins = []
        if self.ligne < lignes - 1 and not grid[self.ligne + 1][self.col].dessin_grille():  # Bas
            self.voisins.append(grid[self.ligne + 1][self.col])

        if self.ligne > 0 and not grid[self.ligne - 1][self.col].dessin_grille():  # Haut
            self.voisins.append(grid[self.ligne - 1][self.col])

        if self.col < cols - 1 and not grid[self.ligne][self.col + 1].dessin_grille():  # Droite
            self.voisins.append(grid[self.ligne][self.col + 1])

        if self.col > 0 and not grid[self.ligne][self.col - 1].dessin_grille():  # Gauche
            self.voisins.append(grid[self.ligne][self.col - 1])


# Reconstruire le chemin une fois trouvé
def chemin_reconst(viens_de, moment, draw):
    while moment in viens_de:
        moment = viens_de[moment]
        moment.chemin()
        draw()

# L'algorithme de Dijkstra
def dijkstra(draw, grid, point_debut, point_fin):
    c = 0
    ouverture = PriorityQueue()
    ouverture.put((0, c, point_debut))
    viens_de = {}
    g_score = {spot: float("inf") for ligne in grid for spot in ligne}
    g_score[point_debut] = 0

    ouverture_hash = {point_debut}

    while not ouverture.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        moment = ouverture.get()[2]
        ouverture_hash.remove(moment)

        if moment == point_fin:
            chemin_reconst(viens_de, point_fin, draw)
            point_fin.arriver()
            return True

        for v in moment.voisins:
            temp_g_score = g_score[moment] + 1

            if temp_g_score < g_score[v]:
                viens_de[v] = moment
                g_score[v] = temp_g_score
                if v not in ouverture_hash:
                    c += 1
                    ouverture.put((g_score[v], c, v))
                    ouverture_hash.add(v)
                    v.ouverture_voisins()  

        draw()

        # Ralentir
        pygame.time.delay(50)  

        if moment != point_debut:
            moment.fermer()

    return False

# Créer la grille
def make_grid():
    grid = []
    for ligne in range(lignes):
        grid.append([])
        for col in range(cols):
            spot = Spot(ligne, col, cell_size)
            grid[ligne].append(spot)

    return grid

# Dessiner la grille 
def dessin_lignes(e):
    for i in range(lignes):
        pygame.draw.line(e, NOIR, (0, i * cell_size), (ecran_taille, i * cell_size))  
        for j in range(cols):
            pygame.draw.line(e, NOIR, (j * cell_size, 0), (j * cell_size, ecran_taille))  


def draw_grid(e, grid):
    e.fill(BLANC)

    for ligne in grid:
        for spot in ligne:
            spot.draw(e)

    dessin_lignes(e)  
    pygame.display.update()


def main():
    grid = make_grid()

    point_debut = grid[start[0]][start[1]]
    point_fin = grid[end[0]][end[1]]
    point_debut.debut()
    point_fin.arriver()

    run = True
    while run:
        draw_grid(ecran, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  
                    for ligne in grid:
                        for spot in ligne:
                            spot.update_voisins(grid)

                    dijkstra(lambda: draw_grid(ecran, grid), grid, point_debut, point_fin)

    pygame.quit()

main()
