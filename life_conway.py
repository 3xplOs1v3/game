#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import numpy as np
import time
from numpy.random import choice, random

pygame.init()

width, height = 1000, 1000
screen=pygame.display.set_mode((height,width))

bg = 25, 25, 25 #color


nxC, nyC = 100, 100

dimCW = width / nxC
dimCH = height / nyC

gameState = np.zeros((nxC,nyC))


# condiciones iniciales
for i in range(nxC):
    gameState[i,i] = 1
    gameState[i,-i] = 1
    
"""
for i in range(10000):
    gameState[int(random()*nxC),int(random()*nyC)]=1
"""


while True:
    
    newGameState = np.copy(gameState)
    
    screen.fill(bg)
    time.sleep(0.1)
    
    for x in range(0,nxC):
        for y in range(0, nyC):
            
            n_vecinos = gameState[(x-1) %nxC, (y-1) %nyC]+\
                        gameState[(x-1) %nxC, (y) %nyC]+\
                        gameState[(x-1) %nxC, (y+1) %nyC]+\
                        gameState[(x) %nxC, (y-1) %nyC]+\
                        gameState[(x) %nxC, (y+1) %nyC]+\
                        gameState[(x+1) %nxC, (y-1) %nyC]+\
                        gameState[(x+1) %nxC, y %nyC]+\
                        gameState[(x+1) %nxC, (y+1) %nyC] 
                        
            # vive 
            if gameState[x,y] == 0 and n_vecinos == 3:
                newGameState[x,y] = 1
            
            # muere por falta/exceso recursos
            elif gameState[x,y] == 1 and (n_vecinos < 2 or n_vecinos > 3):
                newGameState[x,y] = 0 
            
            poly= [((x)*dimCW , y*dimCH ),
                   ((x+1)*dimCW , y*dimCH ),
                   ((x+1)*dimCW , (y+1)*dimCH ),
                   ((x)*dimCW , (y+1)*dimCH) ]
           
           
            # dibujar 
            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
    
    #actualiza
    gameState = np.copy(newGameState)
    pygame.display.flip()
