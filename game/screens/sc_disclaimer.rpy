# coding=utf-8
screen sc_disclaimer:
    frame:
        text "WARNING!!!":           # Отдельно так как нужно спозиционировать по центру.
            color "#f00"            # Текст красного цвета
            align(0.5, 0.15)      # Положение на экране
            size 40
        text("   This game contents multiple scenes of extreme violence and strong sexual content, and thus cannot be recommended to anyone. PG-99.\n"
            "   By clicking “proceed” you confirm that you are an adult and choose to play at your own risk. This game is NOT meant to be commercially distributed. All graphical, audio and text elements used in the game are either freely available on internet or created by authors of the game, and used for the sake of parody.\n"
            "   Program code of the game, created by our team, is licensed under the BSD license (see LICENCE.txt for details)"):
            align(0.5, 0.4)
            color "#f00"            # Текст красного цвета
    
        textbutton "Proceed":       
            align(0.4, 0.8)        # Положение на экране
            action Return(True)     # Возвращаем True, что мы приняли дисклеймер
            
        textbutton "Stop":
            action Quit(False)      # Сразу выходим
            align(0.6, 0.8)        # Положение на экране
    
        background "#000"