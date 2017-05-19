# coding=utf-8
#spellchecked

init python:
    from pythoncode.utils import weighted_random
    from pythoncode.characters import Enemy
    
    visitStack = []
        
label lb_location_road_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))    
    $ place = 'road'
    hide bg
    show expression get_place_bg(place) as bg
    nvl clear
    
    if game.dragon.energy() == 0:
        '[game.dragon.name] needs to sleep!'
        return
        
    python:
        nochance = game.poverty.value * 3
        choices = [
            ("lb_enc_tournament", 5),
            ("lb_enc_inn", 15),
            ("lb_enc_peasant_cart", 15),
            ("lb_enc_carriage", 5),
            ("lb_enc_questing_knight", 10),
            ("lb_enc_trader", 10),
            ("lb_enc_caravan", 7),
            ("lb_enc_lcaravan", 3),
            ("lb_enc_outpost", 10),
            ("lb_manor_full", 15),
            ("lb_wooden_fort_full", 10),
            ("lb_abbey_full", 7),
            ("lb_castle_full", 5),
            ("lb_palace_full", 3),
            ("lb_patrool_road", 3 * game.mobilization.level),
            ("lb_enc_noting", nochance)]
        
        choices = game.removeVisited(choices, visitStack)
        enc = weighted_random(choices)
        
        game.appendVisited(visitStack, enc)
        renpy.call(enc)
        
    return
    
    
label lb_enc_tournament:
    'A noise in the distance...'
    show expression 'img/bg/special/tornament.jpg' as bg
    '...it\'s a jousting tournament. The winner is preparing to put a golden crown on the \"queen of love and beauty\"".'
    python:
        game.foe = Enemy('champion', game_ref=game)
        chances = show_chances(game.foe)
    '[chances]'
    nvl clear
    menu:
        'Challenge the Champion':
            $ game.dragon.drain_energy()
            call lb_fight
            'When they see their champion defeated, the guests of the tournament scatter in panic, dropping everything and screaming in horror. [game.dragon.name] does not pay attention to them, he takes the prize - the \"Queen of Love and Beauty\", and her golden crown.'
            $ game.dragon.reputation.points += 5
            $ description = game.girls_list.new_girl('princess')
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_girl_sex
            
        'Go away' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            'Caution cannot hurt. If this knight is really the best in the region, he could be dangerous. A woman and a piece of gold can be found somewhere else.'
            
    return
    
label lb_enc_inn:
    show expression 'img/bg/special/tabern.jpg' as bg    
    'A two-storey inn stands on a busy intersection of a trade route. Spotting the dragon, the unarmed humans run in horror into the building and barricade the doors and windows. The inn\'s destruction would do real damage to the economy of the settled lands...'
    nvl clear
    python:
        doit = False
        if 'fire_breath' in game.dragon.modifiers(): 
            doit = True
    menu:
        'Breathe fire' if doit:
            $ game.dragon.drain_energy()
            "Unleashing his fiery breath, [game.dragon.name] torches the building on all four sides. The wooden inn burns rapidly, burning the people barricaded inside in flaming wreckage."
            $ game.poverty.value += 1
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'
            
        'Conjure poisonous vapors' if game.dragon.mana > 0:
            $ game.dragon.drain_energy()
            $ game.dragon.drain_mana()
            "[game.dragon.name] calls on dark magic to fill the locked up rooms with poisonous fog. The inn stands as before, but inside are nothing but corpses."
            $ game.poverty.value += 1
            $ game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'
            
        'Demand a barrel of ale':
            show expression 'img/bg/special/fear.jpg' as bg  
            $ game.dragon.drain_energy()
            "[game.dragon.name] receives from the frightened tavern owner a whole barrel of fine ale. After such a binge, he needs a woman and a good meal!"
            python:
                if game.dragon.bloodiness < 5:
                    game.dragon.bloodiness += 1
                if game.dragon.lust < 3:
                    game.dragon.lust += 1
                if game.dragon.hunger < 3:
                    game.dragon.hunger += 1
                    
        'Let it be' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            
    return
    
label lb_enc_peasant_cart:
    'On the road a peasant cart loaded with hay slowly travels. These carts are common around here, and every one of them is completely useless. Even the horse is skinny and unappetizing. Already the dragon\'s blood boils.'
    menu:
        'Kill the peasant' if game.dragon.bloodiness >= 5:
            $ game.dragon.drain_energy()
            'Giving free rein to his anger, [game.dragon.kind] turns over the cart, killing the horse farmer and tearing him to pieces. The miserable peasant had nothing of value! How dare he meet a dragon, and have nothing to take?!'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            
        'Swallow the horse whole' if game.dragon.hunger > 0: #old huntsman's original translation: "vore the horse". kek
            $ game.dragon.drain_energy()
            'While [game.dragon.name] devours the sinewy peasant horse, the owner of the wagon runs away in terror. Let him tell other miserable mortals of your greatness.'
            python:
                if game.dragon.bloodiness > 0:
                    game.dragon.bloodiness = 0
                game.dragon.hunger -= 1
                game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            
        'Let them go' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return
    
label lb_enc_carriage:
    'On the road a pillar of dust rises. In a coach a noble lady travels, with heavily armed mounted crossbowmen as guards. Good spoils, but not the easiest to take...'
    python:
        game.foe = Enemy('mounted_guard', game_ref=game)
        chances = show_chances(game.foe)
    '[chances]'
    nvl clear
    menu:
        'Attack the coach':
            $ game.dragon.drain_energy()
            call lb_fight
            'Now that the bodyguards are not a threat, the dragon can inspect the carriage. Tearing off its body like gift wrap, [game.dragon.name] finds three women inside - a mother, a daughter, and a servant. Old women are of no interest to a fiend like you, but with a girl, you can have a wonderful time!'
            python:
                game.dragon.reputation.points += 5
                description = game.girls_list.new_girl('princess')
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_girl_sex
            
        'Demand tribute' if game.dragon.fear > 4:
            $ game.dragon.drain_energy()
            'The bodyguards are intimidated enough that they decide not to risk their charge\'s life. The noblewoman\'s handmaiden is dragged out of the carriage kicking and screaming and thrown to the waiting dragon, and the coach and bodyguards quickly flee down the road, leaving the poor girl to her fate...'
            $ game.dragon.reputation.points += 1
            $ description = game.girls_list.new_girl('citizen')
            '[game.dragon.reputation.gain_description]'
            nvl clear
            game.girl.third "[description]"
            call lb_girl_sex
            
        'Let it go' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()        
            
    return
    
label lb_enc_questing_knight:
    python:
        game.foe = Enemy('champion', game_ref=game)
        chances = show_chances(game.foe)    
    'On the road rides a knight, accompanied by a servant on an old donkey. It would be a sin for a knight errant not to challenge the dragon, but will he survive to gain fame from such a battle?'
    '[chances]'
    nvl clear
    
    menu:
        'Accept the challenge':
            $ game.dragon.drain_energy()
            call lb_fight
            $ game.dragon.reputation.points += 5
            'The knight is defeated. [game.dragon.reputation.gain_description]'
            '[game.dragon.name] found something valuable on the corpse:'
            python:
                count = random.randint(1, 5)
                alignment = 'knight'
                min_cost = 10
                max_cost = 250
                obtained = "This item belonged to an obscure knight errant."
                trs = treasures.gen_treas(count, data.loot['knight'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                game.lair.treasury.receive_treasures(trs)                
                trs_descrptn = '\n'.join(trs_list)
            '[trs_descrptn]'
            
        'Go away' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()   
            
    return
    
label lb_enc_trader:
    'On the road is a big colorful wagon covered in painted advertisements. It\'s some kind of traveling merchant, not very successful but judging by the smell there is some silver to be found in his pockets. Someone should ease his burden.'
    nvl clear
    
    menu:
        'Extort money':
            python:
                game.dragon.drain_energy()
                passing_tool = random.randint(10, 200)
                slvr_trs = [treasures.Coin('taller', passing_tool)]
                game.lair.treasury.receive_treasures(slvr_trs)
            'The relieved merchant gives the dragon some silver taller in exchange for being left alone and allowed to pass.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            
        'Rob the merchant' if game.dragon.bloodiness >= 5:
            python:
                game.dragon.drain_energy()
                gold_trs = [treasures.Coin('farthing', 100), treasures.Coin('taller', 10)]
                game.lair.treasury.receive_treasures(gold_trs)
            '[game.dragon.name] releases his anger and overturns the wagon, kills the horse, and tears the trader to pieces. His wares are of little interest, but there is some money in his wallet:'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            
        'Let him go' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            
    return
    
label lb_enc_caravan:
    python:
        game.foe = Enemy('xbow_rider', game_ref=game)
        chances = show_chances(game.foe)
    '[game.dragon.name] stumbles on a caravan that promises to be a good catch. Unfortunately, the traders did not skimp on protection - they are accompanied by a platoon of mounted crossbowmen.'
    '[chances]'
    nvl clear
    
    menu:
        'Extort money' if game.dragon.fear > 3:
            python:
                game.dragon.drain_energy()
                passing_tool = random.randint(5, 25)
                gold_trs = treasures.Coin('dubloon', passing_tool)
                game.lair.treasury.receive_treasures([gold_trs])
            'The caravan hands over some gold dubloons to the growling dragon in exchange for safe passage.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            
        'Rob the caravan':
            $ game.dragon.drain_energy()
            call lb_fight
            '[game.dragon.name] releases his anger and overturns the wagons, kills the horses, and tears the traders to pieces. Their wares are of little interest, but there are some bags full of money:'
            python:
                count = random.randint(5, 15)
                alignment = 'human'
                min_cost = 1
                max_cost = 1000
                obtained = "Просто монеты."
                trs = treasures.gen_treas(count, ['taller', 'dubloon'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
                game.lair.treasury.receive_treasures(trs)
            '[trs_descrptn]'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            
        'Let it go' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()    
    return
   
label lb_enc_lcaravan:
    python:
        game.foe = Enemy('mounted_guard', game_ref=game)
        chances = show_chances(game.foe)
    '[game.dragon.name] decides to be methodical and lies in wait in an overgrown roadside ditch. After half a day, at last a decent target comes by - on the road is a rich merchant caravan. Judging by the quality and quantity of protection, these merchants pay in gold.'
    '[chances]'
    nvl clear
    
    menu:
        'Extort money' if game.dragon.fear > 6:
            python:
                game.dragon.drain_energy()
                passing_tool = random.randint(20, 100)
                gold_trs = treasures.Coin('dubloon', passing_tool)
                game.lair.treasury.receive_treasures([gold_trs])
            'The caravan hands over a heavy bag of gold dubloons to the growling dragon in exchange for safe passage.'
            $ game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            
        'Rob the rich caravan':
            $ game.dragon.drain_energy()
            call lb_fight from _call_lb_fight_17
            'Smashing the guards and the caravan, [game.dragon.name] searches the broken carts for everything of value. Mostly there are products of no value to any self-respecting dragon - fabrics, spices, oils and the like. But in the purses of the merchants there is hard cash:'
            python:
                count = random.randint(5, 15)
                alignment = 'human'
                min_cost = 1
                max_cost = 1000
                obtained = "Просто монеты."
                trs = treasures.gen_treas(count, ['taller', 'dubloon'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
                game.lair.treasury.receive_treasures(trs)
            '[trs_descrptn]'
            $ game.dragon.reputation.points += 3
            '[game.dragon.reputation.gain_description]'
            
        'Let it go' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
        
    return
    
label lb_enc_outpost:
    python:
        game.foe = Enemy('footman', game_ref=game)
        chances = show_chances(game.foe)
    'To maintain order and the collection of tariffs, the kingdom has established a series of outposts. The garrison is comprised of conventional infantry, and a sergeant, cook and clerk. But inside is a money chest where the day\'s tolls are kept!'
    '[chances]'
    nvl clear
    
    menu:
        'Attack outpost':
            $ game.dragon.drain_energy()
            call lb_fight
            'Most of the guards are dead, the rest flee in horror, but the outpost still stands and restoring its operation will not be difficult. But inside is a chest with the recently collected trade taxes:'
            python:
                passing_tool = random.randint(10, 50)
                slvr_trs = treasures.Coin('taller', passing_tool)
                game.narrator(slvr_trs.description() + '.')
                game.lair.treasury.receive_treasures([slvr_trs])
                game.dragon.reputation.points += 5
            '[game.dragon.reputation.gain_description]'
  
        'Go away' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            'Certainly it would be profitable to take the trade duties, but there is too much protection. To fight with the royal soldiers is pointless, it is better to look for easier or richer prey.'
        
    return
    
label lb_patrool_road:
    python:
        chance = random.randint(0, game.mobilization.level)
        if chance < 4:
            patrool = 'archer'
            dtxt = 'Along the country road walks a bearded man with a longbow, sent by the local sheriff to patrol for suspicious people on the road. Will he be brave enough to fight?'
        elif chance < 7:
            patrool = 'xbow_rider'
            dtxt = 'A detachment of light cavalry patrol the trade route. They are ready to respond quickly to any threat, be it bandits, monsters, or even a dragon.'
        elif chance < 11:
            patrool = 'heavy_cavalry'
            dtxt = 'The dragon runs into a detachment of heavy cavalry. The people appear to be so intimidated that they\'ve begun sending knights on highway patrol.'
        elif chance < 16:
            patrool = 'griffin_rider'
            dtxt = 'A shrill cry is heard from heaven - a rider on a griffon swoops down from the sky, having spotted shining dragonscale on the road.'
        else:
            patrool = 'angel'
            dtxt = '%s is forced to shut his eyes by a bright glare. A voice loudly proclaims: "Die, vile offspring of sin!" This guardian angel was sent by heaven to protect the people.' % game.dragon.name
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
