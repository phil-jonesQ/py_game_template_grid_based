""" Version 1.00 - simple game template.. Grid Based Game

Phil Jones - Jan 2021

Version 1.01 - Draws Grid And Can Exist
Version 1.02 -

"""


import pygame
import sys
import os
import random
from random import randint


# Initialise Constants

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 600
ROWS = 32
DECK_LIMIT = 52

cell_sz = WINDOW_HEIGHT // ROWS
surface_sz = ROWS * cell_sz

pygame.font.init()  # you have to call this at the start,
thefont = pygame.font.SysFont('Courier New', 20)

images = {
                    'ace of clubs': 'AC.png',
                    'ace of diamonds': 'AD.png',

}

# Load Image set
# Store in a dictionary so we can map the image to name
card_images = {}
path = "assets/"
for name, file_name in images.items():
    image = pygame.transform.scale(pygame.image.load(path + os.sep + file_name), (70, 90))
    card_images[name] = image

# Track the game state by storing each cell's card and if it's been revealed (True|False)
cell_tracker = {}
compare_tracker = {}
matched_cells_tracker = []


def reset():
    """Reset Game state"""
    pass


def game_stats_display():
    attempts_string = "ATTEMPTS " + str(attempts)
    matches_string = "MATCHES " + str((len(matched_cells_tracker)))
    message_string = "SPACE TO RESTART.."

    textsurface1 = thefont.render(attempts_string, False, (0, 255, 0))
    textsurface2 = thefont.render(matches_string, False, (0, 255, 0))
    textsurface3 = thefont.render(message_string, False, (255, 0, 0))

    SCREEN.blit(textsurface1, (WINDOW_WIDTH - 150, WINDOW_HEIGHT - 100))
    SCREEN.blit(textsurface2, (WINDOW_WIDTH - 150, WINDOW_HEIGHT - 150))
    SCREEN.blit(textsurface3, (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 75))
    pygame.display.update()
    pygame.display.flip()


def draw_grid():
    SCREEN.fill(BLACK)
    for ROW in range(ROWS):
        for COL in range(ROWS):
            rect = pygame.Rect(COL*cell_sz, ROW*cell_sz,
                               cell_sz, cell_sz)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)


def update_grid():
    SCREEN.fill(BLACK)
    counter = 0
    for ROW in range(ROWS):
        for COL in range(ROWS):
            counter += 1
            pass

    pygame.display.update()
    pygame.display.flip()


def main():
    global SCREEN, CLOCK
    global TURNS
    global enabled
    global attempts
    TURNS = 2
    attempts = 0
    pygame.init()
    SCREEN = pygame.display.set_mode((surface_sz, surface_sz))
    CLOCK = pygame.time.Clock()
    reset()
    draw_grid()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset()
            if event.type == pygame.MOUSEBUTTONDOWN:
                enabled = True
                # Set the x, y positions of the mouse click
                x, y = event.pos
                # Translate x, y pos to grid coord
                clicked_col = (event.pos[0] // cell_sz) + 1
                clicked_row = (event.pos[1] // cell_sz) + 1
                # Translate col_row coord to a cell number
        game_stats_display()


main()
