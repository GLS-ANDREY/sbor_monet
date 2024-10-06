import random,time,pygame,settings
clock = pygame.time.Clock()
#TODO: Сделать так что бы центр ректа становился четко по центру экрана
rect_display = pygame.Rect(0,0,settings.width_display,settings.height_display)
rect_start = pygame.Rect(rect_display.centerx, rect_display.centery, 300, 300)