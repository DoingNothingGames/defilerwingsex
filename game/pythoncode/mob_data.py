# coding=utf-8
# Одноразовые противники
#translator: spellchecked, not proofread
mob = {
    'aircruiser': {
        'name': u"Flying cruiser",  # The name of the mob used ingame
        'power': {'base': (6, 0)},  # attack force (обычная, верная)
        'defence': {'base': (6, 2)},  # damage resistance (обычная, верная)
        'modifiers': ['sfatk_up', 'poison_immunity'],  # special modifiers
        'image': 'aircruiser',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"A dwarven flying cruiser slowly turns its side to face the enemy. Steam artillery prepares to fire a salvo."],
            [['foe_fear'],  u"The heavily armed battle cruiser rapidly unfurls all sails and flies away. There are opponents that not even the brave dwarves will face..."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name_full)s furiously smashes decks and bulkheads, breaking the ship in half and flinging dwarven bodies overboard. Dwarves simply cannot match a dragon in a close fight, and soon the burning fragments of the ship rain down on the ground."],
            [['foe_dead', 'dragon_wounded'], u"Volleys of the flying cruiser\'s onboard artillery hit their mark. Cast iron projectiles crush the dragon\'s scales and break bones, but %(dragon_name)s does not stop. The pain of his wounds just enrages him and gives him strength. As the dwarves try to quickly reload their weapon, the %(dragon_type)s rushes to the deck and begins to tear into the ship. Seeing their futile situation the artillery crew jumps overboard in a vain attempt to escape. Less than a minute later, the main boiler explodes and the ship is split in two."],
            [['foe_alive', 'dragon_wounded'], u"Accelerating to great speed, the %(dragon_type)s tries to break onto the deck of the cruiser, but a well aimed volley of artillery blasts it back. %(dragon_name)s roars with pain."],
            [['foe_alive', 'dragon_undamaged'], u"The airship captain waits for the dragon to close. %(dragon_name)s also waits, in no hurry to take a volley from the steam artillery. Someone must take a chance."],
            [['foe_alive', 'lost_head'], u"The cruiser\'s onboard artillery fires a broadside. Heavy iron balls crash into the dragon\'s head, smashing his skull with a crunch. Luckily %(dragon_name_full)s is able to survive such damage..."],
            [['foe_dead', 'lost_head'], u"Ignoring the danger, the %(dragon_type)s rams the flying cruiser The dwarven artillery fires a salvo at point blank range into one of the dragon\'s heads, but his inertia carries him forward to smash through the hull of the ship. %(dragon_name_full)s is able to survive the loss of his head, but the dwarven ship is ruined."],
            [['dragon_dead'], u"Time after time, %(dragon_name_full)s rushes at the steam ship, and time after time, bursts of explosive bombs force it back. Even the scales and bones of a dragon cannot withstand this forever. Beaten and mortally wounded, the %(dragon_type)s falls to the ground and breathes his last breath..."]
        ]
    },

    'airfleet': {
        'name': u"Air fleet",  # The name of the mob used ingame
        'power': {'base': (5, 1)},  # attack force (обычная, верная)
        'defence': {'base': (6, 3)},  # damage resistance (обычная, верная)
        'modifiers': ['sfatk_up', 'poison_immunity'],  # special modifiers
        'image': 'airfleet',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"A fleet of flying ships line up to attack."],
            [['foe_fear'],  u"At first sight of the dragon, the flying ships quickly turn full steam in the other direction."],
            [['foe_dead', 'dragon_undamaged'], u"The flying dwarven ships are too slow and clumsy to withstand the onslaught of the dragon. %(dragon_name_full)s destroys them one by one, never once crossing the firing zones of the steam guns."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s bursts into the battle formation of the flying fleet and begins destroying warships. Their panicked fire does more damage to themselves than the dragon, though a few projectiles hit their target. %(dragon_name_full)s triumphs."],
            [['foe_alive', 'dragon_wounded'], u"%(dragon_type_cap)s tries to break into the ranks of the fighting ships, but is thrown back by salvos from multiple ships."],
            [['foe_alive', 'dragon_undamaged'], u"%(dragon_type_cap)s is cautious, trying not to get into a crossfire from the steam guns. But there is no way to destroy the ships without getting closer."],
            [['foe_alive', 'lost_head'], u"The airborne cruisers\' artillery fires steady volleys. A heavy iron ball smashes into one of the dragon\'s heads with a crunch and shatters his skull. Luckily %(dragon_name_full)s is able to survive such an injury..."],
            [['foe_dead', 'lost_head'], u"Flying ships cannot withstand the onslaught of a furious dragon, but the dwarves fight to the death. Although the %(dragon_type)s wins, one of his heads does not survive its wounds."],
            [['dragon_dead'], u"%(dragon_name_full)s bursts into the flagship of the fleet, smashing through bulkheads and killing crewmen. The captain, seeing that his crew cannot be saved, closes the valves on the ship\'s boiler. A massive explosion of superheated steam takes with it the ship, the crew, and the dragon..."]
        ]
    },

    'airship': {
        'name': u"Airship",  # The name of the mob used ingame
        'power': {'base': (4, 0)},  # attack force (обычная, верная)
        'defence': {'base': (4, 1)},  # damage resistance (обычная, верная)
        'modifiers': ['poison_immunity'],  # special modifiers
        'image': 'airship',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"A flying dwarven ship slowly turns to face its enemy. A steam catapult prepares to fire."],
            [['foe_fear'],  u"(Rapidly unfurling all sails, the airship turns and flies away. There are opponents not even the brave dwarves will face..."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name_full)s furiously smashes decks and bulkheads, breaking the ship in half and flinging dwarven bodies overboard. Dwarves simply cannot match a dragon in a close fight, and soon the burning fragments of the ship rain down on the ground."],
            [['foe_dead', 'dragon_wounded'], u"Shots from the airship\'s steam catapult hit their mark. Cast iron projectiles crush the dragon\'s scales and break bones, but %(dragon_name)s does not stop. The pain of his wounds just enrages him and gives him strength. As the dwarves try to quickly reload their weapon, the %(dragon_type)s rushes to the deck and begins to tear into the ship. Seeing their futile situation the catapult crew jumps overboard in a vain attempt to escape. Less than a minute later, the main boiler explodes and the ship is split in two."],
            [['foe_alive', 'dragon_wounded'], u"Accelerating to great speed, the %(dragon_type)s tries to break onto the deck of the airship, but a well aimed catapult shot knocks it back. %(dragon_name)s roars with pain."],
            [['foe_alive', 'dragon_undamaged'], u"The airship captain waits for the dragon to close. %(dragon_name)s also waits, in no hurry to take a hit from the steam catapult. Someone must take a chance."],
            [['foe_alive', 'lost_head'], u"The airship\'s onboard catapult fires repeatedly. Heavy iron balls crash into the dragon\'s head, smashing his skull with a crunch. Luckily %(dragon_name_full)s is able to survive such damage..."],
            [['foe_dead', 'lost_head'], u"Ignoring the danger, the %(dragon_type)s rams the flying ship The dwarven catapult hurls a ball at point blank range into one of the dragon\'s heads, but his inertia carries him forward to smash through the hull of the ship. %(dragon_name_full)s is able to survive the loss of his head, but the dwarven ship is ruined."],
            [['dragon_dead'], u"Time after time, %(dragon_name_full)s rushes at the airship, and time after time, explosive bombs force it back. Even the scales and bones of a dragon cannot withstand this forever. Beaten and mortally wounded, the %(dragon_type)s falls to the ground and breathes his last breath..."]
        ]
    },

    'angel': {
        'name': u"Angel",  # The name of the mob used ingame
        'power': {'base': (8, 3)},  # attack force (обычная, верная)
        'defence': {'base': (6, 3)},  # damage resistance (обычная, верная)
        'modifiers': ['sound_immunity'],  # special modifiers
        'image': 'angel',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"An angel holds a shining sword. He is determined the punish the dragon in the name of heaven."],
            [['foe_fear'],  u"The angel runs away in fear."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name_full)s easily evades a blow from a magic sword and bites the angel\'s throat. His blood tastes like wine..."],
            [['foe_dead', 'dragon_wounded'], u"The battle of the two mighty creatures lasts a long time, but in the end the %(dragon_name)s emerges as the victor, covered in wounds."],
            [['foe_alive', 'dragon_wounded'], u"%(dragon_type_cap)s charges the enemy but, receiving a painful blow from a magic sword, is forced to retreat."],
            [['foe_alive', 'dragon_undamaged'], u"The fight continues for some time, but neither fighter gains the advantage. They are an equal match for each other."],
            [['foe_alive', 'lost_head'], u"With a mighty blow the angel takes off one of the dragon\'s heads. But this is not the end, %(dragon_name_full)s can survive such a wound."],
            [['foe_dead', 'lost_head'], u"%(dragon_type_cap)s defeats the angel, but one of his heads is dying from its wounds."],
            [['dragon_dead'], u"Covered with wounds, the %(dragon_type)s charges for a final attack, but filled with holy fury the angel does not flinch. Putting all his force into one mighty blow, the winged warrior splits the dragon in half!"]
        ]
    },

    'archer': {
        'name': u"Archer",  # The name of the mob used ingame
        'power': {'base': (3, 0)},  # attack force (обычная, верная)
        'defence': {'base': (1, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'archer',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"A royal archer nocks an arrow."],
            [['foe_fear'],  u"The royal archer runs away in horror. He was not prepared for this fight."],
            [['foe_dead', 'dragon_undamaged'], u"The archer manages to fire three times before %(dragon_name)s reaches him. But the arrows simply glance of the scaly skin of the dragon. At close range, the archer has no defense against the fanged lizard."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s opens his jaws to roar, and an arrow punctures his soft mouth. Unable to bite, the %(dragon_type)s angrily beats the archer to death with his tail."],
            [['foe_alive', 'dragon_wounded'], u"The sharpshooting archer manages to hit the lizard right in the eye. The lizard stops, going mad with pain."],
            [['foe_alive', 'dragon_undamaged'], u"The archer\'s arrows glance off the natural armor of the dragon."],
            [['foe_alive', 'lost_head'], u"A tempered arrow with a fire hardened shaft pierces through one of the dragon\'s mouths and into a brain. Luckily, %(dragon_name_full)s can survive such a wound."],
            [['foe_dead', 'lost_head'], u"%(dragon_type_cap)s wins, but one of his heads is withering from its wounds."],
            [['dragon_dead'], u"The archer looses a tempered arrow with a fire hardened shaft, and it pierces through one the dragon\'s mouth and into his brain. %(dragon_name_full)s falls dead."]
        ]
    },

    'band': {
        'name': u"Band of thieves",  # The name of the mob used ingame
        'power': {'base': (3, 0)},  # attack force (обычная, верная)
        'defence': {'base': (5, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'xbow',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"Bandits are lined up in a semicircle, squeezing their weapons tightly."],
            [['foe_fear'],  u"When the dragon attacks the bandits, they flee in fear in all directions. By blind luck, a few escape."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name)s bursts into the crowd of robbers and begins to tear them to pieces. The disorganized bandits are unable to put up worthy resistance."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s bursts into the crowd of robbers and begins to tear them to pieces. A few strokes of the bandits reach their mark, but the wounded %(dragon_type)s emerges victorious."],
            [['foe_alive', 'dragon_wounded'], u"Using effectively coordinated tactics, the bandits strongly rebuff the dragon, inflicting injury. A few of the robbers are dead, but the rest are full of determination."],
            [['foe_alive', 'dragon_undamaged'], u"The thieves fight desperately, and manage to hold back the furious assault of the dragon."],
            [['foe_alive', 'lost_head'], u"The %(dragon_type)s attacks thoughtlessly, exposing his back to several bandits. One clever thief jumps onto his back, smashing one of his skulls in with an iron capped club."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s is covered with serious injuries, the victory over the bandits hurt him badly. One of his heads is mortally wounded."],
            [['dragon_dead'], u"The robbers pounce on the dragon all at once, frantically thrashing him with their weapons. In a fit of rage the wounded %(dragon_type)s manages to kill a few enemies, but there are too many. %(dragon_name_full)s falls to the ground and breathes his last breath."]
        ]
    },


    'battleship': {
        'name': u"Battleship",  # The name of the mob used ingame
        'power': {'base': (7, 0)},  # attack force (обычная, верная)
        'defence': {'base': (7, 2)},  # damage resistance (обычная, верная)
        'modifiers': ['sfatk_up', 'poison_immunity'],  # special modifiers
        'image': 'ship',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"On the deck of a warship, a boatswain whistles frantically. Gunners quickly roll out their cannons."],
            [['foe_fear'],  u"Unfurling its sails, the formidable warship turns into the wind and sails from the dragon at top speed. The captain is not ready to fight with such a monster as %(dragon_name_full)s."],
            [['foe_dead', 'dragon_undamaged'], u"Hiding beneath the waves, %(dragon_name)s swims under the warship, and punches a hole in it at top speed. Now the sinking sailors can be caught one by one."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s dives into the depths, but not quickly enough. The warship has time for one volley, and cannonballs break the dragon\'s ribs. The furious %(dragon_type)s rips off a section of the ship\'s hull under the waterline. The ocean quickly rushes in, and the battleship is doomed."],
            [['foe_alive', 'dragon_wounded'], u"Coordinated volleys of cannonfire smash into the dragon and he is forced to retreat, throwing up swirling columns of water."],
            [['foe_alive', 'dragon_undamaged'], u"%(dragon_name)s dives under the ship and tries to punch a hole below the waterline, but to no avail."],
            [['foe_alive', 'lost_head'], u"A cast-iron bomb stuffed with black powder detonates directly on the dragon\'s forehead. From such a wound few can recover..."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s climbs onto the deck of the ship and happily starts to make a bloodbath out of the crew. The sailors scatter in panic, and in his enthusiastic pursuit %(dragon_name)s fails to notice the captain climbing on a yardarm. Jumping from above, the captain slices off the dragon\'s head with a blow from his sword. Unfortunately for him, it isn\'t enough for victory. The warship is doomed."],
            [['dragon_dead'], u"%(dragon_name_full)s is too weak to withstand another volley from the warship. Pummeled by iron projectiles, the dragon sinks beneath the depths, no longer able to cling to life."]
        ]
    },

    'boar': {
        'name': u"Enormous boar",  # The name of the mob used ingame
        'power': {'base': (3, 0)},  # attack force (обычная, верная)
        'defence': {'base': (3, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'boar',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"A huge boar bows his head to the ground, exposing his menacing curved tusks."],
            [['foe_fear'],  u"The huge boar shrieks in fear of the monstrous predator and tries to escape it. Not that it can..."],
            [['foe_dead', 'dragon_undamaged'], u"The wild boar charges forward, but the %(dragon_type)s knocks him off his feet with one powerful blow."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s wrestles with the giant boar. The horrible fangs of the forest boar pierce the scales of the dragon, inflicting a bleeding wound, but nevertheless the dragon gains the advantage. Within a minute, everything is still and %(dragon_name_full)s can at last eat in peace..."],
            [['foe_alive', 'dragon_wounded'], u"The two huge bodies collide with a roar and a squeal. The impact from the boar is great that the %(dragon_type)s goes flying off to the side."],
            [['foe_alive', 'dragon_undamaged'], u"The fight continues for some time, but no one gains the upper hand."],
            [['foe_alive', 'lost_head'], u"The wounded dragon makes a clumsy move, and the curved tusk of the boar gores one of his necks. This may end badly..."],
            [['foe_dead', 'lost_head'], u"The wounded dragon makes a clumsy move, and the curved tusk of the boar gores one of his necks. But in the end, the boar is doomed to defeat."],
            [['dragon_dead'], u"%(dragon_name_full)s receives a mortal blow. The last thought in his fading consciousness - how humiliating to die from a pig."]#trans: could not translate last part of last sentence.  "буд-то какой-нибудь пьяный человеческий королёк..."
        ]
    },


    'bear': {
        'name': u"Cave bear",  # The name of the mob used ingame
        'power': {'base': (3, 0)},  # attack force (обычная, верная)
        'defence': {'base': (3, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'bear',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"A cave bear stands on its hind legs and bares its teeth."],
            [['foe_fear'],  u"The huge cave bear runs like a frightened puppy. He is surprisingly fast, considering his clumsy gait, but not fast enough..."],
            [['foe_dead', 'dragon_undamaged'], u"\n %(dragon_name)s knocks down the cave bear and bites into its throat. It clumsily attempts to fight back but to no avail, its struggles soon fade."],
            [['foe_dead', 'dragon_wounded'], u"\n The roars of the battling monsters echo through the mountains. Punctured by bear claws, the %(dragon_type)s comes out of the battle victorious, but at great cost."],
            [['foe_alive', 'dragon_wounded'], u"The %(dragon_type)s tries to attack the huge bear, but receives a painful blow from heavy caws in response. This animal will not give up easily..."],
            [['foe_alive', 'dragon_undamaged'], u"The battle continues for some time, but neither combatant gains the upper head."],
            [['foe_alive', 'lost_head'], u"The cave bear manages to crack the skull of the dragon. %(dragon_name)s is still alive, but his head likely cannot be saved. This battle is too expensive..."],
            [['foe_dead', 'lost_head'], u"The wounded %(dragon_type)s overcomes the bear with great difficulty. Under the blows of its heavy clawed feet one head is so badly torn that it cannot be saved..."],
            [['dragon_dead'], u"The wounded dragon fiercely attacks the giant bear, but he proves stronger. %(dragon_name_full)s falls to the ground unable to stand the weight of the bear, and is suffocated in its hairy arms."]
        ]
    },

    'bull': {
        'name': u"Bull",  # The name of the mob used ingame
        'power': {'base': (2, 0)},  # attack force (обычная, верная)
        'defence': {'base': (2, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'bull',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The bull puts up its horns and digs its hooves into the ground."],
            [['foe_fear'],  u"Distraught with fear the bull rushes away, but the %(dragon_type)s is faster..."],
            [['foe_dead', 'dragon_undamaged'], u"With a mighty blow %(dragon_name)s knocks the bull to the ground and crushes it with his teeth."],
            [['foe_dead', 'dragon_wounded'], u"During a short but fierce struggle, the bull manages to penetrate the dragon\'s scales with its horn, but the wounded %(dragon_name)s still comes out of the battle victorious."],
            [['foe_alive', 'dragon_wounded'], u"The bull rams the dragon at full speed, knocking him aside. %(dragon_name)s is seriously wounded."],
            [['foe_alive', 'dragon_undamaged'], u"The battle continues for some time, but neither side can gain the advantage."],
            [['foe_alive', 'lost_head'], u"The wounded %(dragon_type)s moves too slowly and the sharp curved bull\'s horn hits the lizard directly in the eye, tearing through the brain of one of his heads."],
            [['foe_dead', 'lost_head'], u"The wounded %(dragon_type)s moves too slowly and the sharp bull\'s one of his heads, but the dragon emerges victorious..."],
            [['dragon_dead'], u"The wounded %(dragon_type)s moves too slowly and the sharp bull\'s horns pierce the scales on his chest. %(dragon_name_full)s dies from terrible injuries."]
        ]
    },

    'bull_champion': {
        'name': u"Prize bull",  # The name of the mob used ingame
        'power': {'base': (3, 0)},  # attack force (обычная, верная)
        'defence': {'base': (3, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'bull',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The large bull puts up its horns and digs its hooves into the ground."],
            [['foe_fear'],  u"Distraught with fear the bull rushes away, but the %(dragon_type)s is faster..."],
            [['foe_dead', 'dragon_undamaged'], u"With a mighty blow %(dragon_name)s knocks the bull to the ground and crushes it with his teeth."],
            [['foe_dead', 'dragon_wounded'], u"During a short but fierce struggle, the bull manages to penetrate the dragon\'s scales with its horn, but the wounded %(dragon_name)s still comes out of the battle victorious."],
            [['foe_alive', 'dragon_wounded'], u"The bull rams the dragon at full speed, knocking him aside. %(dragon_name)s is seriously wounded."],
            [['foe_alive', 'dragon_undamaged'], u"The battle continues for some time, but neither side can gain the advantage."],
            [['foe_alive', 'lost_head'], u"The wounded %(dragon_type)s moves too slowly and the sharp curved bull\'s horn hits the lizard directly in the eye, tearing through the brain of one of his heads."],
            [['foe_dead', 'lost_head'], u"The wounded %(dragon_type)s moves too slowly and the sharp bull\'s one of his heads, but the dragon emerges victorious..."],
            [['dragon_dead'], u"The wounded %(dragon_type)s moves too slowly and the sharp bull\'s horns pierce the scales on his chest. %(dragon_name_full)s dies from terrible injuries."]
        ]
    },

    'castle_guard': {
        'name': u"Castle guards",  # The name of the mob used ingame
        'power': {'base': (7, 0)},  # attack force (обычная, верная)
        'defence': {'base': (5, 2)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'town',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The castle defenders take their places on the walls. They prepare spears, heavy stones, and cauldrons of boiling tar."],
            [['foe_fear'],  u"Looking at the dragon the castle defenders waver. They flee in panic from the walls, looking for somewhere, anywhere to hide, and the battle is over before it even begins."],
            [['foe_dead', 'dragon_undamaged'], u"Under a useless hail of stones, spears, and arrows, %(dragon_name_full)s approaches the gates and rams through them with all his weight. The remaining soldiers are exposed to the fury of the dragon."],
            [['foe_dead', 'dragon_wounded'], u"Under a hail of stones, spears, and arrows, %(dragon_name_full)s approaches the gates and rams through them with all his weight. The missiles of the defenders covered the dragon\'s body with wounds, but with the gate fallen there is nothing left to stop him."],
            [['foe_alive', 'dragon_wounded'], u"The hail of stones, arrows, and spears from the walls and towers is so heavy that the dragon is forced to pull back from the gate. Taking this fortress will not be so easy..."],
            [['foe_alive', 'dragon_undamaged'], u"The %(dragon_type)s leans all his weight on the gates, trying to break through them as the defenders pour stones, spears, and arrows on the dragon. But both are completely ineffective. The projectiles glance off the dragon\'s scales, and the steel gates will not give in."],
            [['foe_alive', 'lost_head'], u"Five stalwart defenders throw a thick tree trunk from the wall, which crushes one of the dragon\'s heads."],
            [['foe_dead', 'lost_head'], u"Five stalwart defenders throw a thick tree trunk from the wall, which crushes one of the dragon\'s heads. But it is useless, the furious %(dragon_type)s breaks the gates and rushes into the castle."],
            [['dragon_dead'], u"%(dragon_name_full)s is too tired and wounded for such a battle. Just one well aimed stone from the walls stops his assault. The brave city defenders celebrate victory as %(dragon_name_full)s dies at the unyielding gates."]
        ]
    },
        
    'catapult': {
        'name': u"Catapult",  # The name of the mob used ingame
        'power': {'base': (3, 1)},  # attack force (обычная, верная)
        'defence': {'base': (2, 0)},  # damage resistance (обычная, верная)
        'modifiers': ['sfatk_up', 'poison_immunity'],  # special modifiers
        'image': 'catapult',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"Aiming in front of their charging target, the catapult crew frantically prepares to fire."],
            [['foe_fear'],  u"The catapult crew scatters in fear, leaving the formidable fighting machine without control."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name_full)s easily destroys the catapult and slaughters the crew."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s rushes into a frontal attack and is hit at point-blank range, but does not stop. The siege engine is doomed."],
            [['foe_alive', 'dragon_wounded'], u"An accurate catapult shot throws the dragon back, but he is not finished!"],
            [['foe_alive', 'dragon_undamaged'], u"The catapult engineers do not hurry, they know they only have time for one shot and are afraid to miss. %(dragon_name)s maneuvers around, giving them no chance to aim."],
            [['foe_alive', 'lost_head'], u"A catapult projectile falls directly on the dragon\'s head. This is a very grave wound!"],
            [['foe_dead', 'lost_head'], u"A catapult projectile falls directly on the dragon\'s head, but the dragon does not stop. Enraged by his injuries, the %(dragon_type)s brutally destroys the catapult!"],
            [['dragon_dead'], u"%(dragon_name_full)s overestimated his strength. A well aimed shot from the catapult blows off his only head."]
        ]
    },
    
    'champion': {
        'name': u"Champion",  # The name of the mob used ingame
        'power': {'base': (5, 1)},  # attack force (обычная, верная)
        'defence': {'base': (5, 1)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'champion',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The tournament winner picks up a lance and readies his steed for an attack."],
            [['foe_fear'],  u"The winner of the tournament is spoiling for a fight, but his horse is too scared - it gets up on his hind legs and throws the rider into the mud, leaving him defenseless."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name)s deftly dodges the sharp lance and with a vicious attack knocks the champion spinning out of his saddle."],
            [['foe_dead', 'dragon_wounded'], u"The %(dragon_type)s and the champion collide together with a terrible roar. The knight topples from his horse, but %(dragon_name)s is also injured."],
            [['foe_alive', 'dragon_wounded'], u"A lance blow with all the weight and speed of the horse behind it throws the dragon aside."],
            [['foe_alive', 'dragon_undamaged'], u"The opponents battle, producing sounds of clashing metal and a neighing steed, but the foes are of equal strength."],
            [['foe_alive', 'lost_head'], u"An aimed blow from the knight pierces one of the dragon\'s heads, but the fight is not yet over."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s wins, but one of his heads is dying from its wounds."],
            [['dragon_dead'], u"The knight aims a blow at %(dragon_name_full)s\'s head, killing him."]
        ]
    },

    'city_guard': {
        'name': u"City watch",  # The name of the mob used ingame
        'power': {'base': (6, 0)},  # attack force (обычная, верная)
        'defence': {'base': (6, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'city_guard',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The guards are arrayed in a semicircle, squeezing their halberds tightly."],
            [['foe_fear'],  u"When the dragon attacks, the city guard scatter in all directions. Some escape by blind luck, and others are caught."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name)s bursts into the formation of guards and begins to tear them to pieces. The disorganized fighters lose the ability to put up resistance."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s bursts into the formation of guards and begins to tear them to pieces. The heavily armed soldiers put up a hard resistance, but the wounded %(dragon_type)s emerges from the battle victorious."],
            [['foe_alive', 'dragon_wounded'], u"Using organized tactics the guards strongly rebuff the dragon, inflicting wounds. A few of the guards fall dead, but the rest are full of determination."],
            [['foe_alive', 'dragon_undamaged'], u"The guards fight desperately, and manage to hold back the furious assault of the dragon."],
            [['foe_alive', 'lost_head'], u"The %(dragon_type)s attacks thoughtlessly, exposing his back to several guards. This mistake costs him his head. Well, one of them..."],
            [['foe_dead', 'lost_head'], u"%(dragon_type_cap)s is covered with serious injuries, the victory over the guards hurt him badly. One of his heads is mortally wounded."],
            [['dragon_dead'], u"The guards pounce on the dragon all at once, frantically thrashing him with their halberds. In a fit of rage the wounded %(dragon_type)s manages to kill a few enemies, but there are too many. %(dragon_name_full)s falls to the ground and breathes his last breath.."]
        ]
    },

    'city': {
        'name': u"Gatehouse",  # The name of the mob used ingame
        'power': {'base': (9, 0)},  # attack force (обычная, верная)
        'defence': {'base': (5, 3)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'city_siege',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"Guards grab their weapons and stand in their places."],
            [['foe_fear'],  u"The defenders of the gate flee in terror from the attacking dragon. An easy victory."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name_full)s breaches the gate and scatters those who try to fight back like rag dolls."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s throws himself at the gate, under a rain of stones and arrows. It is impossible to avoid injury, but eventually the gate is broken and the guards flee in terror."],
            [['foe_alive', 'dragon_wounded'], u"The %(dragon_type)s throws himself at the gate, under a rain of stones and arrows. This is a bad idea - the gate is too strong, and the scales of the dragon are punctured in several places."],
            [['foe_alive', 'dragon_undamaged'], u"The %(dragon_type)s throws himself at the gate, under a rain of stones and arrows. The defender\'s fire does not cause him any harm, but the gate is well made and the fortifications do not give in."],
            [['foe_alive', 'lost_head'], u"Someone pours a vat of boiling tar on one of the dragon\'s heads."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s wins, but the victory costs him a head. An expensive price."],
            [['dragon_dead'], u"The wounded %(dragon_type)s frantically beats at the strong gates, but they do not give in. Unable to continue fighting, %(dragon_name_full)s falls bleeding in front of the insurmountable fortification."]
        ]
    },
    
    'dog': {
        'name': u"Sheepdog",  # The name of the mob used ingame
        'power': {'base': (1, 0)},  # attack force (обычная, верная)
        'defence': {'base': (1, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'dog',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The dog growls and bares its teeth."],
            [['foe_fear'],  u"The dog whimpers and hides in fear."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name)s tears the dog into pieces."],
            [['foe_dead', 'dragon_wounded'], u"The %(dragon_type)s and the dog tangle together in a whirl of teeth and scraping claws. %(dragon_name)s emerges victorious, but not without injury."],
            [['foe_alive', 'dragon_wounded'], u"The angry dog manages to wrestle the dragon to the ground and clutch at his throat. This position is not pleasant."],
            [['foe_alive', 'dragon_undamaged'], u"The dragon and the dog circle around each other, baring teeth and growling. Neither dares to lunge."],
            [['foe_alive', 'lost_head'], u"The angry dog manages to wrestle the dragon to the ground and tear through one of his throats. The wound is very serious."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s wins, but one of his heads is dying from its wounds.."],
            [['dragon_dead'], u"%(dragon_name_full)s is torn apart by a country mutt. What a dishonor for his whole family!"]
        ]
    },

    'domik': {
        'name': u"Wooden house",  # The name of the mob used ingame
        'power': {'base': (7, 1)},  # attack force (обычная, верная)
        'defence': {'base': (5, 4)},  # damage resistance (обычная, верная)
        'modifiers': ['poison_immunity', 'magic_immunity'],  # special modifiers
        'image': 'domik',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"A ramshackle hut on hinged legs like a chicken. A huge, aggressive chicken armed with 50 caliber guns..."],
            [['foe_fear'],  u"%(dragon_name_full)s gives off such an aura of fear that even the wooden house runs away from him."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name)s strikes the log house with sudden force that it breaks and cracks, nails flying like bullets and tiles smashing on the ground."], #translator: cant translate last sentence. "Древний ужас лесов столетиями набигающий эльфов..."
            [['foe_dead', 'dragon_wounded'], u"The %(dragon_type)s and the house squeeze each other in a deadly embrace of steel. The dragon\'s ribs crack, but the wood is weaker, and the house collapses like a big box of matches."],
            [['foe_alive', 'dragon_wounded'], u"A volley of automatic gunfire throws the dragon aside."],
            [['foe_alive', 'dragon_undamaged'], u"The %(dragon_type)s and the golem hit each other hard, but both are so well protected that they take only minor scrapes. The old firs shake from this battle of giants."],
            [['foe_alive', 'lost_head'], u"A volley of automatic gunfire throws the dragon back. Shots burst through one of %(dragon_name)s\'s brains."],
            [['foe_dead', 'lost_head'], u"The wounded %(dragon_type)s rips apart the wooden body of the house, but leaves a torn-off head in the tenacious steel toes of the golem."],
            [['dragon_dead'], u"Bursts of automatic gunfire impact %(dragon_name)s\' skull, bursting his brains."]
        ]
    },

    'druid': {
        'name': u"Druid",  # The name of the mob used ingame
        'power': {'base': (5, 1)},  # attack force (обычная, верная)
        'defence': {'base': (5, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'druid',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The grass around the dragon shimmers emerald green - the druid gathers strength from wildlife."],
            [['foe_fear'],  u"The druid transforms into a fleet-footed deer and runs away. He is not ready to fight with such an enemy as %(dragon_name_full)s."],
            [['foe_dead', 'dragon_undamaged'], u"The druid calls a cloud of killer bees, but this is a fatal mistake - they cannot pierce the scales of the dragon with their stings. The %(dragon_type)s breaks the druid\'s body into pieces."],
            [['foe_dead', 'dragon_wounded'], u"The druid surrounds himself with a wall of poisonous thorns, but the %(dragon_type)s cuts through them and kills him. The dragon\'s blood is already poisonous."],
            [['foe_alive', 'dragon_wounded'], u"The druid calls a variety of wild animals to his aid. In a fierce battle %(dragon_name_full)s wins a hard victory. The druid is unharmed, but the %(dragon_type)s is covered with blood."],
            [['foe_alive', 'dragon_undamaged'], u"The druid manages to hold the dragon with poisonous vines. But this is only a temporary solution, sooner or later %(dragon_name)s will break out."],
            [['foe_alive', 'lost_head'], u"The druid uses the strength of the earth to conjure stone mouths full of sharp stalactites. One of them rips off the dragon\'s head."],
            [['foe_dead', 'lost_head'], u"The druid meets the attack of the dragon with a blow from a rod of shining green fire. The blow is so strong that %(dragon_name_full)s loses one of his heads, but he is not defeated and in one blow kills the hated child of Danu."],
            [['dragon_dead'], u"The wounded %(dragon_type)s cannot overcome the druid\'s spells. %(dragon_name)s falls from a blow to the head from a thick oak branch, and then the furious beasts of the forest pounce on him."]
        ]
    },

    'dwarf_champion': {
        'name': u"Dwarven champion",  # The name of the mob used ingame
        'power': {'base': (7, 0)},  # attack force (обычная, верная)
        'defence': {'base': (5, 2)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'dwarf_champion',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The dwarven king puts on a fireproof mask and tightly grips a battle axe inscribed with magic runes."],
            [['foe_fear'],  u"As soon as they notice the approaching dragon, the king of the dwarves and all his entourage scatter, hoping to find refuge in workshops or hide in secret passages."],
            [['foe_dead', 'dragon_undamaged'], u"The king of the dwarves fights a desperate, doomed battle, but he cannot withstand the onslaught of the dragon. The injured warrior falls lifeless."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s meets the king in close combat and defeats him, but at a price - the enchanted axe has cut a gash into his chest."],
            [['foe_alive', 'dragon_wounded'], u"The %(dragon_type)s confidently attacks the adamant clad dwarf, but is forced to retreat under a flood of sharp blows."],
            [['foe_alive', 'dragon_undamaged'], u"The bout with the dwarven king lasts for some time, but neither side gains the advantage. Both fighters are stout and perfectly armored."],
            [['foe_alive', 'lost_head'], u"With a mighty blow the dwarf king\'s runic axe cuts off one of the dragon\'s heads. However, %(dragon_name_full)s is able to survive it."],
            [['foe_dead', 'lost_head'], u"%(dragon_name_full)s is able to overcome the king dwarf, but at great cost. A blow from the runic axe cuts off one of his heads."],
            [['dragon_dead'], u"Gathering his last strength the wounded %(dragon_type)s rushes into a desperate attack, but the king of the dwarves stands firmly on his feet and delivers a skilled slash. %(dragon_name_full)s falls headless at this feet!"]
        ]
    },

    'dwarf_citizen': {
        'name': u"Dwarves",  # The name of the mob used ingame
        'power': {'base': (2, 0)},  # attack force (обычная, верная)
        'defence': {'base': (3, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'dwarf_citizen',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The cornered dwarves prepare for a desperate fight."],
            [['foe_fear'],  u"Even cornered, the dwarves are so terrified of the dragon that they are unable to defend themselves. Easy prey."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name_full)s easily overcomes the nearly defenseless dwarves."],
            [['foe_dead', 'dragon_wounded'], u"The poorly armed dwarves manage to inflict injuries on the dragon before dying in his jaws. Such is the power of their fighting spirit!"],
            [['foe_alive', 'dragon_wounded'], u"Seemingly almost defenseless, the dwarves nonetheless give a fierce resistance. The wounded %(dragon_type)s has to shrink back."],
            [['foe_alive', 'dragon_undamaged'], u"The nimble dwarves deftly maneuver in narrow passages and hide behind columns - getting them is not easy!"],
            [['foe_alive', 'lost_head'], u"A dwarf hiding on a dark upper level passage manages to jump directly on the back of the dragon. His heavy steel pickaxe breaks through the skull of the snake! Fortunately for the dragon, such a wound is not fatal."],
            [['foe_dead', 'lost_head'], u"The last fighter, hiding on a dark upper level passage, manages to jump directly on the back of the dragon. His heavy steel pickaxe breaks through the skull of the snake! %(dragon_name)s rolls on his back to crush the loathsome dwarf."],
            [['dragon_dead'], u"A dwarf hiding on a dark upper level passage manages to jump directly on the back of the dragon. His heavy steel pickaxe breaks through the skull of the snake! This wound is mortal..."]
        ]
    },

    'dwarf_guards': {
        'name': u"Tunnel guards",  # The name of the mob used ingame
        'power': {'base': (6, 0)},  # attack force (обычная, верная)
        'defence': {'base': (4, 1)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'dwarf_guards',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"Dwarves in steel armor line up in a tight group, forming a solid metal wall"],
            [['foe_fear'],  u"%(dragon_name_full)s strikes a special terror into the heart of the dwaves. The guardians of the tunnels are not ready to do battle with such an enemy."],
            [['foe_dead', 'dragon_undamaged'], u"Using all his considerable weight, the %(dragon_type)s pushes through the closely arrayed shields of the dwarves, breaking their ranks. After this, victory is easy."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s decides to charge the shield wall. Spear points puncture his scales in many places, but the %(dragon_type)s is able to keep up the pressure, and knocks the dwarves over like bowling pins."],
            [['foe_alive', 'dragon_wounded'], u"%(dragon_name)s decides to charge the shield wall. but the dwarves are ready. Planting their spears on the ground they stop the monster and even get in a few well aimed blows with two-handed axes."],
            [['foe_alive', 'dragon_undamaged'], u"%(dragon_name)s does not dare to attack the shield wall in the front, it is too dangerous. The dwarves hold their positions and try to engage the dragon with crossbows, but to no avail."],
            [['foe_alive', 'lost_head'], u"A frontal attack on the shield wall is a very bad idea. One of the dwarves in the second row strikes the dragon\'s head with a two-handed axe! This not fatal, but a very serious blow."],
            [['foe_dead', 'lost_head'], u"Using all his considerable weight, the %(dragon_type)s breaches through the close held shields of the dwarves and scatters their ranks. Even deprived of protection the dwarves fight desperately, and before they are defeated %(dragon_name_full)s loses one of his heads."],
            [['dragon_dead'], u"%(dragon_name)s suffers from wounds received in the bloody battle. Seeing this the tunnel guards attack and triumph, beating the dragon. This victory cost them dearly, a victory that will be sung of in legends!"]
        ]
    },

    'elf_ranger': {
        'name': u"Border guard",  # The name of the mob used ingame
        'power': {'base': (6, 0)},  # attack force (обычная, верная)
        'defence': {'base': (2, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'elf_ranger',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The border guard draws his bow and takes aim."],
            [['foe_fear'],  u"Deciding that the dragon is too tough for him, the guardian of the border dissolves in the dense foliage. He will go raise the alarm..."],
            [['foe_dead', 'dragon_undamaged'], u"The %(dragon_type)s powerfully beats his tail on a tree trunk, knocking the border guard out of it. In melee he has no chance."],
            [['foe_dead', 'dragon_wounded'], u"The %(dragon_type)s shakes the tree to throw the elf from the branch, but in the process gets an arrow in the mouth. The archer is also unlucky, falling directly after his arrow on the angry dragon..."],
            [['foe_alive', 'dragon_wounded'], u"The border guard deftly jumps through trees, hiding in the leaves and making sudden shots. The magic arrows inflict painful wounds..."],
            [['foe_alive', 'dragon_undamaged'], u"The border guard deftly jumps through trees, hiding in the leaves. He is waiting for the right moment for a single precise shot. Probably conserving his arrows..."],
            [['foe_alive', 'lost_head'], u"The wounded %(dragon_type)s rams a tree trunk with the full weight of his body, and the border guard falls squarely on his head. Unfazed, the elf grabs an arrow and plunges it into the dragon\'s eye, then immediately jumps into the bushes."],
            [['foe_dead', 'lost_head'], u"The wounded %(dragon_type)s rams a tree trunk with the full weight of his body, and the border guard falls squarely on his head. Unfazed, the elf grabs an arrow and plunges it into the dragon\'s eye, but it does not save him from his grisly fate"],
            [['dragon_dead'], u"The boarder guard readies an enchanted arrow with a green tip. He waits until the dragon rears up, and then aims a shot right into the heart of the beast. %(dragon_name_full)s dies in terrible convulsions."]
        ]
    },

    'elf_witch': {
        'name': u"Forest witch",  # The name of the mob used ingame
        'power': {'base': (6, 0)},  # attack force (обычная, верная)
        'defence': {'base': (3, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'elf_witch',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The %(dragon_type)s sneaks as softly as he can, but sharp elven ears pick up even the slightest movement. With an explosion of gold-green flame, the forest sorceress soars into the trees and begins to weave a deadly spell."],
            [['foe_fear'],  u"The dragon gives off an aura of terror and darkness so strong that even the flowers and leaves wither around him. Unable to look into the eyes of the monster, the forest sorceress covers her face waiting to be taken and not thinking of resistance."],
            [['foe_dead', 'dragon_undamaged'], u"The enchantress encases herself in a thick shell of living tree bark, and knotted roots stretch out towards the dragon\'s claws. Against a person this might work, but the %(dragon_type)s easily breaks the wooden shell and pulls out the soft stuffing. The threat of the dragon\'s teeth is enough to stop the sorceress\'s tricks."],
            [['foe_dead', 'dragon_wounded'], u"The forest maiden beats the dragon with her shining staff hard enough to leave imprints, but %(dragon_name)s lashes his tail in response. The %(dragon_type)s remains standing while the sorceress falls writhing in pain and with ringing ears."],
            [['foe_alive', 'dragon_wounded'], u"The forest witch calls a variety of wild animals to her aid. In a fierce battle %(dragon_name_full)s wins a hard victory. The woman is unharmed, but the %(dragon_type)s is covered with blood."],
            [['foe_alive', 'dragon_undamaged'], u"The beautiful sorceress throws one spell after another at the dragon, but to no avail. %(dragon_name)s maneuvers around, wondering how to grab the girl without hurting her, because she needs to bear his children..."],
            [['foe_alive', 'lost_head'], u"Using the power of the earth the sorceress produces stone mouths full of sharp stalactites. One of them rips off the head of the dragon."],
            [['foe_dead', 'lost_head'], u"The forest sorceress meets the dragon with a glowing staff of green fire. The blow is so strong that %(dragon_name_full)s loses on of his heads, but he is not stopped and soon holds a lovely child of Danu on the ground."],
            [['dragon_dead'], u"The wounded %(dragon_type)s cannot overcome the sorceress\'s enchantments. %(dragon_name)s falls from a blow to the head from a thick oak branch, and then the furious beasts of the forest pounce on him."]
        ]
    },
    
    'footman': {
        'name': u"Infantry",  # The name of the mob used ingame
        'power': {'base': (3, 0)},  # attack force (обычная, верная)
        'defence': {'base': (5, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'footman',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"Infantry line up in a semicircle, clutching strong swords and spears."],
            [['foe_fear'],  u"When the dragon attacks the men at arms escape in all directions. By dumb luck, a few escape..."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name)s bursts into the formation of soldiers and begins to tear them to pieces. The disorganized fighters are unable to put up effective resistance."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s bursts into the formation of soldiers and begins to tear them to pieces. The disorganized fighters put up resistance, but the %(dragon_type)s emerges from the battle victorious, though wounded."],
            [['foe_alive', 'dragon_wounded'], u"Using organized tactics, the infantry manage to repulse the dragon, even inflicting serious injury. A few men are killed, but the rest are determined."],
            [['foe_alive', 'dragon_undamaged'], u"The infantry fight fiercely, and for a while they manage to keep the dragon at bay."],
            [['foe_alive', 'lost_head'], u"The %(dragon_type)s attacks thoughtlessly, exposing his back to several soldiers. This mistake costs him his head. Well, one of his heads..."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s is covered with serious injuries, the victory over the soldiers hurt him badly. One of his heads is mortally wounded."],
            [['dragon_dead'], u"The infantry pounce on the dragon all at once, frantically thrashing him with their swords. In a fit of rage the wounded %(dragon_type)s manages to kill a few enemies, but there are too many. %(dragon_name_full)s falls to the ground and breathes his last breath."]
        ]
    },

    'golem': {
        'name': u"Steel golem",  # The name of the mob used ingame
        'power': {'base': (7, 1)},  # attack force (обычная, верная)
        'defence': {'base': (5, 4)},  # damage resistance (обычная, верная)
        'modifiers': ['poison_immunity', 'fire_immunity', 'magic_immunity'],  # special modifiers
        'image': 'golem',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"A squat steel giant, resembling a living suit of armor, blocks the entire passage."],
            [['foe_fear'],  u"%(dragon_name_full)s gives off an aura of horror so great that even the steel guardian retreats before it."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name)s strikes the golem with such force that the steel breaks and cracks, rivets fly like bullets, and pieces of armor spill onto the ground with a crash. The nearly invincible guardian is defeated..."],
            [['foe_dead', 'dragon_wounded'], u"The %(dragon_type)s and golem compress each other in a deadly embrace of steel. The dragon\'s ribs crack, but the golem is weaker and caves in like a huge tin can."],
            [['foe_alive', 'dragon_wounded'], u"The nearly invulnerable ancient giant hammers the lizard with his iron fist."],
            [['foe_alive', 'dragon_undamaged'], u"The %(dragon_type)s and the golem hit each other hard, but both are so well protected that they escape with only minor wounds. The walls of the tunnel shake from this clash of giants."],
            [['foe_alive', 'lost_head'], u"The iron giant lifts his arms above his head, and dropping them like hammers on the dragon\'s head smashes it into paste."],
            [['foe_dead', 'lost_head'], u"In a hard struggle the %(dragon_type)s rips the shrieking steel body of the golem to pieces, leaving the guards fingers on the ground still grasping the dragon\'s head."],
            [['dragon_dead'], u"The iron giant lifts his arms above his head, and dropping them like hammers on the dragon\'s head smashes it into paste. %(dragon_name_full)s dies from his wounds."]
        ]
    },

    'griffin': {
        'name': u"Wild griffon",  # The name of the mob used ingame
        'power': {'base': (5, 0)},  # attack force (обычная, верная)
        'defence': {'base': (3, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'griffin',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The huge wild griffon spreads its eagle wings and draws sharp claws. There is fury in his eyes."],
            [['foe_fear'],  u"With a plaintive screech the wild griffon turns in the air and tries to escape, but the %(dragon_type)s catches and kills him with a single blow."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name)s swoops on the wild griffon like a hawk on a partridge. Feathers and blood fly in all directions."],
            [['foe_dead', 'dragon_wounded'], u"Clasped in the air like two cats, the %(dragon_type)s and the wild griffon fall to the ground. This blow is fatal to the griffon, and also injures the %(dragon_type)s."],
            [['foe_alive', 'dragon_wounded'], u"The %(dragon_type)s grabs the wild griffon\'s neck, but it thrusts back with its claws, nearly ripping open the dragon\'s belly. %(dragon_name)s flies back with a painful scream."],
            [['foe_alive', 'dragon_undamaged'], u"The wild griffon twists and somersaults in the air. The flying enemies are too busy fighting for a better position to meet hand to hand."],
            [['foe_alive', 'lost_head'], u"With a blow of its mighty talons the wild griffon slashes the dragon\'s throat. Not many creatures can survive such a blow, but %(dragon_name_full)s is one of them."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s wins the battle with the wild griffon, but one of his heads is dying from its wounds."],
            [['dragon_dead'], u"With a blow of its mighty talons the wild griffon slashes the dragon\'s throat. Even %(dragon_name_full)s can not survive such a blow."]
        ]
    },

    'griffin_rider': {
        'name': u"Griffon rider",  # The name of the mob used ingame
        'power': {'base': (9, 0)},  # attack force (обычная, верная)
        'defence': {'base': (7, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'griffin_rider',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The flying knight steers his mount upwards, preparing his lance and crossbow."],
            [['foe_fear'],  u"The sky knight flies away."], #hard to translate
            [['foe_dead', 'dragon_undamaged'], u"Rapidly drawing close to the flying knight, %(dragon_type)s knocks the rider out of his saddle with one precise blow. The uncontrolled griffon is easy prey without its knight, who is broken from such a high fall."],
            [['foe_dead', 'dragon_wounded'], u"The griffon and %(dragon_type)s collide head to head, like knights in a tournament. %(dragon_name)s is injured from a shattered lance, but the rider is knocked from his saddle and falls from a great height."], 
            [['foe_alive', 'dragon_wounded'], u"Keeping at a safe distance, the griffon rider fires at the dragon from his crossbow. One of his shots reaches its target."],
            [['foe_alive', 'dragon_undamaged'], u"The sky knight makes unbelievable twists and turn in the air. The flying enemies fight for a better position, not coming close enough to strike."], 
            [['foe_alive', 'lost_head'], u"Keeping at a safe distance, the griffon rider fires at the dragon from his crossbow. One of his shots hits the dragon in the eye!"],
            [['foe_dead', 'lost_head'], u"The griffon and %(dragon_type)s collide head to head, like knights in a tournament. The rider\'s lance enters the open mouth of the dragon inflicting a terrible wound, but he is knocked from his saddle and falls from a great height."],
            [['dragon_dead'], u"Wounded and weak, the %(dragon_type)s tries o land, but the flying knight catches him in the air and runs him through with a sharp lance."]
        ]
    },

    'heavy_cavalry': {
        'name': u"Heavy cavalry",  # The name of the mob used ingame
        'power': {'base': (8, 0)},  # attack force (обычная, верная)
        'defence': {'base': (6, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'heavy_cavalry',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"Clad in steel armor, the cavalry deploy into formation and level their spears."],
            [['foe_fear'],  u"%(dragon_name_full)s emits a terrifying roar and the horses of the cavalry scatter, throwing off and trampling their own riders."],
            [['foe_dead', 'dragon_undamaged'], u"One by one the crusaders attack the dragon, but %(dragon_name)s cleverly evades these awkward and predictable attacks. Flicking his tail like a gigantic whip the %(dragon_type)s kicks the cavalry out of their saddles."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s is able to overturn a horse and rider with a single blow, but there are so many of them that he does not leave the battle uninjured."],
            [['foe_alive', 'dragon_wounded'], u"The %(dragon_type)s is distracted by one of the armored riders and does not notice a second passing close, thrusting his lance into the scaled side of the lizard at full gallop."],
            [['foe_alive', 'dragon_undamaged'], u"The heavy cavalry deftly maneuvers, avoiding the fangs of the dragon, and trying to get him with their lances. Such tactics are unlikely to bring them victory, but they save lives."],
            [['foe_alive', 'lost_head'], u"The %(dragon_type)s knocks down an armored horse and rushes to the rider, but he quickly jumps on his feed and lands a perfect swing with a sharp sword. The head of the dragon falls to the ground. It\'s good that there are more heads in stock..."],
            [['foe_dead', 'lost_head'], u"In a fierce battle the %(dragon_type)s wins, but one of his heads lies on the field, severed by a heavy cavalry sword."],
            [['dragon_dead'], u"The wounded %(dragon_type)s tries to fight, but there are too many riders. After killing many men and horses, %(dragon_name_full)s finally falls to the ground, bleeding."]
        ]
    },

    'heavy_infantry': {
        'name': u"Heavy infantry",  # The name of the mob used ingame
        'power': {'base': (5, 0)},  # attack force (обычная, верная)
        'defence': {'base': (7, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'heavy_infantry',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"Iron armored troops are arrayed in a semicircle, strongly gripping two-handed swords."],
            [['foe_fear'],  u"When the dragon attacks the men at arms escape in all directions. By dumb luck, a few escape..."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name)s bursts into the formation of soldiers and begins to tear them to pieces. The disorganized fighters are unable to put up effective resistance."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s bursts into the formation of soldiers and begins to tear them to pieces. The scattered fighters put up resistance, but the %(dragon_type)s emerges from the battle victorious, though wounded."],
            [['foe_alive', 'dragon_wounded'], u"Using organized tactics, the heavy infantry manage to repulse the dragon, even inflicting serious injury. A few men are killed, but the rest are determined."],
            [['foe_alive', 'dragon_undamaged'], u"The heavy infantry fight fiercely, and for a while they manage to keep the dragon at bay."],
            [['foe_alive', 'lost_head'], u"The %(dragon_type)s attacks thoughtlessly, exposing his back to several soldiers. This mistake costs him his head. Well, one of his heads..."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s is covered with serious injuries, the victory over the armored soldiers hurt him badly. One of his heads is mortally wounded."],
            [['dragon_dead'], u"The heavy infantry pounce on the dragon all at once, frantically thrashing him with their two handed swords. In a fit of rage the wounded %(dragon_type)s manages to kill a few enemies, but there are too many. %(dragon_name_full)s falls to the ground and breathes his last breath."]
        ]
    },

    'ifrit': {
        'name': u"Fire giant",  # The name of the mob used ingame
        'power': {'base': (6, 1)},  # attack force (обычная, верная)
        'defence': {'base': (5, 2)},  # damage resistance (обычная, верная)
        'modifiers': ['fire_immunity', 'sfatk_2up'],  # special modifiers
        'image': 'ifrit',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The fire giants eyes glow like coals. He tightens his grip on his fiery hammer, and flashes of smoky red flame cover him from head to toe."],
            [['foe_fear'],  u"The fire giant is for a while motionless, frightened by the appearance of the dragon. Then he disappears in a flash of flame, leaving a trail of black smoke like a puff from a pipe."],
            [['foe_dead', 'dragon_undamaged'], u"The fire giant is powerless - %(dragon_name_full)s is the victor."],
            [['foe_dead', 'dragon_wounded'], u"The %(dragon_type)s engages the fire giant in melee. Fierce flames envelop both fighters and although %(dragon_name)s is terribly burnt, he emerges from the fight victorious."],
            [['foe_alive', 'dragon_wounded'], u"The fire giant\'s hammer strikes with such overwhelming force that the %(dragon_type)s flies into the corner like a kicked dog."],
            [['foe_alive', 'dragon_undamaged'], u"Steel and flame against scales and fangs. For a while the fighting is equal, and it seems like neither side can win this battle."],
            [['foe_alive', 'lost_head'], u"With a powerful hammer blow the fire giant smashes one of the dragon\'s heads like a ripe watermelon. The %(dragon_name_full)s miraculously survives."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s wins, but one of his heads is dying from its wounds."],
            [['dragon_dead'], u"The wounded %(dragon_type)s overestimated his strength. The fire giant easily overwhelms him, easily breaking him on the volcanic ground with his fiery hammer."]
        ]
    },

    'jotun': {
        'name': u"Frost giant",  # The name of the mob used ingame
        'power': {'base': (6, 1)},  # attack force (обычная, верная)
        'defence': {'base': (5, 2)},  # damage resistance (обычная, верная)
        'modifiers': ['siatk_2up', 'ice_immunity'],  # special modifiers
        'image': 'jotun',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The blue haired giant with a horned helmet tightly grips an axe covered with frost."],
            [['foe_fear'],  u"%(dragon_name_full)s gives off such an aura of fear and panic that the frost giant runs away."],
            [['foe_dead', 'dragon_undamaged'], u"The giant is too slow. As he swings his huge axe, the %(dragon_type)s unleashes an onslaught. With several deadly snakelike strikes, the outcome of the battle is decided."],
            [['foe_dead', 'dragon_wounded'], u"The giant\'s huge axe crashes into a wall, getting stuck in a crack. %(dragon_name)s immediately rushes forward, trying to use the opportunity to engage in melee. The unarmed frost giant still manages to break some of the dragon\'s bones, but he is not as strong, and %(dragon_name_full)s wins."],
            [['foe_alive', 'dragon_wounded'], u"The frost giant breaks a giant icicle from the ceiling and throws it like a dart. The blow is not fatal, but very painful."],
            [['foe_alive', 'dragon_undamaged'], u"The giant swings his frosty axe in a frenzy, preventing the dragon from coming closer."],
            [['foe_alive', 'lost_head'], u"With one mighty blow of his frost covered axe the frost giant severs one of the dragon\'s heads. But %(dragon_name_full)s is able to survive even such a wound!"],
            [['foe_dead', 'lost_head'], u"During the heaviest fighting %(dragon_name_full)s overcomes the giant, but one of his heads is dying from wounds received in the battle."],
            [['dragon_dead'], u"The wounded %(dragon_type)s fights to his last, but the frost giant gets the better of him. With a mighty blow of his ice axe, he cuts the dragon in half!"]
        ]
    },

    'jagger': {
        'name': u"Huntsman",  # The name of the mob used ingame
        'power': {'base': (3, 0)},  # attack force (обычная, верная)
        'defence': {'base': (1, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'jagger',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The huntsman nocks an arrow."],
            [['foe_fear'],  u"The huntsman runs away in terror. He\'s not ready for this fight."],
            [['foe_dead', 'dragon_undamaged'], u"The huntsman manages to fire three times before %(dragon_name)s reaches him. But the missiles simply bounce of the scaly skin of the dragon. At close range, he has no protection against the lizard\'s teeth."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s opens his jaws to roar, and an arrow punctures his soft mouth. Unable to bite, the %(dragon_type)s angrily beats the archer to death with his tail."],
            [['foe_alive', 'dragon_wounded'], u"The sharpshooting archer manages to hit the lizard right in the eye. The lizard stops, going mad with pain."],
            [['foe_alive', 'dragon_undamaged'], u"The archer\'s arrows glance off the natural armor of the dragon."],
            [['foe_alive', 'lost_head'], u"A tempered arrow with a fire hardened shaft pierces through one of the dragon\'s mouths and into a brain. Luckily, %(dragon_name_full)s can survive such a wound."],
            [['foe_dead', 'lost_head'], u"%(dragon_type_cap)s wins, but one of his heads is withering from its wounds."],
            [['dragon_dead'], u"The archer looses a tempered arrow with a fire hardened shaft, and it pierces through one the dragon\'s mouth and into his brain. %(dragon_name_full)s falls dead."]
        ]
    },

    'knight': {
        'name': u"Knight",  # The name of the mob used ingame
        'descriptions': [
            [['foe_intro'], u"%(foe_name)s is ready to fight."],
            [['foe_fear'], u"%(foe_name)s runs in fear."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name_full)s triumphs"],
            [['foe_dead', 'dragon_wounded'], u"%(foe_name)s injures the dragon, but %(dragon_name)s emerges victorious."],
            [['foe_alive', 'dragon_wounded'], u"%(foe_name)s seriously wounds the dragon."],
            [['foe_alive', 'dragon_undamaged'], u"The fight continues for some time, but neither side gains the advantage."],
            [['foe_alive', 'lost_head'], u"%(foe_name)s hits the dragon\'s head with a well aimed blow."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s wins, but one of his heads is dying from its wounds."],
            [['dragon_dead'], u"%(dragon_name_full)s dies of his wounds."]
        ],
    },
    
    'king': {
        'name': u"Warrior king",  # The name of the mob used ingame
        'power': {'base': (5, 2)},  # attack force (обычная, верная)
        'defence': {'base': (6, 1)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'king',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"%(dragon_name_full)s breaks through the ranks of the men guarding the king and prepares to strike."],
            [['foe_fear'],  u"The brave king is spoiling for a fight, but his horse is too scared - it rears up on its hind legs and throws the rider into the mud, leaving him defenseless."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name)s deftly doges the king\'s sharps spear and with a swift attack knocks him from his saddle."],
            [['foe_dead', 'dragon_wounded'], u"The %(dragon_type)s and the king of the people collide with a terrible crash. The noble rider topples from his horse, but %(dragon_name)s is injured."],
            [['foe_alive', 'dragon_wounded'], u"The impact of the spear, with the weight and speed of the horse and rider behind it, throws the dragon aside."],
            [['foe_alive', 'dragon_undamaged'], u"Metal grinds and the horse whinnies as the opponents battle, but the match is roughly equal."],
            [['foe_alive', 'lost_head'], u"The king of the people cripples the dragon\'s head with a well-aimed blow, but the fight is not yet over."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s wins, but one of his heads is dying from its wounds."],
            [['dragon_dead'], u"The king of the people smashes the dragon\'s head with a well-aimed blow. %(dragon_name_full)s lies dying."]
        ]
    },
    
    'kraken': { #Translator: I don't think this fight is implemented
        'name': u"Kraken",  # The name of the mob used ingame
        'power': {'base': (6, 3)},  # attack force (обычная, верная)
        'defence': {'base': (6, 3)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'kraken',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The enemy is preparing to fight."],
            [['foe_fear'],  u"The enemy flees in fear."],
            [['foe_dead', 'dragon_undamaged'], u"(flawless victory) \n %(dragon_name_full)s побеждает"],
            [['foe_dead', 'dragon_wounded'], u"The enemy inflicts injuries on the dragon, but %(dragon_name)s emerges victorious."],
            [['foe_alive', 'dragon_wounded'], u"The enemy inflicts serious injuries on the dragon."],
            [['foe_alive', 'dragon_undamaged'], u"The fight continues for some time, but neither side gains the advantage."],
            [['foe_alive', 'lost_head'], u"The enemy aims a blow at the dragon\'s head."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s wins, but one of his heads is dying from its wounds."],
            [['dragon_dead'], u"%(dragon_name_full)s dies of his wounds."]
        ]
    },

    'merman': {
        'name': u"Shoal guard",  # The name of the mob used ingame
        'power': {'base': (3, 0)},  # attack force (обычная, верная)
        'defence': {'base': (1, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'merman',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The merman prepares to fight with a net and trident. He will not give up so easily."],
            [['foe_fear'],  u"Turning pale with fear the merman swims into the depths, dropping his trident."],
            [['foe_dead', 'dragon_undamaged'], u"Easily dodging a blow from the trident, the %(dragon_type)s bites down with a death grip. The water turns red with blood."],
            [['foe_dead', 'dragon_wounded'], u"The underwater warrior intercepts the charging dragon with his trident, but even wounded %(dragon_name)s is able to tear him to pieces in seconds."],
            [['foe_alive', 'dragon_wounded'], u"Using his extraordinary speed and agility the merman manages to hit the dragon with his trident and evade counterattacks."],
            [['foe_alive', 'dragon_undamaged'], u"For a while both opponents maneuver in the water, but neither finds a good position to attack from."],
            [['foe_alive', 'lost_head'], u"Avoiding several blows from the dragon\'s powerful tail, the sea dweller plunges his trident deep into the dragon\'s mouth."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s wins, but one of his heads is dying from its wounds.."],
            [['dragon_dead'], u"%(dragon_name_full)s dies of his wounds.."]
        ]
    },

    'militia': {
        'name': u"Militia",  # The name of the mob used ingame
        'power': {'base': (2, 0)},  # attack force (обычная, верная)
        'defence': {'base': (4, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'militia',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"Armed with spears, axes, and torches, the militia gathers in a dense crowd, encouraging each other with aggressive shouts."],
            [['foe_fear'],  u"The militia gathered to repel the monster scatter in fear as soon as %(dragon_name_full)s approaches within striking distance."],
            [['foe_dead', 'dragon_undamaged'], u"The disorganized militiamen are unable to resist the onslaught of the dragon for long. A few manage to escape, but the majority lie lifeless."],
            [['foe_dead', 'dragon_wounded'], u"Breaking into the crowd of peasants the %(dragon_type)s begins a real massacre. However, the people fight back surprisingly bravely, and after such a victory %(dragon_name)s must go lick his wounds."],
            [['foe_alive', 'dragon_wounded'], u"With enough fighting spirit even a hastily trained militia becomes a serious fighting force. They easily throw back and injure the dragon with their weapons."],
            [['foe_alive', 'dragon_undamaged'], u"The %(dragon_type)s bursts into a crowd of peasants, but they immediately scatter around him. While fighting one enemy, another comes from behind. The fire, smoke, and shouts confuse him. This battle threatens to drag."],
            [['foe_alive', 'lost_head'], u"A big lumberjack with an axe seizes the moment and jumps on the back of the wounded dragon, and with a powerful blow cuts off one of his heads!"],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s wins, but one of his heads is dying from its wounds."],
            [['dragon_dead'], u"%(dragon_name_full)s dies of his wounds... the farmers will sing of this day for centuries!"]
        ]
    },

    'mob': {
        'name': u"Mob",  # The name of the mob used ingame
        'power': {'base': (1, 0)},  # attack force (обычная, верная)
        'defence': {'base': (5, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'mob',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"Armed with pitchforks and torches peasants crowd closely together, encouraging each other with aggressive shouts."],
            [['foe_fear'],  u"The mob of farmers gathered to repel the monster scatter in fear as soon as %(dragon_name_full)s approaches within striking distance."],
            [['foe_dead', 'dragon_undamaged'], u"The disorganized farmers are unable to resist the onslaught of the dragon for long. A few manage to escape, but the majority lie lifeless."],
            [['foe_dead', 'dragon_wounded'], u"Breaking into the crowd of peasants the %(dragon_type)s begins a real massacre. However, the people fight back surprisingly bravely, and after such a victory %(dragon_name)s must go lick his wounds."],
            [['foe_alive', 'dragon_wounded'], u"With enough fighting spirit even untrained peasants become a serious fighting force. They easily throw back and injure the dragon with their weapons."],
            [['foe_alive', 'dragon_undamaged'], u"The %(dragon_type)s bursts into a crowd of peasants, but they immediately scatter around him. While fighting one enemy, another comes from behind. The fire, smoke, and shouts confuse him. This battle threatens to drag."],
            [['foe_alive', 'lost_head'], u"A big lumberjack with an axe seizes the moment and jumps on the back of the wounded dragon, and with a powerful blow cuts off one of his heads!"],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s wins, but one of his heads is dying from its wounds."],
            [['dragon_dead'], u"%(dragon_name_full)s dies of his wounds... the farmers will sing of this day for centuries!"]
        ]
    },

    'mounted_guard': {
        'name': u"Mounted guard",  # The name of the mob used ingame
        'power': {'base': (5, 0)},  # attack force (обычная, верная)
        'defence': {'base': (7, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'mounted_guard',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"Clad in steel armor, the cavalry deploy into formation and level their spears."],
            [['foe_fear'],  u"%(dragon_name_full)s emits a terrifying roar and the horses of the mounted guard scatter, throwing off and trampling their own riders."],
            [['foe_dead', 'dragon_undamaged'], u"One by one the heavy riders attack the dragon, but %(dragon_name)s cleverly evades these awkward and predictable attacks. Flicking his tail like a gigantic whip %(dragon_type)s kicks the cavalry out of their saddles."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s is able to overturn a horse and rider with a single blow, but there are so many of them that he does not leave the battle uninjured."],
            [['foe_alive', 'dragon_wounded'], u"The %(dragon_type)s is distracted by one of the riders and does not notice a second passing close, thrusting his lance into the scaled side of the lizard at full gallop."],
            [['foe_alive', 'dragon_undamaged'], u"The mounted guardsmen deftly maneuver, avoiding the fangs of the dragon, and trying to get him with their lances. Such tactics are unlikely to bring them victory, but they save lives."],
            [['foe_alive', 'lost_head'], u"The %(dragon_type)s knocks down an armored horse and rushes to the rider, but he quickly jumps on his feet and lands a perfect swing with a sharp sword. The head of the dragon falls to the ground. It\'s a good thing there are more heads in stock..."],
            [['foe_dead', 'lost_head'], u"In a fierce battle the %(dragon_type)s wins, but one of his heads lies on the field, severed by a heavy cavalry sword."],
            [['dragon_dead'], u"The wounded %(dragon_type)s tries to fight, but there are too many riders. After killing many men and horses, %(dragon_name_full)s finally falls to the ground, bleeding."]
        ]
    },


    'ogre': {
        'name': u"Ogre",  # The name of the mob used ingame
        'power': {'base': (7, 0)},  # attack force (обычная, верная)
        'defence': {'base': (7, 0)},  # damage resistance (обычная, верная)
        'modifiers': ['poison_immunity'],  # special modifiers
        'image': 'ogre',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The ogre clutches an enormous club, almost an uprooted tree."],
            [['foe_fear'],  u"Considering the enemy, the ogre shirks and retreats."],
            [['foe_dead', 'dragon_undamaged'], u"The clumsy giant deals powerful, methodical blows in a pattern that is easy to figure out. Moving like flowing mercury, %(dragon_name)s attacks over and over, pulling bloody chunks out of the ogre\'s body. The man eating giant had no chance..."],
            [['foe_dead', 'dragon_wounded'], u"Not wanting to risk a strike from the club, %(dragon_name)s jumps on the ogre, grappling viciously. This strategy is successful, though the dragon suffers many blows from the giant\'s fists."],
            [['foe_alive', 'dragon_wounded'], u"A sweeping strike from the giant\'s cudgel casts the dragon aside. %(dragon_name)s hisses from the pain."],
            [['foe_alive', 'dragon_undamaged'], u"The ogre howls and waves his huge club like a reed in all directions. Moving closer to him is dangerous so the %(dragon_type)s circles around, waiting for the right moment to attack."],
            [['foe_alive', 'lost_head'], u"A blow from the the giant\'s club is so heavy that it breaks the neck of the dragon, completely crippling one of his heads. Luckily, %(dragon_name_full)s is able to survive."],
            [['foe_dead', 'lost_head'], u"In a fierce battle with the ogre the %(dragon_type)s wins, but one of his heads is broken from a mighty blow of the giant\'s club."],
            [['dragon_dead'], u"The wounded %(dragon_name)s fights bravely, but the ogre gains the upper hand. His huge club goes up and down again and again until the lizard is stamped down into a gory mess of blood and bones..."]
        ]
    },

    'old_knight': {
        'name': u"Old knight",  # The name of the mob used ingame
        'power': {'base': (4, 0)},  # attack force (обычная, верная)
        'defence': {'base': (2, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'knight/knight1',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The old knight puts a bucket-like helmet on his head and picks up a two-handed sword with a shabby hilt. He is determined to defend his home."],
            [['foe_fear'],  u"Seeing the enemy he has to fight, the old knight runs away, dropping his weapon."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name)s fiercely strikes the knight\'s armor, bending it like paper. The old man is too slow to win the battle with the dragon - his best years are long past."],
            [['foe_dead', 'dragon_wounded'], u"With a scathing attack of his tail, %(dragon_name)s knocks the sword from the hands of the old knights and pounces on him to finish him. But before he gives up the ghost, the veteran manages to stick a knife into the dragon\'s belly!"],
            [['foe_alive', 'dragon_wounded'], u"Years of combat experience allow the old knight to judge very accurately when to attack. The %(dragon_type)s barely begins to move forward when he is hit by a stroke of the two-handed sword."],
            [['foe_alive', 'dragon_undamaged'], u"The fight continues for some time, but neither side gains the advantage.."],
            [['foe_alive', 'lost_head'], u"Years of combat experience allow the old knight to judge very accurately when to attack. The %(dragon_type)s barely begins to move forward when he is hit by a stroke of the two-handed sword, losing one of his heads."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s wins, but one of his heads is dying from its wounds."],
            [['dragon_dead'], u"%(dragon_name_full)s dies of his wounds.."]
        ]
    },


    'palace_guards': {
        'name': u"Palace guards",  # The name of the mob used ingame
        'power': {'base': (5, 1)},  # attack force (обычная, верная)
        'defence': {'base': (6, 2)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'castle_guard',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The palace is protected by elite royal guards. They bravely face the dragon in open battle, not wanting to sit behind walls."],
            [['foe_fear'],  u"When the dragon attacks, the royal guards flee in all directions. The gates of the fortress are wide open..."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name)s bursts into the formation of soldiers and begins to tear them to pieces. Even the king\'s knights are unable to put up decent resistance to this dreadful onslaught."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s bursts into the formation of soldiers and begins to tear them to pieces. The scattered fighters put up fierce resistance, but the %(dragon_type)s emerges from the battle victorious, though wounded."],
            [['foe_alive', 'dragon_wounded'], u"Using organized tactics, the palace guards manage to repulse the dragon, even inflicting serious injury. A few men are killed, but the rest are determined."],
            [['foe_alive', 'dragon_undamaged'], u"The guards fight desperately, and for a while they manage to keep the dragon at bay."],
            [['foe_alive', 'lost_head'], u"The %(dragon_type)s attacks thoughtlessly, exposing his back to several heavily armed guards. This mistake costs him his head. Well, one of his heads..."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s is covered with serious injuries, the victory over the palace guard hurt him badly. One of his heads has been chopped off by a two-handed sword."],
            [['dragon_dead'], u"The heavy infantry pounce on the dragon all at once, frantically thrashing him with their gilded swords. In a fit of rage the wounded %(dragon_type)s manages to kill a few enemies, but there are too many. %(dragon_name_full)s falls to the ground and breathes his last breath."]
        ]
    },
    
    'shark': {
        'name': u"Shark",  # The name of the mob used ingame
        'power': {'base': (3, 0)},  # attack force (обычная, верная)
        'defence': {'base': (3, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'shark',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The shark swims in circles and grins."],
            [['foe_fear'],  u"The shark times to swim away, but the %(dragon_type)s swims faster and overtakes him. The predator becomes the prey."],
            [['foe_dead', 'dragon_undamaged'], u"Grabbing the shark by the gills %(dragon_name)s completely breaks its resistance. The marine predator is unable to do anything but gnash its teeth."],
            [['foe_dead', 'dragon_wounded'], u"The two terrible sea predators weave around each other in the depths, wounding each other with their teeth. The salt water is red with blood, but %(dragon_name)s emerges victorious from the fight fight."],
            [['foe_alive', 'dragon_wounded'], u"Using his speed and maneuverability, the shark lures the dragon into murky water, and then suddenly speeds by, tearing off a chunk of the dragon!"],
            [['foe_alive', 'dragon_undamaged'], u"The two terrible sea predators circle each other in the water, each trying to attack the other from behind. So far they are equal..."],
            [['foe_alive', 'lost_head'], u"The shark bites off one of the dragon\'s heads!"],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s wins, but one of his heads is dying from its wounds..."],
            [['dragon_dead'], u"%(dragon_name_full)s dies of his wounds.."]
        ]
    },


    'ship': {
        'name': u"Ship",  # The name of the mob used ingame
        'power': {'base': (3, 0)},  # attack force (обычная, верная)
        'defence': {'base': (4, 1)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'ship',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"On the deck of a ship a frantic boatswain whistles. "],
            [['foe_fear'],  u"Unfurling every sail it has, the merchant ship turns against the wind and flees from the dragon at top speed. But it is too heavy laden, so that proves to be a mistake. After a brief chase %(dragon_name_full)s catches and sinks the vessel."],
            [['foe_dead', 'dragon_undamaged'], u"Hiding in the ocean depths, %(dragon_name)s swims under the bottom of the vessel and smashes a hole in it at top speed. Now you can catch the escaping sailors one by one."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s dives into the depths, but not quickly enough. The merchant ship has time for one volley, and cannonballs break the dragon\'s ribs. The furious %(dragon_type)s rips off a section of the ship\'s hull under the waterline. The ocean quickly rushes in, and the merchant ship is doomed."],
            [['foe_alive', 'dragon_wounded'], u"Coordinated volleys of cannonfire smash into the dragon and he is forced to retreat, throwing up swirling columns of water."],
            [['foe_alive', 'dragon_undamaged'], u"%(dragon_name)s dives under the ship and tries to punch a hole below the waterline, but to no avail."],
            [['foe_alive', 'lost_head'], u"A cast-iron bomb stuffed with black powder detonates directly on the dragon\'s forehead. From such a wound few can recover..."],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s climbs onto the deck of the ship and happily makes a bloodbath out of the crew. The sailors scatter in panic, and in his enthusiastic pursuit %(dragon_name)s fails to notice the captain climbing on a yardarm. Jumping from above, the captain slices off the dragon\'s head with a blow from his sword. Unfortunately for him, it isn\'t enough for victory. The merchant ship is doomed."],
            [['dragon_dead'], u"%(dragon_name_full)s is too weak to withstand another volley from the warship. Pummeled by iron projectiles, the dragon sinks beneath the depths, no longer able to cling to life."]
        ]
    },


    'steamgun': {
        'name': u"Steam cannon",  # The name of the mob used ingame
        'power': {'base': (5, 5)},  # attack force (обычная, верная)
        'defence': {'base': (4, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'steamgun',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The dwarves are busy with their steam gun, preparing it to fire."],
            [['foe_fear'],  u"Hearing the thunderous roar of the dragon, the steam gun engineers flee, leaving the powerful fighting machine standing as a useless piece of junk."],
            [['foe_dead', 'dragon_undamaged'], u"Zigzagging, %(dragon_name)s closes with the steam cannon, avoiding its deadly shells. When the distance has shrunk to a minimum the panicking engineers try to escape, but it is too late..."],
            [['foe_dead', 'dragon_wounded'], u"Deciding to destroy the hated siege engine in one stroke the %(dragon_type)s shatters it into pieces, but the exploding boiler injures the dragon more than the gunfire did!"],
            [['foe_alive', 'dragon_wounded'], u"Explosive shells strike the dragon directly in the chest, throwing him back from the steam gun."],
            [['foe_alive', 'dragon_undamaged'], u"The steam gun fires rapidly and continuously. %(dragon_name)s maneuvers around, not daring to approach."],
            [['foe_alive', 'lost_head'], u"A powerful high explosive shell falls directly onto the dragon\'s head, blasting it into bloody chunks."],
            [['foe_dead', 'lost_head'], u"A powerful high explosive shell falls directly onto the dragon\'s head, blasting it into bloody chunks. But %(dragon_name_full)s is not stopped, and breaks through to the defenseless engineers."],
            [['dragon_dead'], u"Pummeled by explosions %(dragon_name)s slow and stumbles. He is no longer able to fight. A final shell rends his only living head asunder."]
        ]
    },

    'templars': {
        'name': u"Templars",  # The name of the mob used ingame
        'power': {'base': (8, 0)},  # attack force (обычная, верная)
        'defence': {'base': (6, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'templars',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"Clad in steel armor, the templars deploy into formation and level their spears."],
            [['foe_fear'],  u"%(dragon_name_full)s emits a terrifying roar and the horses of the crusaders scatter, throwing off and trampling their own riders."],
            [['foe_dead', 'dragon_undamaged'], u"One by one the crusaders attack the dragon, but %(dragon_name)s cleverly evades these awkward and predictable attacks. Flicking his tail like a gigantic whip the %(dragon_type)s kicks the cavalry out of their saddles."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s is able to overturn a horse and rider with a single blow, but there are so many of them that he does not leave the battle uninjured."],
            [['foe_alive', 'dragon_wounded'], u"The %(dragon_type)s is distracted by one of the crusaders and does not notice a second passing close, thrusting his lance into the scaled side of the lizard at full gallop."],
            [['foe_alive', 'dragon_undamaged'], u"The crusaders deftly maneuver, avoiding the fangs of the dragon, and trying to get him with their long lances. Such tactics are unlikely to bring them victory, but they save lives."],
            [['foe_alive', 'lost_head'], u"The %(dragon_type)s knocks down an armored horse and rushes to the rider, but he quickly jumps to his feet and lands a perfect swing with a sharp sword. The head of the dragon falls to the ground. It\'s a good thing there are more heads in stock..."],
            [['foe_dead', 'lost_head'], u"In a fierce battle the %(dragon_type)s wins, but one of his heads lies on the field, severed by a blessed sword."],
            [['dragon_dead'], u"The wounded %(dragon_type)s tries to fight, but there are too many riders. After killing many men and horses, %(dragon_name_full)s finally falls to the ground, bleeding."]
        ]
    },

    'titan': {
        'name': u"Titan",  # The name of the mob used ingame
        'power': {'base': (8, 1)},  # attack force (обычная, верная)
        'defence': {'base': (8, 2)},  # damage resistance (обычная, верная)
        'modifiers': ['lightning_immunity', 'slatk_2up'],  # special modifiers
        'image': 'titan',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"Clad in golden armor the titan calls on the forces of wind and thunder. He is as strong with with magic as he is with physical force!"],
            [['foe_fear'],  u"Even the godlike titan runs in fear when %(dragon_name_full)s attacks."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name)s breaks through the sheets of lightning and doesn\'t even seem to notice the gale-force winds. The titan raises his shield and and points his spear, but the %(dragon_type)s swipes the titan\'s legs with his tail, and then attacks the helplessly overturned giant."],
            [['foe_dead', 'dragon_wounded'], u"The sky darkens and the air smells of the thunder as the two giants face each other in a deadly battle. The titan strikes with lightning and a magic spear, putting wounds in the dragon, but %(dragon_name_full)s is stronger. The giant falls prostrate on the ground, bleeding bright blue blood."],
            [['foe_alive', 'dragon_wounded'], u"The titan throws a sheet of sparkling lighting at the dragon, and slams it back with a gust of hurricane wind."],
            [['foe_alive', 'dragon_undamaged'], u"Powerful gusts of wind protect the titan, giving the dragon no chance to approach within striking distance."],
            [['foe_alive', 'lost_head'], u"The wounded %(dragon_type)s manages to break through the gusts of gale and reach the giant, but the titan meets him with a well aimed spear blow directly into his open jaws!"],
            [['foe_dead', 'lost_head'], u"%(dragon_name_full)s fights with his last strength and incredible rage and anger. The titan pierces one of his heads, but cannot stop the fury of the dragon, and falls to the ground."],
            [['dragon_dead'], u"The titan invokes the power of storm in his spear and thrusts it into the wounded dragon. %(dragon_name_full)s looks with darkening eyes at the black pole sticking from his chest, thick as an age-old oak tree."]
        ]
    },

    'town': {
        'name': u"Town defenders",  # The name of the mob used ingame
        'power': {'base': (4, 0)},  # attack force (обычная, верная)
        'defence': {'base': (6, 1)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'town',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The town defenders take their places on the walls. They prepare spears, heavy stones, and cauldrons of boiling tar."],
            [['foe_fear'],  u"Looking at the dragon the town defenders waver. They flee in panic from the walls, looking for somewhere, anywhere to hide, and the battle is over before it even begins."],
            [['foe_dead', 'dragon_undamaged'], u"Under a useless hail of stones, spears, and arrows, %(dragon_name_full)s approaches the gates and rams through them with all his weight. The remaining soldiers are exposed to the fury of the dragon."],
            [['foe_dead', 'dragon_wounded'], u"Under a hail of stones, spears, and arrows, %(dragon_name_full)s approaches the gates and rams through them with all his weight. The missiles of the defenders covered the dragon\'s body with wounds, but with the gate fallen there is nothing left to stop him."],
            [['foe_alive', 'dragon_wounded'], u"The hail of stones, arrows, and spears from the walls and towers is so heavy that the dragon is forced to pull back from the gate. Taking this fortress will not be so easy..."],
            [['foe_alive', 'dragon_undamaged'], u"The %(dragon_type)s leans all his weight on the gates, trying to break through them as the defenders pour stones, spears, and arrows on the dragon. But both are completely ineffective. The projectiles glance off the dragon\'s scales, and the steel gates will not give in."],
            [['foe_alive', 'lost_head'], u"Five stalwart defenders throw a thick tree trunk from the wall, which crushes one of the dragon\'s heads."],
            [['foe_dead', 'lost_head'], u"Five stalwart defenders throw a thick tree trunk from the wall, which crushes one of the dragon\'s heads. But it is useless, the furious %(dragon_type)s breaks the gates and rushes into the town."],
            [['dragon_dead'], u"%(dragon_name_full)s is too tired and wounded for such a battle. Just one well aimed stone from the walls stops his assault. The brave town defenders celebrate victory as %(dragon_name_full)s dies at the unyielding gates."]
        ]
    },

    'treant': { 
        'name': u"Tree ent",  # The name of the mob used ingame
        'power': {'base': (12, 0)},  # attack force (обычная, верная)
        'defence': {'base': (8, 2)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'treant',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The human shaped tree looks frightening. His gnarled hand-branches stretch out for the neck of the dragon."],
            [['foe_fear'],  u"Twisting his rooted feet out of the ground, the humanoid tree runs away, trying to disguise himself in the forest. He leaves behind a trail of plowed earth."],
            [['foe_dead', 'dragon_undamaged'], u"%(dragon_name_full)s manages to topple the treant, and tears chunk after chunk of bark out of it until it reaches the relative softness of sapwood. Sweet, sticky treant-sap flies in all directions."],
            [['foe_dead', 'dragon_wounded'], u"The treant\'s hands wrap themselves around the dragon\'s neck too low, and though it does serious damage it is bitten over and over again in the process, finally succumbing as a waterfall of sap pours from gaping holes in it\'s form."],
            [['foe_alive', 'dragon_wounded'], u"The treant's hand-branches leave long, painful gouges in the dragon's flesh."],
            [['foe_alive', 'dragon_undamaged'], u"The dragon circles the treant warily, staying out of reach of the enormous hand-branches."],
            [['foe_alive', 'lost_head'], u"The treant manages to tear one of the dragon\'s heads clean off."],
            [['foe_dead', 'lost_head'], u"The treant succeeds in fatally throtting one of the dragon\'s heads, but neglected to defend itself from other angles, and it is quickly torn apart by jagged teeth."],
            [['dragon_dead'], u"%(dragon_name_full)s succumbds to thorttling by the enraged tree."]
        ]
    },

    'triton': {
        'name': u"Triton",  # The name of the mob used ingame
        'power': {'base': (7, 1)},  # attack force (обычная, верная)
        'defence': {'base': (7, 1)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'triton',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The sea giant moves his enormous trident and the water responds, swirling in whirlpools and boiling towers of foam. The triton commands the abyss!"],
            [['foe_fear'],  u"The triton lifts his magic trident and calls forth a huge school of tuna. The bodies of the fish block it from view, and when they swim away, it is nowhere to be seen. The coward escaped!"],
            [['foe_dead', 'dragon_undamaged'], u"The triton creates a seething maelstrom, trying to pull the dragon to the bottom, but %(dragon_name)s overcomes the force of the water and bites his teeth into the startled triton."],
            [['foe_dead', 'dragon_wounded'], u"Swimming through a whirlpool, %(dragon_name)s rushes towards the triton. He is struck hard by its trident, but it doesn\'t stop the furious dragon. %(dragon_name)s tears the sea giant into pieces."],
            [['foe_alive', 'dragon_wounded'], u"%(dragon_name)s cannot cope with the magic whirlpool of the triton, and the churning water dashes him onto the jagged reefs."],
            [['foe_alive', 'dragon_undamaged'], u"%(dragon_name)s tries in vain to reach the triton, but over and over the whirlpools pull him back towards the depths."],
            [['foe_alive', 'lost_head'], u"The triton strikes accurately with his trident, spitting the dragon\'s neck like a fish on its tip."],
            [['foe_dead', 'lost_head'], u"The two sea giants face each other in battle. With great difficulty the %(dragon_type)s wins, but one of his heads is dying, punctured by the huge trident of the triton."],
            [['dragon_dead'], u"The wounded %(dragon_name)s is no longer able to resist the magic whirlpool. Relentless currents of water carry him down into the cold and dark depths."]
        ]
    },

    'wizard': {
        'name': u"Wizard",  # The name of the mob used ingame
        'power': {'base': (5, 0)},  # attack force (обычная, верная)
        'defence': {'base': (1, 0)},  # damage resistance (обычная, верная)
        'modifiers': ['sfatk_up', 'siatk_up', 'slatk_up'],  # special modifiers
        'image': 'wizard',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"The wizard makes strange gestures with his hands, applying protective spells."],
            [['foe_fear'],  u"The wizard assesses the situation and decides to use emergency teleportation to escape the furious dragon."],
            [['foe_dead', 'dragon_undamaged'], u"The sorcerer uses a fireball spell, but the magical flames do nothing. Cutting through the fire, the %(dragon_type)s squashes the frail old man like a bug!"],
            [['foe_dead', 'dragon_wounded'], u"The warlock shoots arrows of pure magical power, easily puncturing the dragon\'s scales. But even wounded, %(dragon_name)s is able to tear the frail old man to bloody shreds."],
            [['foe_alive', 'dragon_wounded'], u"The sorcerer conjures a huge ghostly fist that falls on the dragon with the weight of an ore-laden minecart."],
            [['foe_alive', 'dragon_undamaged'], u"The sorcerer calls a stone elemental to protect him. %(dragon_name_full)s deals with the spirit of the earth for a few minutes, as the wizard stands safe and sound on the sidelines."],
            [['foe_alive', 'lost_head'], u"The wizard summons a sword of pure magic energy. The blade flies and cuts by itself, and it is so sharp that it cleanly slices through one of the dragon\'s heads."],
            [['foe_dead', 'lost_head'], u"The wizard summons a sword of pure magic energy. The blade flies and cuts by itself, and it is so sharp that it cleanly slices through one of the dragon\'s heads. However, this is of no help to the wizard, the %(dragon_name)s survives the wound and crushes him like a cockroach."],
            [['dragon_dead'], u"Weakened and wounded, the %(dragon_type)s is an easy target. The wizard calls a 9th level sphere of total annihilation, which consumes the lizard\'s body like a miniature black hole."]
        ]
    },

    'xbow': {
        'name': u"Арбалетчики",  # The name of the mob used ingame
        'power': {'base': (4, 0)},  # attack force (обычная, верная)
        'defence': {'base': (4, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'xbow',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"Crossbowmen hastily load their weapons, preparing to fire."],
            [['foe_fear'],  u"The crossbowmen do not even try to fight, simply fleeing in terror."],
            [['foe_dead', 'dragon_undamaged'], u"Rapidly closing the distance, the %(dragon_type)s bursts into the formation of crossbowmen and scatters them like rag dolls."],
            [['foe_dead', 'dragon_wounded'], u"Cutting through a coordinated volley of crossbow bolts, the %(dragon_type)s bursts into their formation and throws the crossbowmen like rag dolls. Nevertheless, some bolts punctured the dragon\'s skin, and now he must lick his wounds."],
            [['foe_alive', 'dragon_wounded'], u"The well coordinated volley of crossbow bolts is so effective that the dragon is wounded and forced to restrain his enthusiastic charge."],
            [['foe_alive', 'dragon_undamaged'], u"The crossbowmen take cover and fire from sheltered positions. The dragon could get them one by one, but it would take a very long time."],
            [['foe_alive', 'lost_head'], u"A heavy iron arrow flies right into the eye of the dragon. This injury will cost him a head!"],
            [['foe_dead', 'lost_head'], u"The %(dragon_type)s wins, but one of his heads is dying from its wounds.."],
            [['dragon_dead'], u"%(dragon_name_full)s dies from a heavy crossbow bolt shot at point blank range."]
        ]
    },

    'xbow_rider': {
        'name': u"Mounted crossbowmen",  # The name of the mob used ingame
        'power': {'base': (4, 1)},  # attack force (обычная, верная)
        'defence': {'base': (4, 0)},  # damage resistance (обычная, верная)
        'modifiers': [],  # special modifiers
        'image': 'xbow_rider',  # background image for the fight "img/scene/fight/%s.jpg"
        # descriptions of battle events
        'descriptions': [
            [['foe_intro'], u"Mounted crossbowmen gather loosely at range, ready for battle."],
            [['foe_fear'],  u"%(dragon_name_full)s emits a terrifying roar and the horses throw their own riders loose, trampling them."],
            [['foe_dead', 'dragon_undamaged'], u"One by one, the riders discharge their crossbows, but %(dragon_name)s does not even notice the flying arrows. One by one, the %(dragon_type)s knocks the riders down and rips them to shreds with his teeth."],
            [['foe_dead', 'dragon_wounded'], u"%(dragon_name)s is able to knock over a rider and his horse with a single blow, but there are so many of them that the dragon does not make it out of the battle uninjured."],
            [['foe_alive', 'dragon_wounded'], u"The %(dragon_type)s is distracted by one of the riders and does notice another passing by at full gallop, shooting a bolt into the vulnerable side of the dragon."],
            [['foe_alive', 'dragon_undamaged'], u"The riders deftly maneuver, avoiding the fangs of the dragon, and try to shoot him with their crossbows from long range. Such tactics are unlikely to bring them victory, but it preserves their lives."],
            [['foe_alive', 'lost_head'], u"The %(dragon_type)s knocks down a rider and rushes to tear him to pieces, but the rider jumps to his feet and swings his sharp sword. The dragon\'s head falls to the ground. It\'s good that he has more left..."],
            [['foe_dead', 'lost_head'], u"In a fierce battle the %(dragon_type)s wins, but one of its heads remains lying on the field, severed by a heavy sabre."],
            [['dragon_dead'], u"The wounded %(dragon_type)s tries to fight, but there are too many riders. After killing many men and horses, %(dragon_name_full)s finally falls to the ground, bleeding."]
        ]
    },

}