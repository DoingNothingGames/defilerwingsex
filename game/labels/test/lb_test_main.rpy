# coding=utf-8
init python:
    from pythoncode import girls_data

label lb_test_main:
    nvl clear
    while True:
        menu:
            "Summary":
                python hide:
                    tmp = "Mobilization level: [game.mobilization.level]"
                    tmp += "\nPoverty level: [game.poverty.value]"
                    tmp += "\nInfamy level/level: [game.dragon.reputation.points]/[game.dragon.reputation.level]"
                    tmp += "\nDragon level: [game.dragon.level]"
                    tmp += "\nDragon attack power:"
                    for type in data.attack_types:
                        tmp += "\n  %s: %s" % (str(type), str(game.dragon.attack()[type]))
                    tmp += "\nDragon defense power:"
                    for type in data.protection_types:
                        tmp += "\n  %s: %s" % (str(type), str(game.dragon.protection()[type]))
                    tmp += "\n Army of darkness:"
                    tmp += "\n  Grunts: [game.army.grunts]. [game.army.grunts_list]"
                    tmp += "\n  Elites: [game.army.elites]. [game.army.elites_list]"
                    tmp += "\n  Diversity: [game.army.diversity]. "
                    tmp += "\n  Money: [game.army.money]. Equipment: [game.army.equipment]"
                    tmp += "\n  Force: [game.army.force] Power percentage: [game.army.power_percentage] %)."
                    narrator(tmp)
                return
            "Debugging":
                call lb_test_debug from _call_lb_test_debug
            "Achievements":
                call lb_achievements_list from _call_lb_achievements_list
            "Reset achievements":
                python:
                    for a in persistent.achievements.keys():
                        persistent.achievements.__delitem__(a)
                "Achievement list cleared"
            "Back":
                return
    return
    
label lb_test_debug:
    nvl clear
    menu:
        "Debugging"
        "Enabling debug output":
            $ config.debug = True
        "Kingdom":
            menu:
                "Increase mobilization":
                    $ game.mobilization.level += 1
                "Decrease mobilization":
                    $ game.mobilization.level -= 1
                "Increase poverty":
                    $ game.poverty.value += 1
                "Decrease poverty":
                    $ game.poverty.value -= 1
                "Weaken Army of Darkness":
                    $ game.army.power_percentage -= 10
        "Dragon":
            while True:
                menu:
                    "Lose a point of health":
                        $ game.dragon.struck()
                    "Add a point of health" if game.dragon.health < 2:
                        $ game.dragon.health += 1
                    "Spend one energy":
                        $ res = game.dragon.drain_energy()
                        if res:
                            game.dragon "Strength left me."
                        else:
                            game.dragon "I\'m already exhausted..."
                    "Add one energy" if game.dragon._tiredness > 0:
                        $ game.dragon._tiredness -= 1
                    "Dragon type":
                        python hide:
                            head_menu = []
                            for head_type in data.dragon_heads.iterkeys():
                                head_menu.append((data.heads_name_rus[head_type], head_type))
                            game.dragon.heads[0] = renpy.display_menu(head_menu)
                    "Add a head":
                        $ game.dragon.heads.append('green')
                        game.dragon "I gained one more head."
                    "Paint a head" if 'green' in game.dragon.heads:
                        python hide:
                            head_colors = []
                            for color in game.dragon.available_head_colors:
                                head_colors.append((data.heads_name_rus[color], color))
                            color = menu(head_colors)
                            game.dragon.heads[game.dragon.heads.index('green')] = color
                    "Add a feature" if len(game.dragon.available_features) > 0:
                        python hide:
                            special_features = []
                            if game.dragon.size < 6:  # TODO: magic number!
                                special_features.append(("Increase the size of a category", 'size'))
                            if game.dragon.paws < 3:  # TODO: magic number!
                                special_features.append(("paws", 'paws'))
                            if game.dragon.wings < 3:  # TODO: magic number!
                                special_features.append(("wings", 'wings'))
                            for feature in game.dragon.available_features:
                                special_features.append((data.special_features_rus[feature], feature))
                            special_features.append(("cunning", 'cunning'))
                            feature = renpy.display_menu(special_features)
                            game.dragon.anatomy.append(feature)
                    "Cast a spell":
                        python hide:
                            spells = []
                            available_spell = [spell for spell in data.spell_list_rus if spell not in game.dragon.spells]
                            for spell in available_spell:
                                spells.append((data.spell_list_rus[spell], spell))
                            spell = menu(spells)
                            game.dragon.add_effect(spell)
                    "Create new offspring":
                        call lb_choose_dragon from _call_lb_choose_dragon_3
                    "Go back":
                        return
        "Lair":
            while True:
                menu:
                    "Create lair":
                        call lb_test_debug_create_lair from _call_lb_test_debug_create_lair
                    "Describe lair":
                        nvl clear
                        python hide:
                            lair_description = u"Lair: %s.\n" % game.lair.type.name
                            if len(game.lair.upgrades) > 0:
                                lair_description += u"Improvements:\n"
                                for upgrade in game.lair.upgrades.values():
                                    lair_description += u" %s\n" % upgrade.name
                            else:
                                lair_description += u"No improvements."
                            narrator(lair_description)
                    "Add improvement":
                        python hide:
                            upgrades_available = [(data.lair_upgrades[u].name, u) for u in data.lair_upgrades if u not in game.lair.upgrades]
                            upg = menu(upgrades_available)
                            game.lair.add_upgrade(upg)

                    "Debug treasure trove":
                        call lb_test_debug_treasury from _call_lb_test_debug_treasury
                    "Add a girl":
                        python hide:
                            from pythoncode import treasures
                            girls_menu = []
                            for girl_type in girls_data.girls_info.keys():
                                girl_type_name = girls_data.girls_info[girl_type]['description']
                                girls_menu.append((girl_type_name, girl_type))
                            girl_type = renpy.display_menu(girls_menu)
                            game.girls_list.new_girl(girl_type)
                            game.girls_list.jail_girl()
                    "Edit gems in the treasury":
                        call screen sc_treasury_gems
                    "Edit thief items":
                        call screen sc_container_editor(game.lair.treasury.thief_items, [data.thief_items, data.thief_items_cursed])
                    "Make a thief come to rob" if game.thief is not None and game.thief.is_alive:
                            $ game.thief.steal(lair=game.lair, dragon=game.dragon)
                    "go back":
                        return
        "Thief":
            menu:
                "(Re)create a thief (in game)":
                    $ game._create_thief()
                "Create a thief of a certain level":
                    python hide:
                        lvls = []
                        for i in data.thief_titles:
                            lvls.append((i, data.thief_titles.index(i) + 1))
                        thief_lvl = menu(lvls)
                        game._create_thief(thief_level=thief_lvl)
                "Describe thief" if game.thief is not None:
                    $ narrator(game.thief.description())
                "Edit thief skills" if game.thief is not None:
                    call screen sc_container_editor(game.thief.abilities, [data.thief_abilities])
                "Edit thief items" if game.thief is not None:
                    call screen sc_container_editor(game.thief.items, [data.thief_items, data.thief_items_cursed])
                "Make a thief come to rob" if game.thief is not None and game.thief.is_alive:
                    $ game.thief.steal(lair=game.lair, dragon=game.dragon)
        "Knight":
            menu:
                "(Re)create a knight (in game)":
                    $ game._create_knight()
                "Create a knight of a certain level":
                    python hide:
                        lvls = []
                        for i in data.knight_titles:
                            lvls.append((i, data.knight_titles.index(i) + 1))
                        knight_lvl = menu(lvls)
                        game._create_knight(knight_level=knight_lvl)
                "Describe knight" if game.knight is not None:
                    $ narrator(game.knight.description())
                "Edit knight skills" if game.knight is not None:
                    call screen sc_container_editor(game.knight.abilities, [data.knight_abilities])
                "Edit knight items" if game.knight is not None:
                    call screen sc_equip_editor(game.knight, [data.knight_items])
                "Have knight call the dragon to battle" if game.knight is not None:
                    $ game.knight.go_challenge()
                "Force the knight to fight the dragon" if game.knight is not None:
                    $ game.knight.forced_to_challenge = True
        "Stop saving":
            menu:
                "Plot game save":
                    $ renpy.unlink_save("1-1")
                    "Canceled story game save!"
                "Free game save":
                    $ renpy.unlink_save("1-3")
                    "Canceled free mode save!"
                "Go back":
                    pass
    return

label lb_test_debug_create_lair:
    python:
        menu_options = []
        for a in data.lair_types:
            menu_options.append((data.lair_types[a].name, a, True, True))
        type = renpy.call_screen("dw_choice", menu_options)
        game.create_lair(type)
    return
    
    
label lb_test_debug_treasury:  
    while True: 
        menu:
            "Add money":
                "Value of treasury: [game.lair.treasury.wealth]"
                $ treasure_list = treasures.gen_treas(10, ['farthing', 'farthing', 'dubloon'], 'elf', 1, 1000, "")
                $ game.lair.treasury.receive_treasures(treasure_list)
                $ treasure_list = game.lair.treasury.treasures_description(treasure_list)
                $ treasure_list = '\n'.join(treasure_list)
                "List of coins added:\n[treasure_list]"
                "Value of treasury after adding: [game.lair.treasury.wealth]"
            "Add bars":
                "Value of treasury: [game.lair.treasury.wealth]"
                $ test_list = treasures.gen_treas(10, ["silver", "gold", "mithril", "adamantine"], 'elf', 1, 1000000, "")
                $ treasure_list = game.lair.treasury.treasures_description(test_list)
                $ treasure_list = '\n'.join(treasure_list)
                "List of bars added:\n[treasure_list]"
                $ game.lair.treasury.receive_treasures(test_list)
                "Value of treasury after adding: [game.lair.treasury.wealth]"
            "Add materials":
                "Value of treasury: [game.lair.treasury.wealth]"
                $ test_list = treasures.gen_treas(10, treasures.material_types.keys(), 'elf', 1, 1000000, "")
                $ treasure_list = game.lair.treasury.treasures_description(test_list)
                $ treasure_list = '\n'.join(treasure_list)
                "List of materials added:\n[treasure_list]"
                $ game.lair.treasury.receive_treasures(test_list)
                "Value of treasury after adding: [game.lair.treasury.wealth]"
            "Add gems":
                "Value of treasury: [game.lair.treasury.wealth]"
                $ test_list = treasures.gen_treas(10, treasures.gem_types.keys(), 'elf', 1, 1000000, "")
                $ treasure_list = game.lair.treasury.treasures_description(test_list)
                $ treasure_list = '\n'.join(treasure_list)
                "List of gems added:\n[treasure_list]"
                $ game.lair.treasury.receive_treasures(test_list)
                "Value of treasury after adding: [game.lair.treasury.wealth]"
            "Add treasures":
                "Value of treasury: [game.lair.treasury.wealth]"
                $ test_list = treasures.gen_treas(10, treasures.treasure_types.keys(), 'elf', 1, 1000000, "")
                $ treasure_list = game.lair.treasury.treasures_description(test_list)
                $ treasure_list = '\n'.join(treasure_list)
                "List of treasures added:\n[treasure_list]"
                $ game.lair.treasury.receive_treasures(test_list)
                "Value of treasury after adding: [game.lair.treasury.wealth]"
            "Robbery":
                "Value of treasury: [game.lair.treasury.wealth]"
                $ abducted_list = game.lair.treasury.rob_treasury(10)
                $ abducted_list = game.lair.treasury.treasures_description(abducted_list)
                $ abducted_list = '\n'.join(abducted_list)
                "Things taken: [abducted_list]"
                "Value of treasury afterwards: [game.lair.treasury.wealth]"
            "Go back":
                return
    return

