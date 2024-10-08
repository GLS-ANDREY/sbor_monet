import random, time, pygame, settings

clock = pygame.time.Clock()

pygame.init()
font = pygame.font.Font("start_font.TTF", 100)
# font = pygame.font.SysFont("Fixedsys", 100, True)

start = font.render("START", True, [255, 255, 255])
continue_img = font.render("CONTINUE", True, [255, 255, 255])

size_start = start.get_size()
size_continue = continue_img.get_size()

rect_display = pygame.Rect(0, 0, settings.width_display, settings.height_display)
rect_start = pygame.Rect(0, 0, size_start[0], size_start[1])
rect_continue = pygame.Rect(0, 0, size_continue[0], size_continue[1])

rect_start.centerx = rect_display.centerx
rect_start.centery = rect_display.centery + 250

rect_continue.centerx = rect_display.centerx
rect_continue.centery = rect_display.centery + 250

