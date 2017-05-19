# coding=utf-8
# Here we keep long game texts
#spell checked and mostly proofread 
python early:
    from pythoncode import data
     
    chance_win_texts = {
        0: "{color=#ff0000}miserable{/color}",
        10: "{color=#ff00ff}low{/color}",
        30: "{color=#0000ff}acceptable{/color}",
        60: "{color=#EAC117}good{/color}",
        90: "{color=#00ff00}splendid{/color}"
    }
    
    chance_wound_texts = {
        0: "{color=#00ff00}minimal{/color}",
        10: "{color=#EAC117}acceptable{/color}",
        30: "{color=#0000ff}average{/color}",
        60: "{color=#ff00ff}considerable{/color}",
        90: "{color=#ff0000}immense{/color}"
    }
    
    def show_chances(foe):
        """
        Вывод шансов победы и ранения дракона для игрока 
        """
        chance = battle.victory_chance(game.dragon, foe)
        chance_win = data.get_description_by_count(chance_win_texts, chance)

        chance = battle.victory_chance(foe, game.dragon)
        chance_wound = data.get_description_by_count(chance_wound_texts, chance)
        
        return " Chance to win: %s.\n Danger: %s." % (chance_win, chance_wound)

    # Описания дракона
    hunger_texts = {
        0: '{font=fonts/AnticvarShadow.ttf}{color=#ff0000}Overfed{/color}{/font}',
        1: '{font=fonts/AnticvarShadow.ttf}{color=#ff00ff}Full{/color}{/font}',
        2: '{font=fonts/AnticvarShadow.ttf}{color=#0000ff}Hungry{/color}{/font}',
        3: '{font=fonts/AnticvarShadow.ttf}{color=#00ff00}Starving{/color}{/font}'
    }

    lust_texts = {
        0: '{font=fonts/AnticvarShadow.ttf}{color=#ff0000}Exhausted{/color}{/font}',
        1: '{font=fonts/AnticvarShadow.ttf}{color=#ff00ff}Aroused{/color}{/font}',
        2: '{font=fonts/AnticvarShadow.ttf}{color=#0000ff}Horny{/color}{/font}',
        3: '{font=fonts/AnticvarShadow.ttf}{color=#00ff00}Lustful{/color}{/font}'
    }

    bloodlust_texts = [
        '{font=fonts/AnticvarShadow.ttf}{color=#00ff00}Placid{/color}{/font}',
        '{font=fonts/AnticvarShadow.ttf}{color=#ccccff}Calm{/color}{/font}',
        '{font=fonts/AnticvarShadow.ttf}{color=#0000ff}Tense{/color}{/font}',
        '{font=fonts/AnticvarShadow.ttf}{color=#ff00ff}Annoyed{/color}{/font}',
        '{font=fonts/AnticvarShadow.ttf}{color=#ff00ff}Angry{/color}{/font}',
        '{font=fonts/AnticvarShadow.ttf}{color=#ff0000}Furious{/color}{/font}'
    ]

    health_texts = {
        0: '{font=fonts/AnticvarShadow.ttf}{color=#ff0000}Half-dead{/color}{/font}',
        1: '{font=fonts/AnticvarShadow.ttf}{color=#ff00ff}Wounded{/color}{/font}',
        2: '{font=fonts/AnticvarShadow.ttf}{color=#00ff00}Healthy{/color}{/font}'
    }

    womennum = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
    
    # Описания эффекта события на дурную славу
    reputation_rise = [
        'People will notice this evil deed.',
        'News of the dragon\'s notorious acts spread throughout the Kingdom.',
        'Today the dragon gained great infamy.',
        'All inhabitants of the kingdom will hear about this action and be terrified.',
        'Such a terrible act will live in legends for hundreds of years.'
    ]

    # Описание деревень
    village = {
        'overview': [
            u'Abandoned settlement',
            u'A lonely farm. The people here have no protection except a large chained dog.',
            u'A small village. Seeing the approach of the dragon people grab everything at hand that can be used as a makeshift weapon, and look for safety in numbers.',
            u'A village. A ship\'s bell rings desperately as the dragon is noticed from afar. Residents quickly organize into a militia.',
            u'A large village. A church bell urges people to take cover, and a detachment of crossbowmen files onto the main street.',
            u'A town. As the dragon approaches the gates are hastily closed, and warriors armed with bows and spears rise up on the walls.'
        ],
        'deffence': [
            'dog',
            'dog',
            'mob',
            'militia',
            'xbow',
            'town',
        ]
    }

# Прыдстория игры
    intro_text = '{font=fonts/AnticvarShadow.ttf}{size=+10}    Long ago, in ancient times, the world was young and unspoiled. All five nations lived in peace and harmony, developing and prospering. Men planted endless fields of golden wheat on the plains, and blooming gardens of sweet fruit on the hills. The children of the goddess Danu, wise and beautiful elves, wove magic patterns of songs and moonlight deep in the vast forests. Skilled dwarves forged metal and cut gems that shone like stars in the shadow of their carved stone palaces. Mermaids played carelessly with silver fish and danced under the blue surface of the ocean. And even the giants, old as the world itself, did not harm the small nations, but instructed them in ancient knowledge.   {vspace=30}Those days vanished without a trace, when evil came into the world. Nobody is sure where she came from. Naked, winged, beautiful, she was as lovely as a noon daydream and as terrible as a midnight nightmare. Tradition says she came out of the milk white morning fog that thickened in the depths of an impassible windbreak. Others believe she came from the pit of hell itself.   {vspace=30} Able to take on any shape, seductive or terrifying, she brought decay and strife. In an insatiable lust she sought out everyone she could find. She craved all male seed, from proud kings to peasants and filthy animals. In unnatural unions legions of creatures were spawned, deformed and vicious, cruel, greedy, and full of sin.  {vspace=30}With fear and hatred, the Mistress of Darkness forged an army and marched it to the free nations to enslave the whole world. The ruthless army of darkness left behind only corpses, ashes, and barren earth.     {vspace=30}But the five free nations fought back. Gathering together, an army of men, elves, dwarves, mermaids, and giants defeated the dark forces and drove the Mistress\'s spawn into a barren volcanic land far to the east. Since then, to protect themselves, men have built impregnable fortress cities with high walls and towers, dwarves have created machines and engines of war, and elves have put spells of concealment on their groves and guards on their boundaries. Even carefree mermaids wield tridents and nets, ready to repel an attack.      {vspace=30}Looking at this irresistible alliance, the Mistress vowed to create a monster of such power that no one in the world could stand before it. Breathing the poisonous fumes of the southern marshes, she took up the fattest snake which she could find and set aside three large eggs, from which she hatched a monster the likes of which had never been seen before on the earth - a dragon.    {vspace=30}   All mortal sins merged into these creatures. The violent and bloodthirsty dragons know nothing of mercy and compassion. Their pride and envy makes them seek ill fame, destroying all that is beautiful and spreading suffering. In their insatiable lust they defile innocent girls, who like the Mistress give birth to more degenerate monsters. Voracious, they devour men, animals, fish and birds. Greedily they rake silver and gold into their fetid caves, hoarding treasure and sleeping it on for years, indulging in sloth and complacency.       {vspace=30}The first of the dragons were not very strong, not much more than huge swamp snakes. But Mistress repeatedly selects the best, and with incestuous, abominable intercourse generates new and constantly mutating offspring. All larger, stronger, more vicious, and more insidious. If their race is not stopped, the day will come when the highest wall and largest army cannot stand against their might. Even the god-like titans in their strongholds will not sleep easy. But for now, hope is still alive... {/size}{/font}'

     
    # Названия мест
    toptxt = {
        'plain': u'THE COUNTRYSIDE \n\n'
    }

    # Тексты для энкаунтеров
    txt_enc_fair = [
        ['%(dragon_name)s notices colorful tents in a meadow. It\'s a big fair, which has brought together all the people from surrounding villages. Here they trade, talk, and show off their best animals and most marriageable brides. Do something to make money!'],
        ['%(dragon_name)s bursts into a crowd of peasants and emits a thunderous roar. People flee in terror, but the snake does not spend time chasing them all down, he needs only one woman - the most beautiful virgin, who had hoped to find a good groom. It\'s time for her to find out who is the most eligible bachelor in this village!']
    ]

# Тексты для особых мест
    txt_place_manor = [
        ['Not far from the road is a fortified stone manor - the home of a poor knight. Inside could be some gold or a woman, so it pays to look closely.'],
        ['%(dragon_name)s sniffs. Inside there is the clear scent of a virgin of noble blood and a little treasure. But it won\'t be gotten just yet, servants have noticed the approach of the dragon and now the owner of the manor hurriedly puts on his armor. The old knight won\'t give up without a fight!'],
        ['Ignoring the terrified fleeing servants, %(dragon_name)s searches the mansion for valuables:'],
        ['In a spacious and brightly lit room on the second floor, the trembling daughter of the slain knight hides under the bed. But %(dragon_name)s can smell innocent flesh many miles away.'],
        ['The fortifications did not save the now-deserted mansion from your looting, but strong walls can serve as a good protection for a dragon\'s treasure. A small enough dragon could arrange a cozy lair in the wine cellar, you just have to squeeze through the narrow door.'],
        ['%(dragon_name)s gives a victory roar. No one else stands in his way and the knightly manor is defenseless.']
    ]

    txt_place_wooden_fort = [
        ['On a hill near the road stands a wooden fort. %(dragon_name)s decides to scout out what\'s inside.'],
        ['This wooden fort was build in the usual way - a large courtyard surrounded by a moat and palisade, dominated by the tower built on a man-made mound. The garrison consists of ordinary foot soldiers, and the owner isn\'t present. From the top floor of the tower comes the scent of a virgin.'],
        ['The resistance of the defenders is broken. Just a minute is needed to tear down the gates of the tower on the hill and burst inside. Servants flee in terror, but %(dragon_name)s pays them no attention, methodically stripping the place of everything of value:'],
        ['On the top floor of the front room, a young maiden and a old nurse woman huddle in fear in the corner. %(dragon_name_full)s smacks the old woman with a flick on the tail and turns his head to the girl.'],
        ['The wooden walls are in poor condition, but the tower on the hill still stands. In the main hall you can make a den and dump treasures, and keep captive maidens on the upper floors. Not a great place for a den, but better than a ravine or a hole in the ground.'],
        ['%(dragon_name)s gives a victory roar. No one else stands in the way, the fort on the hill is now defenseless.']
    ]
    
    txt_place_abbey = [
        ['In the distance there are walls and towers, but it\'s not a fortress - it\'s a fortified monastery. The clergy tend to collect treasures, almost like dragons. They have much more than they are able to protect, so it\'s worth a look.'],
        ['A fairly rich and well fortified convent. From inside comes the smell of gold, silver, and virgin women, but also something else...Knight Crusaders.'],
        ['The foolish nuns gathered everything of value in a single room, near the altar where they pray. %(dragon_name)s takes the church\'s loot:'],
        ['At the rear of the monastery cells are nuns. Most of them are virgins, although many are old and rotten, but here and there is a special sweet smell. Focusing on it, %(dragon_name)s finds in the farthest cell a maiden of noble blood, who took vows of chastity as a nun - but now a quite different fate awaits!'],
        ['The old convent has strong and high walls, and a large dining room spacious enough to allow for a large den, even for a dragon. It may be a good idea to settle here.'],
        ['%(dragon_name_full)s roars in victory. No one else stands in his way, and the monastery is now defenseless.']
    ]

    txt_place_castle = [
        ['%(dragon_name)s spies a huge stone fortress from afar.'],
        ['Such heavily fortified castles with high walls and towers in the kingdom are rare. The dragon\'s instincts tell him there is a treasury full of gold and precious stones, and in the high tower noble maidens are languishing. It should be entertained, but the garrison will be hard to defeat.'],
        ['The central stronghold of the castle was protected by a sturdy gate that proved hard to break. Inside are valuable treasures:'],
        ['On the top floor of the front room, a young maiden and a old nurse woman huddle in fear in the corner. %(dragon_name_full)s smacks the old woman with a flick on the tail and turns his head to the girl.'],
        ['The great stone castle has intact fortifications and many spacious rooms - an almost perfect place for the dragon\'s lair.'],
        ['%(dragon_name_full)s roars in victory. No one else stands in his way, and the mighty fortress is now defenseless.']
    ]
    
    txt_place_palace = [
        ['In the distance you can see a majestic fortified palace, this is clearly something worth attention!'],
        ['It appears that %(dragon_name)s found a royal castle. Such a mighty stronghold in the land of free people is very rare, and its owner must be a very rich lord. Of course many interesting things are inside... and a lot of protection.'],
        ['The %(dragon_type)s quickly rushes to the treasury, eagerly shovelling piles of jewelry:'],
        ['Every self respecting palace must have a princess languishing, and of course there she is, on the top floor of the tallest tower.'],
        ['This recently depopulated palace is huge and perfectly placed. If you make your lair here, people will tremble at the mere mention of the name of the dragon who was so powerful that he took it for himself!'],
        ['%(dragon_name_full)s roars in victory. No one else stands in his way, and the royal palace is now defenseless.']
    ]
    
    txt_place_enfr = [
        ['An elven castle. Bingo!'],
        ['The sacred tree of the elves, grown from a gift of the goddess Danu, is huge and immense. In its branches, under the roots and in the hollows, elves have arranged a splendid palace in which the king and queen reside. Inside reside many treasures, but a large forest guard protects this place, and will be difficult to combat.'],
        ['Elves carry their treasures on themselves, and here there are enough elves to borrow a few things from:'],
        ['%(dragon_name)s finds the Queen of the Elves.'],
        ['Now the grove is empty, but the old magic still glimmers in the trunk of the great tree, protecting the surrounding area. Here you can make a secret lair.'],
        ['%(dragon_name_full)s roars in victory. No one else stands in his way, and the elven forest palace is now defenseless.']
    ]
    
    txt_enc_forest_guardian = [
        ['%(dragon_name_full)s is wandering through the woods. Suddenly...'],
        ['A border guard with a bow appears. Elves carefully guard their sacred groves. Maybe he knows the way to the enchanted land.'],
        ['%(dragon_name)s triumphs. But trying to find the secret path that the guardian was protecting does not work...'],
        ['%(dragon_name)s cunning interrogation has revealed information about the secret paths, allowing him to enter the enchanted forest of the elves.']
    ]
    
    txt_place_jotun = [
        ['In this gigantic palace, built of blocks of ice, a frost giant - Jotun - lives in seclusion. Inside is the smell of treasure and a big woman, and this would be a great place for a lair. But the giant vigilantly guards his home.'],
        ['In the depths of the den is a frost giantess. Her womb would be an exceptional place for dragon seed.'],
        ['The ice citadel is now empty. Here you can make a perfect lair, with the protection of ice walls, steep mountains, and piercing frosty wind.']
    ]
    
    txt_place_ifrit = [
        ['Fortified forge, built of black obsidian blocks, located in the crater of an active volcano. Judging by the smell there is something valuable - but the fire giants - Ifrit - will not give up their treasures without a fight.'],
        ['The fire giantess tries to put up a fight, but she is much weaker than the male and not armed, so the Dragon can do whatever he wants with her.'],
        ['The volcanic forge of the molten giants is now empty. Here you can make a great den, because it is protected by thick walls, cliffs, and the unbearable heat of the magma lake.']
    ]

    txt_place_triton = [
        ['This is the underwater palace of Triton - the sea giant. Surely he has amassed a sizable treasure, but a giant is a serious opponent.'],
        ['In the luxuriously furnished underwater apartments, a giantess with a fish tail waits for her fate. It\'s a chance to produce mighty sea creatures!'],
        ['The mansion where the proud Triton once lived can be a good den for a water dragon. Few will be able to reach the underwater entrance.']
    ]
    
    txt_place_titan = [
        ['This island flies about the clouds thanks to the magic power of the lighting giant - Titan. The castle itself is striking in its monumental size and luxury. Surely untold riches await inside, but the Titans are one of the mightiest enemies that one can face.'],
        ['The dragon goes to the scent of a woman. According to the custom of princesses, the giantess is sitting in a room on the top of the tower. It looks like she did not even hear the sounds of the battle down below!'],
        ['This is now an empty castle, once belonging to the mighty Titan. The old magic still keeps the island in the sky, floating above the clouds. Such a spacious, durable, and unreachable structure, it is difficult to imagine a better den.']
    ]
    
    #Сцены секса с госпожой в человеческом облике
    txt_human_mistress_fuck = {}
    txt_human_mistress_fuck['dragon remains'] = ['This is an error, the current dragon is dead',]
    txt_human_mistress_fuck['serpent'] = ['Mistress descended from her throne, at the same time taking human form and a suitable size - half that of her son. So that he could feel big and strong, but at the same time do what he was there to do. \n The serpent opened his mouth and licked his lips in anticipation, he had long dreamed of this moment. Snaking forward, %(dragon_name)s crawled to his feet and wrapped around Mistress with his body, climbing higher and higher with each turn until level with the bright scarlet lips of the woman. She groaned, squeezed by his strong scaly body, and the snake immediately launched his forked tongue into her mouth. Unwrapping the coils of its tail, the serpent moved between her legs as the Mistress spread them, both thrusting together simultaneously. \n The scaly serpent squeezed hard enough to crush any mortal woman, but Mistress only moaned in pleasure as she felt her son ram his inhuman member into her wet narrow folds. This passionate mating is repeated over and over again for many days and nights, until it becomes clear that in the womb of the Mistress new dragon eggs are maturing.',]
    txt_human_mistress_fuck['lindwurm'] = ['The mistress descended from her throne and looking her son straight into the eyes said, "I\'m yours. Do what you want." Throwing off his timidity, the lizard furiously roared and lashed out at the woman he desired for so long. Knocking her down with a well-aimed blow of the tail, he pushed her head to the grown and then roughly entered into her coveted womb. Though the Mistress had no foreplay before the penetration, inside it was hot and wet. For a second the dragon thought, was she also yearning for this moment, or did she only use magic to imitate lust? But the thought quickly vanished with the pleasure of animal penetration into her fertile but hitherto forbidden womb. The rapacious lizard vowed to rape his mother again and again, until the sperm poured from her everywhere, even from her ears...',]
    txt_human_mistress_fuck['flying serpent'] = ['%(dragon_name_full)s spread his mighty wings and soared to a high ceiling of the throne room. Mistress went to the center of the room and held her hands up, calling her son for a loving embrace. The %(dragon_type)s dived at her like a hawk to its prey. The impact of bodies was so strong that the demoness fell to the ground under the weight of the serpent. Quickly he wrapped his membranous wings around her lithe body, so that nothing could be seen from outside. \n But within the leathery cocoon boiled animal passion. \n Under the wings the writhing bodies paused as the serpent gave his first discharge in the womb of his mother, but not for long. A minute later, he spread his wings, and holding her in his scaly embrace soared once again to the ceiling. \n The serpent and the woman indulged in incestuous lovemaking on the floor, in the air, on land and in water countless times, but he did not release her from his embrace until her belly was round and heavy with new ripening snakes... ',]
    txt_human_mistress_fuck['hydra'] = ['%(dragon_name_full)s crept to the foot of the throne and stretched his neck to look at the Mistress from every side. In response, she held out her hands with a smile and put them on two of his snouts, holding onto them tightly. Realizing his mother\'s idea the %(dragon_type)s rolled onto his back so that his cock pointed straight up a sharpened stake for an execution, while the demoness holding his muzzles was raised up in the air. %(dragon_name)s spread his necks sharply apart, and Mistress plunged down and was penetrated by the genitals of the beast. The two issued a cry of mixed pain and pleasure.  The %(dragon_type)s twisted the writhing witch around on his cock, and lifted her again, amazed at how deeply he had driven into such a small body.\n In this bouncing dance %(dragon_name)s and his lustful mother spent many hot nights, until her belly began to bulge from the ripening eggs of the next generation.',]
    txt_human_mistress_fuck['wyvern'] = ['Having took the form of an innocent and seductive maiden, Mistress faced the dragon and took off her clothes.  %(dragon_name_full)s grabbed her with his powerful wings, embracing her. Her hands slipped down the sharp scales of his chest, stomach, moving downwards to grope his cock.   %(dragon_name)s impatiently pushed his mother down and felt her greedily take his spine covered member into her slimy lips. Nobody would have believed that such an impressive organ would fit in such a small mouth, but the Mistress is capable of it. The proportions were made to fit within a millimeter, so that the moist pink flesh of her throat is completely filled by her son. In such a situation Mistress could neither breathe not moan, and could only stretch the muscles of her throat and move her head to enhance the pleasure of her son. \n In passionate embraces they will spend many more days and nights...',]
    txt_human_mistress_fuck['dragon'] = ['Having took the form of an innocent and seductive maiden, Mistress faced the dragon and took off her clothes.  %(dragon_name_full)s grabbed her with his powerful wings, embracing her. Her hands slipped down the sharp scales of his chest, stomach, moving downwards to grope his cock.   %(dragon_name)s impatiently pushed his mother down and felt her greedily take his spine covered member into her slimy lips. Nobody would have believed that such an impressive organ would fit in such a small mouth, but the Mistress is capable of it. The proportions were made to fit within a millimeter, so that the moist pink flesh of her throat is completely filled by her son. In such a situation Mistress could neither breathe not moan, and could only stretch the muscles of her throat and move her head to enhance the pleasure of her son. \n In passionate embraces they will spend many more days and nights...',]
    txt_human_mistress_fuck['multi headed flying serpent'] = ['%(dragon_name_full)s spread his mighty wings and soared to a high ceiling of the throne room. Mistress went to the center of the room and held her hands up, calling her son for a loving embrace. The %(dragon_type)s dived at her like a hawk to its prey. The impact of bodies was so strong that the demoness fell to the ground under the weight of the serpent. Quickly he wrapped his membranous wings around her lithe body, so that nothing could be seen from outside. \n But within the leathery cocoon boiled animal passion. \n Under the wings the writhing bodies paused as the serpent gave his first discharge in the womb of his mother, but not for long. A minute later, he spread his wings, and holding her in his scaly embrace soared once again to the ceiling. \n The serpent and the woman indulged in incestuous lovemaking on the floor, in the air, on land and in water countless times, but he did not release her from his embrace until her belly was round and heavy with new ripening snakes...',]
    txt_human_mistress_fuck['multi headed wyvern'] = ['%(dragon_name_full)s crept to the foot of the throne and stretched his neck to look at the Mistress from every side. In response, she held out her hands with a smile and put them on two of his snouts, holding onto them tightly. Realizing his mother\'s idea the %(dragon_type)s rolled onto his back so that his cock pointed straight up a sharpened stake for an execution, while the demoness holding his muzzles was raised up in the air. %(dragon_name)s spread his necks sharply apart, and Mistress plunged down and was penetrated by the genitals of the beast. The two issued a cry of mixed pain and pleasure.  The %(dragon_type)s twisted the writhing witch around on his cock, and lifted her again, amazed at how deeply he had driven into such a small body.\n In this bouncing dance %(dragon_name)s and his lustful mother spent many hot nights, until her belly began to bulge from the ripening eggs of the next generation.',]
    txt_human_mistress_fuck['multi headed dragon'] = ['%(dragon_name_full)s crept to the foot of the throne and stretched his neck to look at the Mistress from every side. In response, she held out her hands with a smile and put them on two of his snouts, holding onto them tightly. Realizing his mother\'s idea the %(dragon_type)s rolled onto his back so that his cock pointed straight up a sharpened stake for an execution, while the demoness holding his muzzles was raised up in the air. %(dragon_name)s spread his necks sharply apart, and Mistress plunged down and was penetrated by the genitals of the beast. The two issued a cry of mixed pain and pleasure.  The %(dragon_type)s twisted the writhing witch around on his cock, and lifted her again, amazed at how deeply he had driven into such a small body.\n In this bouncing dance %(dragon_name)s and his lustful mother spent many hot nights, until her belly began to bulge from the ripening eggs of the next generation.',]
    
    #Сцены секса с госпожой в драконьем облике
    txt_dragon_mistress_fuck = {}
    txt_dragon_mistress_fuck['dragon remains'] = ['Error, the current dragon is dead.',]
    txt_dragon_mistress_fuck['serpent'] = ['Mistress rose from her iron throne and moved to her son. Her body subtly twisted and stretched, taking elongated form. The two snakes stood up on their tails and began to weave around each other. %(dragon_name)s released his forked tongue, which Mistress quickly met with her own. \n Strange to human eyes, the slow writhing and all-consuming love of the two great servants lasted many days...',]
    txt_dragon_mistress_fuck['lindwurm'] = ['Mistress gripped the arms of her iron throne and %(dragon_name_full)s watched as her graceful hands and painted nails transformed into claws and scaly paws.  \n Vertical slits cut across her yellow eyes, and rattling came from her changing throat. Anyone else would run in terror at the sight, but %(dragon_name)s rushed forward to touch the only woman in the world worthy of mothering his children. \n     The two lizards attacked each other like like enemies, and the grinding of their scales shook of stained-glass windows of the great hall. %(dragon_name)s knocked Mistress to the ground and forcefully entered her, grasping the back of her armored neck with his claws. Their fierce passion blossomed and he came into her, holding her tenderly in his scaly arms. So wave after wave of stormy love will rage in the throne womb until new life grows in the belly of the reptile demoness.',]
    txt_dragon_mistress_fuck['hydra'] = ['Mistress gripped the arms of her iron throne and %(dragon_name_full)s watched as her graceful hands and painted nails transformed into claws and scaly paws.  \n Vertical slits cut across her yellow eyes, and rattling came from her changing throat. Anyone else would run in terror at the sight, but %(dragon_name)s rushed forward to touch the only woman in the world worthy of mothering his children. \n     The two lizards attacked each other like like enemies, and the grinding of their scales shook of stained-glass windows of the great hall. %(dragon_name)s knocked Mistress to the ground and forcefully entered her, grasping the back of her armored neck with his claws. Their fierce passion blossomed and he came into her, holding her tenderly in his scaly arms. So wave after wave of stormy love will rage in the throne womb until new life grows in the belly of the reptile demoness.',]
    txt_dragon_mistress_fuck['flying serpent'] = ['Mistress rose from her iron throne and moved to her son. Her body subtly twisted and stretched, taking snakelike form. The two snakes stood up on their tails and began to weave around each other. %(dragon_name)s released his forked tongue, which Mistress quickly met with her own. \n Strange to human eyes, the slow writhing and all-consuming love of the two great servants lasted many days...',]
    txt_dragon_mistress_fuck['wyvern'] = ['Mistress\'s eyes lit up with magic fire. Her body lengthened, and on scales began to form on her skin. Her nails extended, taking the shape of claws. The fire in her eyes kept burning: now she was a dangerous winged creature, queen of the night and bearer of his offspring, Mother and Mistress. He wanted her, his gaze wandered on her alluring scales. Compared to to those wild girls, she was a goddess. \n Mistress rushed to the dragon, softly growling. He responded with a gentle bite and a stronger male growl. He rolled over on top of her, and with his eyes devoured every curve of her body, feeling its power. His cock was ready to burst into this night creature, it swayed gently between her legs, covered with veins and shining with moonlight. The dragoness abruptly grabbed hold of his legs and pulled him towards her, as he opened his mighty wings and clamped down on her neck. Her hot slit touched him, and he could not resist. For so many years he terrified the free settlements, killing, raping, plundering, burning their houses. All for the sake of this. Every time he killed another unfortunate victim, he thought only of her. With a mighty roar the dragon moved forward, his cock plunging into the burning depths of the Mistress, like a gate to hell itself. She thrust back and plunged it in to the hilt, eagerly accepting the mating. The dragon rose slightly, flapping his wings, and then began to sharply thrust and deeply penetrate his mistress. She writhed and snarled from each penetration of the monster member, as more and more love juice splashed from her pussy. It could not last for long, the Dragon had been waiting for too long. Soon the gloomy dwelling was filled with the load roars of the mating dragons. He drove his cock all the way into her, feeling her eagerly grasp it as he poured his seed into her, to grow new nightmarish monsters in the depths of the Mistress\'s womb. ',]
    txt_dragon_mistress_fuck['dragon'] = ['Mistress\'s eyes lit up with magic fire. Her body lengthened, and on scales began to form on her skin. Her nails extended, taking the shape of claws. The fire in her eyes kept burning: now she was a dangerous winged creature, queen of the night and bearer of his offspring, Mother and Mistress. He wanted her, his gaze wandered on her alluring scales. Compared to to those wild girls, she was a goddess. \n Mistress rushed to the dragon, softly growling. He responded with a gentle bite and a stronger male growl. He rolled over on top of her, and with his eyes devoured every curve of her body, feeling its power. His cock was ready to burst into this night creature, it swayed gently between her legs, covered with veins and shining with moonlight. The dragoness abruptly grabbed hold of his legs and pulled him towards her, as he opened his mighty wings and clamped down on her neck. Her hot slit touched him, and he could not resist. For so many years he terrified the free settlements, killing, raping, plundering, burning their houses. All for the sake of this. Every time he killed another unfortunate victim, he thought only of her. With a mighty roar the dragon moved forward, his cock plunging into the burning depths of the Mistress, like a gate to hell itself. She thrust back and plunged it in to the hilt, eagerly accepting the mating. The dragon rose slightly, flapping his wings, and then began to sharply thrust and deeply penetrate his mistress. She writhed and snarled from each penetration of the monster member, as more and more love juice splashed from her pussy. It could not last for long, the Dragon had been waiting for too long. Soon the gloomy dwelling was filled with the load roars of the mating dragons. He drove his cock all the way into her, feeling her eagerly grasp it as he poured his seed into her, to grow new nightmarish monsters in the depths of the Mistress\'s womb.',]
    txt_dragon_mistress_fuck['multi headed flying serpent'] = ['Mistress rose from her iron throne and moved to her son. Her body subtly twisted and stretched, taking snakelike form. The two snakes stood up on their tails and began to weave around each other. %(dragon_name)s released his forked tongue, which Mistress quickly met with her own. \n Strange to human eyes, the slow writhing and all-consuming love of the two great servants lasted many days...',]
    txt_dragon_mistress_fuck['multi headed wyvern'] = ['Mistress gripped the arms of her iron throne and %(dragon_name_full)s watched as her graceful hands and painted nails transformed into claws and scaly paws.  \n Vertical slits cut across her yellow eyes, and rattling came from her changing throat. Anyone else would run in terror at the sight, but %(dragon_name)s rushed forward to touch the only woman in the world worthy of mothering his children. \n     The two lizards attacked each other like like enemies, and the grinding of their scales shook of stained-glass windows of the great hall. %(dragon_name)s knocked Mistress to the ground and forcefully entered her, grasping the back of her armored neck with his claws. Their fierce passion blossomed and he came into her, holding her tenderly in his scaly arms. So wave after wave of stormy love will rage in the throne womb until new life grows in the belly of the reptile demoness. ',]
    txt_dragon_mistress_fuck['multi headed dragon'] = ['Mistress\'s eyes lit up with magic fire. Her body lengthened, and on scales began to form on her skin. Her nails extended, taking the shape of claws. The fire in her eyes kept burning: now she was a dangerous winged creature, queen of the night and bearer of his offspring, Mother and Mistress. He wanted her, his gaze wandered on her alluring scales. Compared to to those wild girls, she was a goddess. \n Mistress rushed to the dragon, softly growling. He responded with a gentle bite and a stronger male growl. He rolled over on top of her, and with his eyes devoured every curve of her body, feeling its power. His cock was ready to burst into this night creature, it swayed gently between her legs, covered with veins and shining with moonlight. The dragoness abruptly grabbed hold of his legs and pulled him towards her, as he opened his mighty wings and clamped down on her neck. Her hot slit touched him, and he could not resist. For so many years he terrified the free settlements, killing, raping, plundering, burning their houses. All for the sake of this. Every time he killed another unfortunate victim, he thought only of her. With a mighty roar the dragon moved forward, his cock plunging into the burning depths of the Mistress, like a gate to hell itself. She thrust back and plunged it in to the hilt, eagerly accepting the mating. The dragon rose slightly, flapping his wings, and then began to sharply thrust and deeply penetrate his mistress. She writhed and snarled from each penetration of the monster member, as more and more love juice splashed from her pussy. It could not last for long, the Dragon had been waiting for too long. Soon the gloomy dwelling was filled with the load roars of the mating dragons. He drove his cock all the way into her, feeling her eagerly grasp it as he poured his seed into her, to grow new nightmarish monsters in the depths of the Mistress\'s womb. ',]

    #Сообщеения для битвы армий
    reinforcement_ask = 'Mistress, my troops have taken unsustainable losses, and I can\'t risk going out on the front. I beg you, help us crush the enemy! '
    reinforcement_agree = 'So be it. Watch and tremble as I wipe our foes off the face of the earth like dried autumn leaves in a hurricane! '
    reinforcement_refuse = 'Did we prepare a mighty army for nothing? Did I foster dragons for so many centuries in vain? Stop whining - bring me victory or die trying!!!'
    
    
    #СОВЕТЫ ВЛАДЫЧИЦЫ
    txt_advice = ['The safest place to start is the countryside and forests. But bear in mind that with increased mobilization comes more patrols, and they will be stronger. It will take them time to mobilize.',
    'If you are looking for giants, the weakest of them, the man-eating ogres, can be found in the forest caves. Tritons live in water, fire and ice giants high in the mountains, and they are very strong. But the mightiest of all, the Titans - they live in the clouds, on the flying island fortress.',
    'If you wander through the roads of men, you can find their strongholds - knightly manors, wooden and stone castles, monasteries...tough nuts to crack, but in them are virgin women and precious treasures. And an abandoned castle can be a wonderful den.',
    'Somewhere in the forest live the Elves, the people of Danu. Their maidens are very fair, but the elves conceal their possessions with magic. Try to catch and interrogate someone from their border guards. They sometimes go beyond the magic veil. Be sure to visit the island of smugglers, royal law holds no sway there. You will be able to sell your stolen treasure for coin, but bear in mind that you will get no good deals there. You can also find mercenaries to guard the den, or to sabotage enemy mobilization.',
    #'Чтобы взететь в небо нужны крылья. Или заклинание полёта. С высоты можно разглядеть укрепления людей - замки в которых они держат сокровища и благородных дев. Впрочем эти места можно и на дорогах найти, зато взлетев над облаками у тебя будет шанс обнаружить летающий остров Титанов.', #trans: Is this talking about using flight to scout/explore?
    'In the sea live mermaids, but their children are fit only for the protection of underwater dens. There you can also rob merchant ships, but to get to the ships and mermaids you must be able to breathe underwater. Gills help, as well as a special spell.',
    'In your den you can use various spells. Only if you have enough magic energy, of course. But do not use up everything as soon as you wake up. Magic can be useful to change your appearance, or destroy the people\'s supplies.',
    'Peasants are easy to catch, but they are able to produce only poisonous animals, useless for the army of darkness. Townswomen are better, but harder to find. Here\'s some advice - use guile to approach and kidnap one from the city market.',
    'Be sure to make use of Gremlins. They are bad fighters, but masters of stone, wood, and metal - as good as dwarves. And they lust for gold. You can hire them as servants or pay them to construct lair improvements. They can even create jewelry, if you give them the materials. ',
    'I don\'t want to see you going to that witch that lives in the cemetery. She thinks too much of herself - wants to become as powerful as I am. For your seed she will offer you magic services, but better you spend your energy on reproduction than that witch-whore. She\'ll milk you dry, and you won\'t be able to knock anyone up.',
    'The city has treasure to plunder, but the gate is well guarded. You can fly over them with wings, or disguise yourself, if you have the magic power. In human form you can even trade with jewelers - they give better prices for treasure than smugglers, and will sell their wares for money.',
    'If you impregnate a woman and let her go free, then your offspring will terrorize people and increase the level of devastation. But it is better to keep a pregnant maiden locked in the den, so you can make a servant of the offspring, or send it to the Army of Darkness. Do not forget that someone must care for them while you sleep.',
    'When your quest is complete, you can come to me for your reward at once. But you can also wait for the end of your alloted time, do not worry. Save money to supply my army, and spawn more monsters. It is important that our army is well equipped, numerous, and diverse.',
    'Мy advice: \n Steal \n and \n Kill',
    'Some chance encounters are more rare than others. For example, you\'re more likely to meet a farmer with a cart of hay than a rich caravan. If something does not interest you, do not waste time and energy. Constrain your rage until a better time.',
    'With the increasing mobilization of the entire kingdom, patrols will wander, and become stronger. Even a weak patrol is an annoyance, because it takes up time and effort. Too much devastation is also not good - smoldering ruins produce nothing to steal.',
    'Knights and thieves come in many different varieties. The higher your infamy, the more dangerous the opponents you will draw to your lair. Be careful, watch out for them and take countermeasures.',
    'If you do not do evil, even for selfish reasons like letting a common girl go to spare time and effort, your rage will increase. With too much rage bottled inside you, will be unable to control yourself, attacking everyone you encounter. Devour someone alive once in a while to release your anger.',
    'In the mountains you can find the entrance to the underground kingdom of the dwarves, concealing countless treasures. Additionally there are many mines that extract precious metals, and gems from which your gremlins can fashion expensive jewelry.']
    
    """
    Шаблон
    txt_ = [[
        '',
        ],
    
        ['',
        ],
    
        ['',
        ],
    
        ['',
        ],
        ]
    """