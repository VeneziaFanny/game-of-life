# This Python script uses the Pygame library to implement Conway's Game of Life, a cellular automaton
# devised by the British mathematician John Horton Conway.

import pygame
import time
import random
import numpy as np
import os
import grid

os.environ["SDL_VIDEO_CENTERED"]='1'

#resolution
width, height = 1020,880
size = (width, height)

pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
# Définition de l'écran de jeu avec la taille spécifiée
screen = pygame.display.set_mode(size)

# Création d'une horloge pour contrôler le taux de rafraîchissement du jeu
clock = pygame.time.Clock()

# Définition du nombre d'images par seconde
fps = 30

# Définition des couleurs utilisées dans le jeu
black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0,14,71)
white = (255, 255, 255)

# Définition du facteur d'échelle et du décalage pour la grille
scaler = 15
offset = 1

# Création d'une instance de la classe Grid
Grid = grid.Grid(width,height, scaler, offset)

# Initialisation de la grille avec des valeurs aléatoires
Grid.random2d_array()

# Définition des variables de contrôle du jeu
pause = False
run = True
# Boucle principale du jeu
while run:
    # Contrôle du taux de rafraîchissement du jeu
    clock.tick(fps)
    
    # Remplissage de l'écran avec la couleur noire
    screen.fill(black)

    # Traitement des événements de jeu
    for event in pygame.event.get():
        # Si l'événement est QUIT, arrêtez le jeu
        if event.type == pygame.QUIT:
            run = False
        # Si une touche est relâchée
        if event.type == pygame.KEYUP:
            # Si la touche est ESCAPE, arrêtez le jeu
            if event.key == pygame.K_ESCAPE:
                run = False
            # Si la touche est SPACE, mettez le jeu en pause ou reprenez-le
            if event.key == pygame.K_SPACE:
                pause = not pause
    
    # Mise à jour de la grille en fonction des règles du jeu de la vie de Conway
    Grid.Conway(off_color=white, on_color=blue1, surface=screen, pause=pause)

    # Si le bouton gauche de la souris est enfoncé
    if pygame.mouse.get_pressed()[0]:
        # Obtenez la position de la souris
        mouseX, mouseY = pygame.mouse.get_pos()
        # Traitez l'événement de la souris
        Grid.HandleMouse(mouseX, mouseY)

    pygame.display.update()

pygame.quit()
