import pygame, model, random, time

pygame.key.set_repeat(50)

timer_grafika = pygame.event.custom_type()
pygame.time.set_timer(timer_grafika, 50)

type_spawn_monetki = pygame.event.custom_type()
pygame.time.set_timer(type_spawn_monetki, 1500)

type_ilona_maska = pygame.event.custom_type()
pygame.time.set_timer(type_ilona_maska, 50)


def allsobitiya():
    global random_append
    s = pygame.event.get()
    for a in s:
        if a.type == type_spawn_monetki:
            model.timer_spawna_monetki()

        #TODO: сейчас тут проверяется - не соприкоснулся ли левый верхний угол с монеткой, а нужно проверять не соприкоснулись внутренности илона маска с монеткой
        if model.rect_monetki.collidepoint(model.rect_ilona_maska.x,model.rect_ilona_maska.y):
            print(1)

        if a.type == pygame.MOUSEBUTTONDOWN and model.rect_monetki.collidepoint(a.pos[0], a.pos[1]):
            model.bank += 1
            pygame.time.set_timer(type_spawn_monetki, 1500)
            model.timer_spawna_monetki()

        if a.type == pygame.QUIT:
            exit()

        if a.type == timer_grafika:
            model.grafik()

        if a.type == type_ilona_maska:
            model.speed_ilon_mask()

