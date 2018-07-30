import pygame
from pygame.locals import *
import numpy
import random


def drawGrid(display, width, height, cellSize):
    for x in range(0, width, cellSize):
        pygame.draw.line(display, (0, 0, 0), (x, 0), (x, height))
    for y in range(0, height, cellSize):
        pygame.draw.line(display, (0, 0, 0), (0, y), (width, y))


def populate(width, height, cellSize):
    grid = numpy.zeros((width, height), dtype=numpy.dtype('b'))
    for x in range(width // cellSize):
        for y in range(height // cellSize):
            grid[x, y] = random.randint(0, 1)
    return grid


def displayCells(display, width, height, cellSize, grid, color=(255, 155, 0)):
    for x in range(width // cellSize):
        for y in range(height // cellSize):
            if grid[x, y] == 1:
                pygame.draw.rect(display, color, (x * cellSize, y * cellSize, cellSize, cellSize))
            else:
                pygame.draw.rect(display, (255, 255, 255), (x * cellSize, y * cellSize, cellSize, cellSize))


def initWindow(width=640, height=480, cellSize=10):
    if width % cellSize != 0:
        print('WARNING: width MUST be a multiple of cell size !')
        exit(1)
    if height % cellSize != 0:
        print('WARNING: height MUST be a multiple of cell size !')
        exit(2)
    pygame.init()
    display = pygame.display.set_mode((width, height))
    display.fill((255, 255, 255))
    pygame.display.set_caption('Game of life')
    grid = populate(width, height, cellSize)
    displayCells(display, width, height, cellSize, grid)
    drawGrid(display, width, height, cellSize)

    return grid


def main():
    initWindow()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit(0)
        pygame.display.update()


if __name__ == '__main__':
    main()
