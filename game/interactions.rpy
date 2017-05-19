# coding=utf-8
# interactions location

label lb_girl_sex:
    if game.girl.jailed:
        $ place = 'prison'
        show place as bg
    nvl clear
    menu:
        'Defile and impregnate' if game.girls_list.is_mating_possible:
            call lb_girl_impregnate
            
        'Magical growth' if not game.girls_list.is_mating_possible and game.girl.virgin and game.girl.is_gigant and game.dragon.can_grow:
            $ game.dragon.drain_mana()
            game.dragon 'Spell of temporary growth!'
            call lb_girl_impregnate
            
        'Mock and rob' if game.girl.treasure:
            $ description = game.girls_list.rob_girl()
            game.girl.third "[description]"
            
        'Put back in jail' if game.girl.jailed:
            $ description = game.girls_list.jail_girl()
            game.girl.third "[description]"
            return
            
        'Take back to the lair' if not game.girl.jailed:
            call lb_girl_imprison
            return
            
        'Let her go':
            $ description = game.girls_list.free_girl()
            game.girl.third "[description]"
            return
            
        'Eat her lustfully' if game.dragon.hunger > 0:
            call lb_girl_eat
            return
            
    jump lb_girl_sex
    
label lb_girl_impregnate:
    # Alex: Added sex images:
    $ description = game.girls_list.impregnate()
    stop music fadeout 1.0            
    game.girl "[description]"
    show expression sex_imgs(game.girl.sex_expression) as xxx
    play sound get_random_file("sound/sex")
    pause (500.0)
    stop sound fadeout 1.0
    hide xxx
    return

label lb_girl_imprison:
    $ description = game.girls_list.steal_girl()
    game.girl.third "[description]"
    $ place = game.lair.type_name
    show place
    nvl clear
    $ description = game.girls_list.jail_girl()
    game.girl.third "[description]"
    return

label lb_girl_eat:
    $ description =  game.girls_list.eat_girl()
    game.girl "[description]"
    play sound "sound/eat.ogg"
    show expression sex_imgs.get_eat_image() as eat_image
    pause (500.0)
    hide eat_image     
    return

label lb_lair_sex:
    if game.girl.virgin:
        game.girl "I want to go home. Please..."
    if game.girl.pregnant > 0:
        game.girl "What did you do to me... I can feel something growing in me..."
    if not game.girl.virgin:
        if game.girl.pregnant == 0:
            game.girl "I laid the eggs. Just let me go. Please..."
    python:
        if game.girl.type == 'ice' or game.girl.type == 'fire' or game.girl.type == 'ogre' or game.girl.type == 'titan' or game.girl.type == 'siren':
            renpy.jump('lb_gigant_sex')
    jump lb_nature_sex

label lb_gigant_sex:
    jump lb_nature_sex

label lb_water_sex:
    jump lb_nature_sex
    
label lb_nature_sex:
    jump lb_girl_sex

label lb_knight_new:
    show expression 'img/bg/special/oath.jpg' as bg
    'Knight vowed to slay the dragon.'
    return

    