import model, pygame, view_game
import model_nevazhno

pygame.init()
font2 = pygame.font.SysFont("comicsansms", 27, True)
display = pygame.display.set_mode([1500, 1000])

spacex = pygame.image.load("spacex.jpg")

spacex_transform = pygame.transform.scale(spacex, [1500, 1000])


def risovanie_stat_start():
    display.fill([0, 0, 0])
    # ��������
    display.blit(spacex_transform, [0, 0])
    # �����
    # view_game.risovanie_nadpisi("��� ���� ����� �����",0)
    # view_game.risovanie_nadpisi("������� �������:" + str(model_nevazhno.ris_lvl), 0)
    # view_game.risovanie_nadpisi("����� ������ �����:" + str(model.mirovoy_bank), 30)
    # view_game.risovanie_nadpisi("����� ������� �����:" + str(model.bank), 60)
    # view_game.risovanie_nadpisi("����� ������ ����� �� ����:" + str(model_nevazhno.clicks), 90)
    # view_game.risovanie_nadpisi("����� ���� ���� �������� ��������:" + str(model.pixel), 120)
    pygame.display.flip()
