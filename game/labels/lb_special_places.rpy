# coding=utf-8
#spellchecked

init python:
    from pythoncode.utils import weighted_random
    from pythoncode.characters import Enemy
    
label lb_special_places:
    nvl clear
    python:
        special_places_menu = []
        for special_place in game.dragon.special_places.keys():
            # Add to the list of investigated points of interest
            special_stage = game.dragon.special_places[special_place]
            special_places_menu.append((data.special_places[special_stage][0], special_stage))
        special_places_menu.append(('Back', 'back'))
        special_stage = renpy.display_menu(special_places_menu)
        
        if special_stage == 'back':
            pass
        else:
            renpy.call(data.special_places[special_stage][1])
    return
    
label lb_enchanted_forest:
    show expression 'img/bg/special/enchanted_forest.jpg' as bg
    'Even knowing the way to the enchanted forest, it is not easy to pass through a magic elven veil. A powerful spell will be needed.'
    menu:
        'Open the elvenpath (magic)' if game.dragon.mana > 0:
            $ game.dragon.drain_mana()
            '[game.dragon.fullname] uses black magic to break the veil of illusion, confusion, and sleep that the elves hide their possessions under. Unnoticed, the deadly [game.dragon.kind] comes under the shadow of the ancient trees.'
            nvl clear
            call lb_enchanted_forest_enter
            
        'Go back':
            return
        
    return

label lb_enchanted_forest_enter:        
    stop music fadeout 1.0
    play music "mus/forest.ogg"    
    menu:
        'Prowl around':
            python:
                choices = [
                    ("lb_enchanted_forest_elfgirl", 10 * game.dragon.lust), # more lustful dragons will target elf girls
                    ("lb_enchanted_forest_druid", 10),
                    ]
                enc = weighted_random(choices)
                renpy.call(enc)
    
        'Defile the Tree of Life':
            call lb_enchanted_forest_grove
            
    return

label lb_enchanted_forest_elfgirl:
    '[game.dragon.name] smells the mouthwatering aroma that comes only from innocence, beauty, and magic. This is a forest enchantress of the people of the goddess Danu, the elves. No flesh is more sweet and desirable, but because of her witchcraft it will not be easy to capture her.'
    python:
        game.foe = Enemy('elf_witch', game_ref=game)
        narrator(show_chances(game.foe))
    nvl clear
    menu:
        'Fight the Fey':
            $ game.dragon.drain_energy()
            call lb_fight
            'Despite her fierce resistance, the sorceress is mostly unharmed. She is helpless and untouched...for now.'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            nvl clear
            
            $ description = game.girls_list.new_girl('elf')
            game.girl.third "[description]"
            call lb_girl_sex
        
        'Flee' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()        
    return

label lb_enchanted_forest_druid:
    '[game.dragon.name] does not remain unnoticed for long. On the path of the dragon, a druid armed with a gnarled leafy stick materializes. He does not look particularly impressive, but it is an illusion. The very strength of the forest is on the side of this priest of Danu.'
    python:
        game.foe = Enemy('druid', game_ref=game)
        narrator(show_chances(game.foe))
    menu:
        'Fight the Druid':
            $ game.dragon.drain_energy()
            call lb_fight
            $ game.dragon.reputation.points += 3
            'Druid defeated. [game.dragon.reputation.gain_description]'
            '[game.dragon.name] finds something valuable on the corpse:'
            python:
                count = random.randint(1, 2)
                alignment = 'elf'
                min_cost = 25
                max_cost = 500
                obtained = "This item belong to the druid - guard of the enchanted forest.."
                trs = treasures.gen_treas(count, data.loot['knight'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
            '[trs_descrptn]'
            
        'Flee' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()   
            
    return

label lb_enchanted_forest_grove:
    python:
        txt = game.interpolate(random.choice(txt_place_enfr[1]))
        game.foe = Enemy('treant', game_ref=game)
        chances = show_chances(game.foe)
        
    show expression 'img/bg/special/enchanted_forest.jpg' as bg
    nvl clear
    '[txt]'    
    '[chances]'
    nvl clear
    
    menu:
        'Fight the Treant':
            $ game.dragon.drain_energy()
            call lb_fight
            $ txt = game.interpolate(random.choice(txt_place_enfr[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 25
            '[game.dragon.reputation.gain_description]' 
            nvl clear
            call lb_enchanted_forest_grove_rob
            
        'Flee' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            
    return
    
label lb_enchanted_forest_grove_rob:
    python:
        game.dragon.add_event('ravage_sacred_grove')
        count = random.randint(5, 10)
        alignment = 'elf'
        min_cost = 500
        max_cost = 3000
        obtained = "This is from the royal treasury of the elves of the enchanted forest."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Defile the Sacred Grove':
            python:
                txt = game.interpolate(random.choice(txt_place_enfr[2]))
                game.lair.treasury.receive_treasures(trs)
                    
            show expression 'img/bg/lair/elfruin.jpg' as bg
            '[txt]'    
            '[trs_descrptn]'
            nvl clear
            
            python:
                txt = game.interpolate(random.choice(txt_place_enfr[3]))
                description = game.girls_list.new_girl('elf')
            show expression 'img/bg/special/bedroom.jpg' as bg
            '[txt]'    
            nvl clear
            
            game.girl.third "[description]"
            call lb_girl_sex
            $ game.dragon.add_special_place('enchanted_forest', 'elf_forest_empty')
            call lb_dead_grove
                                        
        'Remember this place and depart':
            $ game.dragon.add_special_place('enchanted_forest', 'elf_forest_empty')
            
    return
    
label lb_dead_grove:
    $ txt = game.interpolate(random.choice(txt_place_enfr[4]))
    show expression 'img/bg/special/enchanted_forest.jpg' as bg
    '[txt]'   
    nvl clear
    
    menu:
        'Make a lair here':
            $ game.create_lair('forest_heart')
            $ game.dragon.del_special_place('enchanted_forest')
        
        'Go away':
            $ game.dragon.add_special_place('enchanted_forest', 'elf_forest_empty')
    
    return

# Knight's manor
    
label lb_manor_full:
    python:
        game.foe = Enemy('old_knight', game_ref=game)
        chances = show_chances(game.foe)
        
    show expression 'img/bg/special/castle1.jpg' as bg
    if not game.dragon.contains_special_place('manor'):
        $ txt = game.interpolate(random.choice(txt_place_manor[0]))
        '[txt]'    
        nvl clear
        
    $ txt = game.interpolate(random.choice(txt_place_manor[1]))
    '[txt]'
    '[chances]'
    nvl clear
    
    menu:
        'Challenge the old knight':
            $ game.dragon.drain_energy()
            call lb_fight
            $ txt = game.interpolate(random.choice(txt_place_manor[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            nvl clear
            call lb_manor_rob
            
        'Remember this place and go' if game.dragon.bloodiness < 5:
            python:
                game.dragon.add_special_place('manor', 'manor_full')
                game.dragon.gain_rage()
            
    return
    
label lb_manor_rob:
    python:
        count = random.randint(1, 5)
        alignment = 'knight'
        min_cost = 10
        max_cost = 250
        obtained = "Looted from the knightly manor."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
        
    menu:
        'Rob the manor':
            python:
                txt = game.interpolate(random.choice(txt_place_manor[2]))
                game.lair.treasury.receive_treasures(trs)
                
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            '[txt]'    
            '[trs_descrptn]'
            nvl clear
            
            $ txt = game.interpolate(random.choice(txt_place_manor[3]))
            show expression 'img/bg/special/bedroom.jpg' as bg
            '[txt]'    
            nvl clear
            
            $ description = game.girls_list.new_girl('princess')
            game.girl.third "[description]"
            call lb_girl_sex
            call lb_manor_empty
            $ game.dragon.add_special_place('manor', 'manor_empty')
        
        'Remember this place and go':
            $ game.dragon.add_special_place('manor', 'manor_empty')
            
    return
            
label lb_manor_empty:
    $ txt = game.interpolate(random.choice(txt_place_manor[4]))
    
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    '[txt]'   
    nvl clear
    
    menu:
        'Make lair here':
            $ game.create_lair('castle')
            $ game.dragon.del_special_place('manor')
        
        'Go away':
            $ game.dragon.add_special_place('manor', 'manor_empty')
            
    return

# Wooden Fort
    
label lb_wooden_fort_full:
    show expression 'img/bg/special/castle2.jpg' as bg
    if not game.dragon.contains_special_place('wooden_fort'):
        $ txt = game.interpolate(random.choice(txt_place_wooden_fort[0]))
        '[txt]'
        nvl clear

    python:
        txt = game.interpolate(random.choice(txt_place_wooden_fort[1]))
        game.foe = Enemy('footman', game_ref=game)
        chances = show_chances(game.foe)
    '[txt]'    
    '[chances]'
    nvl clear
    
    menu:
        'Siege the motte and bailey':
            $ game.dragon.drain_energy()
            call lb_fight
            $ txt = game.interpolate(random.choice(txt_place_wooden_fort[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'            
            nvl clear
            call lb_wooden_fort_rob
            
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('wooden_fort', 'wooden_fort_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_wooden_fort_rob:
    python:
        count = random.randint(2, 6)
        alignment = 'knight'
        min_cost = 25
        max_cost = 500
        obtained = "Looted from the wooden fort."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Rob the keep':
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_wooden_fort[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            show expression 'img/bg/special/bedroom.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_wooden_fort[3]))
            '[txt]'    
            nvl clear
            $ description = game.girls_list.new_girl('princess')
            nvl clear
            game.girl.third "[description]"
            call lb_girl_sex
            $ game.dragon.add_special_place('wooden_fort', 'wooden_fort_empty')
            call lb_wooden_fort_empty
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('wooden_fort', 'wooden_fort_empty')
            
    return
            
label lb_wooden_fort_empty:
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_wooden_fort[4]))
    '[txt]'   
    nvl clear
    menu:
        'Make a lair here':
            $ game.create_lair('castle')
            $ game.dragon.del_special_place('wooden_fort')
        
        'Go away':
            $ game.dragon.add_special_place('wooden_fort', 'wooden_fort_empty')
            
    return

# Abbey Castle
    
label lb_abbey_full:
    show expression 'img/bg/special/castle3.jpg' as bg
    if not game.dragon.contains_special_place('abbey'):
        $ txt = game.interpolate(random.choice(txt_place_abbey[0]))
        '[txt]'
        nvl clear

    python:
        txt = game.interpolate(random.choice(txt_place_abbey[1]))
        game.foe = Enemy('templars', game_ref=game)
        chances = show_chances(game.foe)
        
    '[txt]'
    '[chances]'
    nvl clear
    
    menu:
        'Storm the abbey':
            $ game.dragon.drain_energy()
            call lb_fight
            $ txt = game.interpolate(random.choice(txt_place_abbey[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 10
            '[game.dragon.reputation.gain_description]'  
            nvl clear
            call lb_abbey_rob
            
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('abbey', 'abbey_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_abbey_rob:
    python:
        count = random.randint(4, 10)
        alignment = 'cleric'
        min_cost = 10
        max_cost = 500
        obtained = "Looted from the convent."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
   
    menu:
        'Rob the abbey':
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_abbey[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            show expression 'img/bg/special/bedroom.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_abbey[3]))
            '[txt]'    
            nvl clear
            $ description = game.girls_list.new_girl('princess')
            nvl clear
            game.girl.third "[description]"
            call lb_girl_sex
            $ game.dragon.add_special_place('abbey', 'abbey_empty')
            call lb_abbey_empty
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('abbey', 'abbey_empty')
            
    return
            
label lb_abbey_empty:
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_abbey[4]))
    '[txt]'   
    nvl clear
    menu:
        'Make a lair here':
            $ game.create_lair('castle')
            $ game.dragon.del_special_place('abbey')
        
        'Go away':
            $ game.dragon.add_special_place('abbey', 'abbey_empty')
            
    return

# Castle
    
label lb_castle_full:
    show expression 'img/bg/special/castle4.jpg' as bg
    
    if not game.dragon.contains_special_place('castle'):
        $ txt = game.interpolate(random.choice(txt_place_castle[0]))
        '[txt]'
        nvl clear

    python:
        txt = game.interpolate(random.choice(txt_place_castle[1]))
        game.foe = Enemy('castle_guard', game_ref=game)
        chances = show_chances(game.foe)
        
    '[txt]'
    '[chances]'
    nvl clear
    
    menu:
        'Siege the castle':
            $ game.dragon.drain_energy()
            call lb_fight
            $ txt = game.interpolate(random.choice(txt_place_castle[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 10
            '[game.dragon.reputation.gain_description]'                
            nvl clear
            call lb_castle_rob
            
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('castle', 'castle_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_castle_rob:
    python:
        count = random.randint(3, 8)
        alignment = 'knight'
        min_cost = 100
        max_cost = 1000
        obtained = "Looted from the fortress."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
        
    menu:
        'Rob the citadel':
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_castle[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            show expression 'img/bg/special/bedroom.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_castle[3]))
            '[txt]'    
            nvl clear
            $ description = game.girls_list.new_girl('princess')
            nvl clear
            game.girl.third "[description]"
            call lb_girl_sex
            $ game.dragon.add_special_place('castle', 'castle_empty')
            call lb_castle_empty
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('castle', 'castle_empty')
            
    return
            
label lb_castle_empty:
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_castle[4]))
    '[txt]'   
    nvl clear
    menu:
        'Make a lair here':
            $ game.create_lair('castle')
            $ game.dragon.del_special_place('castle')
        
        'Go away':
            $ game.dragon.add_special_place('castle', 'castle_empty')
            
    return

# Palace
        
label lb_palace_full:
    show expression 'img/bg/special/castle5.jpg' as bg
    if not game.dragon.contains_special_place('palace'):
        $ txt = game.interpolate(random.choice(txt_place_palace[0]))
        '[txt]'
        nvl clear
    
    python:
        txt = game.interpolate(random.choice(txt_place_palace[1]))
        game.foe = Enemy('palace_guards', game_ref=game)
        chances = show_chances(game.foe)
    
    '[txt]'    
    '[chances]'
    nvl clear
    
    menu:
        'Attack the royal palace':
            $ game.dragon.drain_energy()
            call lb_fight
            $ txt = game.interpolate(random.choice(txt_place_palace[5]))
            '[txt]' 
            $ game.dragon.reputation.points += 25
            '[game.dragon.reputation.gain_description]'                 
            nvl clear
            call lb_palace_rob
            
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('palace', 'palace_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_palace_rob:
    python:
        count = random.randint(5, 10)
        alignment = 'knight'
        min_cost = 250
        max_cost = 2500
        obtained = "Looted from the royal palace."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
        
    menu:
        'Rob the palace':
            show expression 'img/bg/lair/ruins_inside.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_palace[2]))
            '[txt]'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            show expression 'img/bg/special/bedroom.jpg' as bg
            $ txt = game.interpolate(random.choice(txt_place_palace[3]))
            '[txt]'    
            nvl clear
            $ description = game.girls_list.new_girl('princess')
            nvl clear
            game.girl.third "[description]"
            call lb_girl_sex
            $ game.dragon.add_special_place('palace', 'palace_empty')
            call lb_palace_empty
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('palace', 'palace_empty')
            
    return
            
label lb_palace_empty:
    show expression 'img/bg/lair/ruins_inside.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_place_palace[4]))
    '[txt]'   
    nvl clear
    
    menu:
        'Make a lair here':
            $ game.create_lair('castle')
            $ game.dragon.del_special_place('palace')
        
        'Remember this place and leave':
            $ game.dragon.add_special_place('palace', 'palace_empty')
            
    return

    
    
# Ogre\'s home
        
label lb_ogre_den_full:
    if not game.dragon.contains_special_place('ogre'):
        'The dragon wanders for some time through the woods...'
        show expression 'img/bg/special/cave_enter.jpg' as bg
        'And stumbles upon the entrance to a cave spacious enough for a lair. Judging by the smell, an ogre has already made one.'
        
    python:
        game.foe = Enemy('ogre', game_ref=game)
        chances = show_chances(game.foe)
        
    '[chances]'
    nvl clear
    
    menu:
        'Challenge the ogre':
            $ game.dragon.drain_energy()
            call lb_fight
            '[game.dragon.name] is victorious.'
            call lb_ogre_den_explore
            
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('ogre', 'ogre_den_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_ogre_den_explore:
    $ game.dragon.add_special_place('ogre', 'ogre_den_empty')
    
    menu:
        'Rob the den':
            'In the cave a frightened giantess is hiding. Either a daughter or the wife of the ogre whose body is lying outside.'
            $ description = game.girls_list.new_girl('ogre')
            nvl clear
            game.girl.third "[description]"
            call lb_girl_sex
            call lb_ogre_den_empty
            
        'Remember this place and leave':
            $ pass
    
    return
 
label lb_ogre_den_empty:
    menu:
        'The cave where the ogre lived is now empty. Here you could make a den, not a very nice one, but still better than an open ravine in a thicket.'
        
        'Make a lair here':
            $ game.create_lair('ogre_den')
            $ game.dragon.del_special_place('ogre')
            
        'Remember this place and leave':
            $ game.dragon.add_special_place('ogre', 'create_ogre_lair')
    
    return
            
            
# Frost giant\'s home  
    
label lb_jotun_full:
    if not game.dragon.contains_special_place('jotun'):
        'High in the mountains, where everything is covered with ice and snow, there is a giant ice palace. Interesting...'
        nvl clear
    
    python:
        txt = game.interpolate(random.choice(txt_place_jotun[0]))
        game.foe = Enemy('jotun', game_ref=game)
        chances = show_chances(game.foe)
    
    show expression 'img/bg/lair/icecastle.jpg' as bg
    '[txt]'
    '[chances]'
    nvl clear
    
    menu:
        'Challenge the Jotun':
            $ game.dragon.drain_energy()
            call lb_fight
            call lb_jotun_rob
            
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('jotun', 'jotun_full')
            $ game.dragon.gain_rage()
    return
    
label lb_jotun_rob:
    menu:
        'Rob the Icy Citadel':
            python:
                txt = game.interpolate(random.choice(txt_place_jotun[1]))
                description = game.girls_list.new_girl('ice')
                game.dragon.add_special_place('jotun', 'jotun_empty')
                
            '[txt]'
            nvl clear
            
            game.girl.third "[description]"
            call lb_girl_sex
            call lb_jotun_empty
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('jotun', 'jotun_empty')
            
    return
 
label lb_jotun_empty:
    $ txt = game.interpolate(random.choice(txt_place_jotun[2]))
    show expression 'img/bg/lair/icecastle.jpg' as bg
    '[txt]'
    menu:
        'Make a lair here':
            $ game.create_lair('ice_citadel')
            $ game.dragon.del_special_place('jotun')
            
        'Remember this place and leave':
            $ game.dragon.add_special_place('jotun', 'jotun_empty')
            
    return 
    
# Fire forge
    
label lb_ifrit_full:
    if not game.dragon.contains_special_place('ifrit'):
        'Above a volcanic crater rises a tower of black obsidian. I wonder who lives there...'
        nvl clear
    
    python:
        txt = game.interpolate(random.choice(txt_place_ifrit[0]))
        game.foe = Enemy('ifrit', game_ref=game)
        chances = show_chances(game.foe)
    
    show expression 'img/bg/lair/volcanoforge.jpg' as bg
    '[txt]'
    '[chances]'
    nvl clear
    
    menu:
        'Challenge the fire giant':
            $ game.dragon.drain_energy()
            call lb_fight
            call lb_ifrit_rob
            
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('ifrit', 'ifrit_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_ifrit_rob:
    menu:
        'Rob the volcanic forge':
            python:
                txt = game.interpolate(random.choice(txt_place_ifrit[1]))
                description = game.girls_list.new_girl('fire')
                game.dragon.add_special_place('ifrit', 'ifrit_empty')
                
            '[txt]'
            nvl clear
            game.girl.third "[description]"
            call lb_girl_sex
            call lb_ifrit_empty
            
        'Remember this place and leave':
            $ game.dragon.add_special_place('ifrit', 'ifrit_empty')
            
    return
 
label lb_ifrit_empty:
    $ txt = game.interpolate(random.choice(txt_place_ifrit[2]))
    show expression 'img/bg/lair/volcanoforge.jpg' as bg
    '[txt]'
    
    menu:
        'Make a lair here':
            $ game.create_lair('vulcanic_forge')
            $ game.dragon.del_special_place('ifrit')
            
        'Remember this place and leave':
            $ game.dragon.add_special_place('ifrit', 'ifrit_empty')
            
    return 

    
# Underwater palace
        
label lb_triton_full:
    if not game.dragon.contains_special_place('triton'):
        'The dragon swims along the coast...'
        show expression 'img/bg/lair/underwater.jpg' as bg
        'And discoveres an underwater arch, decorated with corals and seashells. The doorway is big enough for even a sperm whale to swim through.'
        nvl clear
    
    python:
        txt = game.interpolate(random.choice(txt_place_triton[0]))
        game.foe = Enemy('triton', game_ref=game)
        choices = show_chances(game.foe)
    
    show expression 'img/bg/lair/underwater.jpg' as bg
    '[txt]'
    '[choices]'
    nvl clear
    
    menu:
        'Challenge the Triton':
            $ game.dragon.drain_energy()
            call lb_fight
            call lb_triton_rob
            
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('triton', 'triton_full')
            $ game.dragon.gain_rage()
            
    return
    
label lb_triton_rob:
    menu:
        'Rob the underwater mansion':
            python:
                txt = game.interpolate(random.choice(txt_place_triton[1]))
                description = game.girls_list.new_girl('siren')
                game.dragon.add_special_place('triton', 'triton_empty')

            '[txt]'
            nvl clear
            game.girl.third "[description]"
            call lb_girl_sex
            call lb_triton_empty
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('triton', 'triton_empty')
            
    return
 
label lb_triton_empty:
    $ txt = game.interpolate(random.choice(txt_place_triton[2]))
    show expression 'img/bg/lair/underwater.jpg' as bg
    '[txt]'
    menu:
        'Make a lair here':
            $ game.create_lair('underwater_mansion')
            $ game.dragon.del_special_place('triton')
            
        'Go away':
            $ game.dragon.add_special_place('triton', 'triton_empty')
    return 
    
# Titan Cloud Castle
        
label lb_titan_full:   
    if not game.dragon.contains_special_place('titan'):
        'The dragon rises above the clouds...'
        show expression 'img/bg/special/cloud_castle.jpg' as bg
        'And discovers a floating island and beautiful castle. I wonder who built it...'
        nvl clear
    
    python:
        txt = game.interpolate(random.choice(txt_place_titan[0]))
        game.foe = Enemy('titan', game_ref=game)
        chances = show_chances(game.foe)
    
    show expression 'img/bg/special/cloud_castle.jpg' as bg
    '[txt]'
    '[chances]'
    nvl clear
    
    menu:
        'Challenge the Titan':
            $ game.dragon.drain_energy()
            call lb_fight
            $ game.dragon.reputation.points += 10
            '[game.dragon.reputation.gain_description]'   
            call lb_titan_rob
            
        'Remember this place and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.add_special_place('titan', 'titan_full')
            $ game.dragon.gain_rage()
    return
    
label lb_titan_rob:
    menu:
        'Rob the cloud castle':
            python:
                txt = game.interpolate(random.choice(txt_place_titan[1]))
                description = game.girls_list.new_girl('titan')
                game.dragon.add_special_place('titan', 'titan_empty')
                
            '[txt]'
            nvl clear
            game.girl.third "[description]"
            call lb_girl_sex
            call lb_titan_empty
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('titan', 'titan_empty')
            
    return
 
label lb_titan_empty:
    $ txt = game.interpolate(random.choice(txt_place_titan[2]))
    
    show expression 'img/bg/lair/cloud_castle.jpg' as bg
    '[txt]'
    
    menu:
        'Make a lair here':
            $ game.create_lair('cloud_castle')
            $ game.dragon.del_special_place('titan')
            
        'Go away':
            $ game.dragon.add_special_place('titan', 'titan_empty')
            
    return 
    
# Underground Dwarven Kingdom

label lb_backdoor:
    show expression 'img/bg/special/backdor.jpg' as bg
    'The secret door to a kingdom of the dwarves is indicated on the drawings found in the stronghold as the "backdoor". In contrast to the main gate there are no defenses, and anyone who knows the secret can get in. Of course, they still have to face an army of dwarves, but getting to them is easier than trying to pass through the main fortifications.'  
    nvl clear
    menu:
        'Go through the "backdoor"!':
            $ game.dragon.drain_energy()
            stop music fadeout 1.0
            play music "mus/moria.ogg"
            $ renpy.music.queue(get_random_files('mus/ambient'))           
            show expression 'img/bg/special/moria.jpg' as bg
            'Pressing an inconspicuous stone in the right place, [game.dragon.name] opens a secret passage into the dwarven kingdom. There won\'t be a second chance at this, if the dragon retreats the dwarves will seal up their "backdoor" and strengthen it more thoroughly.'
            $ game.dragon.add_special_place('backdoor', 'backdoor_sealed')
            call lb_dwarf_army
            
        'More preparation is needed...':
            $ pass
            
    return

label lb_backdoor_sealed:
    show expression 'img/bg/special/backdor.jpg' as bg
    'There was a secret passage to a dwarven kingdom here, but during the attack the dwarves brought down the tunnel and covered it with stones. The little miners love their explosions...'
    nvl clear
    return
    
label lb_frontgates:
    'Fortified impregnable bulwarks, these impressive metal gates firmly close the only known entry into this dwarven kingdom. There are incredible treasures hidden in its depths, the likes of which are not possessed by any kings on the surface, but only someone very powerful could break inside.'
    show expression 'img/bg/special/gates_dwarf.jpg' as bg
    nvl clear
    
    menu:
        'Crush the Mountain Gates' if game.dragon.size > 3:
            'The pathetic fortifications of the fat little gnomes cannot resist the violent offspring of the Mistress. [game.dragon.fullname] is huge and powerful enough to break through the gates and into the dwarven kingdom. But now there is no going back - if the dwarves are not driven out now, they will rebuild stronger than ever.'
            $ game.dragon.add_special_place('backdor', 'backdor_sealed')
            $ game.dragon.drain_energy()
            call lb_golem_guard
            
        'Flee':
            'Hanging around the front gate of the dwarves is not a good idea, they might fire something.'
            $ game.dragon.gain_rage()
        
    return
    
label lb_golem_guard:
    stop music fadeout 1.0
    play music "mus/moria.ogg"
    $ renpy.music.queue(get_random_files('mus/ambient')) 
    
    python:
        game.foe = Enemy('golem', game_ref=game)
        chances = show_chances(game.foe)
    
    show expression 'img/bg/special/moria.jpg' as bg
    'Even after the gate collapses, dust and pebbles continue to pour from the ceiling. Footsteps of the gate guard echo through the central galley - a fully forged and tempered mechanical giant. There are few creatures on the surface equal to it in strength...'
    '[chances]'
    nvl clear
    
    menu:
        'Fight the Iron Golem':
            $ game.dragon.drain_energy()
            call lb_fight
            call lb_dwarf_army
            
        'Flee' if game.dragon.bloodiness < 5:
            'Today they are lucky, but even if they rebuild the gate, they won\'t be left alone for long...'
            $ game.dragon.gain_rage()
    
    return
    
label lb_dwarf_army:
    python:
        game.foe = Enemy('dwarf_guards', game_ref=game)
        chances = show_chances(game.foe)
    'Like a deadly hurricane [game.dragon.fullname] rushes into the inner chambers of the dwarven kingdom. However, the dwarves are still not defenseless, the dragon stumbles into the path of a hastily assembled strike force...'
    '[chances]'
    
    menu:
        'Massacre':
            call lb_fight
            'Now that the main forces of the dwarves are defeated and demoralized, it is necessary to choose where the final blow will be struck. The housing quarter is almost defenseless and there the dwarves can be killed before they have time to escape. On the other hand, the most important valuables are kept lower, in the main treasury. If you do not pay a visit there now, the cunning dwarves will make out with every last coin.'

            menu:
                'Down to the treasury!':
                    call lb_dwarf_treasury
                    
                'Rob the halls':
                    call lb_dwarf_houses
                    
                'Flee':
                    'It is a shame to retreat when victory is so close, but cornered dwarves can be extremely dangerous opponents. Sometimes it is better not to risk it!'
                    $ game.dragon.gain_rage()
                    
        'Run, tail between legs':
            'Today shorty is lucky, but even if they restore the gate, they will not be left alone for long...'
            $ game.dragon.gain_rage()
            
    return
    
label lb_dwarf_houses:
    python:
        game.foe = Enemy('dwarf_citizen', game_ref=game)
        chances = show_chances(game.foe)
    
    'Although most of the dwarves run around in panic trying to save themselves and their belongings, many clutch crowbars, picks, and axes, ready to repulse the enemy...'
    '[chances]'
    nvl clear
    
    menu:
        'Fight the dwarves':
            call lb_fight
            call lb_dwarf_ruins
            
        'Flee':
            'It is a shame to retreat when victory is so close, but cornered dwarves can be extremely dangerous opponents. Sometimes it is better not to risk it!'
            $ game.dragon.gain_rage()
            
    return
    
label lb_dwarf_treasury:
    python:
        game.foe = Enemy('dwarf_champion', game_ref=game)
        chances = show_chances(game.foe)

    'Realizing that their kingdom is on the brink of collapse, the dwarves are trying to save the largest valuables, and the treasures of the king. There are not many fighters among them, but there is one worth an entire army - clad in armor to the eyes, a dwarven champion stands forth, brandishing a massive and sharp axe.'
    '[chances]'
    nvl clear
    
    menu:
        'Fight the champion':
            call lb_fight
            $ game.dragon.reputation.points += 25
            '[game.dragon.reputation.gain_description]'     
            call lb_dwarf_rob
            
        'Flee':
            'It is a shame to retreat when victory is so close, but cornered dwarves can be extremely dangerous opponents. Sometimes it is better not to risk it!'
            $ game.dragon.gain_rage()
            
    return

label lb_dwarf_rob:
    python:
        count = random.randint(12,15)
        alignment = 'dwarf'
        min_cost = 500
        max_cost = 5000
        obtained = "Looted from the king\'s treasury under the mountain."
        trs = treasures.gen_treas(count, data.loot['palace'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Rob the Great Treasury':
            show expression 'img/bg/hoard/base.jpg' as bg
            'The vile dwarves managed to take many things away, but even what is left is dazzling. Nowhere else is there such a rich hoard!'    
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            nvl clear
            call lb_dwarf_ruins
                                        
        'Remember this place and leave':
            $ game.dragon.add_special_place('palace', 'palace_empty')
    return
            
label lb_dwarf_ruins:
    show expression 'img/bg/special/moria.jpg' as bg
    'There once lived dwarves here, but now this place is desolate and abandoned. Inside, you can make a specious and well-defended lair.'
    menu:
        'Make a lair here':
            $ game.create_lair('underground_palaces')
            $ game.dragon.del_special_place('frontgates')
            $ game.dragon.del_special_place('backdor')
            
        'Go away':
            $ game.dragon.add_special_place('frontgates', 'frontgates_open')
            
    return 
