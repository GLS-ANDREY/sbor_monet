import time, view_game, controller_game, controller_nachalo, view_nachalo, view_pauza, controller_pauza, model

import model_nevazhno

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

    model.fps()
