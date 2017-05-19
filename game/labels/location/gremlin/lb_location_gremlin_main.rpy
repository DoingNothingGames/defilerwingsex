# coding=utf-8
#Proofread and spellchecked
label lb_location_gremlin_main:
    python:
        if not renpy.music.is_playing():
            renpy.music.play(get_random_files('mus/ambient'))
    $ place = 'gremlins'
    hide bg
    show place as bg
        
    # Стоимость года работы гремлинов-слуг
    $ servant_cost = data.lair_upgrades['gremlin_servant']['cost']
    # Стоимость установки механических ловушек
    $ mechanic_traps_cost = 500
    # Стоимость строительства укреплений
    $ fortification_cost = 1000
    nvl clear
        
    menu:
        'Hire the servants' if 'servant' not in game.lair.upgrades and 'gremlin_servant' not in game.lair.upgrades:
            "Gremlins will serve in the den, keeping an eye on the captives for just [servant_cost] farthings per year."
            menu:
                "Promise to pay" if servant_cost <= game.lair.treasury.wealth:
                    $ game.lair.upgrades.add('gremlin_servant', deepcopy(data.lair_upgrades['gremlin_servant']))
                    "Gremlins obey {s}treasure{/s} their master. They will take care of the captives, and won\'t sleep on the job."
                "Go back":
                    $ pass
        'Install lair traps' if (not game.lair.type.provide or 'mechanic_traps' not in game.lair.type.provide) and 'mechanic_traps' not in game.lair.upgrades:
            menu:
                "Cost of traps: [mechanic_traps_cost] farthings."
                "Install traps" if mechanic_traps_cost <= game.lair.treasury.money:
                    $ game.lair.upgrades.add('mechanic_traps', deepcopy(data.lair_upgrades['mechanic_traps']))
                    $ game.lair.treasury.money -= mechanic_traps_cost
                    'Now things will be very difficult for thieves. But after a thief is caught, the traps must be reinstalled.'
                "Go back":
                    $ pass
        'Fortify lair' if 'gremlin_fortification' not in game.lair.upgrades:
            menu:
                "Cost to construct fortifications: [fortification_cost] farthings."
                "Reinforce lair" if fortification_cost <= game.lair.treasury.money:
                    $ game.lair.upgrades.add('gremlin_fortification', deepcopy(data.lair_upgrades['gremlin_fortification']))
                    $ game.lair.treasury.money -= fortification_cost
                    'The gremlins strengthen the walls and set grilles and doors with cunning locks. Thieves shall not pass!'
                "Go back":
                    $ pass
        'Make jewelry':
            $ new_item = game.lair.treasury.craft(**data.craft_options['gremlin'])
            if new_item:
                $ game.lair.treasury.receive_treasures([new_item])
                $ test_description = new_item.description()
                "Manufactured: [test_description]."
        'Go away':
            return
        
    jump lb_location_gremlin_main