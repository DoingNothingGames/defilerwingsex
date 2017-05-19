# coding=utf-8
#spellchecked
init python:
    from pythoncode import battle
    from pythoncode.characters import Enemy, Talker
    
    reinforcement_used = False
    
label lb_location_mordor_main:
    $ reinforcement_used = False
    $ place = 'mordor' 
    hide bg
    show place as bg
    python:
        if renpy.music.get_playing(channel='music') != "mus/dark.ogg":
            renpy.music.play("mus/dark.ogg")
            renpy.music.queue(get_random_files('mus/ambient'))
    nvl clear
    python:
        mistress = Talker(game_ref=game)
        mistress.avatar = "img/avahuman/mistress.jpg"
        mistress.name = "Mistress"
    
    menu:
        'To the Free Kingdoms':
            $ pass
        'Army of Darkness' if not freeplay:
            show expression 'img/bg/special/army.jpg' as bg
            '[game.army.army_description]'
            nvl clear
            menu:
                'Go to WAR!':
                    $ mistrss_helps = True
                    call lb_war_border from _call_lb_war_border
                'Let them train':
                    'The army is not yet ready.'
                    
            call lb_location_mordor_main from _call_lb_location_mordor_main
            
        'Mistress' if not freeplay:
            jump lb_mistress
        'Retire':
            menu:
                "This will reset the current game and allow you to start fresh!"
                "Do you want to give up?!"
                "Yes":
                    python:
                        if not freeplay:
                            renpy.unlink_save("1-1")
                            renpy.full_restart()
                        else:
                            renpy.unlink_save("1-3")
                            renpy.full_restart()
                "No":
                    return
    return
    
label lb_mistress:
    python:
        if not persistent.isida_done:
            renpy.movie_cutscene("mov/isida.webm")
            persistent.isida_done = True
    nvl clear
    show expression 'img/scene/mistress.jpg' as bg    
    menu:
        'Ask for a reward' if game.is_quest_complete:
            # Если делаем подарок - удаляем его из списка сокровищ
            if game.quest_task == 'gift' and len(game.lair.treasury.jewelry) > 0:
                $ del game.lair.treasury.jewelry[game.lair.treasury.most_expensive_jewelry_index]
            game.dragon 'I have performed your task. I remember being promised a reward...'    
            mistress 'Come to me, darling. You will not regret it, I promise.'
            call lb_mistress_fuck from _call_lb_mistress_fuck
            call lb_choose_dragon from _call_lb_choose_dragon
            return
        'Ask about your quest' if not game.is_quest_complete:
            "Текущее задание:\n[game.quest_text]\n[game.quest_time_text]"
            call lb_mistress from _call_lb_mistress
        'Chat':
            $ txt = game.interpolate(random.choice(txt_advice))
            mistress '[txt]'   
            nvl clear            
            call lb_mistress from _call_lb_mistress_1
        'Treacherous attack':
            game.dragon 'Whether I win this fight or not, it will be the end of my family. Is it worth it to kill my mother?'
            menu:
                'I will crush her!':
                    jump lb_betrayal
                'She is my mother, after all...':
                    'Her son\'s tension did not escape Mistress\'s notice, but she only smiled enigmatically, not showing the slightest concern.'
                    call lb_location_mordor_main from _call_lb_location_mordor_main_1
        'Go away':
            'Sometimes there is simply a desire to touch her again...'  
            call lb_location_mordor_main from _call_lb_location_mordor_main_2
    return

label lb_location_mordor_questtime:
    $ place = 'mordor' 
    show place as bg
    show screen status_bar
    if game.is_quest_complete:
        mistress '[game.dragon.name] , you spend too much time playing with the people, I tire of waiting. Have you forgotten your task?'
        game.dragon 'Not at all, Mistress, I did all that you asked. Here, look.'
        mistress 'Perfect. In that case, you are due for a well-deserved reward. Come to me, darling.'
        call lb_mistress_fuck from _call_lb_mistress_fuck_1
        call lb_choose_dragon from _call_lb_choose_dragon_1
    else:
        $ game.dragon.die()
        mistress 'Your allotted time has passed, [game.dragon.name]. I will only ask you once: have you performed your task?'
        game.dragon 'I did not, Mistress. I need a little more time. Forgive me.'
        mistress 'I am not angry. But I have no pity for you. You have disappointed me, and that can only be done once. Another dragon will be the successor of your race, you will live out your days as you wish. Get out of my sight!'
        menu:
            "Choose another dragon":
                call lb_choose_dragon from _call_lb_choose_dragon_2
                return
    return
    

label lb_mistress_fuck:
    mistress 'I can take any shape that pleases you. Choose how you want to see me.'
    menu:
        'I like your shape as it is':
            show expression sex_imgs("mistress") as xxx
            pause (500.0)
            $ txt = game.interpolate(random.choice(txt_human_mistress_fuck[game.dragon.kind]))
            '[txt]'    
            hide xxx
        'Can you become a dragon-woman?':
            show expression sex_imgs("dragon") as xxx
            pause (500.0)            
            $ txt = game.interpolate(random.choice(txt_dragon_mistress_fuck[game.dragon.kind]))
            '[txt]'
            hide xxx
    show expression 'img/scene/mistress.jpg' as bg
    mistress 'I thank you for your powerful seed, my son. Our children will surpass all that have been born before.'
    game.dragon 'Let my sons continue my work when they grow up.'
    mistress 'When they hatch, you will have to choose your successor, my beloved..'
    nvl clear
    'Nine months passed, and a clutch of eggs hatched.'
    python:
        if not persistent.lada_done:
            renpy.movie_cutscene("mov/lada.webm")
            persistent.lada_done = True    
    return

label lb_betrayal:
    $ renpy.movie_cutscene("mov/kali.webm")
    $ atk_tp = 'pysical'
    $ mistress_hp = 3
    call lb_new_round from _call_lb_new_round
    return

label lb_new_round:
    nvl clear    
    if mistress_hp < 1:
        mistress 'I will be back!'
        $data.achieve_target("betray", "win")
        $ game.win()
        jump lb_you_win
    $ aspect = 'lb_' + random.choice(['kali','garuda','shiva','agni','indra','pangea','nemesis','amphisbena','gekata','hell',])
    $ renpy.call(aspect)
    return

label lb_tactics_choice:
    menu:
        'Fangs':
            $ atk_tp = 'physical'
        'Spell' if game.dragon.mana > 0:
            $ atk_tp = 'magic'
        'Breathe fire' if 'fire_breath' in game.dragon.modifiers():
            $ atk_tp = 'fire'
        'Icy breath' if 'ice_breath' in game.dragon.modifiers():
            $ atk_tp = 'ice'
        'Thunder roar' if 'sound_breath' in game.dragon.modifiers():
            $ atk_tp = 'thunder'
        'Venomous sting'  if 'poison_breath' in game.dragon.modifiers() or 'poisoned_sting' in game.dragon.modifiers():
            $ atk_tp = 'poison'
        'Dive in the sky' if game.dragon.can_fly:
            $ atk_tp = 'air'
        # 'Зарыться под землю' if game.dragon.can_dig: #TODO надо понять как это правильно проверить
        #    $ atk_tp = 'earth'
        'Dodge':
            $ atk_tp = 'dodge'
        'Hide':
            $ atk_tp = 'hide'
    return

label lb_kali:
    show expression 'img/scene/fight/mistress/kali.jpg' as bg    
    'The mistress takes the shape of the multiarmed goddess Kali, with coal black skin and blood red tongue. She is armed with sharp sickles, and very dangerous when close. '
    call lb_tactics_choice from _call_lb_tactics_choice
    if game.dragon.defence_power()[1] > 0:
        game.dragon 'My scales cannot be cut, mother. You birthed me invincible.'
    else:
        'With one flick, Kali\'s sharp sickle beheads the dragon.'
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'You are finished, my son...in vain you tried to walk the path of Judas.'
            jump lb_game_over
        else:
            mistress 'You\'ve got one less head, sonny. A pity you can\'t think with it any more!'
            
    if atk_tp == 'magic':
        game.dragon 'Your sickles will not protect you from death magic!!!'
        $ mistress_hp -= 1
    else:
        mistress 'Fool, you cannot defeat me!'
    call lb_new_round from _call_lb_new_round_1
    return

label lb_garuda:
    show expression 'img/scene/fight/mistress/garuda.jpg' as bg    
    'Becoming covered entirely in bright feathers and growing sharp copper claws, Mistress takes on the aspect of Garuda. There is no place on heaven or earth to hide from her falcon strike, but she is vulnerable to attack.' 
    call lb_tactics_choice from _call_lb_tactics_choice_1
    if atk_tp == 'earth': #never happens, currently no option to attack with earth? so no need to translate?
        game.dragon 'Под землёй тебе меня не достать, пернатая тварь!'
    else:
        'With the incredible power of Garuda, she rakes the dragon with her claws and tears off his head.'
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'From a snake you were born, and like a worm you die!'
            jump lb_game_over
        else:
            mistress 'Still alive, viper?!'
        
    if atk_tp != 'dodge' and atk_tp != 'hide' and atk_tp != 'earth' and atk_tp != 'air':
        game.dragon 'A hit!'
        $ mistress_hp -= 1
    else:
        mistress 'Run, run! And you had a chance to hurt me, you idiot!'   
            
    call lb_new_round from _call_lb_new_round_2
    return
    

label lb_shiva:
    show expression 'img/scene/fight/mistress/sheeva.jpg' as bg    
    'Taking on the aspect of Shiva, Mistress gains unlimited power over cold and ice. Under her steps the earth is covered in frost, and your scales grow cold.'
    call lb_tactics_choice from _call_lb_tactics_choice_2
    if 'ice_immunity' in game.dragon.modifiers():
        game.dragon 'Cold is nothing to me, Mother. You should have not have forgotten!'
    else:
        'With a single touch, Shiva turns the head of the dragon into a fragile block of ice. With a one blow, she shatters it into splinters.'
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'Lie frozen in ice, you failure of a son!'
            jump lb_game_over
        else:
            mistress 'See, it doesn\'t even hurt. The cold is merciful. But the next head will be less lucky!'

    if atk_tp == 'fire':
        game.dragon 'Flame, I command you! Melt, vaporize, burn!!!'
        $ mistress_hp -= 1
    else:
        mistress 'Only fire could help you, but you have not mastered it! I know all of your weaknesses.'
            
    call lb_new_round from _call_lb_new_round_3
    return

label lb_agni:
    show expression 'img/scene/fight/mistress/agni.jpg' as bg    
    'Taking on the aspect of Agni, the Mistress is wrapped in a dress of crimson flame and choking black smoke. From it comes sizzling heat that no one but a fire giant could withstand.'
    call lb_tactics_choice from _call_lb_tactics_choice_3
    if 'fire_immunity' in game.dragon.modifiers():
        game.dragon 'Ha! Really, you mad old woman, you decided to burn the master of fire? Your heat will only make me stronger, let me have it.'
    else:
        "From the touch of Agni, the dragon\'s head flashes and instantly turns into a blackened char."
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'Feel my heart\'s raging fury, miserable traitor! DIE! DIE!!!'
            jump lb_game_over
        else:
            mistress 'Feel the fire of my soul! You\'re still twitching, pathetic worm?!'
        
    if atk_tp == 'ice':
        game.dragon 'Your fire will be snuffed out by my cold breath, Agni!'
        $ mistress_hp -= 1
    else:
        mistress 'How can you hope to break fire itself, fool?'
                            
    call lb_new_round from _call_lb_new_round_4
    return

label lb_indra:
    show expression 'img/scene/fight/mistress/indra.jpg' as bg    
    'Taking the aspect of Indra, Mistress gets power of the lightning and thunder of heaven. She is as untouchable as the air and sky that feed her power.'
    call lb_tactics_choice from _call_lb_tactics_choice_4
    if 'lightning_immunity' in game.dragon.modifiers():
        game.dragon 'The titans could not strike me with lightning, and neither will you, Indra. In storm clouds I am at home!'
    else:
        'A thunderbolt falls directly on the dragon\'s head, incinerating it in an instant!'
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'My retribution is as fast as lightning. Do think it was worth it, traitor?!'
            jump lb_game_over
        else:
            mistress 'Minus one. And now say goodbye to the next one!'
        
    if atk_tp == 'poison':
        game.dragon 'I poison the air that gives you strength. No one can stand the toxic fumes, not even god!'
        $ mistress_hp -= 1
    else:
        mistress 'You are strong, but not strong enough to throw down the heavens, traitor!'
                            
    call lb_new_round from _call_lb_new_round_5
    return
    

label lb_pangea:
    show expression 'img/scene/fight/mistress/pangea.jpg' as bg    
    'Mistress\'s body turns into a huge living crystal, the perfect embodiment of the earth goddess Pangea. Her flesh is as hard as diamond.'
    call lb_tactics_choice from _call_lb_tactics_choice_5
    if game.dragon.defence_power()[0] + game.dragon.defence_power()[1] >= 5:
        game.dragon 'My scales are no softer than your diamond skin, Pangea! You did not even scratch me.'
    else:
        "Pangea squeezes the dragon\'s head in a death grip, popping it like a ripe watermelon."
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'For raising a hand against your mother, you deserved to be crushed.'
            jump lb_game_over
        else:
            mistress 'I will break you! No matter how tenacious you are, sooner or later you will die, bastard!'
        
    if atk_tp == 'thunder':
        game.dragon 'Hit!'
        $ mistress_hp -= 1
    else:
        mistress 'Missed!'   
                            
    call lb_new_round from _call_lb_new_round_6
    return

label lb_nemesis:
    show expression 'img/scene/fight/mistress/nemesis.jpg' as bg    
    'Mistress takes the aspect of the goddess Nemesis. Her body is covered with sharp spikes, representing inevitable retribution.'
    call lb_tactics_choice from _call_lb_tactics_choice_6
    if atk_tp == 'dodge' or atk_tp == 'hide' or atk_tp == 'earth' or atk_tp == 'air':
        game.dragon 'I know Nemesis\'s justice. If I don\'t attack, neither can you!'
    else:
        'The attack on Nemesis leads to the inevitable punishment The dragon loses his head..'
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'Such is the fate of all traitors - DEATH!'
            jump lb_game_over
        else:
            mistress 'My revenge is not yet complete, but the hour of your death is near, traitor!'
        
    if atk_tp != 'dodge' and atk_tp != 'hide' and atk_tp != 'earth' and atk_tp != 'air': 
        game.dragon 'But she is also injured!'
        $ mistress_hp -= 1
    else:
        mistress 'You\'re smart to hide, you can live an extra minute, or maybe even two!'  
                            
    call lb_new_round from _call_lb_new_round_7
    return

label lb_amphisbena:
    show expression 'img/scene/fight/mistress/amfisbena.jpg' as bg    
    'Mistress\'s body is covered with brightly colored scales as she takes on the aspect of Amphisbena, a creeping and venomous bringer of death to all living creatures.'
    call lb_tactics_choice from _call_lb_tactics_choice_7
    if atk_tp == 'air':
        game.dragon 'You were born to crawl, not fly. Just try to reach me here!'
    else:
        'Touched by the poison of Amphisbena, the dragon\'s head shrinks and withers.'
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'I was hoping that you would suffer longer, Judas!'
            jump lb_game_over
        else:
            mistress 'Feel the poison? I\'m glad that you\'re still moving, so my revenge will be more sweet.'
        
    if game.dragon.attack_strength()[1] > 0:
        game.dragon 'I will crush you, viper!'
        $ mistress_hp -= 1
    else:
        mistress 'Is that all you can do? Weakling!'
                            
    call lb_new_round from _call_lb_new_round_8
    return
    

label lb_gekata:
    show expression 'img/scene/fight/mistress/gekata.jpg' as bg    
    'Taking on the aspect of Hecate, the Mistress is given the power of night and death. Only one unafraid of mortal wounds can do battle with her, but sometime\'s it\'s better to be a coward.'
    call lb_tactics_choice from _call_lb_tactics_choice_8
    if atk_tp != 'hide':
        game.dragon 'I will take cover in the darkness.'
    else:
        'Deadly Hecate easily tears off the dragon\'s head.'
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'I\'ll feed your body to the jackals, since you are nothing but dog meat!'
            jump lb_game_over
        else:
            mistress 'Still you twitch, carrion?!'
        
    if game.dragon.attack_strength()[0] + game.dragon.attack_strength()[1] >= 5:
        game.dragon 'Take this! I am not so easy to kill.'
        $ mistress_hp -= 1
    else:
        mistress 'I had hoped that my child would hit stronger than a little peasant girl...' 
                            
    call lb_new_round from _call_lb_new_round_9
    return

label lb_hell:
    show expression 'img/scene/fight/mistress/hell.jpg' as bg    
    'The mistress grows to the heavens, her head touching the top of the clouds, as she takes on the aspect of the giantess Hel - undead empress of the lower world. Her movements are slow, but her punches can destroy even granite rocks.'
    call lb_tactics_choice from _call_lb_tactics_choice_9
    if atk_tp == 'dodge':
        game.dragon 'Too slow! You missed!'
    else:
        "With a crushing blow from her huge hand, the giantess flattens the dragon\'s head."
        if 'dragon_dead' in game.dragon.decapitate():
            mistress 'HA! Not even a splatter remains.'
            jump lb_game_over
        else:
            mistress 'Feel the pain! I will squash you like a dirty cockroach!'
        
    if atk_tp == 'magic':
        game.dragon 'My spells surpass your brute force, Hel!'
        $ mistress_hp -= 1
    else:
        mistress 'Nice try, kid, but you\'re too small for me!'  
                            
    call lb_new_round from _call_lb_new_round_10
    return
    
label lb_war_border:
    # TODO: Дракон ведёт свою армию на вольные земли. На протяжении всех событий отступать нельзя - дракон умрёт или победит. Один раз можно попросить госпожу одолеть любого врага вместо дракона.
    # Чтобы пройти АТ нужно взять пограничную крепость. Дракон берёт на себя катапульты, армия штурмует стены.
    # Если и дракон и армия победили, засчитываем победу.
    # Если дракон победил, но армия слишком слаба даём второй энкаунтер для дракона - воздушный флот цвергов приходит
    # на помощь осаждённым, дракон должен их победить.
    python:
        battle.army_battle = True #Из боя теперь нельзя отступить
        army_decimator = 10
    
    show expression 'img/scene/dark_march.jpg' as bg
    'The Army of Darkness enters into a skirmish near the border. The defense is based around catapults.'
    
    $ game.foe = Enemy('catapult', game_ref=game)
    $ narrator(show_chances(game.foe))
            
    menu:
        'Watch calmly' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'The Army of Darkness takes losses, but soldiers advance to the catapults and destroy them. One step towards victory.'
            $ game.army.power_percentage -= army_decimator
            
        'Crush the catapults': #Дракон бережёт армию и сам уничтожает наиболее опасные очаги сопротивления
            call lb_fight from _call_lb_fight_42

        'Plead for help': #Владычица вступает в бой и выигрывает его вместо дракона и армии
            game.dragon '[reinforcement_ask]'
            python:
                if reinforcement_used:
                    reinforcement_answer = reinforcement_refuse
                else:
                    reinforcement_answer = reinforcement_agree
            mistress '[reinforcement_answer]'
            if reinforcement_used:
                call lb_war_border from _call_lb_war_border_1
            else:
                $ renpy.movie_cutscene("mov/kali.webm")
                $ reinforcement_used = True

    call lb_war_border_continue from _call_lb_war_border_continue
    return

label lb_war_border_continue:
    nvl clear
    show expression 'img/scene/dark_march.jpg' as bg
    'The battle is almost won on the ground, but the dragon notices a new danger. From the mountains a fleet of dwarven flying machines are coming through the air. If left unchecked they will drop barrels filled with alchemical fire into the thick of the monster army. The losses will be enormous.'
    $ game.foe = Enemy('airfleet', game_ref=game)
    $ narrator(show_chances(game.foe))
    
    menu:
        'Watch calmly' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'Heavy ships fly defiantly over the masses of monsters and drop fat barrels with lit fuses directly onto the heads of the Mistress\'s soldiers. The earth lights up in flashes and is covered with fluid fire. Flaming goblins scatter and roll on the ground to extinguish themselves. When the supply of bombs on the ships runs out, they return safely back to base. The attack cost the Army of Darkness a tenth of soldiers! However, the border soldiers have retreated, and the path inland lays open.'
            $ game.army.power_percentage -= army_decimator
            
        'Intercept skyfleet': #Дракон бережёт армию и сам уничтожает наиболее опасных врагов
            call lb_fight from _call_lb_fight_43

        'Plead for help': #Владычица вступает в бой и выигрывает его вместо дракона и армии
            game.dragon '[reinforcement_ask]'
            python:
                if reinforcement_used:
                    reinforcement_answer = reinforcement_refuse
                else:
                    reinforcement_answer = reinforcement_agree
            mistress '[reinforcement_answer]'
            if reinforcement_used:
                call lb_war_border_continue from _call_lb_war_border_continue_1
            else:
                $ renpy.movie_cutscene("mov/kali.webm")
                $ reinforcement_used = True
    
    call lb_war_field from _call_lb_war_field
    return

    
label lb_war_field:
    # TODO: Армия продвигается вглубь страны и встречает объединённые войска Вольных Народов. Дракон должен победить титана, армия сражается с войском.
    # Если дракон и АТ победили, продвигаемся дальше. Если дракон победил а АТ проигрывает, даём дракону схватку против короля людей.

    nvl clear    
    show expression 'img/scene/great_force.jpg' as bg
    'The battle on the border was just a skirmish. Now the free people have gathered a coalition to meet the dark army in the open field. Towering over them all is a giant in gold armor - a titan decided to fight on the side of the free!'
    $ game.foe = Enemy('titan', game_ref=game)
    $ narrator(show_chances(game.foe))
    
    menu:
        'Watch calmly' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'The titan does enormous damage to the dark host, but still they manage to overcome it. The free people are wavering, press forward!'
            $ game.army.power_percentage -= army_decimator
            
        'Slay the Titan': #Дракон бережёт армию и сам уничтожает наиболее опасных врагов
            '[game.dragon.fullname] personally enters into battle with the titan in order to save the troops.'
            call lb_fight from _call_lb_fight_44

        'Plead for help': #Владычица вступает в бой и выигрывает его вместо дракона и армии
            game.dragon '[reinforcement_ask]'
            python:
                if reinforcement_used:
                    reinforcement_answer = reinforcement_refuse
                else:
                    reinforcement_answer = reinforcement_agree
            mistress '[reinforcement_answer]'
            if reinforcement_used:
                call lb_war_border_continue from _call_lb_war_border_continue_2
            else:
                $ renpy.movie_cutscene("mov/kali.webm")
                $ reinforcement_used = True
    call lb_war_field_continue from _call_lb_war_field_continue
    return

label lb_war_field_continue:
    # TODO: Армия продвигается вглубь страны и встречает объединённые войска Вольных Народов. Дракон должен победить титана, армия сражается с войском.
    # Если дракон и АТ победили, продвигаемся дальше. Если дракон победил а АТ проигрывает, даём дракону схватку против короля людей.
    
    nvl clear
    show expression 'img/scene/dark_march.jpg' as bg
    'A fighter himself, the king inspires the people and does not allow them to retreat. When he is defeated, the battle can be considered won.'
    $ game.foe = Enemy('king', game_ref=game)
    $ narrator(show_chances(game.foe))
    
    menu:
        'Watch calmly' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'At the cost of huge losses, elite units of the dark forces break through to the king and finish him. This becomes the turning point of the battle. By sunset, the scattered and broken troops of the Free People flee the field opening the way further inland.'
            $ game.army.power_percentage -= army_decimator
            
        'Slay the Warrior-King': #Дракон бережёт армию и сам уничтожает наиболее опасных врагов
            'The battle can be won with just one precise blow. [game.dragon.fullname] challenges the king of the people!'
            call lb_fight from _call_lb_fight_45

        'Plead for help': #Владычица вступает в бой и выигрывает его вместо дракона и армии
            game.dragon '[reinforcement_ask]'
            python:
                if reinforcement_used:
                    reinforcement_answer = reinforcement_refuse
                else:
                    reinforcement_answer = reinforcement_agree
            mistress '[reinforcement_answer]'
            if reinforcement_used:
                call lb_war_field_continue from _call_lb_war_field_continue_1
            else:
                $ renpy.movie_cutscene("mov/kali.webm")
                $ reinforcement_used = True
    call lb_war_siege from _call_lb_war_siege
    return
    
label lb_war_siege:
    # TODO: Армия Тьмы осаждает столицу людей. Дракон должен пробить огромные ворота чтобы армия могла ворваться в город.
    # Если дракон и АТ победили, продвигаемся дальше. Если дракон победил а АТ проигрывает, даём дракону схватку
    # против городской стражи.

    nvl clear
    show expression 'img/scene/city_fire.jpg' as bg
    'After defeating the main forces of the Free Peoples, the army of darkness comes close to the walls of the capital. In this great fortified city resistance may last for years. While the capital is untaken, the Free Lands have not been conquered.'
    $ game.foe = Enemy('city', game_ref=game)
    $ narrator(show_chances(game.foe))
    
    menu:
        'Watch calmly' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'Storming the main gate of the city, the troops take terrible losses, but there are too few defenders. The monsters demolish the gate and burst onto the streets of the city.'
            $ game.army.power_percentage -= army_decimator
            
        'Break the gates': #Дракон бережёт армию и сам уничтожает наиболее опасных врагов
            'If you break through the main gate, the defending forces will be exposed. [game.dragon.fullname] charges forward to assault them. '
            call lb_fight from _call_lb_fight_46

        'Plead for help': #Владычица вступает в бой и выигрывает его вместо дракона и армии
            game.dragon '[reinforcement_ask]'
            python:
                if reinforcement_used:
                    reinforcement_answer = reinforcement_refuse
                else:
                    reinforcement_answer = reinforcement_agree
            mistress '[reinforcement_answer]'
            if reinforcement_used:
                call lb_war_siege from _call_lb_war_siege_1
            else:
                $ renpy.movie_cutscene("mov/kali.webm")
                $ reinforcement_used = True
                
    call lb_war_siege_inside from _call_lb_war_siege_inside
    return

    
label lb_war_siege_inside:
    # TODO: Армия Тьмы осаждает столицу людей. Дракон должен пробить огромные ворота чтобы армия могла ворваться в город.
    # Если дракон и АТ победили, продвигаемся дальше. Если дракон победил а АТ проигрывает, даём дракону схватку
    # против городской стражи.
    nvl clear
    show expression 'img/scene/city_raze.jpg' as bg
    'On the streets of the city there is fierce fighting. Elite squads of city guards put up resistance.'
    $ game.foe = Enemy('city_guard', game_ref=game)
    $ narrator(show_chances(game.foe))
    
    menu:
        'Watch calmly' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'The battle on the city streets is incredibly brutal, blood flows in rivers and there are countless wounded and dead on both sides. But the forces of darkness are too numerous - the defenders of the city are doomed.'
            $ game.army.power_percentage -= army_decimator
            
        'Murder the city guard': #Дракон бережёт армию и сам уничтожает наиболее опасных врагов
            '[game.dragon.fullname] personally leads his troops in the attack, helping to slaughter the guards.'
            call lb_fight from _call_lb_fight_47

        'Plead for help': #Владычица вступает в бой и выигрывает его вместо дракона и армии
            game.dragon '[reinforcement_ask]'
            python:
                if reinforcement_used:
                    reinforcement_answer = reinforcement_refuse
                else:
                    reinforcement_answer = reinforcement_agree
            mistress '[reinforcement_answer]'
            if reinforcement_used:
                call lb_war_siege_inside from _call_lb_war_siege_inside_1
            else:
                $ renpy.movie_cutscene("mov/kali.webm")
                $ reinforcement_used = True
                
    call lb_war_citadel from _call_lb_war_citadel
    return

label lb_war_citadel:
    # TODO: Армия Тьмы захватила город, но центральная цитадель ещё держится. Дракон должен схватиться в воздухе с ангелом-хранителем, пока АТ штурмует.
    # Если дракон и АТ победили, продвигаемся дальше. Если дракон победил а АТ проигрывает, даём дракону схватку
    # против стального стража цвергов.
    # После окончательной победы переходим к сцене финальной оргии и концу игры.
    nvl clear
    show expression 'img/scene/city_raze.jpg' as bg
    'Although the city was taken, and already blazes, in a citadel on the hill defenders still remain. Considering all the treasure that is stored there, taking the stronghold is absolutely essential. Unfortunately, over the citadel hovers an angelic defender, sent by heaven in response to the pleas of the innocent. This winged defender is worth an entire army.'
    $ game.foe = Enemy('angel', game_ref=game)
    $ narrator(show_chances(game.foe))
    
    menu:
        'Watch calmly' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'The spawn of darkness release hundreds of arrows at the angel, but they burn on approaching. The heavenly guardian cuts down squads of goblins with his sword like mowing dry grass with a sickle. Finally he is knocked down with a well-aimed shot from a heavy catapult, but the losses are high.'
            $ game.army.power_percentage -= army_decimator
            
        'Attack the seraph': #Дракон бережёт армию и сам уничтожает наиболее опасных врагов
            'This opponent [game.dragon.fullname] will battle himself - it is too tough for ordinary foot soldiers.'
            call lb_fight from _call_lb_fight_48

        'Plead for help': #Владычица вступает в бой и выигрывает его вместо дракона и армии
            game.dragon '[reinforcement_ask]'
            python:
                if reinforcement_used:
                    reinforcement_answer = reinforcement_refuse
                else:
                    reinforcement_answer = reinforcement_agree
            mistress '[reinforcement_answer]'
            if reinforcement_used:
                call lb_war_citadel from _call_lb_war_citadel_1
            else:
                $ renpy.movie_cutscene("mov/kali.webm")   
                $ reinforcement_used = True
                
    call lb_war_final from _call_lb_war_final
    return
    
label lb_war_final:
    nvl clear
    show expression 'img/scene/city_raze.jpg' as bg
    'Inspired by the victory over the angel, the dragon\'s spawn burst into the citadel, but are just as soon forced out again. The internal gates are protected by a huge mechanical guard of the dwarves - an invincible iron golem.'
    $ game.foe = Enemy('golem', game_ref=game)
    $ narrator(show_chances(game.foe))
    
    menu:
        'Watch calmly' if game.army.force >= 1000: # Армия Тьмы теряет 10% силы и разбирается с противником без вмешательства дракона.
            'With wave after wave of suicide attacks, the iron golem is buried under a mountain of meat and steel. Nevertheless, it is a victory!'
            $ game.army.power_percentage -= army_decimator
            
        'Attack the golem': #Дракон бережёт армию и сам уничтожает наиболее опасных врагов
            'This iron guard is not so mighty compared to everything else that has stood in the way of victory. [game.dragon.fullname] charges forward.'
            call lb_fight from _call_lb_fight_49

        'Plead for help': #Владычица вступает в бой и выигрывает его вместо дракона и армии
            game.dragon '[reinforcement_ask]'
            python:
                if reinforcement_used:
                    reinforcement_answer = reinforcement_refuse
                else:
                    reinforcement_answer = reinforcement_agree
            mistress '[reinforcement_answer]'
            if reinforcement_used:
                call lb_war_final from _call_lb_war_final_1
            else:
                $ renpy.movie_cutscene("mov/kali.webm")               
                $ reinforcement_used = True    
    jump lb_orgy

label lb_orgy:
    nvl clear
    show expression 'img/scene/city_raze.jpg' as bg
    'The defenders have fallen, and the Free Peoples of the earth are now under the authority of the Mistress, the Mother of Dragons!'
    game.dragon 'We have won!'
    mistress 'Yes. Thanks to you, you and your bloodline... How long have I been waiting for this! I\'ll give you and the army three days of plundering the city, and then we will start building the FIRST | WORLD | EMPIRE!'
    game.dragon 'You heard the mistress, soldiers. Bring all the girls to me, and throw them in a pile!'    
    show expression 'img/scene/girls.jpg' as bg
    pause (500.0)
    nvl clear
    'The dragonspawn combed the burning city, seizing all the pretty young women, stripping them bare and putting them in the throne room of the devastated citadel. Hundreds of nude beauties filled the hall so full that the dragon had to swim through a sea of naked bodies to reach the middle.'
    game.dragon 'Today, you can enjoy the victory with me, my children! Do everything you wish to these girls.' 
    show expression 'img/scene/orgy.jpg' as bg
    pause (500.0)    
    nvl clear
    'Pandemonium began. Embittered by the desperate fighting the soldiers of darkness attacked the women like crazy. Looking at the orgy around him, the dragon did not waste any time. Squeezed all around by naked bodies he plunged his dick blindly into tender female flesh, and at the same time bit down with his teeth. A bloody dance began combining hunger and rage, greed and lust. This will continue until the last woman in the crowd loses the ability to squeal and twitch...'
    jump lb_you_win
