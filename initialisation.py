# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 11:53:40 2018

@author: akshat
"""

import pygame, os, random
from time import sleep
pygame.init()
class background():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        print("loaded successfully")
    
    def load(self, star_count, planet_count, window):
        #load planets and stars
        planets = [pygame.transform.scale(pygame.image.load("planets/" + i), (200, 200)) for i in os.listdir("planets")] * planet_count
        stars = [pygame.transform.scale(pygame.image.load("stars/" + i), (10, 10)) for i in os.listdir("stars")] * star_count
        #make dict of initial locations
        star_locs = []
        planet_locs = []
        for i in range(len(stars)):
            temp = [random.randint(0, self.width), random.randint(0, self.height)]
            if temp not in star_locs:
                star_locs.append(temp)
            else:
                temp = [random.randint(0, self.width), random.randint(0, self.height)] #this is the cause of double stars
                star_locs.append(temp)
        
        for i in range(len(planets)):
            temp = [random.randint(0, self.width), random.randint(0, self.height)]
            if temp not in star_locs:
                planet_locs.append(temp)
            else:
                temp = [random.randint(0, self.width), random.randint(0, self.height)] #this is the cause of double planets
                planet_locs.append(temp)
        t1 = stars + planets
        t2 = star_locs + planet_locs
        self.background_locs = [tuple([t1[i], t2[i]]) for i in range(len(t1))]
        del t1, t2
        #display
        for i in self.background_locs:
            window.blit(i[0], i[1])
        print("display successful")
    
    def move(self, x, y, window):
        for i in self.background_locs:
            i[1][0] -= x #possible area for stupid scrolling
            i[1][1] -= y
            window.blit(i[0], i[1])
        print("moved successfully")
        
def to_vec(thrust, angle):
    

if __name__ == "__main__":
    win = pygame.display.set_mode((1000,1000))
    b = background(5000, 5000)
    b.load(100, 100, win)
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

