import pygame,model

def allsobitiya_nachalo():
    global random_append
    s = pygame.event.get()
    for a in s:
        if a.type == pygame.QUIT:
            exit()