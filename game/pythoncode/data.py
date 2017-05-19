#!/usr/bin/env python
# coding=utf-8
#spellchecked

import collections


class Modifier(object):
    """
    Various modifiers class.
    Examples: mistress fights, knight's equipment, spells etc.
    """

    def __init__(self, attack=('base', (0, 0)), protection=('base', (0, 0)), magic=0, fear=0, energy=0):
        self.attack = attack
        self.protection = protection
        self.magic = magic
        self.fear = fear
        self.max_energy = energy

    def __contains__(self, item):
        return item in self.__dict__

    @staticmethod
    def attack_filter(attack):
        return attack


class Container(collections.defaultdict):
    """
    Storage class for various properties/modifiers
    TODO: реверсивный поиск
    """

    def __init__(self, container_id=None, data=None, *args, **kwargs):
        super(Container, self).__init__(*args, **kwargs)
        self.id = container_id
        if data is not None:

            for key, value in data.items():
                self.add(key, value)

    def add(self, container_id, data):
        """
        :param container_id: property/modifier identifier
        :param data: dict which contains properties of this property/modifier
        """
        if container_id not in self:
            if type(data) is dict:
                self[container_id] = Container(container_id, data)
            else:
                self[container_id] = data
        else:
            raise Exception("Already in container")

    def sum(self, parameter):
        """
        :param parameter: Value by which you should summarize attributes. Summing goes recursively.
        """
        total = 0
        if parameter in self:
            try:
                total += self[parameter]
            except ValueError:
                pass
        for i in self:
            if type(self[i]) == type(self):
                total += self[i].sum(parameter)
        return total

    def list(self, key):
        """
        Рекурсивно возвращает лист значений по ключу
        :param key: Ключ по которому производится поиск
        :return: Список значений
        """
        result = []
        if key in self:
            if type(self[key]) is list:
                result += self[key]
            else:
                result.append(self[key])
        for i in self:
            if type(self[i]) == type(self):
                result += self[i].list(key)
        return result

    def contains(self, key, value=None):
        """
        Returns a list of IDs that contain given key and and value if specified.
        :param key: Key which element should contain
        :return: list of elements that contain key, if there is no such elements, list is empty
        """
        result = []
        if key in self:
            if value is None:
                result += [self.id]
            else:
                if self[key] == value:
                    result += [self.id]
        for i in self:
            if type(self[i]) == type(self):
                result += self[i].contains(key, value)
        return result

    def select(self, query):
        """
        Return a list of IDs that fits conditions that set in query. Not recursively.
        :param query: tuples list (key, value) which object of search must meet
        :return: list of satisfying elements
        """
        result = []
        for (key, value) in query:
            if key in self and self[key] == value:
                continue
            else:
                break
        else:
            result.append(self.id)
        for i in self:
            if type(self[i]) == type(self):
                result += self[i].select(query)
        return result

    def type(self):
        """
        For test uses
        """
        return type(self)

    def __getattr__(self, name):
        return self[name]

    def __missing__(self, key):
        return None


def get_description_by_count(description_list, count):
    """ 
    :param description_list: dictionary, key - minimum integer number,
    in which value is output with this key.
    Maximum number, in which value is output - minimum number of a next key minus one
    :param count: number for which we want to pick description
    :return: description for number count from dictionary description_list
    For example, if description_list = {0:'A', 10:'B'}, 
    than with count < 0 result is None, with count = 0..9 - 'A', and with count >= 10 - 'B'
    """
    count_list = reversed(sorted(description_list.keys()))
    for count_i in count_list:
        if count >= count_i:
            return description_list[count_i]

#
# Вор
#

thief_first_names = [
    u"Jack",
    u"Harry",
    u"Sem",
    u"Alex",
    u"Buddy",
    u"Buck",
    u"Chuck",
    u"Barry",
    u"Bart",
    u"Beaves",
    u"Bert",
    u"Billy",
    u"Beef",
    u"Butch",
    u"Brook",
    u"Bred",
    u"Willie",
    u"Woodie",
    u"Geib",
    u"Henry",
    u"Glen",
    u"Greg",
    u"Dacks",
    u"Dexter",
    u"Dean",
    u"Jet",
    u"Jessie",
    u"Jobe",
    u"Joy",
    u"Jonnie",
    u"Jhosh",
    u"Duaein",
    u"Duke",
    u"Zack",
    u"Isie",
    u"Kennie",
    u"Kirk",
    u"Klaive",
    u"Kliff",
    u"Klod",
    u"Larrie",
    u"Meddison",
    u"Max",
    u"Marcus",
    u"Marvin",
    u"Martie",
    u"Mett",
    u"Nash",
    u"Nick",
    u"Ollie",
    u"Paul",
    u"Ray",
    u"Rickkie",
    u"Scott",
    u"Spaik",
    u"Stive",
    u"Tedd",
    u"Tonnie",
    u"Troy",
    u"Fill",
    u"Fox",
    u"Sean",
]

thief_last_names = [
    u"the Bald",
    u"Sliptoe",
    u"the Nimble",
    u"the Cunning",
    u"the Fox",
    u"the Jumper",
    u"Fastlegs",
    u"the Joker",
    u"the Rascal",
    u"the Splinter",
    u"the Smelly",
    u"Thorn",
    u"the Shadow",
    u"the Stealthy",
    u"the Calm",
    u"the Smug",
    u"Agile Fingers",
    u"the Sneaking",
    u"cross-eyes",
    u"the Crazed",
    u"the Con-artist",
    u"the Pretender",
    u"the Climber",
    u"the Crawler",
    u"the Rhymer",
    u"the Indecent",
    u"the Immoral",
    u"the Cocky",
    u"the Nervous",
    u"the Scretchy",
    u"the Stutterer",
    u"the Pockmarked",
    u"Cutthroat",
    u"Hungman",
    u"the Angry",
    u"the Sycophant",
    u"the Headless",
    u"Frostbite",
    u"the Immature",
    u"the Snaketongue",
    u"the Venomous",
    u"the Speedy",
    u"the Cautious",
    u"Blacktooth",
    u"Whitetooth",
    u"Witehands",
    u"the Handsome",
    u"the Cat",
    u"the Smutty",
    u"the Hellspawn",
    u"the Greasy",
    u"Fast one",
    u"the Rake",
    u"the Womaniser",
    u"the Bull",
    u"the Noose",
    u"Masterkey",
    u"the Pig Nose",
    u"the Daredevil",
    u"the Sweet Talker",
]

thief_abilities = Container(
    "thief_abilities",
    {
        "climber": {
            "name": u"Alpinist",
            "description": u"can climb high",
            "provide": ["alpinism"]
        },
        "diver": {
            "name": u"Diver",
            "description": u"holds his breath",
            "provide": ["swimming"]
        },
        "greedy": {
            "name": u"Greedy",
            "description": u"will get more treasure from you",
            "provide": []
        },
        "mechanic": {
            "name": u"Mechanist",
            "description": u"disarms mechanical traps",
            "avoids": ["mechanic_traps"],
            "provide": []
        },
        "magicproof": {
            "name": u"Arcane thief",
            "description": u"disarms magical traps",
            "avoids": ["magic_traps"],
            "provide": []
        },
        "poisoner": {
            "name": u"Poisoner",
            "description": u"ignores venomous guards",
            "avoids": ["poison_guards"],
            "provide": []
        },
        "assassin": {
            "name": u"Assasin",
            "description": u"ignores common guards",
            "avoids": ["regular_guards"],
            "provide": []
        },
        "night_shadow": {
            "name": u"Night Shadow",
            "description": u"ignores elite guards",
            "avoids": ["elite_guards"],
            # Это странно, что он может быть пойман обычными стражами
            "provide": []
        },
        "trickster": {
            "name": u"Trickster",
            "description": u"no chance to wake you up",
            "provide": []
        },
    })

thief_items = Container(
    "thief_items",
    {
        "plan": {
            "name": u"Great Plan",
            "level": 1,
            "description": u"more chances to succeed"
        },
        "scheme": {
            "name": u"Secret passage map",
            "description": u"ignores fortifications"
        },
        "sleep_dust": {
            "name": u"Sleepdust",
            "description": u"dragon can't wake up"
        },
        "bottomless_sac": {
            "name": u"Bag of holding",
            "dropable": True,
            "description": u"can get more treasures from you"
        },
        "antidot": {
            "name": u"Antidote",
            "description": u"ignores venomous guards",
            "avoids": ["poison_guards"]
        },
        "enchanted_dagger": {
            "name": u"Envenomed dagger",  # Applied
            "dropable": True,
            "description": u"ignores common guards",
            "avoids": ["regular_guards"]
        },
        "ring_of_invisibility": {
            "name": u"Ring of invisibility",  # Applied
            "dropable": True,
            "description": u"ignores elite guards",
            "avoids": ["elite_guards"]
        },
        "flying_boots": {
            "name": u"Boots of flying",  # Applied
            "dropable": True,
            "description": u"can fly",
            "provide": ["flight", "alpinism"]
        },
        "cooling_amulet": {
            "name": u"Freezing amulet",  # Applied
            "dropable": True,
            "description": u"protection from fire",
            "provide": ["fireproof"]
        },
        "warming_amulet": {
            "name": u"Fiery amulet",  # Applied
            "dropable": True,
            "description": u"protection from cold",
            "provide": ["coldproof"]
        }
    })

# We planned to use cursed items, but ultimately we didn't implement them
thief_items_cursed = Container(
    "thief_items_cursed",
    {
        "plan": {
            "name": u"Плохой план",  # Applied
            "level": -1,
            "cursed": True,
            "description": u"-1 к уровню вора",
            "fails": []
        },
        "bottomless_sac": {
            "name": u"Дырявый мешок",  # Applied
            "cursed": True,
            "description": u"Вор не уносит никаких сокровищ",
            "fails": []
        },
        "enchanted_dagger": {
            "name": u"Проклятый кинжал",  # Applied
            "cursed": True,
            "description": u"Автоматический успех обычных стражей",
            "fails": ["regular_guards"]
        },
        "ring_of_invisibility": {
            "name": u"Кольцо мерцания",  # Applied
            "cursed": True,
            "description": u"Автоматический успех элитных стражей",
            "fails": ["elite_guards"]
        },
        "flying_boots": {
            "name": u"Ощипанные сандалии",  # Applied
            "cursed": True,
            "description": u"Вор автоматически разбивается насмерть, если идет в логово требующее полета",
            "fails": ["flight", "alpinism"],
            "provide": ["flight", "alpinism"]
        },
        "cooling_amulet": {
            "name": u"Морозильный амулет",  # Applied
            "cursed": True,
            "description": u"Вор замораживается насмерть, если идет в огненное логово",
            "fails": ["fireproof"],
            "provide": ["fireproof"]
        },
        "warming_amulet": {
            "name": u"Шашлычный амулет",  # Applied
            "cursed": True,
            "description": u"Вор зажаривается насмерть, если идет в ледяное логово",
            "fails": ["coldproof"],
            "provide": ["coldproof"]
        },
    })

thief_titles = [
    u"Marauder",
    u"Rogue",
    u"Burglar",
    u"Tomb Raider",
    u"Master thief",
    u"Prince of Thieves"
]

'''
Calls label shown in value of dictionary. If list is shown, calls all labels shown at list in specified order.
Crucial parameters are:
thief - thief which triggered an event
Additionally for: "start_trap", "die_trap", "pass_trap", "pass_trap_by_luck", "pass_trap_no_influence", "end_trap":
trap - upgrade which triggered an event
Additionally for "pass_trap_by_luck":
drain_luck - amount of luck, removed from thief who passed this trap.
Additionally for "die_item", "receive_item":
item - item that thief get
'''
thief_events = {
    "spawn": "lb_event_thief_spawn",
    "lair_unreachable": "lb_event_thief_lair_unreachable",
    "prepare": "lb_event_thief_prepare",
    "prepare_usefull": "lb_event_thief_prepare_usefull",
    "prepare_useless": "lb_event_thief_prepare_useless",
    "lair_enter": "lb_event_thief_lair_enter",
    "die_inaccessability": "lb_event_thief_die_inaccessability",
    "start_trap": None,
    "die_trap": "lb_event_thief_die_trap",
    "pass_trap": "lb_event_thief_pass_trap",
    "end_trap": None,
    "receive_no_item": "lb_event_thief_receive_no_item",
    "receive_item": "lb_event_thief_receive_item",
    "steal_items": "lb_event_thief_steal_items",
    "retire": None,
    # @Review: Alex: Added new event:label k/v to fill in the gaps:
    "checking_accessability": "lb_event_thief_checking_accessability",
    "checking_accessability_success": "lb_event_thief_checking_accessability_success",
    "trying_to_avoid_traps_and_guards": "lb_event_thief_trying_to_avoid_traps_and_guards",
    "retreat_and_try_next_year": "lb_event_thief_retreat_and_try_next_year",
    "starting_to_rob_the_lair": "lb_event_thief_starting_to_rob_the_lair",
    "took_an_item": "lb_event_thief_took_an_item",
    "lair_empty": "lb_event_thief_lair_empty",
    "awakened_the_dragon": "lb_event_thief_awakened_dragon"
}

#
# Knight
#

knight_first_names = [
    u"Havein",
    u"Lancelot",
    u"Gallahad",
    u"Percevail",
    u"Boris",
    u"Kay",
    u"Mordred",
    u"Harret",
    u"Urience",
    u"Yveyn",
    u"Ouen",
    u"Bediver",
    u"Gaheris",
    u"Argavein",
    u"Alan",
    u"Alistair",
    u"Alven",
    u"Alen",
    u"Anakin",
    u"Ardeen",
    u"Arman",
    u"Anrie",
    u"Archibald",
    u"Bardrick",
    u"Bardolf",
    u"Barklai",
    u"Barnabas",
    u"Benvan",
    u"Bartolomeus",
    u"Benjamine",
    u"Bedivir",
    u"Benneth",
    u"Benedict",
    u"Bertran",
    u"Blaine",
    u"Blaze",
    u"Bolduin",
    u"Valentain",
    u"Virgile",
    u"Willford",
    u"Wayland",
    u"Gabriel",
    u"Hammilton",
    u"Garfild",
    u"Hilbert",
    u"Gordon",
    u"Taiven",
    u"Darnell",
    u"Dastin",
    u"Daireel",
    u"Dilbert",
    u"Denzel",
    u"Jarred",
    u"Geralt",
    u"Jaison",
    u"Diggory",
    u"Douglass",
    u"Daiton",
    u"Igglebert",
    u"Ingramm",
    u"Inescent",
    u"Irvain",
    u"Carlail",
    u"Cventine",
    u"Curtis",
    u"Kingsley",
    u"Clarence",
    u"Clivlend",
    u"Connor",
    u"Cristofer",
    u"Kaspian",
    u"Lionnel",
    u"Leopold",
    u"Lindsey",
    u"Listar",
    u"Lorence",
    u"Maximillian",
    u"Melburn",
    u"Milford",
    u"Montgommery",
    u"Mordicain",
    u"Naijell",
    u"Nicolas",
    u"Nordbert",
    u"Nimbus",
    u"Norton",
    u"Norris",
    u"Oberon",
    u"Oldredd",
    u"Orson",
    u"Osbert",
    u"Percie",
    u"Rassel",
    u"Redcliff",
    u"Redmoond",
    u"Reginald",
    u"Rainold",
    u"Rondile",
    u"Ronald",
    u"Rendall",
    u"Sebastian",
    u"Silvester",
    u"Stenlie",
    u"Theiobald",
    u"Timoty",
    u"Thobias",
    u"Trevice",
    u"Willbert",
    u"Willfred",
    u"Warren",
    u"Fabian",
    u"Fredderick",
]

knight_last_names = [
    u"of the Lake",
    u"the Glorious",
    u"of the Meadows",
    u"the Proud",
    u"the Kind",
    u"the Courageous",
    u"the Brave",
    u"the Faithful",
    u"the Gallant",
    u"the Glorious",
    u"the Handsome",
    u"the Great",
    u"the Radiant",
    u"Whiteshield",
    u"the Strong",
    u"the Kin Eye",
    u"the Lionhart",
    u"Oakenshield",
    u"the Patient",
    u"the Timid",
    u"the Seeker",
    u"the Adherent",
    u"the Defender",
    u"the Savior",
    u"the Benevolent",
    u"the Exemplar",
    u"the Sagacious",
    u"the Farseer",
    u"the Wise",
    u"the Marvellous",
    u"the Daydreamer",
    u"the Chosen One",
    u"the Honorable",
    u"the Blessed One",
    u"the Fine",
    u"the Virgin",
    u"the Modest",
    u"the Humble",
    u"the Generous",
    u"the Thrifty",
    u"the Merciful",
    u"the Beneficent",
    u"the Sweet Voice",
    u"the Witty",
    u"the Landless",
    u"the White Face",
    u"the Honest",
]

knight_abilities = Container(
    "knight_abilities",
    {
        "brave": {
            "name": u"Braveheart",
            "description": u"no fear of dragons",
            "modifiers": ["fearless"]
        },
        "charmed": {
            "name": u"Charmed",
            "description": u"can get to any lair",
            "modifiers": ["swimming", "flight", "alpinism"]
        },
        "liberator": {
            # Implemented at Knight._ability_modifiers
            "name": u"Liberator",
            "description": u"becomes stronger if you hold captives",
            "modifiers": []
        },
        "fiery": {
            "name": u"Fiery",
            "description": u"stronger attack",
            "modifiers": ['atk_up', 'atk_up']
        },
        "cautious": {
            "name": u"Cautious",
            "description": u"more armor",
            "modifiers": ['def_up', 'def_up']
        }
    }
)

knight_items = Container(
    "knight_items",
    {
        # Breastplates
        "basic_vest": {
            "id": "basic_vest",
            "name": u"Chainmail",
            "description": u"standard armor",
            "type": "vest",
            "basic": True,
            "modifiers": []
        },
        "glittering_vest": {
            "id": "glittering_vest",
            "name": u"Shining platemail",
            "description": u"strong armor",
            "type": "vest",
            "basic": False,
            "modifiers": ['def_up', 'def_up']
        },
        "gold_vest": {
            "id": "gold_vest",
            "name": u"Golden platemail",
            "description": u"great armor",
            "type": "vest",
            "basic": False,
            "modifiers": ['sdef_up']
        },
        "magic_vest": {
            # Implemented at Knight.enchant_equip
            "id": "magic_vest",
            "name": u"Enchanted platemail",
            "description": u"protection from elements",
            "type": "vest",
            "basic": False,
            "modifiers": []
        },
        # Spears
        "basic_spear": {
            "id": "basic_spear",
            "name": u"Steel lance",
            "description": u"standard weapon",
            "type": "spear",
            "basic": True,
            "modifiers": []
        },
        "blued_spear": {
            "id": "blued_spear",
            "name": u"Burnished lance",
            "description": u"strong weapon",
            "type": "spear",
            "basic": False,
            "modifiers": ['atk_up', 'atk_up']
        },
        "spear_with_scarf": {
            "id": "spear_with_scarf",
            "name": u"Lance with scarf",
            "description": u"great weapon",
            "type": "spear",
            "basic": False,
            "modifiers": ['satk_up']
        },
        "dragonslayer_spear": {
            # implemented at Knight._item_modifiers and battle_action
            "id": "dragonslayer_spear",
            "name": u"Dragonslayer lance",  # TODO: implement
            "description": u"kills you outright",
            "type": "spear",
            "basic": False,
            "modifiers": []
        },
        # Swords
        "basic_sword": {
            "id": "basic_sword",
            "name": u"Longsword",
            "description": u"standard weapon",
            "type": "sword",
            "basic": True,
            "modifiers": []
        },
        "glittering_sword": {
            "id": "glittering_sword",
            "name": u"Shiny longsword",
            "description": u"strong weapon",
            "type": "sword",
            "basic": False,
            "modifiers": ['atk_up', 'atk_up']
        },
        "lake_woman_sword": {
            "id": "lake_woman_sword",
            "name": u"Lady of the Lake Sword",
            "description": u"irresistible attack",
            "type": "sword",
            "basic": False,
            "modifiers": ['satk_up']
        },
        "flameberg_sword": {
            "id": "flameberg_sword",
            "name": u"Flamberge",
            "description": u"fiery weapon",
            "type": "sword",
            "basic": False,
            "modifiers": ['sfatk_up', 'sfatk_up']
        },
        "icecracker_sword": {
            "id": "icecracker_sword",
            "name": u"Icecracker sword",
            "description": u"frost weapon",
            "type": "sword",
            "basic": False,
            "modifiers": ['siatk_up', 'siatk_up']
        },
        "thunderer_sword": {
            "id": "thunderer_sword",
            "name": u"The Thunderer",
            "description": u"thunder weapon",
            "type": "sword",
            "basic": False,
            "modifiers": ['slatk_up', 'slatk_up']
        },
        # Shields
        "basic_shield": {
            "id": "basic_shield",
            "name": u"Heraldic shield",
            "description": u"standard",
            "type": "shield",
            "basic": True,
            "modifiers": []
        },
        "polished_shield": {
            "id": "polished_shield",
            "name": u"Polished shield",
            "description": u"strong",
            "type": "shield",
            "basic": False,
            "modifiers": ['def_up', 'def_up']
        },
        "mirror_shield": {
            # Implemented at Knight._item_modifiers
            "id": "mirror_shield",
            "name": u"Mirror shield",
            "description": u"reflects your breath weapon",
            "type": "shield",
            "basic": False,
            "modifiers": []
        },
        # Horses
        "basic_horse": {
            "id": "basic_horse",
            "name": u"Horse",
            "description": u"standard mount",
            "type": "horse",
            "basic": True,
            "modifiers": []
        },
        "white_horse": {
            "id": "white_horse",
            "name": u"White stallion",
            "description": u"stronger atk and def",
            "type": "horse",
            "basic": False,
            "modifiers": ['atk_up', 'def_up']
        },
        "pegasus": {
            "id": "pegasus",
            "name": u"Pegasus",
            "description": u"can fly",
            "type": "horse",
            "basic": False,
            "modifiers": ['flight']
        },
        "firehorse": {
            "id": "firehorse",
            "name": u"Firehorse",
            "description": u"alpinism, protection from fire",
            "type": "horse",
            "basic": False,
            "modifiers": ['alpinism', 'fire_immunity']
        },
        "sivka": {
            "id": "sivka",
            "name": u"Sivka-Burka",
            "description": u"alpinism, protection from cold",
            "type": "horse",
            "basic": False,
            "modifiers": []
        },
        "kelpie": {
            "id": "kelpie",
            "name": u"Kelpie",
            "description": u"swims underwater",
            "type": "horse",
            "basic": False,
            "modifiers": ['swimming']
        },
        "griffon": {
            "id": "griffon",
            "name": u"Griffon",
            "description": u"can fly, strong mount",
            "type": "horse",
            "basic": False,
            "modifiers": ['atk_up', 'def_up', 'flight']
        },
        # Followers
        "basic_follower": {
            "id": "basic_follower",
            "name": u"Squire",
            "description": u"no use",
            "type": "follower",
            "basic": True,
            "modifiers": []
        },
        "squire": {
            "id": "squire",
            "name": u"Agile squire",
            "description": u"can climb",
            "type": "follower",
            "basic": False,
            "modifiers": ['alpinism']
        },
        "veteran": {
            "id": "veteran",
            "name": u"Veteran squire",
            "description": u"stronger defense",
            "type": "follower",
            "basic": False,
            "modifiers": ['sdef_up']
        },
        "pythoness": {
            "id": "pythoness",
            "name": u"Farseer",
            "description": u"stronger attack",
            "type": "follower",
            "basic": False,
            "modifiers": ['satk_up']
        },
        "thaumaturge": {
            "id": "thaumaturge",
            "name": u"Wizard",
            "description": u"more atk and def",
            "type": "follower",
            "basic": False,
            "modifiers": ['satk_up', 'sdef_up']
        },
    }
)

knight_titles = [
    u"Poor knight",
    u"Questing knight",
    u"Knight of the Mark",
    u"Noble knight",
    u"Paladin",
    u"Prince"]

knight_events = {
    "spawn": "lb_event_knight_spawn",
    "prepare": None,
    "prepare_usefull": None,
    "prepare_useless": None,
    "receive_item": "lb_event_knight_receive_item",
    "challenge_start": "lb_event_knight_challenge_start",   # Должен возвращать True или False
                                                            # True - бой с рыцарем начинается
                                                            # False - нет
    "challenge_end": "lb_event_knight_challenge_end",       # В ивент передается параметр result, содержащий
                                                            # теги исхода битвы дракона с рыцарем
}

#
# Lair
#

lair_types = Container(
    "lair_types",
    {
        "impassable_coomb": {
            "name": u"Impassable combe",
            "inaccessability": 0
        },
        "impregnable_peak": {
            "name": u"Impregnable peak",
            "inaccessability": 0,
            "require": ["alpinism"],
            'prerequisite': ['wings']
        },
        "solitude_citadel": {
            "name": u"Solitary citadel",
            "inaccessability": 0,
            "require": ["alpinism", "coldproof"],
            'prerequisite': ['wings', 'ice_immunity']
        },
        "vulcano_chasm": {
            "name": u"Volcano chasm",
            "inaccessability": 0,
            "require": ["alpinism", "fireproof"],
            'prerequisite': ['wings', 'fire_immunity']
        },
        "underwater_grot": {
            "name": u"Underwater grotto",
            "inaccessability": 0,
            "require": ["swimming"],
            'prerequisite': ['swimming']
        },
        "underground_burrow": {
            "name": u"Underground burrow",
            "inaccessability": 1,
            "require": [],
            'prerequisite': ['can_dig']
        },
        "dragon_castle": {
            "name": u"Dragon castle",
            "inaccessability": 1,
            "require": []
        },
        "castle": {
            "name": u"Old ruins",
            "inaccessability": 1,
            "require": []
        },
        "ogre_den": {
            "name": u"Ogre Den",
            "inaccessability": 1,
            "require": []
        },
        "broad_cave": {
            "name": u"Broad Cave",
            "inaccessability": 1,
            "require": []
        },
        "tower_ruin": {
            "name": u"Tower Ruin",
            "inaccessability": 1,
            "provide": ["magic_traps"]
        },
        "monastery_ruin": {
            "name": u"Monastery Ruin",
            "inaccessability": 1,
            "require": []
        },
        "fortress_ruin": {
            "name": u"Fortress ruin",
            "inaccessability": 2,
            "require": []
        },
        "castle_ruin": {
            "name": u"Castle ruins",
            "inaccessability": 2,
            "require": []
        },
        "ice_citadel": {
            "name": u"Ice citadel",
            "inaccessability": 1,
            "require": ["alpinism", "coldproof"]
        },
        "vulcanic_forge": {
            "name": u"Volcanic Forge",
            "inaccessability": 1,
            "require": ["alpinism", "fireproof"]
        },
        "forest_heart": {
            "name": u"Forest Heart",
            "inaccessability": 2,
            "provide": ["magic_traps"]
        },
        "cloud_castle": {
            "name": u"Cloud Castle",
            "inaccessability": 2,
            "require": ["flight"]
        },
        "underwater_mansion": {
            "name": u"Underwater mansion",
            "inaccessability": 1,
            "require": ["swimming"]
        },
        "underground_palaces": {
            "name": u"Underground Palace",
            "inaccessability": 2,
            "require": ["alpinism"],
            "provide": ["mechanic_traps"]
        },
    }
)

lair_upgrades = Container(
    "lair_upgrades",
    {
        "mechanic_traps": {
            "name": u"Mechanical traps",
            "protection": 1,
            "success": [
                u'Thief bypasses the traps.',
            ],
            "fail": [
                u'The unlucky thief steps on a pressure plate and activates '
                u'a deadly blade trap.',
            ]
        },
        "magic_traps": {
            "name": u"Magic trap",
            "protection": 1,
            "success": [
                u'The cunning thief spots a glimmer and avoids a magical trap.',
            ],
            "fail": [
                u'A magical trap disintegrates the trespasser.',
            ]
        },
        "poison_guards": {
            "name": u"Venomous guards",
            "protection": 1,
            "success": [
                u"Venomous beasts can't stop the trespasser.",
            ],
            "fail": [
                u'A sneaky venomous beast bites the unlucky thief. '
                u'He dies in great pain...',
            ]
        },
        "regular_guards": {
            "name": u"Common guards",
            "replaces": "smuggler_guards",  # какое улучшение автоматически заменяет
            "protection": 2,
            "success": [
                u'The burglar stealthily stabs guards with his dagger, one by one.',
            ],
            "fail": [
                u'A guard spots the thief and raises the alarm. '
                u'After a short but brutal fight thief is defeated and executed.',
            ]
        },
        "smuggler_guards": {
            "name": u"Mercenary guards",
            "cost": 100,
            "protection": 2,
            "success": [
                u'The burglar stealthily stabs guards with his dagger, one by one.',
            ],
            "fail": [
                u'Guard spots the thief and raises the alarm. '
                u'After a short but brutal fight thief is defeated and executed.',
            ]
        },
        "elite_guards": {
            "name": u"Elite guard",
            "protection": 3,
            "success": [
                u'Under the cover of darkness, thief slips behind '
                u'the elite guard and into the treasure chamber.',
            ],
            "fail": [
                u'Thief tried to sneak up on the guard of the treasure chamber but fails. '
                u'The bloodthirsty monster rips him apart.',

            ]
        },
        "gremlin_fortification": {
            "name": u"Fortifications",
            "inaccessability": 1,
            "protection": 0
        },
        "gremlin_servant": {
            "name": u"Gremlin servants",
            "cost": 100,
            "protection": 0
        },
        "servant": {
            "name": u"Servants",
            "replaces": "gremlin_servant",  # какое улучшение автоматически заменяет
            "protection": 0
        },
    }
)

attack_types = ['base', 'fire', 'ice', 'poison', 'sound', 'lightning']
protection_types = ['base', 'scale', 'shield', 'armor']

#
# Reputation
#

reputation_levels = {
    0: 0,
    3: 1,
    6: 2,
    10: 3,
    15: 4,
    21: 5,
    28: 6,
    36: 7,
    45: 8,
    55: 9,
    66: 10,
    78: 11,
    91: 12,
    105: 13,
    120: 14,
    136: 15,
    153: 16,
    171: 17,
    190: 18,
    210: 19,
    231: 20
}

reputation_gain = {
    1: u"Common folk will notice this misdeed.",
    3: u"Ill fame of the dragon rises in the Free Kingdoms.",
    5: u"Defiler\'s ill fame rises considerably.",
    10: u"This dread deed will be remembered far and wide.",
    25: u"The legend of this dread deed will persist through the ages."
}

#
# Dragon
#

# Names
dragon_names = [
    u'Azogh',
    u'Auring',
    u'Alaphis',
    u'Braghnir',
    u'Bellywyrg',
    u'Bloodwing',
    u'Beorgis',
    u'Buran',
    u'Wicerin',
    u'Wazgor',
    u'Balerion',
    u'Meraxes',
    u'Wxagar',
    u'Syraxis',
    u'Tyraxes',
    u'Wermax',
    u'Arrax',
    u'Kharaxes',
    u'Thadnros',
    u'Moonhide',
    u'Silverwing',
    u'Vermitor',
    u'Shiptif',
    u'Shrikos',
    u'Morgul',
    u'Urraks',
    u'Drogo',
    u'Reyerghal',
    u'Wizerion',
    u'Essovius',
    u'Gicksar',
    u'Wermitrax',
    u'Archoney',
    u'Desterion',
    u'Alhafton',
    u'Torogrim',
    u'Korinstraz',
    u'Ironicus',
    u'Charris',
    u'Itarius',
    u'Izondir',
    u'Lithurgahn',
    u'Taeradh',
    u'Morphals',
    u'Nepharian',
    u'Searnox',
    u'Pyonix',
    u'Ldorynx',
    u'Scipionax',
    u'Erihthon',
    u'Ghoronis',
    u'Gorgatrox',
    u'Artaxerks',
    u'Aitvaras',
    u'Balaur',
    u'Orlangoor',
    u'Shadizar',
]

dragon_surnames = [
    u'the Furious',
    u'the Mighty',
    u'the Sinister',
    u'the Stormborn',
    u'the Omnious',
    u'the Dark',
    u'the Baleful',
    u'the Arrogant',
    u'the Greedy',
    u'the Covetous',
    u'the Merciless',
    u'the Ruthless',
    u'the Proud',
    u'the Glutton',
    u'Loudroar',
    u'the Horrendous',
    u'the Deadly',
    u'the Quarellsome',
    u'the Awesome',
    u'the Envious',
    u'the Vicious',
    u'the Snakeeyed',
    u'the Longtailed',
    u'the Ugly',
    u'the Spikescaled',
    u'the Insidious',
    u'the Defiler',
    u'the Devourer',
    u'the Vivisector',
    u'the Doom-eyed',
    u'the Deathstalker',
    u'the Shaded',
    u'the Bloody',
    u'the Sabertooth',
    u'the Tempestuous',
    u'the Shameless',
    u'the Foul',
    u'the Crazed',
    u'the Impaler',
    u'the Voluminous',
    u'the Angry',
    u'the Gutspiller',
    u'the Flayer',
    u'the Swallower',
    u'the Indolent',
    u'the Slimy',
    u'the Destroyer',
    u'the Snake Eater',
    u'the Cursed',
    u'the Bloodthirsty',
    u'the Molester',
    u'the Godless',
    u'the Powerful',
    u'the Liar',
    u'the Thunderbird',
    u'the Sneaky',
    u'the Duplicitous',
    u'the Wise',
    u'the Keen-eyed',
    u'the Impetuous',
    u'the Unholy',
]

# Sizes
dragon_size = [
    u'Small',
    u'Modest-sized',
    u'Large',
    u'Huge',
    u'Gigantic',
    u'Gargantuous',
]

dragon_size_description = [
    u'Will not impress anyone with its size. '
    u'Although quite long, this snake weighs no more than a peasant dog.',

    u'It weighs about the same as an healthy adult man, nothing special.',

    u'Large enough to be compared with a horse.',

    u'There are few animals in the local forests that come close to his size. '
    u'Only the most well fed bulls or cave bears compare with him.',

    u'He can give even an elephant a run for its money in size and weight. '
    u'Other than that there is no equal in the forests and fields of the kingdom.',

    u'Even titans pale in comparison, only whales and krakens come even close in weight. '
    u'As agile and deadly as they are in the sea, he is on land and in the sky!',
]

head_description = {
    'green': u'has no special abilities.',
    'red': u'spews fire.',
    'white': u'chilling breath.',
    'blue': u'has gills and a venomous bite.',
    'black': u'spews poisonous gas.',
    'iron': u'covered in tough steel-like scales.',
    'bronze': u'can dig the earth.',
    'silver': u'spews lightning bolts.',
    'gold': u'can see the unseen.',
    'shadow': u'commands sinister necromantic powers.'
}

wings_description = [
    u'He crawls like a big snake.',
    u'He has a pair of mighty wings to fly in the sky.',
    u'He has two pairs of mighty wings.',
    u'He has three pairs of different sized wings, giving him incredible agility.'
]

paws_description = [
    u'He crawls like a big snake.',
    u'He walks with a pair of mighty legs.',
    u'He has two pairs of paws with claws.',
    u'He has three pairs of legs.'
]

special_features = ('tough_scale', 'poisoned_sting', 'clutches', 'horns', 'fangs', 'ugly')

special_description = [
    u'He has impenetrable scales.',

    u'He has a deadly poison sting on the tip of his tail.',

    u'His claws are razor sharp.',

    u'Mighty horns top his head, providing protection and a scary appearance.',

    u'He has long, vicious saber-teeth.',

    u'He is so ugly and terrifying that no one can look straight at him, '
    u'and weaklings simply flee in terror.',
]

special_features_rus = {
    "tough_scale": u"Tough scales",
    "poisoned_sting": u"Venomous sting",
    "clutches": u"Razor claws",
    "horns": u"Magnificent horns",
    "fangs": u"Sabertooth fangs",
    "ugly": u"Ugliness",
}

cunning_description = [
    u'The magical spark is flickering in his eyes.',

    u'The flame of magic fires in his eyes. '
    u'His magical power is great.',

    u'He commands immense magical powers.',
]

# TODO: Text module with numerals
head_num = [
    u'main',
    u'second',
    u'third',
    u'forth',
    u'fifth',
    u'sixth',
    u'seventh',
    u'eighth',
    u'ninth',
    u'tenth'
]

# heads amount description
head_count = {
    2: u"two-headed",
    3: u"three-headed",
    4: u"four-headed",
    5: u"five-headed",
    6: u"six-headed",
    7: u"seven-headed",
    8: u"eight-headed",
    9: u"many-headed",
    10: u"many-headed",
    11: u"many-headed",
}

# Head types(colors)
dragon_heads = {
    'green': [],
    'red': ['fire_breath', 'fire_immunity'],
    'white': ['ice_breath', 'ice_immunity'],
    'blue': ['swimming', 'poisoned_bite'],
    'black': ['black_power', 'poison_breath'],  # black_power -- +1 атака
    'iron': ['iron_scale', 'sound_breath'],  # iron_scale -- +1 защита
    'bronze': ['bronze_scale', 'can_dig'],  # bronze_scale -- +1 защита
    'silver': ['lightning_breath', 'lightning_immunity'],
    'gold': ['gold_magic', 'greedy'],  # greedy -- -2 к шансам вора
    'shadow': ['shadow_magic', 'fear_of_dark'],  # fear_of_dark -- +2 к страху
}

heads_name_rus = {
    'red': u"red",
    'black': u"black",
    'blue': u"blue",
    'gold': u"golden",
    'silver': u"silver",
    'bronze': u"bronze",
    'iron': u"steel",
    'shadow': u"phantom",
    'white': u"white",
    'green': u"green"
}

dragon_gifts = dict()

# Spells
spell_list = {
    # заговоры -- дают иммунитет к атаке выбранного типа
    'fire_protection': ['fire_immunity'],
    'ice_protection': ['ice_immunity'],
    #'poison_protection': ['poison_immunity'],
    'lightning_protection': ['lightning_immunity'],
    #'sound_protection': ['sound_immunity'],
    # сердца -- дают дыхание нужного типа
    'fire_heart': ['fire_breath'],
    'ice_heart': ['ice_breath'],
    'poison_heart': ['poison_breath'],
    'thunder_heart': ['sound_breath'],
    'lightning_heart': ['lightning_breath'],
    # прочие
    'wings_of_wind': ['wings_of_wind'],
    'aura_of_horror': ['aura_of_horror'],
    'unbreakable_scale': ['virtual_head'],
    'spellbound_trap': ['spellbound_trap'],
    'swimmer_spell': ['swimming'],
    'impregnator': ['impregnator'],
}

# Русское название для отображения заклинания
spell_list_rus = {
    # заговоры -- дают иммунитет к атаке выбранного типа
    'fire_protection': u"Protection from fire",
    'ice_protection': u"Protection from cold",
    #'poison_protection': u"Защита от яда",
    'lightning_protection': u"Protection from lightning",
    #'sound_protection': u"Защита от грома",
    # сердца -- дают дыхание нужного типа
    'fire_heart': u"Breath of Fire",
    'ice_heart': u"Breath of Ice",
    'poison_heart': u"Breath of Toxins",
    'thunder_heart': u"Breath of Thunder",
    'lightning_heart': u"Breath of Lightning",
    # прочие
    'wings_of_wind': u"Wing of Wind",
    'aura_of_horror': u"Sinister Aura",
    'unbreakable_scale': u"Phantom head",
    'spellbound_trap': u"Magic trap",
    'swimmer_spell': u"Gills",
    'impregnator': u"Impregnator",
}

effects_list = {
    # effects from food and other sourcesспецеффекты от еды и других прокачек дракона помимо собственных заклинаний
    'boar_meat': ['atk_up'],
    'bear_meat': ['def_up'],
    'griffin_meat': ['mg_up'],
    'shark_meat': ['mg_up'],
}

modifiers = {
    # global
    'fire_immunity': Modifier(),
    'community': Modifier(),
    'poison_immunity': Modifier(),
    'lightning_immunity': Modifier(),
    'ice_immunity': Modifier(),
    'sound_immunity': Modifier(),
    'magic_immunity': Modifier(),

    'flight': Modifier(),
    'alpinism': Modifier(),
    'swimming': Modifier(),

    'atk_up': Modifier(attack=('base', (1, 0))),  # 1 простая атака
    'satk_up': Modifier(attack=('base', (0, 1))),  # 1 верная атака
    'sfatk_up': Modifier(attack=('fire', (0, 1))),  # 1 верная атака огнем
    'sfatk_2up': Modifier(attack=('fire', (0, 2))), # 2 верных атаки огнём
    'siatk_up': Modifier(attack=('ice', (0, 1))),  # 1 верная атака льдом
    'siatk_2up': Modifier(attack=('ice', (0, 2))),  # 2 верных атаки льдом
    'slatk_up': Modifier(attack=('lightning', (0, 1))),  # 1 верная атака молнией  
    'slatk_2up': Modifier(attack=('lightning', (0, 2))),  # 2 верных атаки молнией    
    'def_up': Modifier(protection=('base', (1, 0))),  # 1 защита
    'sdef_up': Modifier(protection=('base', (0, 1))),  # 1 верная защита
    'decapitator': Modifier(),  # Обезглавливатель, при наличии этого модификатора у врага дракон вместо получения урона
                                # сразу теряет одну голову
    # Knight-specific
    'fearless': Modifier(),
    # Dragon-specific
    'can_dig': Modifier(),
    'greedy': Modifier(),
    'virtual_head': Modifier(),
    'spellbound_trap': Modifier(),
    'impregnator': Modifier(),
    'poisoned_bite': Modifier(attack=('poison', (0, 1))),
    # Заклинания
    'fire_breath': Modifier(attack=('fire', (0, 1))),
    'ice_breath': Modifier(attack=('ice', (0, 1))),
    'poison_breath': Modifier(attack=('poison', (0, 1))),
    'sound_breath': Modifier(attack=('sound', (0, 1))),
    'lightning_breath': Modifier(attack=('lightning', (0, 1))),
    'black_power': Modifier(attack=('base', (1, 0))),
    'iron_scale': Modifier(protection=('scale', (1, 0))),
    'bronze_scale': Modifier(protection=('scale', (1, 0))),
    'silver_magic': Modifier(magic=1),
    'gold_magic': Modifier(magic=1),
    'shadow_magic': Modifier(magic=1),
    'fear_of_dark': Modifier(fear=2),
    'aura_of_horror': Modifier(fear=1),
    'wings_of_wind': Modifier(energy=1),
    #
    'size': Modifier(attack=('base', (1, 0)), protection=('base', (1, 0)), fear=1),
    'paws': Modifier(attack=('base', (1, 0)), energy=1),
    'wings': Modifier(protection=('base', (1, 0)), energy=1),
    'tough_scale': Modifier(protection=('scale', (0, 1))),
    'clutches': Modifier(attack=('base', (0, 1))),
    'fangs': Modifier(attack=('base', (2, 0)), fear=1),
    'horns': Modifier(protection=('base', (2, 0)), fear=1),
    'ugly': Modifier(fear=2),
    'poisoned_sting': Modifier(attack=('poison', (1, 1))),
    'cunning': Modifier(magic=1),
    #
    'mg_up': Modifier(magic=1),
}


def get_modifier(name):
    if name in modifiers:
        return modifiers[name]
    raise NotImplementedError(name)

# lairs, images
lair_image = {
    'ravine': 'ravine'
}

# Dictionary with "showplaces",
# key - stage name,
# value - tuple of stage name for menu and mark you should jump to
special_places = {
    # лесная пещера с огром
    'ogre_den_full': (u"Ogre den", 'lb_ogre_den_full'),
    'ogre_den_empty': (u"Abandoned ogre den", 'lb_ogre_den_empty'),
    # йотун
    'jotun_full': (u"Ice citadel", 'lb_jotun'),
    'jotun_empty': (u"Abandoned ice citadel", 'lb_jotun_empty'),
    # Ифрит
    'ifrit_full': (u"Volcanic cave", 'lb_ifrit'),
    'ifrit_empty': (u"Abandoned volcanic cave", 'lb_ifrit_empty'),
    # Тритон
    'triton_full': (u"Underwater mansion", 'lb_triton'),
    'triton_empty': (u"Abandoned underwater mansion", 'lb_triton_empty'),
    # Титан
    'titan_full': (u"Cloud castle", 'lb_titan'),
    'titan_empty': (u"Abandoned cloud castle", 'lb_titan_empty'),
    # рыцарский манор
    'manor_full': (u"Manor", 'lb_manor_full'),
    'manor_empty': (u"Abandoned manor", 'lb_manor_empty'),
    # деревянный замок
    'wooden_fort_full': (u"Motte and bailey", 'lb_wooden_fort_full'),
    'wooden_fort_empty': (u"Abandoned fort", 'lb_wooden_fort_empty'),
    # монастрыь
    'abbey_full': (u"Monastery", 'lb_abbey_full'),
    'abbey_empty': (u"Abandoned monastery", 'lb_abbey_empty'),
    # каменный замок
    'castle_full': (u"Castle", 'lb_castle_full'),
    'castle_empty': (u"Abandoned castle", 'lb_castle_empty'),
    # королевский замок
    'palace_full': (u"Palace", 'lb_palace_full'),
    'palace_empty': (u"Abandoned palace", 'lb_palace_empty'),
    # зачарованный лес
    'elf_forest_full': (u"Enchanted wood", 'lb_enchanted_forest'),
    'elf_forest_empty': (u"Defiled wood", 'lb_dead_grove'),
    # задний проход в морию
    'backdoor_open': (u"Back door", 'lb_backdoor'),
    'backdoor_sealed': (u"Sealed back door", 'lb_backdoor_sealed'),
    # мория
    'frontgates_guarded': (u"Mountain Gate", 'lb_frontgates'),
    'frontgates_open': (u"Broken Gates", 'lb_dwarf_ruins'),
}

quest_list = (
    {   # только для дебага, не используется
        'min_lvl': 25,  # минимальный уровень дракона для получения квеста
        'max_lvl': 25,  # максимальный уровень дракона для получения квеста
        'text': u"Проживи 5 лет.",  # текст квеста
        'fixed_time': 25,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        # ключевое слово для описания задачи, 'autocomplete' - задача выполняется автоматически
        'task': 'autocomplete',
    },
    {   # Набрать дурной славы (уровень 2)
        'min_lvl': 1,  # минимальный уровень дракона для получения квеста
        'max_lvl': 1,  # максимальный уровень дракона для получения квеста
        # текст квеста, {0} будет заменён на требуемый уровень
        'text': u"My son, you're all grown up, and it\'s time to get down to real business. Beyond my possession are the Free Peoples of the earth, they humiliated me and drove me into the barren wasteland. You will be start of a bloodline that will bring them destruction. \n Let\'s see what you are capable of. Travel to the land of the Free Peoples and make a name for yourself - let them speak of you and fear you. But do not go on a thoughtless rampage, we don\'t want you to die without leaving a son, right? If you see that the enemy is strong - run away. Fight stealthily. Scour the woods and fields, kill lone women and ruin herds. When the people begin to whisper, come back to me and I\'ll give you a son, who will become stronger and achieve more than you. \n My advice - do not sleep in the Free Lands. When you sleep, you will slumber for a year, or more if you must heal wounds, and in the meantime men will hunt for you and your treasure. The more infamous you are the more attention you attract, though that is not a concern just yet. If you have time before you are exhausted, return here. If unable, stay in a flood gully as a last resort. \n If you are unable to accomplish this within five years, I will find another successor. ",
        'fixed_time': 5,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        # ключевое слово для описания задачи, 'reputation' - проверяется уровень дурной славы
        'task': 'reputation',
        'fixed_threshold': 1,  # 'fixed_'+ ключевое слово для задания фиксированного требуемого значения
    },
    {   # Породить любое потомство.
        'min_lvl': 2,  # минимальный уровень дракона для получения квеста
        'max_lvl': 2,  # максимальный уровень дракона для получения квеста
        'text': u"Well, you too have grown up. You are stronger than your father, but still are not mighty enough to avenge me - that is a task for your descendants. And do you know what to do to make children? No, not with me, silly. \n   You have a very strong seed, you will be able to impregnate any whom you desire. But not all will be able to bear strong children to term. The greater the strength of the woman, the better the reproduction will be. Be sure to take virgins who have not known the male touch. For giantesses it makes no difference, they will give you one offspring even if they have already had ordinary children. Look for the best blood. \n   You\'re the first in the family, and it\'s too early for you to chase magic maidens, for your first time peasants are enough. Somewhere near the village you must catch not just one, but several. Fertilize them and set them free, because there is no one in your den to guard them while you sleep. If they are not killed by their own people, in a year when you wake up they will have spawned creatures. Not dragons of course, dragons only I can produce, but monsters that will run rampant among the Free People. When something hatches come back to me, and I will give you a special reward! \n    For this you have five years. If you cannot handle it in that time, don\'t come back.",  # текст квеста
        'fixed_time': 5,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        'task': 'offspring',  # ключевое слово для описания задачи, 'offspring' - породить потомство
        # кортеж с требованиями, для выполнения задания нужно выполнить любое из них,
        # 'free_spawn' - потомство, рождённое на воле, 'educated_spawn' - воспитанное потомство
        'task_requirements': (('free_spawn', 'educated_spawn'),)
    },
    {   # Снизить боеспособность королевства.
        'min_lvl': 3,  # минимальный уровень дракона для получения квеста
        'max_lvl': 3,  # максимальный уровень дракона для получения квеста
        'text': u"Today you have reached maturity. That means the time has come for you, like your ancestors before, to go to the Free Peoples of the earth. The humans are the most vile species of all. They are numerous and organized. Their kingdom is enormous. And they already know about the appearance of the dragons, and thus will have protection. \n   When your notoriety increases, the kingdom will mobilize. They will increase their army size and begin to patrol the roads. The higher the mobilization, the better the kingdom will be protected. But we can prevent them from gathering strength. To do this, you can use many methods. You can ruin the countryside, burning barns and mills, reducing their ability to field armies. You can flood the kingdom with spawn, and troops will be diverted to deal with them. And you may simply pay robbers from the lonely island to plunder and sabotage. One way or another, you should be able to cope with the threat. This is what you have to do: \n   First, acquire notoriety and go to sleep. When you wake up, the people will have arisen. Then, you must do something to reduce their enthusiasm. When their mobilization falls, I think you will have done all that I need from you. Come back to me for a reward! \n     I will give you a term of ten years. That should be than enough for such a simple task.",  # текст квеста
        'fixed_time': 10,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        # ключевое слово для описания задачи, 'poverty' - проверяется уровень понижения мобилизации из-за разрухи
        'task': 'poverty',
        'fixed_threshold': 1,  # 'fixed_'+ ключевое слово для задания фиксированного требуемого значения
    },
    {   # Переселиться в приличное логово, сделать там любое улучшение, завести слуг и охрану.
        # минимальный уровень дракона для получения квеста
        'min_lvl': 4,
        # максимальный уровень дракона для получения квеста
        'max_lvl': 4,
        # текст квеста
        'text': u"     Already you\'re quite an adult, son. And you\'re a lot stronger than the first of your kind were at your age. The time has come for dragons to behave like kings. I want you thoroughly settled on the lands of the free. You need to have a dragon\'s lair, not some crude gully or hole in the ground. It is better to find a good cave, or take from a knight a small estate or castle. You will need servants and guards. It is best to be protected by your own spawn, but for a start mercenaries are found on the predatory island. As servants hire gremlins, who will look after the captives while you sleep. Creatures born in your den can be told what to do. If you want them to harass the people - let them go free. If you need protection or servants who will not require payment, leave them in the den. There are roles for servants, chained poisonous creatures, guards and elite treasure defenders. If your den is protected enough, send intelligent spawn to me - they will be added to my army along with my goblins, and multiply under my hand. \n     Gremlins are skilled craftsmen - be sure to order them to build traps and fortifications for the new lair, so it is more difficult for thieves to get to the treasure. Attend carefully to the arrangement of the den, because if you are forced to move you will lose everything that you had made, keeping only the treasure. When you have decent housing with servants, guards, traps, and fortifications, call me to look. Ten years I give you, if you can handle this you will become the successor of your race.",
        # количество лет на выполнение квеста, не зависящее от уровня дракона
        'fixed_time': 10,
        # ключевое слово для описания задачи, 'lair' - проверяется тип логова и его улучшений
        'task': 'lair',
        # кортеж с описанием препятствий для выполнения квеста,
        # 'impassable_coomb' - буреломный овраг, квест не выполнится с этим типом логова
        'task_obstruction': ('impassable_coomb',),
        # кортеж с требованиями, для выполнения задания нужно выполнить любое из них,
        # чтобы потребовать список требований - нужно использовать кортеж внутри кортежа
        # а для вариантов среди списка требований - нужно использовать котреж,
        # который будет внутри кортежа для списка, который уже внутри кортежа
        'task_requirements': (
            ('mechanic_traps', 'magic_traps', 'gremlin_fortification'),
            ('gremlin_servant', 'servant'),
            ('poison_guards', 'regular_guards', 'elite_guards', 'smuggler_guards'),
        )
    },
    {   # Поймать вора или одолеть рыцаря в собственном логове.
        'min_lvl': 5,  # минимальный уровень дракона для получения квеста
        'max_lvl': 5,  # максимальный уровень дракона для получения квеста
        'text': u" \n   At your age, your father went to the land of the Free and made a great lair. The truth is, he never dealt with the real concerns that a lair is necessary for. In the lair you keep your treasures and captives hatching your offspring. The more notorious you become, the more villains will come to harm you. \n     Knights will come while you sleep, wake you up with the sound of a battle horn, and call you out to fight. If the knight overpowers you, you can run, but all the treasures and prisoners will be lost forever! \n Thieves are not as dangerous, but they are very irritating. Like flies to honey, they come for gold. The thief will try to sneak into the treasury while you sleep and steal the most valuable things from right under your nose! \n   Here\'s the value of guards, fortifications, and traps.  \n Make yourself an unapproachable den and test it in action - catch the thief or overcome the knight. Then I will be able to sleep peacefully, knowing that my children can take care of themselves and live a long life in the land of our enemies. \n A quarter century should be enough, but if you can handle it faster - come earlier.",  # текст квеста
        'fixed_time': 25,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        'task': 'event',  # ключевое слово для описания задачи, 'event' - должно произойти какое-то событие
        # кортеж с требованиями, нужно либо 'thief_killer' - поймать вора, либо 'knight_killer' - убить рыцаря
        'task_requirements': (('thief_killer', 'knight_killer')),
    },
    {   'min_lvl': 6,  # минимальный уровень дракона для получения квеста    {   # Набрать дурной славы (уровни 6-11)
        'max_lvl': 11,  # максимальный уровень дракона для получения квеста
        # текст квеста, {0} будет заменён на требуемый уровень
        'text': u"Sit down and listen, my child. Your carefree days are over, and now you are an adult on your own, alone in the world of men. Can you take care of yourself as well as your ancestors did? If you want to be a successor, then prove yourself - gain infamy (not less than {0}) and return to me for a reward. \n   But do not hurry too much. We have a lot of time, but we must think about the future. Gold which you may gather, and offspring that you send my army will be very useful to us when the hour of war comes.  \n   Let thy name be a nightmare for all the Free Peoples!",
        'lvlscale_time': 5,  # на что нужно умножить уровень дракона, чтобы получить число лет на выполнение
        # ключевое слово для описания задачи, 'reputation' - проверяется уровень дурной славы
        'task': 'reputation',
        'fixed_threshold': 5,  # задаёт фиксированное значения для задачи
        # число, на которое нужно умножить уровень дракона, чтобы получить необходимый уровень
        'lvlscale_threshold': 1,
    },
    {   # Набрать сокровищ
        'min_lvl': 6,  # минимальный уровень дракона для получения квеста
        'max_lvl': 10,  # максимальный уровень дракона для получения квеста
        # текст квеста, {0} будет заменён на требуемый уровень
        'text': u"I can see how your eyes burn at the sight of gold and the female form. You've become quite an adult, a strong dragon. But here all the gold is mine, as well as all feminine charms. If you want something for yourself, my dear, go to the land of the Free Peoples. There\'s plenty of flesh and precious metal, go and take it! \n Our army grows, they need equipment, weapons, and food. We need gold. Collect treasure for me, no less than {0} f. If your golden bed is worth enough, I will allow you to continue your line and your descendants shall praise you!",
        'lvlscale_time': 5,  # на что нужно умножить уровень дракона, чтобы получить число лет на выполнение
        'task': 'wealth',  # ключевое слово для описания задачи, 'wealth' - проверяется стоимость сокровищ
        'fixed_threshold': 10000,  # задаёт фиксированное значения для задачи
        # число, на которое нужно умножить уровень дракона, чтобы получить необходимый уровень
        'lvlscale_threshold': 5000,
    },
    {   # Подарок владычице
        'min_lvl': 6,  # минимальный уровень дракона для получения квеста
        'max_lvl': 12,  # максимальный уровень дракона для получения квеста
        # текст квеста, {0} будет заменён на требуемый уровень
        'text': u"You want me? I know, I know. The older you get, the more you want. You\'re consumed by desire to continue your bloodline, but this right must be earned, my son. Kidnapping and raping is a trick that will not work on me. But I will be gracious if you give me something beautiful. And expensive. No less than {0} f, and bigger is better! I\'m sure you can find something suitable in the treasures of the Free People, or you may even gather materials and make something special. After all, you want me...but it will be years before you can have me. Let this passion feed you, my child. Let it develop into rage. I want to feel your lustful rage! Go and bring me a gift, I\'ll be patient, I\'ll wait for you.",
        'lvlscale_time': 5,  # на что нужно умножить уровень дракона, чтобы получить число лет на выполнение
        'task': 'gift',  # ключевое слово для описания задачи, 'wealth' - проверяется стоимость сокровищ
        'fixed_threshold': 1500,
        # число, на которое нужно умножить уровень дракона, чтобы получить необходимый уровень
        'lvlscale_threshold': 100,
    },
    {   # Породить потомка от великанши.
        'min_lvl': 7,  # минимальный уровень дракона для получения квеста
        'max_lvl': 11,  # максимальный уровень дракона для получения квеста
        'text': u"Congratulations on your day of maturity. You\'ve grown up and are ready, I see you looking at me. All in good time. First prove you\'re a real male. Knocking up peasants is easy, the goblins can handle it. But if you get offspring from a giantess, that is an an achievement. Then I would agree that you are worthy to become the successor of the dragon race. \n     Just please do not forget that in addition to cannon fodder, we need gold. The more you gather, the better we will be prepared for war. Now go, sow terror in the land of the Free Peoples!",  # текст квеста
        'fixed_time': 50,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        'task': 'offspring',  # ключевое слово для описания задачи, 'offspring' - породить потомство
        # кортеж с требованиями, для выполнения задания нужно выполнить любое из них, 'giantess' - потомок от великанши
        'task_requirements': 'giantess',
        # требования для анатомии дракона - список из вариантов, достаточных для выполнения задания
        # каждый вариант - словарь, в котором значение - необходимый модификатор анатомии дракона,
        # а значение - пороговое значение, достаточное для выполнения требования
        'anatomy_required': ({'size': 4}, {'cunning': 1}),
        # наличие этого ключа - задание выполняется только один раз в течение игры,
        # значение - ключ для game.unique, который добавится после выполнения
        'unique': 'giantess'
    },
    {   # Разорить рощу альвов
        'min_lvl': 8,  # минимальный уровень дракона для получения квеста
        'max_lvl': 12,  # максимальный уровень дракона для получения квеста
        'text': u"You grew up. You\'ve become so large and powerful. Stronger than any of your ancestors, I remember them all. A little more and dragons will be ready to fulfill their destiny. But not you. For you, I have a test worthy of your power and splendor. Until now, we have attacked men, and they are really the most vile race of all. But there are others. The forests are hiding cowardly elves, children of the goddess Danu. Show them what dragons are capable of. Find and destroy their sacred tree, kill their rulers, defile their magical grove. Waiting for you are untold wealth and eternally young and beautiful maidens. But remember, none of them hold a candle to me. And you will only have me when you overcome the forest people. Now go!",  # текст квеста
        'fixed_time': 75,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        'prerequisite': 'giantess',  # ключ для game.unique, который необходим для получения этой задачи
        'task': 'event',  # ключевое слово для описания задачи, 'event' - должно произойти какое-то событие
        # кортеж с требованиями, для выполнения задания нужно выполнить любое из них,
        # 'ravage_sacred_grove' - разорить рощу альвов
        'task_requirements': 'ravage_sacred_grove',
        # наличие этого ключа - задание выполняется только один раз в течение игры,
        # значение - ключ для game.unique, который добавится после выполнения
        'unique': 'ravage_sacred_grove'
    },
    {   # Устроить логово в подгорном царстве цвергов
        'min_lvl': 9,  # минимальный уровень дракона для получения квеста
        'max_lvl': 12,  # максимальный уровень дракона для получения квеста
        'text': u"Oh, how did you become so big! Stronger than all the others, I think I know exactly who will become the successor of the draconic race. But like all your ancestors, first you have to prove that you deserve it, my dear. Men are not a threat to you. Even elves cannot resist. But in the Free Lands there is no greater wealth than that concealed in the halls of the dwarves. To impose your paw on them should be an easy task for a mighty snake like you. Defeat the dwarves, and build your den in their palace in mockery of their king. Then I will be yours. \n     Go. The hour is close when all free people bow before the power of my children.",  # текст квеста
        'fixed_time': 75,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        'prerequisite': 'ravage_sacred_grove',  # ключ для game.unique, который необходим для получения этой задачи
        'task': 'lair',  # ключевое слово для описания задачи, 'lair' - проверяется тип логова и его улучшений
        # кортеж с требованиями, для выполнения задания нужно выполнить любое из них,
        # 'ravage_sacred_grove' - разорить рощу альвов
        'task_requirements': 'underground_palaces',
        # наличие этого ключа - задание выполняется только один раз в течение игры,
        # значение - ключ для game.unique, который добавится после выполнения
        'unique': 'underground_palaces'
    },
    {   # Захватить столицу
        'min_lvl': 13,  # минимальный уровень дракона для получения квеста
        'max_lvl': 20,  # максимальный уровень дракона для получения квеста
        'text': u"Come to me, my son. How big and strong you\'ve grown up. We need not wait any longer, you will be the one who will avenge me. You will fulfill the purpose of your existence, and put the crowns of the rulers of the Free Peoples at my feet. \n     Do not hurry, I will give you enough time for preparation. Take care that our army is at full readiness, we need more fighters, the more varied the better. When the time comes to act, remember that there will be many battles without time to rest. In each fight we will have losses, many if you stand aside and fewer if you spearhead the attack. If necessary, I will once myself. When the capital of man falls, the rest will surrender themselves...",  # текст квеста
        'fixed_time': 1000,  # количество лет на выполнение квеста, не зависящее от уровня дракона
        'task': 'event',  # ключевое слово для описания задачи, 'event' - должно произойти какое-то событие
        # кортеж с требованиями, для выполнения задания нужно выполнить любое из них,
        # 'victory' - заглушка для победы
        'task_requirements': 'victory',
    },
)

# Список всех доступных для дракона событий
dragon_events = (
    'ravage_sacred_grove',  # Добавляется при уничтожении священной рощи альвов
    'thief_killer',  # Убил вора
    'knight_killer',  # Убил рыцаря
)

# Словарь с набором параметров создания/покупки вещей для упрощения вызова
craft_options = {
    'jeweler_buy': {
        'is_crafting': False, 
        'quality': ['rough', 'common', 'skillfully', 'mastery'], 
        'alignment': ['human'], 
        'base_cost': 0, 
        'price_multiplier': 200,
    },
    'jeweler_craft': {
        'is_crafting': True, 
        'quality': ['skillfully'], 
        'alignment': ['human'], 
        'base_cost': 200, 
        'price_multiplier': 0,
    },
    'gremlin': {
        'is_crafting': True, 
        'quality': ['random'], 
        'alignment': ['random'], 
        'base_cost': 100, 
        'price_multiplier': 0,
    },
    'servant': {
        'is_crafting': True, 
        'quality': ['common'], 
        'alignment': [], 
        'base_cost': 0, 
        'price_multiplier': 0,
    },
}

# Различный лут
loot = {
    'palace': [
        'taller',
        'taller',
        'taller',
        'taller',
        'dubloon',
        'dubloon',
        'dubloon',
        'dish',
        'dish',
        'goblet',
        'goblet',
        'cup',
        'cup',
        'casket',
        'statue',
        'tabernacle',
        'icon',
        'tome',
        'mirror',
        'band',
        'pendant',
        'broach',
        'gemring',
        'seal',
        'crown',
        'scepter',
        'chain',
        'brooch',
        'silver',
        'gold',
        'ivory',
        'agate',
        'shell',
        'horn',
        'amber',
        'granite',
        'tourmaline',
        'aqua',
        'black_pearl',
        'topaz',
        'sapphire',
        'ruby',
        'emerald',
    ],

    'knight': [
        'goblet',
        'statue',
        'tome',
        'band',
        'pendant',
        'ring',
        'gemring',
        'seal',
        'armbrace',
        'chain',
        'brooch',
        'taller',
        'taller',
        'taller',
        'dubloon',
        'dubloon',
    ],
    
    'jeweler': [
        'taller',
        'taller',
        'dubloon',
        'dubloon',
        'casket',
        'phallus',
        'band',
        'diadem',
        'tiara',
        'earring',
        'necklace',
        'pendant',
        'ring',
        'broach',
        'gemring',
        'armbrace',
        'legbrace',
        'chain',
        'brooch'
    ],
    
    'smuggler': [
        'silver',
        'gold',
        'mithril',
        'adamantine',
        'jasper',
        'turquoise',
        'jade',
        'malachite',
        'coral',
        'ivory',
        'agate',
        'shell',
        'horn',
        'amber',
        'crystal',
        'beryll',
        'tigereye',
        'granite',
        'tourmaline',
        'aqua',
        'pearl',
        'elven_beryll',
        'black_pearl',
        'topaz',
        'sapphire',
        'ruby',
        'emerald',
        'goodruby',
        'goodemerald',
        'star',
        'diamond',
        'black_diamond',
        'rose_diamond',
        'taller',
        'dubloon',
        'taller',
        'dubloon'
    ],
    
    'klad': [
        'goblet',
        'statue',
        'band',
        'diadem',
        'tiara',
        'earring',
        'necklace',
        'pendant',
        'ring',
        'broach',
        'gemring',
        'seal',
        'armbrace',
        'legbrace',
        'crown',
        'scepter',
        'chain',
        'brooch',
        'silver',
        'gold',
        'mithril',
        'adamantine',
        'jasper',
        'turquoise',
        'jade',
        'malachite',
        'coral',
        'ivory',
        'agate',
        'shell',
        'horn',
        'amber',
        'crystal',
        'beryll',
        'tigereye',
        'granite',
        'tourmaline',
        'aqua',
        'pearl',
        'elven_beryll',
        'black_pearl',
        'topaz',
        'sapphire',
        'ruby',
        'emerald',
        'goodruby',
        'goodemerald',
        'star',
        'diamond',
        'black_diamond',
        'rose_diamond',
        'taller',
        'dubloon',
        'taller',
        'dubloon',
        'taller',
        'dubloon',
        'taller',
        'dubloon',
        'taller',
        'dubloon',
    ],
    
    'coins': [
        'farthing',
        'taller',
        'dubloon'
    ],

    'church': [
        'goblet',
        'cup',
        'casket',
        'statue',
        'tabernacle',
        'icon',
        'tome',
        'seal',
    ],
    
    'raw_material': [
        'silver',
        'silver',
        'silver',
        'silver',
        'silver',
        'silver',
        'silver',        
        'gold',
        'gold',
        'gold',
        'gold',
        'gold',
        'mithril',
        'adamantine',
        'jasper',
        'turquoise',
        'jade',
        'malachite',
        'coral',
        'ivory',
        'agate',
        'shell',
        'horn',
        'amber',
        'crystal',
        'beryll',
        'tigereye',
        'granite',
        'tourmaline',
        'aqua',
        'pearl',
        'elven_beryll',
        'black_pearl',
        'topaz',
        'sapphire',
        'ruby',
        'emerald',
        'goodruby',
        'goodemerald',
        'star',
        'diamond',
        'black_diamond',
        'rose_diamond'
    ],

    'any': [
        'farthing',
        'taller',
        'dubloon',
        'dish',
        'goblet',
        'cup',
        'casket',
        'statue',
        'tabernacle',
        'icon',
        'tome',
        'mirror',
        'comb',
        'phallus',
        'band',
        'diadem',
        'tiara',
        'earring',
        'necklace',
        'pendant',
        'ring',
        'broach',
        'gemring',
        'seal',
        'armbrace',
        'legbrace',
        'crown',
        'scepter',
        'chain',
        'brooch',
        'silver',
        'gold',
        'mithril',
        'adamantine',
        'jasper',
        'turquoise',
        'jade',
        'malachite',
        'coral',
        'ivory',
        'agate',
        'shell',
        'horn',
        'amber',
        'crystal',
        'beryll',
        'tigereye',
        'granite',
        'tourmaline',
        'aqua',
        'pearl',
        'elven_beryll',
        'black_pearl',
        'topaz',
        'sapphire',
        'ruby',
        'emerald',
        'goodruby',
        'goodemerald',
        'star',
        'diamond',
        'black_diamond',
        'rose_diamond'
    ],
}

# список специальных мест людей
human_special_places = [
    'lb_manor_found',
    'lb_wooden_fort_found',
    'lb_abbey_found',
    'lb_castle_found',
    'lb_palace_found',
]

game_events = {
    "mobilization_increased": "lb_event_mobilization_increase",
    "poverty_increased": "lb_event_poverty_increase",
    "no_thief": "lb_event_no_thief",    # Не было активного вора и новый не нашелся
    "no_knight": "lb_event_no_knight",  # Не было активного рыцаря и новый не нашелся
    "sleep_start": "lb_event_sleep_start",
    "sleep_new_year": "lb_event_sleep_new_year",
    "sleep_end": "lb_event_sleep_end",
}

dark_army = {
    "grunts": {
        0: u"After defeat in the Battle of Six Armies, pathetic lumps of the Mistress\'s army remain. "
           u"The few surviving goblins hide in their caves and "
           u"multiply like rabbits in an attempt to join the ranks of the troops. ",
        10: u"The good news: in the barren plain there are enough aggressive creatures, "
           u"that one could form an army with them. "
           u"The bad news: this army will be inferior in number to what the free people can gather.",
        25: u"Caves and holes no longer suffice to give shelter to all the hideous soldiers gathered before Mistress. "
            u"The barren plains are the scene of a huge construction site - here and there, there are whole towns of tents. "
            u"Ditches, embankments, and palisades are laboriously dug. "
            u"At a glance this army seems the equal of any coalition of the Free Peoples.",
        50: u"Looking at the barren plains at night, it is difficult to see where they end and the starry sky begins. "
            u"The earth is burnt with countless fires giving light and warmth to the soldiers of Mistress. "
            u"During the day, one can see thousands of tents covering the valley like a thicket of poisonous mushrooms. "
            u"Here and there, soldiers patrol and messengers scurry. "
            u"This huge horde would engulf the armies of the Free Peoples like the surf."
    },
    "elites": {
        0: u"But whatever the number of these common soldiers, the biggest weakness is the lack of elite fighters. "
           u"Having faced giants, elven mages, and dwarven fighting machines on the battlefield, "
           u"Mistress learned that the only beings that can resist them "
           u"surpass the strength of men or goblins. Dragons must generate such fighters, "
           u"the army desperately needs them.",
        1: u"Here and there, you notice huge silhouettes of elite fighters. "
           u"There are not many, but they stand ready to attack at the crucial time and place. ",
        5: u"Each detachment of small creatures includes at least one elite fighter, "
           u"generated by the dragon from the most powerful blood of the Free Peoples. "
           u"Each of these mighty giants is worth an army in a fight.",
        10: u"In this army are so many elite fighters, "
           u"that trifling creatures like goblins serve only as reconnaissance and support. "
           u"This shock power comes from ugly giants produced by dragons from the mightiest blood of the Free Peoples."
    },
    "diversity": {
        0: u"The Army of Darkness lacks variety, "
           u"the vast majority of fighters are from a single species. "
           u"Warriors of the Free people are used to fighting with these creatures, "
           u"and have developed tactics against them.",
        2: u"The variety of forces is not too great, "
           u"though the dragonspawn will be beneficial supplements to the usual goblins on the battlefield. "
           u"Nevertheless, the free people will have little difficulty working out tactics "
           u"to counter the strengths and weaknesses of all the Mistress\'s fighters.",
        4: u"Under the banner of the Mistress are gathered many diverse dragonspawn. "
           u"There are short soldiers and lanky soldiers, rapid spies and massive ground fighters, of all colors, shapes and sizes. "
           #u"Кого-то украшает чеушая, кого-то рога. " #trans: ??
           u"Favorably complementing each other on the battlefield. "
           u"All this motley company makes it impossible for the Free People to use simple and familiar battle tactics.",
        7: u"There are so many different creatures that even the Mistress could probably not distinguish between them all. "
           u"Mixing together uncontrollably "
           u"the dragon\'s offspring generate new mutant hybrids with incredible properties. "
           u"When the war begins, free people will not know how to deal with them."
    },
    "equipment": {
        1: u"Money for military equipment is solely lacking. Some of Mistress\'s warriors walk about in loincloths, "
           u"and are armed with clubs and sharpened sticks. "
           u"Only a few can afford a crude armor of badly treated skins.",
        2: u"The army is armed to a minimum. The rank and file soldiers can hope to obtain an iron spear, "
           u"woven shield, and a simple quilted armor. The elite are armed a little better, but still far from the ideal.",
        3: u"The accumulated dragon treasures allow decent equipment for the Mistress\'s fighters. "
           u"Even ordinary soldiers have a full set of arms and armor,"
           u"and the elite are clad in blue steel from head to toe. "
           u"Ranks of shields and iron points will look very impressive on the battlefield.",
        4: u"Over the years, the Mistress\'s dragons hoarded many treasures, "
           u"more than enough to arm the whole army at the highest level. "
           u"Heavy infantry and cavalry are armed to the teeth, and the elite fighters flaunt magical weapons and armor. "
    },
    "force": {
        0: u"To oppose the Free People with such forces would be suicide, unless the dragon itself could win every fight.",
        500: u"Although the army of darkness has become stronger in recent years, it is not yet ready to battle the free people. The dragon will have to take the brunt of each fight to stand a chance.",
        1000: u"Overall, the Army of Darkness is good enough to have a chance in battles with the armies of the Free People. "
              u"However, there cannot be full confidence in victory. The dragon will have to support the troops by example.",
        1800: u"Through years of preparation the Army of Darkness has soared to incredible heights of power. "
              u"The army of the Free Peoples will be crushed and trampled by this invincible force. Even ignoring the help the dragon and Mistress can personally render."
    }
}
#Achievements
def achieve_target(target, tag=None):
    for achievement in achievements_list:
        if tag == "wealth" or tag == "treasure" or tag == "reputation":
            if achievement.goal == tag:
                    achievement.progress(target)
        elif achievement.goal == tag and target in achievement.targets:
            achievement.progress(target)
def achieve_restart(reason):
    for achievement in achievements_list:
        if achievement.restartif == reason:
            achievement.restart()
def achieve_fail(reason):
    for achievement in achievements_list:
        if achievement.failif == reason:
            achievement.fail()
def achieve_win(dragon):
    achieve_target("win", "win")
    if dragon.size > 1:
        achieve_fail("too_big")
    if dragon.magic > 0:
        achieve_fail("dragon_magic")
    for n in xrange(dragon.size):
        achieve_target("size", "win")
    for head in dragon.heads:
        if head != "green":
            achieve_target("colored_head", "win")
        achieve_target("head", "win")
    if dragon.wings == 1 and dragon.paws == 2 and len(dragon.heads) == 1:
        achieve_target("archetype", "win")
    else:
        achieve_target(dragon.kind, "win")
    achieve_target(dragon.color_eng, "win")
def store_achievements(storage_dict):
    temporary_storage = {}
    for achievement in achievements_list:
        if achievement.unlocked and achievement.name not in storage_dict.keys():
            storage_dict[achievement.name] = achievement.description
            temporary_storage[achievement.name] = achievement.description
    return temporary_storage
class Achievement(object):
    def __init__(self, name="", description="", goal=None, targets=None, restartif=None, failif=None, *args, **kwagrs):
        self.name = name
        self.description = description
        self.unlocked = False
        self.failed = False
        self.restartif = restartif
        self.failif = failif
        self.goal = goal
        self.targets = targets
        self.targets_completed = []
    def progress(self, target):
        if self.failed:
            return
        if self.targets:
            if self.goal == "wealth" or self.goal == "treasure" or self.goal == "reputation":
                for i in self.targets:
                    if target >= i:
                        self.targets.remove(i)
                        self.targets_completed.append(i)
                
            else:
                self.targets_completed.append(target)
                self.targets.remove(target)
                    
        if not self.targets and not self.unlocked:
            self.unlock()
    def unlock(self):
        if not self.failed:
            self.unlocked = True
    def fail(self):
        self.failed = True
    def restart(self):
        if not self.unlocked and self.targets_completed:
            self.targets.extend(self.targets_completed)
            self.targets_completed = []

achievements_list = [Achievement(name = u"The Great Snake",
                                 description = u"Win in story mode",
                                 goal = "win",
                                 targets = ["win"]),
                     Achievement(name = u"Corruptor",
                                 description=u"Make a lair in the elven forest",
                                 goal = "lair",
                                 targets = ["forest_heart"]),
                     Achievement(name = u"Magnificent Smaug",
                                 description = u"Make a den in the dwarven mountain palace",
                                 goal = "lair",
                                 targets = ["underground_palaces"]),
                     Achievement(name = u"Excellent lodge",
                                 description = u"Reached a total treasure value of 100,000 f.",
                                 goal = "wealth",
                                 targets = [100000]),
                     Achievement(name = u"The Crown of the Collection",
                                 description = u"Bear in the treasury an item worth more than 9,000 f.",
                                 goal = "treasure",
                                 targets = [9000]),
                     Achievement(name = u"The Legendary Tyrant",
                                 description = u"Reach a level of notoriety of over 19",
                                 goal = "reputation",
                                 targets = [19]),
                     Achievement(name = u"Inseminator",
                                 description = u"As one dragon, mate with all kinds of non-giantesses",
                                 goal = "impregnate",
                                 targets = ["peasant", "citizen", "princess", "elf", "mermaid"], #вернуть когда появятся  "thief", "knight",
                                 restartif = "new_dragon"),
                     Achievement(name = u"Father of Titans",
                                 description = u"As one dragon, mate with all kinds of giantesses",
                                 goal = "impregnate",
                                 targets = ["ice", "fire", "titan", "ogre", "siren"],
                                 restartif = "new_dragon"),
                     Achievement(name = u"Unbreakable",
                                 description = u"Win in story mode without losing your head",
                                 goal = "win",
                                 targets = ["win"],
                                 failif = "lost_head"),
                     Achievement(name = u"Absolute Predator",
                                 description = u"Defeat an angel, titan, and golem as one dragon.",
                                 goal = "kill",
                                 targets = ["Steel golem", "Angel", "Titan"],
                                 restartif = "new_dragon"),
                     Achievement(name = u"Child of Destiny",
                                 description = u"Win the game by occupying the lands of the Free Peoples",
                                 goal = "win",
                                 targets = ["conquer"]),
                     Achievement(name = u"Judas",
                                 description = u"Win the game by defeating Mistress",
                                 goal = "win",
                                 targets = ["betray"]),
                     Achievement(name = u"Archetype", 
                                 description = u"Win with a regular dragon",
                                 goal = "win",
                                 targets = ["archetype"]),
                     Achievement(name = u"Jormungandr",
                                 description = u"Win with a wingless, limbless wyrm",
                                 goal = "win",
                                 targets = [u"serpent"]),
                     Achievement(name = u"The Hydra",
                                 description = u"Win as a many-headed dragon",
                                 goal = "win",
                                 targets = [u"multi headed dragon"]),
                     Achievement(name = u"Legacy of Tiamat",
                                 description = u"Win as a dragon with 3+ colors",
                                 goal = "win",
                                 targets = ["colored_head", "colored_head", "colored_head"]),
                     Achievement(name = u"Lernaean Hydra",
                                 description = u"Win as a dragon with 4+ heads",
                                 goal = "win",
                                 targets = ["head", "head", "head", "head"]),
                     Achievement(name = u"Leviathan",
                                 description = u"Win as the maximum size of dragon",
                                 goal = "win",
                                 targets = ["size", "size", "size", "size", "size", "size"]),
                     Achievement(name = "T-Rex",
                                 description = u"Win as a green Lindwurm without magic, with one head, and size larger than 4",
                                 goal = "win",
                                 targets = ["size", "size", "size", "size", u"lindwurm", "green"],
                                 failif = "dragon_magic"),
                     Achievement(name = u"Godzilla",
                                 description = u"Win as a red Lindwurm larger than 4",
                                 goal = "win",
                                 targets = ["size", "size", "size", "size", u"lindwurm", "red"]),
                     Achievement(name = u"Feysky Dragon",
                                 description = u"win as a small dragon",
                                 goal = "win",
                                 targets = ["size"],
                                 failif = "too_big"),
                     Achievement(name = u"Watchful Eye",
                                 description = u"Win without losing any treasure to thieves or knights",
                                 goal = "win",
                                 targets = ["win"],
                                 failif = "lost_treasure"),
                     Achievement(name = u"Easter Bunny", #if you change this name, also change it in lb_achievement_acquired
                                 description = u"collect all the easter eggs",
                                 goal = "easter_eggs",
                                 targets = ["domiki_done", "redhood_done"])
                    ]
