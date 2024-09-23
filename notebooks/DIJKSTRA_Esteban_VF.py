import pygame as pg, heapq,random, ctypes;from tkinter import messagebox
pg.init()
N_CELLULES = 20
TAILLE_CELLULE = (pg.display.Info().current_h - 50) // (N_CELLULES + 1)
ecran = pg.display.set_mode((pg.display.Info().current_h + 150, pg.display.Info().current_h - 50))
ctypes.windll.user32.SetForegroundWindow(pg.display.get_wm_info()['window'])
bouton_reset_rect = pg.Rect((N_CELLULES+1) * TAILLE_CELLULE + 10, TAILLE_CELLULE * 1, *(180, TAILLE_CELLULE))
bouton_run_rect = pg.Rect((N_CELLULES+1) * TAILLE_CELLULE + 10, TAILLE_CELLULE * 3, *(180, TAILLE_CELLULE))
obstacles_a_definir = {(0, ligne) for ligne in range(1, N_CELLULES + 1)} | {(x, 0) for x in range(1, N_CELLULES + 1)}
messagebox.showinfo("Instructions", "Bienvenue dans ma simulation de l'algorithme de Dijkstra avec des poids aléatoires !")
def reinitialiser():
    global depart, arrivee, obstacles_definis, peut_definir_obstacle, chemin, lecture_en_cours, matrice_distance, noeuds_visites, gen_dijkstra, poids, precedents
    depart = arrivee = matrice_distance = gen_dijkstra = precedents = None
    peut_definir_obstacle = lecture_en_cours = False
    chemin = []
    noeuds_visites, obstacles_definis = set(), set()
    messagebox.showinfo("Instructions", "Cliquez sur une cellule pour définir le point de départ.")
    poids = {(x, y): random.randint(1, 10) for x in range(1, N_CELLULES + 1) for y in range(1, N_CELLULES + 1)}
reinitialiser()
continuer = True
while continuer:
    for event in pg.event.get():
        if event.type == pg.QUIT:continuer = False
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            x, y = x // TAILLE_CELLULE, y // TAILLE_CELLULE
            if bouton_reset_rect.collidepoint(event.pos):reinitialiser()
            elif bouton_run_rect.collidepoint(event.pos):
                if depart and arrivee:
                    matrice_distance = [[float('inf')] * (N_CELLULES + 1) for _ in range(N_CELLULES + 1)]
                    matrice_distance[depart[1]][depart[0]] = 0
                    precedents = [[None] * (N_CELLULES + 1) for _ in range(N_CELLULES + 1)]
                    priorite = [(0, (depart[1], depart[0]))]
                    noeuds_visites = set()
                    gen_dijkstra =lecture_en_cours= True
            elif 1 <= x <= N_CELLULES and 1 <= y <= N_CELLULES and not lecture_en_cours:
                if not depart:
                    depart = (x, y)
                    messagebox.showinfo("Instructions", "Cliquez sur une autre cellule pour définir le point d'arrivée.")
                elif not arrivee:
                    arrivee = (x, y)
                    messagebox.showinfo("Instructions", "Définissez des obstacles en cliquant ou en glissant.")
                    peut_definir_obstacle = True
                elif (x, y) not in obstacles_definis | {depart, arrivee}:
                    obstacles_definis.add((x, y))
                    poids.pop((x, y), None)
        elif event.type == pg.MOUSEMOTION:
            if pg.mouse.get_pressed()[0] and peut_definir_obstacle and not lecture_en_cours:
                x, y = event.pos
                x, y = x // TAILLE_CELLULE, y // TAILLE_CELLULE
                if 1 <= x <= N_CELLULES and 1 <= y <= N_CELLULES:
                    if (x, y) not in obstacles_definis | obstacles_a_definir | {depart, arrivee}:
                        obstacles_definis.add((x, y))
                        poids.pop((x, y), None)
    if lecture_en_cours and gen_dijkstra:
        if priorite:
            distance_actuelle, (ligne_actuelle, colonne_actuelle) = heapq.heappop(priorite)
            noeuds_visites.add((colonne_actuelle, ligne_actuelle))
            if (ligne_actuelle, colonne_actuelle) == (arrivee[1], arrivee[0]):
                if matrice_distance[arrivee[1]][arrivee[0]] != float('inf'):
                    chemin = []
                    courant = (arrivee[1], arrivee[0])
                    while courant != (depart[1], depart[0]):
                        chemin.append((courant[1], courant[0]))
                        courant = precedents[courant[0]][courant[1]]
                    chemin.append((depart[0], depart[1]))
                    chemin.reverse()
                else: messagebox.showinfo("Instructions", "Il n'y a pas de chemin possible")
                lecture_en_cours = False
            else:
                for delta_l, delta_c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    l_vois, c_vois = ligne_actuelle + delta_l, colonne_actuelle + delta_c
                    if 1 <= l_vois <= N_CELLULES and 1 <= c_vois <= N_CELLULES:
                        if (c_vois, l_vois) in (obstacles_definis | obstacles_a_definir | noeuds_visites):continue
                        nouvelle_distance = distance_actuelle + poids.get((c_vois, l_vois), 1)
                        if nouvelle_distance < matrice_distance[l_vois][c_vois]:
                            matrice_distance[l_vois][c_vois] = nouvelle_distance
                            precedents[l_vois][c_vois] = (ligne_actuelle, colonne_actuelle)
                            heapq.heappush(priorite, (nouvelle_distance, (l_vois, c_vois)))
        else:
            if not chemin:messagebox.showinfo("Instructions", "Il n'y a pas de chemin possible")
            lecture_en_cours = False
    ecran.fill((255, 255, 255))
    pg.draw.rect(ecran, (169, 169, 169), (TAILLE_CELLULE, TAILLE_CELLULE, N_CELLULES * TAILLE_CELLULE, N_CELLULES * TAILLE_CELLULE))
    for i in range(N_CELLULES + 1):pg.draw.line(ecran, (0, 0, 0), (TAILLE_CELLULE + i * TAILLE_CELLULE, TAILLE_CELLULE), (TAILLE_CELLULE + i * TAILLE_CELLULE, TAILLE_CELLULE + N_CELLULES * TAILLE_CELLULE))
    for i in range(N_CELLULES + 1): pg.draw.line(ecran, (0, 0, 0), (TAILLE_CELLULE, TAILLE_CELLULE + i * TAILLE_CELLULE), (TAILLE_CELLULE + N_CELLULES * TAILLE_CELLULE, TAILLE_CELLULE + i * TAILLE_CELLULE))
    pg.draw.line(ecran, (0, 0, 0), (TAILLE_CELLULE + N_CELLULES * TAILLE_CELLULE, 0), (TAILLE_CELLULE + N_CELLULES * TAILLE_CELLULE, TAILLE_CELLULE + N_CELLULES * TAILLE_CELLULE))
    font = pg.font.Font(None, TAILLE_CELLULE)
    for i in range(1, N_CELLULES + 1):
        texte = font.render(str(i), True, (0, 0, 0))
        ecran.blit(texte, (TAILLE_CELLULE // 2 - texte.get_width() // 2, TAILLE_CELLULE + (i - 1) * TAILLE_CELLULE + (TAILLE_CELLULE // 2) - texte.get_height() // 2))
        lettre = chr(64 + i)
        texte = font.render(lettre, True, (0, 0, 0))
        ecran.blit(texte, (TAILLE_CELLULE + (i - 1) * TAILLE_CELLULE + (TAILLE_CELLULE // 2) - texte.get_width() // 2, TAILLE_CELLULE // 2 - texte.get_height() // 2))
    for obstacle in obstacles_definis:pg.draw.rect(ecran, (128, 0, 128), pg.Rect(TAILLE_CELLULE + (obstacle[0] - 1) * TAILLE_CELLULE, TAILLE_CELLULE + (obstacle[1] - 1) * TAILLE_CELLULE, TAILLE_CELLULE, TAILLE_CELLULE))
    if depart:pg.draw.rect(ecran, (0, 255, 0), pg.Rect(TAILLE_CELLULE + (depart[0] - 1) * TAILLE_CELLULE, TAILLE_CELLULE + (depart[1] - 1) * TAILLE_CELLULE, TAILLE_CELLULE, TAILLE_CELLULE))
    if arrivee: pg.draw.rect(ecran, (255, 0, 0), pg.Rect(TAILLE_CELLULE + (arrivee[0] - 1) * TAILLE_CELLULE, TAILLE_CELLULE + (arrivee[1] - 1) * TAILLE_CELLULE, TAILLE_CELLULE, TAILLE_CELLULE))
    for x, y in noeuds_visites:
        if (x, y) != depart:pg.draw.circle(ecran, (255, 105, 180), (TAILLE_CELLULE + (x - 1 + 0.5) * TAILLE_CELLULE,TAILLE_CELLULE + (y - 1 + 0.5) * TAILLE_CELLULE), TAILLE_CELLULE // 6)
    if chemin: 
        pg.draw.lines(ecran, (255, 165, 0), False, [(TAILLE_CELLULE + (x - 1 + 0.5) * TAILLE_CELLULE,TAILLE_CELLULE + (y - 1 + 0.5) * TAILLE_CELLULE)for x, y in chemin], 5)
        font_distance = pg.font.Font(None, 36)
        distance_totale = matrice_distance[arrivee[1]][arrivee[0]] if matrice_distance else "N/A"
        texte_distance = font_distance.render(f"Distance: {distance_totale}", True, (255, 165, 0))
        ecran.blit(texte_distance, texte_distance.get_rect(center=((N_CELLULES+1) * TAILLE_CELLULE + 100, 5 * TAILLE_CELLULE)))
    font_poids = pg.font.Font(None, int(TAILLE_CELLULE * 0.4))
    for (x, y), poids_cellule in poids.items():
        if (x, y) not in obstacles_definis | obstacles_a_definir | {depart}:
            rect_poids = pg.Rect(TAILLE_CELLULE + (x - 1) * TAILLE_CELLULE, TAILLE_CELLULE + (y - 1) * TAILLE_CELLULE, TAILLE_CELLULE, TAILLE_CELLULE)
            texte_poids = font_poids.render(str(poids_cellule), True, (0, 0, 0))
            ecran.blit(texte_poids, texte_poids.get_rect(center=rect_poids.center))
    pg.draw.rect(ecran, (200, 200, 200), bouton_reset_rect)
    pg.draw.rect(ecran, (0, 0, 255), bouton_run_rect)
    font_bouton = pg.font.Font(None, TAILLE_CELLULE)
    texte_reset = font_bouton.render("Réinitialiser", True, (0, 0, 0))
    texte_run = font_bouton.render("Lancer", True, (255, 255, 255) if not lecture_en_cours else (200, 200, 200))
    ecran.blit(texte_reset, texte_reset.get_rect(center=bouton_reset_rect.center))
    ecran.blit(texte_run, texte_run.get_rect(center=bouton_run_rect.center))
    pg.display.flip()
pg.quit()