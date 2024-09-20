import pygame
import math

# Initialisation de Pygame
pygame.init()

# Taille de la fenêtre
window_size = 500
rows, cols = 5, 5  # Taille de la grille (5x5)
cell_size = window_size // rows  # Taille d'une cellule

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Fenêtre
screen = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Grille de distance de Manhattan")

# Police pour afficher le texte
font = pygame.font.SysFont(None, 40)

# Point de départ et d'arrivée
start = (1, 1)
end = (3, 3)

# Fonction pour dessiner la grille et calculer la distance de Manhattan
def draw_grid():
    screen.fill(WHITE)
    
    for row in range(rows):
        for col in range(cols):
            # Calcul de la distance de Manhattan
            g_n = abs(row - start[0]) + abs(col - start[1])
            
            # Dessiner la cellule
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK, rect, 1)
            
            # Colorer le point de départ et d'arrivée
            if (row, col) == start:
                pygame.draw.rect(screen, GREEN, rect)
            elif (row, col) == end:
                pygame.draw.rect(screen, BLUE, rect)
            else:
                # Afficher le coût g(n) au centre des cellules
                text = font.render(str(g_n), True, BLACK)
                screen.blit(text, (col * cell_size + cell_size // 3, row * cell_size + cell_size // 3))

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Dessiner la grille et calculer les distances
    draw_grid()
    
    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
