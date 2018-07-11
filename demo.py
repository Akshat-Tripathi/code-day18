# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 13:25:32 2018

@author: akshat
"""

import pygame
from time import sleep
from initialisation import background

win = pygame.display.set_mode((1000,1000))
b = background(10000, 10000)
b.load(1000, 10, win)
crashed = False
x, y = 0, 0
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_UP]:
        y += 1
    if keys[pygame.K_DOWN]:
        y-=1
    if keys[pygame.K_LEFT]:
        x += 1
    if keys[pygame.K_RIGHT]:
        x-=1
        

    win.fill((0, 0 ,0))
    b.move(x, y, win)
    pygame.display.update()
    sleep(0.1)

