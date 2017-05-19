# coding=utf-8
#spellchecked

init python:
    from pythoncode.utils import weighted_random
    from pythoncode.characters import Enemy
    
    visitStack = []
        
label lb_location_forest_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))    
        place = 'forest'
        
    hide bg
    show expression get_place_bg(place) as bg
    nvl clear
    
    if game.dragon.energy() == 0:
        '[game.dragon.name] needs to sleep!'
        return
    
    python:
        nochance = game.poverty.value * 3
        choices = [
            ("lb_enc_lumberjack", 10),
            ("lb_enc_onegirl", 10),
            ("lb_enc_wandergirl", 10),
            ("lb_ogre_den_full", 10),
            ("lb_enc_deer", 10),
            ("lb_enc_boar", 10),
            ("lb_enc_berries", 10),
            ("lb_enc_shrooms", 10),
            ("lb_enc_guardian", 10),
            ("lb_enc_lumbermill", 10),
            ("lb_enc_klad", 5),
            ("lb_enc_domiki", 1),
            ("lb_patrool_forest", 3 * game.mobilization.level),
            ("lb_enc_noting", nochance)]
        
        choices = game.removeVisited(choices, visitStack)
        enc = weighted_random(choices)
        
        game.appendVisited(visitStack, enc)
        renpy.call(enc)
    
    return
    
label lb_enc_domiki:
    if "domiki_done" in persistent.easter_eggs:
        jump lb_location_forest_main
        
    "SUDDENLY! From a forest thicket something runs at the dragon..."
    show expression 'img/scene/fight/domik.jpg' as bg    
    'A LOG CABIN?!!!! This must be the legendary creation of Cyril "Korvanusya", the ancient mad wandering archmage - a wooden battle golem. It\'s obviously aggressive. ...'
    
    python:
        persistent.easter_eggs.append("domiki_done")
        game.foe = Enemy('domik', game_ref=game)    
        narrator(show_chances(game.foe))
        
    call lb_fight
    'Amongst the wreckage of the house is a sign: "Made by the request of the the wicked one (I have not yet come up with a name for it). What a mad and brilliant creation...'
    return

label lb_enc_lumberjack:
    'Nearby, rhythmic cracks are heard, echoing throughout the forest. It sounds like lumberjacks\' axes. By itself, wood production is completely uninteresting, but the time is right for lunch, and in the human tradition the eldest unmarried daughter brings food to a man working far from home. It\'s worth a look...'
    nvl clear
    python:
        if game.dragon.size < 3: 
            success = True
        else:
            success = False
            
    if success: 
        '[game.dragon.name] drops to the ground and slowly, trying not to make a sound, creeps towards the noise. Fortunately the dumb woodcutters are too busy with their stimulating and creative occupation to notice a giant lizard hiding in the bushes. Now we need only wait...'
        nvl clear
        menu:
            'Watch secretly':
                python:
                    game.dragon.drain_energy()
                    description = game.girls_list.new_girl('peasant')
                    game.dragon.reputation.points += 1
                    
                'Within the hour, another figure appears on the path, a female figure. In her hands is a heavy basket covered with a white rag. [game.dragon.name] sniffs and determines with certainty - a virgin! Although, a peasant...'
                game.girl 'Papaaaa! I brought you something to eat. I\'ve got sweet bread in a basket.'
                nvl clear
                
                'The girl runs to her father to hug him, but he freezes in horror, looking behind her. There stands [game.dragon.name], stretched to full length. Not giving them time to react, [game.dragon.name] kills the woodcutter and knocks down his daughter.'
                '[game.dragon.reputation.gain_description]'
                nvl clear
                
                game.girl.third "[description]"
                call lb_nature_sex

            'Go away' if game.dragon.bloodiness < 5:
                $ game.dragon.gain_rage()
    else: 
        'Crouching and moving slowly, the dragon sneaks towards the noise. But he is too large for such a tactic, the woodcutter hears heavy breathing and snapping branches. Dropping his axe he runs away terrified. What a shame...' 
        $ game.dragon.gain_rage()
            
    return
    
    
label lb_enc_onegirl:
    'If you hide by a forest path, then sooner or later someone will pass by. This time you see a young peasant girl coming down the path, holding a basket. She must be carrying something to a father or a brother working in the woods.'
    nvl clear
    menu:
        'Get the girl':
            python:
                game.dragon.drain_energy()
                description = game.girls_list.new_girl('peasant')
                game.dragon.reputation.points += 1
                
            '[game.dragon.name] breaks through the bushes and storms onto the road. The peasant freezes in terror with a horrified expression. It looks like she is not going to run...of course, running would have been pointless. '
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex
            
        'Let her run' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return

label lb_enc_wandergirl:
    'From the forest thicket you hear someone crying "Help!". It\'s the voice of a woman, a young one. It sounds like she strayed from her group and is lost in the woods. She hopes someone will hear her - well, a dragon hears her...'
    nvl clear
    menu:
        'Call in a human voice':
            python:
                game.dragon.drain_energy()
                description = game.girls_list.new_girl('peasant')
                game.dragon.reputation.points += 1
                
            'Dragons are very talented in deceitful magic. One of their many skills is the ability to impersonate. You needed only to respond to her call, and now she is running right into your clutches!'
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_nature_sex
            
        'Go away' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return

label lb_enc_deer:
    'In the woods a fully grown deer is grazing. Not a bad appetizer if the stomach rumbles, but nothing special. '
    nvl clear
    menu:
        'Hunt down the deer' if game.dragon.hunger > 0:
            python:
                game.dragon.drain_energy()
                if game.dragon.bloodiness > 0:
                    game.dragon.bloodiness = 0
                    game.dragon.hunger -= 1
            '[game.dragon.name] catches and eats the deer.'
                
        'Rip the deer into pieces'  if game.dragon.bloodiness >= 5 and game.dragon.hunger == 0: #
            $ game.dragon.drain_energy()
            '[game.dragon.name] brutally tortures the deer for fun.'    
            
        'Roar and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return

label lb_enc_boar:
    'The wind carries the smell of a large animal. In the underbrush rustles a huge wild boar. More than a meter at the shoulder, the thick-skinned and massive beast is armed with huge curved tusks. The boar is not afraid of anything in the forest - it is not easy prey, but it is a good way to gain strength before more serious battles.'
    python:
        game.foe = Enemy('boar', game_ref=game)
        narrator(show_chances(game.foe))
    nvl clear
    
    menu:
        'Fight the boar':
            $ game.dragon.drain_energy()
            call lb_fight
            if game.dragon.hunger > 0:
                '[game.dragon.name] eats the fallen boar. The meat contains the strength of the boar, and will give the dragon killer power.'
                python:
                    if game.dragon.bloodiness > 0:
                        game.dragon.bloodiness = 0
                    game.dragon.hunger -= 1
                    game.dragon.add_effect('boar_meat')
            else:
                'The dragon triumphs.'
                
        'Back out' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    
    return
    
label lb_enc_guardian:
    $ txt = game.interpolate(random.choice(txt_enc_forest_guardian[0]))
    '[txt]'
    show expression 'img/scene/fight/elf_ranger.jpg' as bg
    $ txt = game.interpolate(random.choice(txt_enc_forest_guardian[1]))
    $ game.foe = Enemy('elf_ranger', game_ref=game)
    '[txt]'
    $ narrator(show_chances(game.foe))
    nvl clear
    
    menu:
        'Attack':
            $ game.dragon.drain_energy()
            call lb_fight
            python:
                txt = game.interpolate(random.choice(txt_enc_forest_guardian[2]))
                if game.dragon.magic > 0:
                    txt = game.interpolate(random.choice(txt_enc_forest_guardian[3]))
                    game.dragon.add_special_place('enchanted_forest', 'elf_forest_full')
            '[txt]'
            
        'Flee' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            return
    return

label lb_enc_lumbermill:
    show expression 'img/bg/special/lumbermill.jpg' as bg
    'On the banks of a forest river a wooden building stands. It encloses a huge mechanism, driven by a water wheel. Chances are the people here are sawing wood.'
    nvl clear
    python:
        doit = False
        if 'fire_breath' in game.dragon.modifiers(): 
            doit = True
    menu:
        'Breathe fire' if doit:
            $ game.dragon.drain_energy()
            "[game.dragon.name] spews a stream of all-consuming flame onto the building. The dry wood lights immediately, starting a raging fire. Now the people will have less building material for their homes and castles."
            $ game.poverty.value += 1
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
        'Conjure blue flames' if game.dragon.mana > 0:
            $ game.dragon.drain_energy()
            $ game.dragon.drain_mana()
            "[game.dragon.name] calls forth magic spellfire, and the dry wood bursts into blue flames. Now the people will have less building material for their homes and castles."
            $ game.poverty.value += 1
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
        'Investigate' if game.dragon.size <= 3 and game.dragon.magic == 0:
            $ game.dragon.drain_energy()
            "[game.dragon.name] carefully examines the unusual structure for its purpose and weaknesses. The rotating flow of water drives a saw hidden inside the building, which the people use to saw logs into board. Nearby are huge stacks of finished boards. What if they all burned? "
            'A waste of time. I leave as wise as I was before.'
        'Ignore' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    
    return
    
label lb_enc_klad:
    'The dragon smells buried treasure.'
    nvl clear
    python:
        tr_lvl = random.randint(1, 100)
        count = random.randint(1, 10)
        alignment = 'human'
        min_cost = 1 * tr_lvl
        max_cost = 10 * tr_lvl
        obtained = "This is from a stash that someone buried in the woods"
        trs = treasures.gen_treas(count, data.loot['klad'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Find the buried treasure':
            $ game.dragon.drain_energy()
            'Digging under the roots of an old oak, the dragon finds an old buried chest. Inside lies:'
            '[trs_descrptn]'
            $ game.lair.treasury.receive_treasures(trs)
            
        'Let it be' if game.dragon.bloodiness < 5:
            'Certainly treasure is good, but what trinkets buried by the common people could be worth the precious time of a noble dragon? '
    return

label lb_patrool_forest:
    python:
        chance = random.randint(0, game.mobilization.level)
        if chance < 4:
            patrool = 'jagger'
            dtxt = 'The woods are patrolled by a royal huntsman -  a ranger armed with a long yew bow and a sharp knife.'
        elif chance < 7:
            patrool = 'footman'
            dtxt = 'On the forest road a detachment of soldiers march. it seems they patrol the area in search of robbers and monsters. Well, they\'ve found one...'
        elif chance < 11:
            patrool = 'heavy_infantry'
            dtxt = 'The forest roads are patrolled by a troop of heavy infantry. If the people care so much about the security of the forests that they send in elite fighters, then they really must be scared.'
        elif chance < 16:
            patrool = 'griffin_rider'
            dtxt = 'A shrill cry is heard from heaven - a rider on a griffon swoops down from the sky, having glimpsed the shine of dragon scales between the trees. '
        else:
            patrool = 'angel'
            dtxt = '%s is forced to close his eyes against a brilliant glare. There is a loud announcement: "Die, vile offspring of sin!". This guardian angel was sent by heaven to protect the people.' % game.dragon.name
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
