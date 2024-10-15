import random, time, pygame, settings,os,model

clock = pygame.time.Clock()

clicks = 0
ris_lvl = 1
def rekord():
    rekord_zapis = open("rekord_file.txt", "w+")
    print("Уровень последней игры:" + str(ris_lvl), file=rekord_zapis,end="")
    rekord_zapis.close()

read_rekord = open("rekord_file.txt", "r")
read_rekord2 = read_rekord.read()

pygame.init()
font = pygame.font.Font("start_font.TTF", 100)
font2 = pygame.font.SysFont("comicsansms", 27, True)


save_urovenb = font2.render(str(read_rekord2), True, [255, 255, 255])
start = font.render("START", True, [255, 255, 255])
continue_img = font.render("CONTINUE", True, [255, 255, 255])

size_start = start.get_size()
size_continue = continue_img.get_size()
size_urovenb = save_urovenb.get_size()


rect_display = pygame.Rect(0, 0, settings.width_display, settings.height_display)
rect_start = pygame.Rect(0, 0, size_start[0], size_start[1])
rect_continue = pygame.Rect(0, 0, size_continue[0], size_continue[1])
rect_urovenb = pygame.Rect(0, 0, size_urovenb[0], size_urovenb[1])


rect_start.centerx = rect_display.centerx
rect_start.centery = rect_display.centery + 250

rect_continue.centerx = rect_display.centerx
rect_continue.centery = rect_display.centery + 250

