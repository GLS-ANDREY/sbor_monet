import time,model, view_game, controller_game, controller_nachalo, view_nachalo, view_pauza, controller_pauza, \
    model_nevazhno, controller_stat_start,view_stat_start

while True:
    if model.ekran == 1:
        view_nachalo.risovanie_nachalo()
        controller_nachalo.allsobitiya_nachalo()
    if model.ekran == 0:
        controller_game.allsobitiya()
        view_game.risovanie_game()
    if model.ekran == 2:
        controller_pauza.allsobitiya_pauza()
        view_pauza.risovanie_pauza()
    if model.ekran == 3:
        controller_stat_start.allsobitiya_stat_start()
        view_stat_start.risovanie_stat_start()
    model.fps()