import time,view_game,controller_game,controller_nachalo,view_nachalo,model

while True:
    if model.ekran == 0:
        controller_game.allsobitiya()
        view_game.risovanie_game()
    if model.ekran == 1:
        view_nachalo.risovanie_nachalo()
        controller_nachalo.allsobitiya_nachalo()
    model.fps()