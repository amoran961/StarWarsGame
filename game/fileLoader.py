#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

def loadImages():
    images = {}
    images["explosion01"] = pygame.image.load("explosion01.png").convert_alpha()
    images["explosion02"] = pygame.image.load("explosion02.png").convert_alpha()
    images["explosion03"] = pygame.image.load("explosion03.png").convert_alpha()
    images["explosion04"] = pygame.image.load("explosion04.png").convert_alpha()
    images["explosion05"] = pygame.image.load("explosion05.png").convert_alpha()
    images["explosion06"] = pygame.image.load("explosion06.png").convert_alpha()
    images["explosion07"] = pygame.image.load("explosion07.png").convert_alpha()
    images["explosion08"] = pygame.image.load("explosion08.png").convert_alpha()
    images["explosion09"] = pygame.image.load("explosion09.png").convert_alpha()
    images["explosion10"] = pygame.image.load("explosion10.png").convert_alpha()
    images["explosion11"] = pygame.image.load("explosion11.png").convert_alpha()
    images["explosion12"] = pygame.image.load("explosion12.png").convert_alpha()
    images["explosion13"] = pygame.image.load("explosion13.png").convert_alpha()
    images["explosion14"] = pygame.image.load("explosion14.png").convert_alpha()
    images["explosion15"] = pygame.image.load("explosion15.png").convert_alpha()
    if(c.BANDO=="Rebelde"):
        images["enemy1"] = pygame.image.load("enemy_imperial1.png").convert_alpha()
        images["enemy2"] = pygame.image.load("enemy_imperial2.png").convert_alpha()
        images["enemy3"] = pygame.image.load("enemy_imperial3.png").convert_alpha()
        images["cruiser"] = pygame.image.load("cruiser_imperial.png").convert_alpha()
    elif(c.BANDO=="Imperio"):
        images["enemy1"] = pygame.image.load("enemy_rebelde1.png").convert_alpha()
        images["enemy2"] = pygame.image.load("enemy_rebelde2.png").convert_alpha()
        images["enemy3"] = pygame.image.load("enemy_rebelde3.png").convert_alpha()
        images["cruiser"] = pygame.image.load("cruiser_rebelde.png").convert_alpha()
    images["ocean"] = pygame.image.load("ocean_texture.png").convert()
    images["missile"] = pygame.image.load("missile.png").convert_alpha()
    images["projectile"] = pygame.image.load("projectile.png").convert()
    images["projectile"].set_colorkey((0,0,0))
    images["gameOver"] = pygame.image.load("game_over.png").convert()
    images["gameOver"].set_colorkey((0,0,0))
    return images

def loadSounds():
    sounds = {}
    sounds["explosion"] = pygame.mixer.Sound("explosion.ogg")
    sounds["plane"] = pygame.mixer.Sound("plane.ogg")
    return sounds
