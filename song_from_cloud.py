import pygame
import requests
pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()
location='d:/temp.mp3' 
url = "http://your_direct_url.xyz/epic_sax_guy.mp3"
file = open(location,"+wb") #create temp file with binary mode, d:/temp.mp3 in this case 
file.write(requests.get(url).content) #download and write it
file.close();  #done
pygame.mixer.init()
pygame.mixer.music.load(location)
pygame.mixer.music.play(-1)
