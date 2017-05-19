# coding=utf-8
#spellchecked, proofread

init python:
    from pythoncode.characters import Talker
    
label lb_location_ruin_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))    
    hide bg
    show expression 'img/bg/special/haunted.jpg' as bg

    if game.dragon.energy() == 0:
        '[game.dragon.name] needs to sleep!'
        return
        
    python:
        witch = Talker(game_ref=game)
        witch.avatar = "img/avahuman/witch.jpg"
        witch.name = "Witch"
        
    menu:
        'Visit the witch':
            show expression 'img/scene/witch.jpg' as bg
            if game.dragon.lust == 3: 
                call lb_witch_agree
            else:
                call lb_witch_refuse
            
        'Leave':
            $ pass
        
    return
    
label lb_witch_agree:
    nvl clear
    witch 'I\'ll give you help if you do me a favor. Share your unique sperm with me. I need it for alchemical purposes. Don\'t worry, the process is enjoyable, you\'ll like it. But be warned - I will suck every drop from you!' 
    menu:
        'Let her milk you':
            $ game.dragon.drain_energy()            
            stop music fadeout 1.0            
            show expression "img/scene/witch_sex.jpg" as xxx
            play sound "sound/milking.ogg"
            pause (500.0)
            'The witch takes out a bucket and begins a long but pleasurable process. In order to milk the dragon dry, she has to work tirelessly with her hands and mouth for several hours. But she REALLY wants dragon seed, all that she can possibly get.'
            hide xxx  
            $ game.dragon.lust = 0
            stop sound fadeout 1.0
            call lb_witch_reward
            
        'Go away':
            $ pass
    
    return

label lb_witch_refuse:
    nvl clear    
    witch 'I would be happy to help you, but I need something in return. You have already spent all your semen in the village sluts. I don\'t need the pitiful remnants. Come back when you\'re ready.'
    return

label lb_witch_reward:
    nvl clear    
    witch 'Mmmm...such density and volume. This will be enough for a year, or even two. Ask for what you want!'
    
    menu:
        'Heal me up' if game.dragon.health < 2:
            $ game.dragon.health = 2
            'Your wounds are healed.'
            
        'Give me money':
            python:
                gain = game.dragon.level + 1
                game.lair.treasury.dubloon += gain
            witch 'A dragon begging for gold? Who have have guessed? Okay, here is all I have: [gain]. It was worth it.'
            
        'Give me magic power':
            witch 'I will give you some of my power, but it won\'t last forever. You will be able to cast one spell when you need it...'
            $ game.dragon.spells.append('griffin_meat')
            # старый вариант "поколдуй для меня"
            # $ game.choose_spell(u"Отказаться от заклинания")   
            
        'I did it for the lulz':
            witch 'Oooh...did you fall in love with me? Haha, just kidding. Thanks for the seed - come at any time if you want to be, ah...discharged. My mouth is always available to serve you, big guy.'
    
    return
    