# coding=utf-8
#checked, proofread
label lb_event_knight_spawn(knight):
    scene
    show expression "img/scene/oath.jpg" as bg
    nvl clear
    "[knight.title] pledges a sacred vow to kill a dragon!"
    knight "Prepare yourself, fiend, I am coming for you!"
    return

label lb_event_knight_receive_item(knight, item):
    scene
    show expression "img/scene/quest_knight.jpg" as bg
    nvl clear
    "Knight performs a quest and receives [item.name]"
    knight "Now the dragon will have no escape from my vengeance!"
    return

label lb_event_knight_challenge_start(knight):
    scene
    show expression "img/scene/quest_knight.jpg" as bg
    nvl clear
    $ game.foe = knight
    "[knight.title] has found the lair where [game.dragon.name] [game.dragon.surname] sleeps! He will call it out to fight."
    knight "Come forth, sneaking [game.dragon.kind]! Give an honest battle!!!"
    $ narrator(knight.intro % game.format_data)
    $ narrator(show_chances(knight))  #TODO: danger level of battle
    menu:
        "Protect your lair":
            "You enter into combat"
            return True
        "Flee and abandon your lair":
            # Here we should check the chance to escape the lair. (No, it's not necessary, escape should always succeed. Losing gold, women, etc is enough. - OH)
            if random.choice(range(4)) in range(3): # 75% chance knight continues
                knight "I will find you!"
                return False
            else:
                knight "Cowardly [game.dragon.kind], such an enemy is not worthy of my efforts."
                return False

label lb_event_knight_challenge_end(knight, result):
    if result in ["defeat", "retreat"]:
        "The dragon was defeated by the valiant knight."
    if result in ["win"]:
        "The dragon ripped the knight to shreds."