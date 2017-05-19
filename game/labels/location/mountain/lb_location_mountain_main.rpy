# coding=utf-8
#spellchecked
init python:
    from pythoncode.utils import weighted_random
    from pythoncode.characters import Enemy
    
    visitStack = []
    
label lb_location_mountain_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))    
    $ place = 'mountain'
    hide bg
    show expression get_place_bg(place) as bg
    nvl clear
    
    if game.dragon.energy() == 0:
        '[game.dragon.name] needs to sleep!'
        return
        
    python:
        nochance = game.poverty.value * 3
        choices = [
            ("lb_enc_miner", 10),
            ("lb_enc_dklad", 10),
            ("lb_enc_mines_silver", 10),
            ("lb_enc_mines_gold", 5),
            ("lb_enc_mines_mithril", 3),
            ("lb_enc_mines_adamantine", 2),
            ("lb_enc_mines_gem_low", 15),
            ("lb_enc_mines_gem_high", 5),
            ("lb_enc_ram", 10),
            ("lb_enc_bear", 10),
            ("lb_jotun_full", 10),
            ("lb_ifrit_full", 10),
            ("lb_enc_smugglers", 10),
            ("lb_enc_slavers", 10),
            ("lb_enc_frontgates_found", 10),
            ("lb_enc_cannontower", 10),
            ("lb_patrool_mountain", 3 * game.mobilization.level),
            ("lb_enc_noting", nochance)]
            
        choices = game.removeVisited(choices, visitStack)
        enc = weighted_random(choices)
        
        game.appendVisited(visitStack, enc)
        renpy.call(enc)
        
    return
    
    
label lb_enc_miner:
    'The breeze brings the faint smell of gold. The aroma leads the dragon to a mountain stream. On the beach sits a miner with a pan, carefully sifting the sand of the river in search of gold dust.'
    nvl clear
    menu:
        'Slay and loot':
            'In the prospector\'s bag is almost a pound of golden dust and nuggets. Thanks for the work, mortal.'
            python:
                gold_trs = treasures.Ingot('gold')
                gold_trs.weight = 1
                game.lair.treasury.receive_treasures([gold_trs])
                game.dragon.drain_energy()
                game.dragon.reputation.points += 1
            '[game.dragon.reputation.gain_description]'
            
        'Let him go' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()

    return
    
label lb_enc_dklad:
    'The sensitive nose of the dragon tells him that treasure lies somewhere nearby. Strange, nothing but wilderness here. Apparently someone decided to bury their treasure here. How nice of them...'
    nvl clear
    python:
        tr_lvl = random.randint(1, 100)
        count = random.randint(1, 10)
        alignment = 'human'
        min_cost = 1 * tr_lvl
        max_cost = 10 * tr_lvl
        obtained = "From a treasure hidden in a mountain crevice."
        trs = treasures.gen_treas(count, data.loot['klad'], alignment, min_cost, max_cost, obtained)
        trs_list = game.lair.treasury.treasures_description(trs)
        trs_descrptn = '\n'.join(trs_list)
    menu:
        'Find buried treasures':
            python:
                game.dragon.drain_energy()
                game.lair.treasury.receive_treasures(trs)
            'Turning every stone and thoroughly looking into every crevice [game.dragon.name] finally discovers the cache. Inside lies:'
            '[trs_descrptn]'
                        
        'Let it be' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            'Of course valuable treasures are useful, but whatever the pitiful mortals hid here is not worth the precious time of a noble dragon.'    
    return

    
label lb_enc_ram:
    'On the rocks stands a ram with huge twisted horns. Not the greatest meal, but a nutritious appetizer.'
    nvl clear
    menu:
        'Devour the ram' if game.dragon.hunger > 0:
            python:
                game.dragon.drain_energy()
                game.dragon.hunger -= 1
                game.dragon.bloodiness = 0
            '[game.dragon.name] catches and devours the ram.'
                    
        'Slaughter the ram' if game.dragon.bloodiness >= 5 and game.dragon.hunger == 0:
            $ game.dragon.drain_energy()
            '[game.dragon.name] violently shreds the ram for fun.'    
            
        'Roar and leave' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return
    
label lb_enc_bear:
    python:
        game.foe = Enemy('bear', game_ref=game)
        chances = show_chances(game.foe)
    'On the mountainside there is a secluded cave entrance. What dragon won\'t stick its nose into a cave? But as it turns out, caves are not only of interest to dragons. A huge cave bear took a fancy to this one. A dangerous opponent, but eating his tough meat will make you strong.'
    '[chances]'
    nvl clear
    
    menu:
        'Fight the dire bear':
            $ game.dragon.drain_energy()
            call lb_fight
            if game.dragon.hunger > 0:
                'The meat of the cave bear is rich in vitamins and minerals, and good for the scales. Maybe it\'s not very tasty, but it\'s healthy. Thanks to this dinner, defense against enemy weapons is increased.'
                python:
                    game.dragon.bloodiness = 0
                    game.dragon.hunger -= 1
                    game.dragon.add_effect('bear_meat')
            else:
                'The dragon celebrates his victory, but he has no appetite. His stomach is already swollen like a drum. A pity, such a rare meat would give the dragon health and strength. '
                
        'Flee' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    
    return
    
label lb_enc_smugglers:
    python:
        game.foe = Enemy('band', game_ref=game)
        chances = show_chances(game.foe)
    'On the mountain pass [game.dragon.name] stumbles upon a caravan of smugglers. They are armed, but will probably prefer to pay for passage rather than fight. Of course, only if the price is reasonable...'
    '[chances]'
    nvl clear
    
    menu:
        'Wring money from them':
            python:
                game.dragon.drain_energy()
                passing_tool = game.dragon.fear * 2 + 1 
                gold_trs = treasures.Coin('taller', passing_tool)
                game.lair.treasury.receive_treasures([gold_trs])
            'The smugglers chip in taller and give [passing_tool] as a payoff to pass peacefully. It\'s good to shear even the black sheep...'
            
        'Take everything':
            $ game.dragon.drain_energy()
            call lb_fight
            python:
                count = random.randint(5, 15)
                alignment = 'human'
                min_cost = 5
                max_cost = 100
                obtained = "Taken from the cargo of smugglers who the dragon robbed in a secret northern mountain pass."
                trs = treasures.gen_treas(count, data.loot['smuggler'], alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
                game.lair.treasury.receive_treasures(trs)
                
            'After searching through the smugglers\' bundles, [game.dragon.name] found some valuables:'
            '[trs_descrptn]'
            
        'Let them pass' if game.dragon.bloodiness < 5:    
            'Let them trade, the richer the country becomes, the more you can profit later!'
            $ game.dragon.gain_rage()
    
    return
    
label lb_enc_slavers:
    python:
        game.foe = Enemy('band', game_ref=game)
        chances = show_chances(game.foe)
    'On the high mountain passes, [game.dragon.name] spots a caravan of slave traders. They lead several slaves on a rope, among them there is one virgin maiden. The robbers are not heavily armed, and will likely hand over a useless slave rather than battle.'
    '[chances]'
    menu:
        'Claim worthless slave' if game.dragon.hunger > 0:
            'For slave traders it is no great loss - they willingly give up their most emaciated slave, and pass [game.dragon.name] without a fight. They even wish the dragon bon appetit.'
            $ game.dragon.drain_energy()
            'The dragon devours the scrawny slave. Not the greatest snack in the world, but hunger is not picky...'
            python:
                game.dragon.bloodiness = 0
                game.dragon.hunger -= 1
        
        'Claim virgin maiden':
            $ game.dragon.drain_energy()            
            'Among the slaves, the young beauty is by far the most valuable. You will have to fight her captors, they will not simply give her up...'
            call lb_fight
            
            'The dragon captures the girl.'
            $ description = game.girls_list.new_girl('citizen')
            nvl clear
            
            game.girl.third "[description]"
            call lb_girl_sex
        
        'Massacre':
            $ game.dragon.drain_energy()
            call lb_fight
        
        'Let them pass' if game.dragon.bloodiness < 5:
            'Let them go about their business. The richer the country becomes through trade, the more there is to steal later!'        
            $ game.dragon.gain_rage()
    
    return

label lb_enc_mines_silver:
    python:
        game.foe = Enemy('xbow', game_ref=game)
        chances = show_chances(game.foe)
    'Silver mine. Protected by a small detachment of crossbowmen.'
    '[chances]'
    menu:
        'Demand some silver' if game.dragon.fear > 3:
            python:
                game.dragon.drain_energy()
                gold_trs = treasures.Ingot('silver')
                gold_trs.weight = 16
                game.lair.treasury.receive_treasures([gold_trs])
                game.dragon.reputation.points += 1
            'The head of the mine hands over a large silver ingot to avoid conflict.'
            '[game.dragon.reputation.gain_description]'
            
        'Take all the silver':
            $ game.dragon.drain_energy()
            call lb_fight
            python:
                count = random.randint(5, 20)
                alignment = 'human'
                min_cost = 1
                max_cost = 1000000
                t_list = ['silver']
                obtained = "Simply silver."
                trs = treasures.gen_treas(count, t_list, alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
                game.lair.treasury.receive_treasures(trs)
                game.dragon.reputation.points += 3
            'In a warehouse the dragon finds stocks of precious metal, smelted and ready for shipment to a treasury:'
            '[trs_descrptn]'
            '[game.dragon.reputation.gain_description]'
            
        'Leave them be' if game.dragon.bloodiness < 5:
            'Human silver is not worth a bolt in the eye!'       
            $ game.dragon.gain_rage()
            
    return

label lb_enc_mines_gold:
    python:
        game.foe = Enemy('heavy_infantry', game_ref=game)
        chances = show_chances(game.foe)
    'Gold mine. Protected by a small detachment of heavy armor-clad infantry.'
    '[chances]'
    menu:
        'Demand some gold' if game.dragon.fear > 5:
            python:
                game.dragon.drain_energy()
                gold_trs = treasures.Ingot('gold')
                gold_trs.weight = 8
                game.lair.treasury.receive_treasures([gold_trs])
                game.dragon.reputation.points += 3
            'The head of the mind hands over a gold nugget to avoid conflict.'
            '[game.dragon.reputation.gain_description]'
            
        'Take all the gold':
            $ game.dragon.drain_energy()
            call lb_fight
            python:
                count = random.randint(3, 15)
                alignment = 'human'
                min_cost = 1
                max_cost = 1000000
                t_list = ['gold']
                obtained = "Simply pure gold."
                trs = treasures.gen_treas(count, t_list, alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
                game.lair.treasury.receive_treasures(trs)
                game.dragon.reputation.points += 5
            'Inside the dragon finds stocks of precious golden metal, smelted and ready for shipment to a treasury:'
            '[trs_descrptn]'
            '[game.dragon.reputation.gain_description]'
            
        'Let them be' if game.dragon.bloodiness < 5:
            'Human gold is not worth a sword in the throat!'       
            $ game.dragon.gain_rage()
            
    return

label lb_enc_mines_mithril:
    python:
        game.foe = Enemy('dwarf_guards', game_ref=game)
        chances = show_chances(game.foe)
    'A dwarven mine, where they get their precious mithril. The entrance to the mine is well protected.'
    '[chances]'
    menu:
        'Demand some mithril' if game.dragon.fear > 7:
            python:
                game.dragon.drain_energy()
                gold_trs = treasures.Ingot('mithril')
                gold_trs.weight = 4
                game.lair.treasury.receive_treasures([gold_trs])
                game.dragon.reputation.points += 1
            'The head dwarf hands over a small bar of mithril to avoid conflict.'
            '[game.dragon.reputation.gain_description]'
            
        'Take it all':
            $ game.dragon.drain_energy()
            call lb_fight
            python:
                count = random.randint(2, 10)
                alignment = 'human'
                min_cost = 1
                max_cost = 1000000
                t_list = ['mithril']
                obtained = "Pure metal."
                trs = treasures.gen_treas(count, t_list, alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
                game.lair.treasury.receive_treasures(trs)
                game.dragon.reputation.points += 3
            'In a warehouse the Dragon finds precious mithril, smelted and ready to be sold to the elves:'
            '[trs_descrptn]'
            '[game.dragon.reputation.gain_description]'
            
        'Let them be' if game.dragon.bloodiness < 5:
            'Dwarven mithril is not worth a steel bolt in the eye!'       
            $ game.dragon.gain_rage()
            
    return

label lb_enc_mines_adamantine:
    python:
        game.foe = Enemy('golem', game_ref=game)
        chances = show_chances(game.foe)
    'A dwarven mine, where they extract precious adamantine. On guard is a virtually invulnerable steel golem.'
    '[chances]'
    menu:
        'Demand some adamantine' if game.dragon.fear > 8:
            python:
                game.dragon.drain_energy()
                gold_trs = treasures.Ingot('adamantine')
                gold_trs.weight = 4
                game.lair.treasury.receive_treasures([gold_trs])
                game.dragon.reputation.points += 1
            'The chief dwarf hands over a small bar of adamantine to avoid conflict.'
            '[game.dragon.reputation.gain_description]'
            
        'Take it all':
            $ game.dragon.drain_energy()
            call lb_fight
            python:
                count = random.randint(1, 5)
                alignment = 'human'
                min_cost = 1
                max_cost = 1000000
                t_list = ['adamantine']
                obtained = "Pure metal."
                trs = treasures.gen_treas(count, t_list, alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
                game.lair.treasury.receive_treasures(trs)
                game.dragon.reputation.points += 3
            'Inside the dragon finds stocks of precious metal, melted and ready for sale to the elves:'
            '[trs_descrptn]'
            '[game.dragon.reputation.gain_description]'
            
        'Leave them be' if game.dragon.bloodiness < 5:
            'Dwarven adamantine is not worth dying by steel!'       
            $ game.dragon.gain_rage()
    return


label lb_enc_mines_gem_low:
    python:
        game.foe = Enemy('xbow', game_ref=game)
        chances = show_chances(game.foe)
    'On a mountain slope a mine entrance is visible. Judging from the smell, semi-precious stones are mined here. The entrance is guarded by a small detachment of crossbowmen.'
    '[chances]'
    
    menu:
        'Demand some gems' if game.dragon.fear > 2:
            python:
                game.dragon.drain_energy()
                count = 1
                alignment = 'human'
                min_cost = 1
                max_cost = 1000000
                t_list = ['jasper', 'turquoise', 'jade', 'malachite', 'coral', 'agate', 'amber', 'crystal', 'beryll', 'tigereye', 'granite', 'tourmaline', 'aqua']
                obtained = "Simply gems."
                trs = treasures.gen_treas(count, t_list, alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
                game.lair.treasury.receive_treasures(trs)
                game.dragon.reputation.points += 1
            'The head of the mine hands over something to appease the dragon:'
            '[trs_descrptn]'
            '[game.dragon.reputation.gain_description]'
            
        'Take it all':
            $ game.dragon.drain_energy()
            call lb_fight
            python:
                count = random.randint(5, 20)
                alignment = 'human'
                min_cost = 1
                max_cost = 1000000
                t_list = ['jasper', 'turquoise', 'jade', 'malachite', 'coral', 'agate', 'amber', 'crystal', 'beryll', 'tigereye', 'granite', 'tourmaline', 'aqua']
                obtained = "Simply gems."
                trs = treasures.gen_treas(count, t_list, alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
                game.lair.treasury.receive_treasures(trs)
                game.dragon.reputation.points += 3
            'Inside the Dragon finds gems of many different colors, shapes and sizes:'
            '[trs_descrptn]'
            '[game.dragon.reputation.gain_description]'
            
        'Let them be' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            
    return

label lb_enc_mines_gem_high:
    python:
        game.foe = Enemy('heavy_infantry', game_ref=game)
        chances = show_chances(game.foe)
    'On a mountain slope a mine entrance is visible. Judging from the smell, gems are mined here of very high quality. Already the dragon drools. But the entrance is guarded by a detachment of heavy infantry.'
    '[chances]'
    
    menu:
        'Demand some gems' if game.dragon.fear > 5:
            python:
                game.dragon.drain_energy()
                count = 1
                alignment = 'human'
                min_cost = 1
                max_cost = 1000000
                t_list = ['elven_beryll', 'topaz', 'sapphire', 'ruby', 'emerald', 'goodruby', 'goodemerald', 'star', 'diamond', 'black_diamond', 'rose_diamond']
                obtained = "Simply gems."
                trs = treasures.gen_treas(count, t_list, alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
                game.lair.treasury.receive_treasures(trs)
                game.dragon.reputation.points += 3
            'The head of the mine hands over something to appease the dragon:'
            '[trs_descrptn]'
            '[game.dragon.reputation.gain_description]'
            
        'Take it all':
            $ game.dragon.drain_energy()
            call lb_fight
            python:
                count = random.randint(3, 10)
                alignment = 'human'
                min_cost = 1
                max_cost = 1000000
                t_list = ['elven_beryll', 'topaz', 'sapphire', 'ruby', 'emerald', 'goodruby', 'goodemerald', 'star', 'diamond', 'black_diamond', 'rose_diamond']
                obtained = "Simply gems."
                trs = treasures.gen_treas(count, t_list, alignment, min_cost, max_cost, obtained)
                trs_list = game.lair.treasury.treasures_description(trs)
                trs_descrptn = '\n'.join(trs_list)
                game.lair.treasury.receive_treasures(trs)
                game.dragon.reputation.points += 5
            'Inside the Dragon finds gems of many different colors, shapes and sizes:'
            '[trs_descrptn]'
            '[game.dragon.reputation.gain_description]'
            
        'Let them be' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
    return
        
label lb_enc_frontgates_found:
    $ game.dragon.add_special_place('frontgates', 'frontgates_guarded')
    'Wandering through the mountain peaks, [game.dragon.fullname] came across...'
    show expression 'img/bg/special/gates_dwarf.jpg' as bg
    'the gates to a dwarven kingdom!'
    call lb_frontgates
    return
    
label lb_enc_cannontower:
    $ game.foe = Enemy('steamgun', game_ref=game)
    'On the mountainside, as if growing directly from the rock, is a small but fortified tower. Judging by the smell, the inside is full of dwarves and their mechanisms.'

    menu:
        'Sneak a peek':
            'Through the firing slits dwarves are seen running around. They are preparing a steam cannon...why?'
            show expression 'img/scene/fight/steamgun.jpg' as bg
            'Ah! They\'re going to shoot me!'
            $ game.dragon.drain_energy()
            call lb_fight
            'Inside the bastion there is no treasure, only armaments, supplies, and documents. There was a deep passage into a mountain kingdom, but after realizing the battle was lost, the dwarves set off a gunpowder charge, bringing down tons of stone. Nobody can get through that blockage.'
            menu:
                'Decipher the papers':
                    'The bulk of the material is a variety of technical schematics, as well as invoices for ammunition and provisions. But in addition there are some very amusing architectural plans. According to this data, in addition to the fortified main gate and cannon bunkers, the dwarven kingdom has one more little disguised and guarded "backdoor". As needed it can be "spread open"... ' #Originally read " в подгорное царство есть ещё один почти не охраняемый но замаскированный "задний проход". При случае можно будет его "раздраконить"..."
                    $ game.dragon.add_special_place('backdor', 'backdor_open')
                    
                'Leave':
                    $ game.dragon.gain_rage()
                            
        'Flee' if game.dragon.bloodiness < 5:
            $ game.dragon.gain_rage()
            
    return
    
label lb_patrool_mountain:
    python:
        chance = random.randint(0, game.mobilization.level)
        if chance < 4:
            patrool = 'jagger'
            dtxt = 'In a valley overgrown with low shrubs, %s runs into an ambush by patrolling mountain rangers.' % game.dragon.name
        elif chance < 7:
            patrool = 'footman'
            dtxt = 'On the pass %s is suddenly faced by a detachment of well-armed infantry in an organized formation.' % game.dragon.name
        elif chance < 11:
            patrool = 'heavy_infantry'
            dtxt = '%s gets caught in a cunning trap and covered in a vast net of thick rope. Such a net will not hold a dragon for long, but around the bend come the sound of loud horns and heavy infantry on the move.' % game.dragon.name
        elif chance < 16:
            patrool = 'griffin_rider'
            dtxt = '%s hears a loud echo reflecting off the mountain slope. A griffon swoops down from the sky, an armed rider on its back!' % game.dragon.name
        else:
            patrool = 'angel'
            dtxt = '%s is forced to close his eyes against a bright glare. A loud voice announces: "Die, vile offspring of sin!" This guardian angel was sent from heaven to protect the people.' % game.dragon.name
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
