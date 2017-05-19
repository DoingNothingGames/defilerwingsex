# coding=utf-8
#spellchecked and proofread

init python:
    from pythoncode.utils import weighted_random
    from pythoncode.characters import Enemy
        
label lb_location_sky_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))    
    $ place = 'sky'
    hide bg
    show expression get_place_bg(place) as bg    
    nvl clear
    
    if game.dragon.energy() == 0:
        '[game.dragon.name] needs to sleep!'
        return
        
    if not game.dragon.can_fly: 
        '[game.dragon.name] longingly gazes at the sky. If only he knew how to fly...'
    else:
        call lb_encounter_sky
    return
    
label lb_encounter_sky:
    python:
        choices = [
            ("lb_titan_full", 10),
            ("lb_enc_swan", 10),
            ("lb_enc_griffin", 10),
            ("lb_enc_skyboat", 10),
            ("lb_abbey_full", 10),
            ("lb_castle_full", 10),
            ("lb_palace_full", 10),
            ("lb_enc_fair_sky", 10),
            ("lb_enc_caravan_sky", 10),
            ("lb_enc_militia_sky", 10),
            ("lb_enc_cannontower", 10),
            ("lb_jotun_full", 10),
            ("lb_ifrit_full", 10),
            ("lb_patrool_sky", 3 * game.mobilization.level)]
            
        choices = game.removeVisited(choices, visitStack)
        enc = weighted_random(choices)
        
        game.appendVisited(visitStack, enc)        
        renpy.call(enc)
    return
    
label lb_enc_swan:
    'Majestically soaring through, the clouds, [game.dragon.name] sees a flock of white swans. In front the huge fattened leader flies - it is the perfect size for a snack!'
    nvl clear
    
    menu:
        'Eat the geese' if game.dragon.hunger > 0:
            python:
                game.dragon.drain_energy()
                game.dragon.hunger -= 1
                game.dragon.bloodiness = 0
            '[game.dragon.name] catches and eats a goose.'
            
        'Shoo' if game.dragon.bloodiness >= 5 and game.dragon.hunger == 0:
            $ game.dragon.drain_energy()
            '[game.dragon.name] violently attacks the leader and a few other birds, and the rest of the flock scatters in panic in all directions.'    
            
        'Fly away' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return
    
label lb_enc_griffin:
    python:
        game.foe = Enemy('griffin', game_ref=game)
        chances = show_chances(game.foe)
    'In the sky soars an experienced wild griffon. He flies over his lands in search of prey and trespassers, and that second category includes dragons. Maybe someone should show Feathers his place - especially since the flesh of a griffin is rich with magical energies.'
    '[chances]'
    nvl clear
    
    menu:
        'Fight the griffon':
            $ game.dragon.drain_energy()
            call lb_fight
            if game.dragon.hunger > 0:
                'The hungry [game.dragon.name] devours the griffon in the air, dropping scraps for the jackals. As the griffin is digested, the magic of the creature infuses the dragon.'
                python:
                    if game.dragon.bloodiness > 0:
                        game.dragon.bloodiness = 0
                    game.dragon.hunger -= 1
                    game.dragon.add_effect('griffin_meat')
            else:
                '[game.dragon.fullname] is not hungry now, so he lets the mortally wounded griffon fall down to the rocks with a crunch.'
                
        'Fly off' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return
    
label lb_enc_skyboat:
    python:
        game.foe = Enemy('airship', game_ref=game)
        chances = show_chances(game.foe)
    'A sail rises over the clouds! This is one of the airships the dwarves use to trade. So there may be loot...'
    '[chances]'
    
    menu:
        'Attack the airship':
            $ game.dragon.drain_energy()
            call lb_fight
            '[game.dragon.name] quickly scours the falling ship and takes everything of value:'
            python:
                count = random.randint(5, 15)
                alignment = 'dwarf'
                min_cost = 1
                max_cost = 10000
                obtained = "Looted from the dwarven airship."
                trs = treasures.gen_treas(count, data.loot['klad'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
                game.lair.treasury.receive_treasures(trs)
                game.dragon.reputation.points += 3
            '[trs_descrptn]'
            '[game.dragon.reputation.gain_description]'
            
        'Let them fly away' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()    
    return
    
label lb_enc_fair_sky:
    'Soaring high in the sky, [game.dragon.fullname] sees some colored patches on the ground. Descending it becomes clear that the people have staged a fair.'
    call lb_enc_fair
    return

label lb_enc_militia_sky:
    if game.mobilization.level <= 0:
        call lb_encounter_sky
    else:
        call lb_enc_militia_sky_true
    return
    
label lb_enc_militia_sky_true:
    '[game.dragon.fullname] sees mass movement on the ground far below. Militia hastily assembled from the surrounding villages are training.'
    call lb_enc_militia_true
    return
    
label lb_enc_caravan_sky:
    'Flying along the dragon notices something moving snake-like on the road. It is a large caravan.'
    call lb_enc_lcaravan
    return
    
label lb_patrool_sky:
    python:
        chance = random.randint(0, game.mobilization.level)
        if chance < 4:
            patrool = 'archer'
            dtxt = 'The dragon is flying along, not bothering anyone, and then sharp arrows come from below! An overly zealous archer decided to show their prowess.'
        elif chance < 7:
            patrool = 'catapult' #actually a ballista? check mob_data
            dtxt = 'Trying to protect their possessions from flying monsters, the people have set up catapults on the top of hills, shooting massive feathered spears tipped with hardened steel.'
        elif chance < 11:
            patrool = 'griffin_rider'
            dtxt = 'The sky has been disturbed, so it is not surprising that the people have sent out one of their flying knights - a griffon rider is a real threat to any winged monster.'
        elif chance < 16:
            patrool = 'airship'
            dtxt = 'A huge airship breaks through the clouds in front of the dragon. It\'s a dwarven patrol cruiser'
        else:
            patrool = 'angel'
            dtxt = '[game.dragon.fullname] is forced to close his eyes from bright glaring light. An angelic voice proclaims: "Die, vile offspring of sin!" This guardian angel was sent by heaven to protect the people.'
    '[dtxt]'
    
    python:
        game.foe = Enemy(patrool, game_ref=game)
        battle_status = battle.check_fear(game.dragon, game.foe)
        
    if 'foe_fear' in battle_status:
        $ narrator(game.foe.battle_description(battle_status, game.dragon))
        return
        
    $ game.dragon.drain_energy()
    call lb_fight(skip_fear=True)
    return
