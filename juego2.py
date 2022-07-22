#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 19:47:43 2020

@author: sk
"""
import pygame
import numpy as np
import time
from numpy.random import choice, random

import pygame, sys
from pygame.locals import *

pygame.init()

width, height = 1000, 1000
screen=pygame.display.set_mode((height,width))

bg = 25, 25, 25 #color


nxC, nyC = 50, 50

dimCW = width / nxC
dimCH = height / nyC

gameState = np.zeros((nxC,nyC*5))


"""
for i in range(nxC):
    gameState[i,i] = 1
    gameState[i,-i] = 1
    

for i in range(10000):
    gameState[int(random()*nxC),int(random()*nyC)]=1
"""
for i in range(6):
    gameState[22+i,nyC-1]=1/2 
for i in range(6-2):
    gameState[23+i,nyC-2]=1/2 
for i in range(6-2-2):
    gameState[24+i,nyC-3]=1/2 

Obs = 200
for k in range(Obs):
    n = int(random()*nyC-1)
    if n<nyC-10: 
    #if True:
        for j in range(int(random()*40)):
            if k%2==0: 
                if n<nyC:gameState[j,n+1]=1/3
                gameState[j,n]=1/3
                gameState[j,n-1]=1/3
            else: 
                if n<nyC-1:gameState[nxC-j-1,n+1]=1/3
                gameState[nxC-j-1,n]=1/3
                gameState[nxC-j-1,n-1]=1/3


while True:
    
    newGameState = np.copy(gameState)
    
    screen.fill(bg)
    time.sleep(0.0005)
    
    events = pygame.event.get()
    #events = pygame.key.get_pressed()
    
    for event in events:
         if event.type == QUIT:
             print('quitting')
             pygame.quit()
             sys.exit()
         else:
             if event.type == KEYDOWN:
                 if event.key == K_ESCAPE:
                     print ("ESCAPE")
                     pygame.quit()
                     sys.exit()
                 if event.key == K_LEFT:
                     print ("LEFT")
                     for x in range(nxC):
                         for y in range(nyC):
                             if newGameState[(x+1)%nxC,y]==1/2: newGameState[x,y]=newGameState[(x+1)%nxC,y]
                             elif  newGameState[x,y]==1/2: newGameState[x,y]=0
                 if event.key == K_RIGHT:
                     print ("RIGHT")
                     for x in range(nxC):
                         for y in range(nyC):
                             if newGameState[(nxC-(x+1))%nxC,y]==1/2: newGameState[(nxC-x)%nxC,y]=newGameState[(nxC-(x+1))%nxC,y]
                             elif  newGameState[(nxC-x)%nxC,y]==1/2: newGameState[(nxC-x)%nxC,y]=0
                 if event.key == K_UP:
                     print("up")
                     for x in range(nxC):
                         for y in range(nyC):
                             if newGameState[x,(y+1)%nyC]==1/2: newGameState[x,y]=newGameState[x,(y+1)%nyC]
                             elif  newGameState[x,y]==1/2: newGameState[x,y]=0
                 if event.key == K_DOWN:
                     print ("DOWN")
                     for x in range(nxC):
                         for y in range(nyC):
                             if newGameState[x,(nyC-(y+1))%nyC]==1/2: newGameState[x,(nyC-y)%nyC]=newGameState[x,(nyC-(y+1))%nyC]
                             elif  newGameState[x,(nyC-y)%nyC]==1/2: newGameState[x,(nyC-y)%nyC]=0
                 
                 else:
                    print (event.key)
             if event.type == KEYUP:
                 print('KEYUP')
             if event.type == pygame.MOUSEBUTTONDOWN:
                 print('got MOUSEBUTTONDOWN')
    
    
    for x in range(0,nxC):
        for y in range(0, nyC):
            """
            n_vecinos = gameState[(x-1) %nxC, (y-1) %nyC]+\
                        gameState[(x-1) %nxC, (y) %nyC]+\
                        gameState[(x-1) %nxC, (y+1) %nyC]+\
                        gameState[(x) %nxC, (y-1) %nyC]+\
                        gameState[(x) %nxC, (y+1) %nyC]+\
                        gameState[(x+1) %nxC, (y-1) %nyC]+\
                        gameState[(x+1) %nxC, y %nyC]+\
                        gameState[(x+1) %nxC, (y+1) %nyC] 
                        
            if gameState[x,y] == 0 and n_vecinos == 3:
                newGameState[x,y] = 1
            
            elif gameState[x,y] == 1 and (n_vecinos < 2 or n_vecinos > 3):
                newGameState[x,y] = 0 
            """
            poly= [((x)*dimCW , y*dimCH ),
                   ((x+1)*dimCW , y*dimCH ),
                   ((x+1)*dimCW , (y+1)*dimCH ),
                   ((x)*dimCW , (y+1)*dimCH) ]
           
           
            # dibujar 
            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            elif newGameState[x,y] == 1 :
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
            elif newGameState[x,y] == 1/2:
                pygame.draw.polygon(screen, (122, 255, 0), poly, 0)
            else:
                pygame.draw.polygon(screen, (255, 0, 0), poly, 0)
    #actualiza
    pygame.display.flip()
    
    """
    for x in range(nxC):
        for y in range(nyC):
           newGameState[x,y]=newGameState[x,y+1]
           """
    
    gameState = np.copy(newGameState)
    