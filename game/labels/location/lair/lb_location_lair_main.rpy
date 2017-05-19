# coding=utf-8
#spellchecked and proofread

init python:
    import random
    
    from pythoncode import utils
    
label lb_location_lair_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))    
    $ place = game.lair.type_name
    hide bg
    show place as bg
    nvl clear
    
    menu:
        'Look in the mirror':
            # чтобы вывести сообщение от имени дракона можно использовать "game.dragon"
            game.dragon.third "{font=fonts/AnticvarShadow.ttf}{size=+5} [game.dragon.fullname] {/size}{/font} \n\n[game.dragon.description]"
            
        'Inspect your lair':
            python hide:
                lair_description = u"Lair: %s.\n" % game.lair.type.name
                if len(game.lair.upgrades) > 0: 
                    lair_description += u"Improvements:\n"
                    for upgrade in game.lair.upgrades.values():   
                        lair_description += u" %s\n" % upgrade.name
                else:
                    lair_description += u"There are no improvements."
                narrator(lair_description)
            
        'Conjure a foul spell' if game.dragon.bloodiness < 5 and game.dragon.mana > 0:
            python:
                if game.choose_spell(u"Return to den"):
                    game.dragon.drain_mana()
                    game.dragon.gain_rage()
                    
        'Admire treasures' if game.lair.treasury.wealth > 0:
            call lb_location_lair_treasures
            
        'Admire hostages' if game.girls_list.prisoners_count > 0:
            call lb_location_lair_girls
            
        'Make jewelry' if ('servant' in game.lair.upgrades) or ('gremlin_servant' in game.lair.upgrades):
            $ new_item = game.lair.treasury.craft(**data.craft_options['servant'])
            if new_item:
                $ game.lair.treasury.receive_treasures([new_item])
                $ test_description = new_item.description()
                "Manufactured: [test_description]."
            
        'Fire the gremlins' if 'gremlin_servant' in game.lair.upgrades:
            $ del game.lair.upgrades['gremlin_servant']
            "The gremlins leave"
            
        'Fire the mercenary guards' if 'smuggler_guards' in game.lair.upgrades:
            $ del game.lair.upgrades['smuggler_guards']
            "The guards leave their posts"
            
        'Go into a deep slumber':
            nvl clear
            python:
                # Делаем хитрую штуку.
                # Используем переменную game_loaded чтобы определить была ли игра загружена.
                # Но ставим ее перед самым сохранинием, используя renpy.retain_after_load() для того
                # чтобы она попала в сохранение.
                if 'game_loaded' in locals() and game_loaded:
                    del game_loaded
                    game.narrator("game loaded")
                    renpy.restart_interaction()
                else:
                    game_loaded = True
                    renpy.retain_after_load()
                    if not freeplay:
                        utils.call ("lb_achievement_acquired")
                        game.save()
                    else:
                        game.save_freegame()
                    save_blocked = True
                    
                    game.sleep()
                    save_blocked = False
                    del game_loaded
                this_turn_achievements = []
            return
            
        'Go out':
            return
            
    jump lb_location_lair_main
    
label lb_location_lair_treasures:
    python:
        files = [f for f in renpy.list_files() if f.startswith("img/bg/hoard/%s" % game.dragon.color_eng)]    
        if len(files) > 0:
            treasurybg = random.choice(files)
        else:
            treasurybg = "img/bg/hoard/base.jpg"
        renpy.treasurybg = ui.image(treasurybg)
            
    show image renpy.treasurybg as bg
    nvl clear
    
    menu:
        '[game.lair.treasury.wealth_description]'
        
        '[game.lair.treasury.gems_mass_description]' if game.lair.treasury.gem_mass > 0:
            "[game.lair.treasury.gems_list]"
            nvl clear
            
        '[game.lair.treasury.materials_mass_description]' if game.lair.treasury.metal_mass + game.lair.treasury.material_mass > 0:
            "[game.lair.treasury.materials_list]"
            nvl clear
            
        '[game.lair.treasury.coin_mass_description]' if game.lair.treasury.coin_mass > 0:
            $ description = u"The treasure:\n"
            if game.lair.treasury.farthing > 0:
                $ description += u"%d farthing%s\n" % (game.lair.treasury.farthing,treasures.number_pluralizer(game.lair.treasury.farthing))
            if game.lair.treasury.taller > 0:
                $ description += u"%d taller%s\n" % (game.lair.treasury.taller, treasures.number_pluralizer(game.lair.treasury.taller))
            if game.lair.treasury.dubloon > 0:
                $ description += u"%d dubloon%s" % (game.lair.treasury.dubloon, treasures.number_pluralizer(game.lair.treasury.dubloon))
            "[description]"
            nvl clear
            
        '[game.lair.treasury.jewelry_mass_description]' if len(game.lair.treasury.jewelry) > 0:
            menu:
                'Most valuable piece':
                    "[game.lair.treasury.most_expensive_jewelry]"
                    nvl clear
                    
                'Cheapest trinket':
                    "[game.lair.treasury.cheapest_jewelry]"
                    nvl clear
                    
                'A random treasure':
                    "[game.lair.treasury.random_jewelry]"
                    nvl clear
                    
                'Back':
                    $ pass
        'Back':
            $ pass
    return
    
label lb_location_lair_girls:
    call screen girls_menu
    if _return:
        call lb_lair_sex
        if game.girls_list.prisoners_count > 0:
            jump lb_location_lair_girls
            
    hide screen girls_menu
    return
