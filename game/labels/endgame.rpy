#Окончание игры

label lb_game_over:
    hide bg
    if freeplay:
        $ renpy.unlink_save("1-3")
    else:
        $ renpy.unlink_save("1-1")
    play music 'mus/outro.ogg'
    show expression 'img/scene/game_over.jpg' as bg with irisin
    show text "{size=+15}GAME OVER{/size}"
    pause
    hide expression 'img/scene/game_over.jpg' 
    with dissolve    
    stop music fadeout 1.0
    hide text
    with dissolve            
    $ renpy.full_restart()
    
label lb_you_win:
    $ data.achieve_target("conquer", "win")
    $ data.achieve_win(game.dragon)
    call lb_achievement_acquired from _call_lb_achievement_acquired
    hide all
    play music 'mus/outro.ogg'
    show black
    show text "{font=fonts/PFMonumentaPro-Regular.ttf}{size=+15}EPIC WIN{/size}{/font}" at truecenter with dissolve
    pause (5.0)
    hide text with dissolve
    show expression 'img/scene/ge0.jpg' at left
    with dissolve
    show text "      THIS PROJECT DEVELOPED BY: \n\n\n Asfdfdfd \n\n Anonimous №13 \n\n Denkun \n\n ImG \n\n Graylor \n\n Roldand \n\n OldHuntsman \n\n HikkeKun \n\n Titlish \n\n Vladimir Sudalov \n\n Xela00 \n\n\n and others..." at topright
    pause (15.0)
    hide text with dissolve
    hide expression 'img/scene/ge0.jpg' at left
    show expression 'img/scene/ge1.jpg' at right
    with dissolve
    show text "      ENGLISH TRANSLAION BY: \n\nHongstts \n\nSalking  \n\nOldHuntsman" at topleft
    with dissolve
    pause (8.0)
    hide expression 'img/scene/ge1.jpg'
    with dissolve    
    hide text
    with dissolve      
    show expression 'img/scene/ge2.jpg' at left
    with dissolve    
    show text '\n\n      This game is just an attempt \n to master this new engine. \n We have huge plans for the future, \n but to achieve them \n will not be easy. \n If you want to help, \n we can always use \n good programmers and designers. \n And, of course \n we do not refuse donations ;) \n Find us at \n\n  http://oldhuntergames.blogspot.com/. ' at topright    
    with dissolve
    pause
    hide expression 'img/scene/ge2.jpg' 
    with dissolve    
    stop music fadeout 1.0
    hide text
    with dissolve        
    $ persistent.allow_freeplay = True
    $ renpy.unlink_save("1-1")
    $ game.win()
    $ renpy.full_restart()
