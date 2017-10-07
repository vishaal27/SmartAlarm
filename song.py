
import pygame
pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()
file='' #TODO: retrieve any online file.
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)
