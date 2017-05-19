# coding=utf-8
#proofread
label lb_event_thief_spawn(thief):
    show expression "img/scene/thief.jpg" as bg
    nvl clear
    "[thief.title] known as [game.thief.name] is going to pilfer some trinkets from the great dragon treasury!"
    nvl clear
    thief "These riches will be mine!"
    return

label lb_event_thief_steal_items(thief, items):
    $ descriptions = "\n".join(game.lair.treasury.treasures_description(items))
    show expression "img/scene/loot.jpg" as bg
    nvl clear
    "[game.thief.name] steals: [descriptions]"
    thief "I got it! I barely made it out, but now I can live like a king for the rest of my life!"
    nvl clear
    return

label lb_event_thief_lair_unreachable(thief):
    nvl clear    
    thief "Fucking [game.dragon.kind], couldn\'t you make your lair somewhere easier to reach? How am I supposed to get up there?"
    return

label lb_event_thief_prepare(thief):
    # nvl clear    
    # thief "To make it out alive and rich, I need to prepare."
    return

label lb_event_thief_prepare_usefull(thief):
    nvl clear    
    thief "Hehe...just as I planned." #planovyy means planned
    return

label lb_event_thief_receive_item(thief, item):
    show expression "img/scene/quest_thief.jpg" as bg
    nvl clear
    "[game.thief.name] is carefully preparing for the heist. His latest acquisition: [item.name]"
    thief "This will be useful."
    nvl clear
    return

label lb_event_thief_prepare_useless(thief):
    nvl clear
    show expression "img/scene/quest_thief.jpg" as bg
    '[game.thief.name] searches for the dragon\'s lair without success'
    thief "Where is this bastard hiding... shit!"
    return

label lb_event_thief_lair_enter(thief):
    nvl clear
    show expression "img/scene/thief_in_lair.jpg" as bg
    thief "There it is, the dragon's lair. I'll go in like a shadow, and slip out the back with a bag of treasure as heavy as my sins." 
    return

label lb_event_thief_die_inaccessability(thief):
    "[thief.title] [game.thief.name] could not even get into the lair - the fortifications were too strong."
    thief 'Damned [game.dragon.kind], entrenched better than a dwarven king. Walls, ditches, shutters, grilles, and locks. I don\'t see a single weak point. Too tough for me.'
    return

label lb_event_thief_die_trap(thief, trap):
    nvl clear    
    show expression "img/scene/thief_in_lair.jpg" as bg    
    $ txt = game.interpolate(random.choice(data.lair_upgrades[trap].fail))
    '[txt]' 
    return

label lb_event_thief_pass_trap(thief, trap):
    if config.debug:
        'pass_trap [trap]'
    show expression "img/scene/thief_in_lair.jpg" as bg    
    $ txt = game.interpolate(random.choice(data.lair_upgrades[trap].success))
    '[txt]' 
    return

label lb_event_thief_receive_no_item(thief):
    nvl clear    
    show expression "img/scene/thief_in_lair.jpg" as bg    
    "The thief finds nothing."
    return
    
# @Review: Alex: Added a bunch of new events to fill in the gaps:
label lb_event_thief_checking_accessability(thief):
    # Checking if thief can get past layer defences:
    # Debug message: thief(u"checking accessibility")
    return
    
label lb_event_thief_checking_accessability_success(thief):
    # Thief can gain access:
    # Debug message: thief(u"I can get into the Lair!")
    return
    
label lb_event_thief_trying_to_avoid_traps_and_guards(thief):
    # Thief is trying to avoid traps and guards:
    # Debug message: thief(u"I try to get around the traps and gaurds")
    return
    
label lb_event_thief_retreat_and_try_next_year(thief):
    # Could not get past traps and guards but did not die either:
    # Debug message: thief(u"Ниосилить, попробую в следущем году")
    thief "I can\'t get through...I have to plan this better. I won\'t give up!" #Translator: a word didn't translate. "it's necessary to prepare крутовато better".  
    return
    
label lb_event_thief_starting_to_rob_the_lair(thief):
    # Got past all traps and guards, thief is starting to rob the lair:
    # Debug message: thief(u"Начинаю вычищать логово")
    show expression "img/scene/loot.jpg" as bg    
    thief "Ooh! What a treasure trove. I have to choose the most valuable items..." #Translator: can't translate stuff. #And [game.dragon.kind], зараза прямо на золоте лежит... Ничего, я аккуратненько... надо только выбрать вещи поценнее."
    return

label lb_event_thief_took_an_item(thief, item):
    # Got an item!
    # Debug message: thief(u"Взял шмотку %s" % stolen_items[i])
    # show expression "img/scene/loot.jpg" as bg    
    # "[game.thief.name] gently pulls a prized object from under the dragon\'s belly:"
    # "[item]"
    return
    
label lb_event_thief_lair_empty(thief):
    # There were no treasures in the lair:
    # Debug message: thief(u"В сокровищнице нечего брать. Сваливаю.")
    show expression "img/scene/thief_in_lair.jpg" as bg        
    thief "Nothing else to take... damn it, I thought dragons were richer. Time to blow this joint."
    return
    
label lb_event_thief_awakened_dragon(thief, stolen_items):
    # Thief awakens the dragon and gets killed... stolen_items: items that dragon takes back from the thief.
    # Debug message: thief(u"Разбудил дракона")
    show expression "img/scene/wokeup.jpg" as bg    
    "The thief disturbs a pile of coins, which roll down clattering on the floor"
    thief "Oops..."
    game.dragon "Well, well...what a meeting. I think I know what you\'re here for." 
    nvl clear
    "[game.dragon.fullname] tears the unlucky robber to ribbons, and having had a bite to eat, goes back to bed."
    return