"""There was some very sick shit going on in this file. 
#russian has noun declension and gender.
#There were data structures listing the he,she,they,it, nominative, genitive, ablative, versions of everything and elaborate code for combining them. I simplified the data structures and tried (badly) to simplify the code.

#Each category of loot has its own class: gems, coins, ingots, treasures, and materials, and there's a main Treasury class that handles all of them.

Every class of loot has a description() function that describes a single loot object, like "Rough common agate". This is always used for treasures, because they're so unique that you only ever deal with single treasure objects.

The treasury class also has functions that take all the gems and stuff and put them in a dictionary like ["agate;common;rough"] : [5], to add up all the duplicates.
And then there will be a function like gem.number_conjugation that takes that key and value and outputs "5 rough common agates". There are also extra functions at the start of this file like number_pluralizer and number_conjugation_rus that do similar things, it's mostly redundant. 

I could improve this, but this version is thoroughly tested and doesn't crash, so I don't want to touch it right now.

"""
#file encoded utf-8
import random

from renpy import store
from renpy.exports import call_screen
from copy import deepcopy
                
from utils import weighted_random
from data import achieve_target, get_description_by_count

"""Dictionary for gems. Keys- the names of the stones. Values- tuples of form (chance of, value of)"""
gem_types = {
    "amber": (5, 3),
    "crystal": (5, 5),
    "beryll": (4, 10),
    "tigereye": (4, 10),
    "granite": (3, 20),
    "tourmaline": (3, 20),
    "aqua": (3, 20),
    "pearl": (3, 10),
    "black_pearl": (3, 15),
    "elven_beryll": (2, 50),
    "topaz": (2, 50),
    "sapphire": (2, 50),
    "ruby": (2, 50),
    "emerald": (2, 25),
    "goodruby": (1, 100),
    "goodemerald": (1, 100),
    "star": (1, 100),
    "diamond": (1, 75),
    "black_diamond": (1, 100),
    "rose_diamond": (1, 100),
}

"""As above, but for type of material"""
material_types = {
    "jasper": (5, 1),
    "turquoise": (5, 1),
    "jade": (5, 1),
    "malachite": (5, 1),
    "coral": (4, 5),
    "ivory": (4, 10),
    "agate": (3, 5),
    "shell": (3, 5),
    "horn": (1, 25),
}

"""словарь для описания типов материалов,
ключи - названия материалов,
значения - словарь для различных падежей русского названия материала"""
material_description_rus = {
    "jasper": u'jasper',
    "turquoise": u'turquoise',
    "jade": u'jade',
    "malachite": u'malachite',
    "coral": u'coral',
    "ivory": u'ivory',
    "agate": u'agate',
    "shell": u'shell',
    "horn": u'horn',
}

"""словарь для описания размеров материалов,
ключи - названия размера материалов,
значения - словарь для русского прилагательного, соответствующего размеру"""
material_size_description_rus = {
    'small': u"small ",
    'common': u"",
    'large': u"large ",
    'exceptional': u"exceptional ",
}
"""словарь для описания степени обработки драгоценных камней,
ключи - названия степени обработки,
значения - словарь для соответствующего русского прилагательного"""
gem_cut_description_rus = {
    ' ': u'',
    'rough': u'rough ',
    'polished': u'polished ',
    'faceted': u'faceted ',
}

"""Словарь для драгоценных камней,
ключ - тип драгоценного камня,
значение - словарь с русским названием драгоценного камня в разных падежах"""
gem_description_rus = {
    "amber": {
        'singular': u'amber',
        'plural': u'amber'},
    "crystal": {
        'singular': u'crystal',
        'plural': u'crystals'},
    "beryll": {
        'singular': u'beryl',
        'plural': u'beryls'},
    "tigereye": {
        'singular': u'tigereye',
        'plural': u'tigereye'},
    "granite": {
        'singular': u'granite',
        'plural': u'granite'},
    "tourmaline": {
        'singular': u'tourmaline',
        'plural': u'tourmalines'},
    "aqua": {
        'singular': u'aqua',
        'plural': u'aqua'},
    "pearl": {
        'singular': u'pearl',
        'plural': u'pearls'},
    "black_pearl": {
        'singular': u'black pearl',
        'plural': u'black pearls'},
    "elven_beryll": {
        'singular': u'elven berylls',
        'plural': u'elven berylls'},
    "topaz": {
        'singular': u'topaz',
        'plural': u'topazes'},
    "sapphire": {
        'singular': u'sapphire',
        'plural': u'sapphires'},
    "ruby": {
        'singular': u'ruby',
        'plural': u'rubies'},
    "emerald": {
        'singular': u'emerald',
        'plural': u'emeralds'},
    "goodruby": {
        'singular': u'fine ruby',
        'plural': u'fine rubies'},
    "goodemerald": {
        'singular': u'emerald',
        'plural': u'fine emeralds'},
    "star": {
        'singular': u'star sapphire',
        'plural': u'star sapphires'},
    "diamond": {
        'singular': u'diamond',
        'plural': u'diamonds'},
    "black_diamond": {
        'singular': u'black diamond',
        'plural': u'black diamonds'},
    "rose_diamond": {
        'singular': u'rose diamond',
        'plural': u'rose diamonds'},
}
"""словарь для типов металлов, ключ - металл, значение - ценность"""
metal_types = {
    "silver": 1,
    "gold": 10,
    "mithril": 25,
    "adamantine": 30,
}
"""key- type of treasure,
value - (base price, gender, can make out of metal(bool), can make out of semi-precious material (bool), can forge an image on(bool), can decorate (bool))"""
treasure_types = {  # допилить типы сокровищ
    "dish": (5, True, False, False, False, True),
    "goblet": (4, True, False, False, True, True),
    "cup": (3, False, True, False, False, True),
    "casket": (5, True, True, False, True, True),
    "statue": (10, True, True, True, False, False),
    "tabernacle": (5, True, True, False, True, True),
    "icon": (10, True, False, True, False, False),
    "tome": (10, True, False, False, True, True),
    "comb": (2, True, True, False, False, True),
    "phallus": (3, True, True, False, False, True),
    "mirror": (4, True, True, False, True, True),
    "band": (3, True, False, False, False, False),
    "diadem": (10, True, False, False, True, False),
    "tiara": (15, True, False, False, True, False),
    "earring": (1, True, False, False, True, False),
    "necklace": (5, True, False, False, True, False),
    "pendant": (3, True, False, False, False, True),
    "ring": (2, True, True, False, False, False),
    "broach": (3, True, False, False, True, False),
    "gemring": (5, True, True, False, True, False),
    "seal": (3, True, True, False, False, True),
    "armbrace": (3, True, True, False, True, True),
    "legbrace": (4, True, True, False, True, True),
    "crown": (15, True, False, False, True, False),
    "scepter": (15, True, False, False, True, False),
    "chain": (3, True, False, False, False, False),
    "brooch": (2, True, False, False, False, True),
}
"""словарь для описания типов драгоценностей,
ключ - тип драгоценностей,
значение - словарь с русским названием драгоценности в разных падежах"""
treasure_description_rus = {  # допилить типы сокровищ
    "dish": u'dish',
    "goblet": u'goblet',
    "cup": u'cup',
    "casket": u'casket',
    "statue": u'statue',
    "tabernacle": u'tabernacle',
    "icon": u'icon',
    "tome": u'tome', 
    "comb": u'comb',
    "phallus": u'phallus',
    "mirror": u'mirror',
    "band": u'band',
    "diadem": u'diadem',
    "tiara": u'tiara',
    "earring": u'earring',
    "necklace": u'necklace',
    "pendant": u'pendant',
    "ring": u'ring',
    "broach": u'broach',
    "gemring": u'gemring',
    "seal": u'seal',
    "armbrace": u'armbrace',
    "legbrace": u'legbrace',
    "crown": u'crown',
    "scepter": u'scepter',
    "chain": u'chain',
    "brooch": u'brooch',
}
"""словарь для описания типов металлов, ключ - тип металла, значение - русское названия драгоценности в разных родах"""
metal_description_rus = {
    'silver': u"silver",
    'gold': u"gold",
    'mithril': u"mithril",
    'adamantine': u"adamantine",
}
"""словарь для изображений, ключ - тип культуры, значение - кортеж из вариантов изображений"""
image_types = { 
    'human': (
        'abstract_ornament', 'concentric_circles', 'round_dance', 'fire-breathing_dragon', 'flying_dragon',
        'wingless_dragon', 'snake_with_a_crown', 'winged_serpent', 'cocatrice', 'basilisk',
        'dragon_entwine_naked_girl', 'battle_dragon_with_knight', 'dancing_girls', 'bathing_girl',
        'children_playing', 'rider_with_bow', 'horseman_with_spear_and_shield', 'dead_knight_with_sword'),
    'knight': (
        'proud_motto', 'battle_scene', 'coat_of_arms_with_rearing_unicorn', 'coat_of_arms_with_head_of_boar',
        'coat_of_arms_with_three_lilies', 'coat_of_arms_with_roaring_lion', 'coat_of_arms_with_proud_eagle',
        'coat_of_arms_with_procession_giraffe', 'coat_of_arms_with_crossed_swords',
        'coat_of_arms_with_shield_and_sword'),
    'cleric': (
        'saying_of_holy_scriptures', 'scene_of_holy_scriptures', 'saint_with_halo', 'angel_with_flaming_sword',
        'angel_winning_serpent', 'raising_hands_angel', 'six-winged_seraph', 'holy_maiden_and_child',
        'holy_maiden_stretches_hands', 'weeping_maiden'),
    'elf': (
        'floral_ornament', 'elegant_runes', 'running_deer', 'bear_with_raised_legs', 'wolf_hunting', 'sneaking_manul',
        'two_songbirds', 'moon_and_stars', 'branched_oak', 'blooming_vine', 'spreading_maple', 'weeping_willow',
        'dancing_nymphs', 'nymph_with_cup', 'nymph_collecting_fruits', 'nymph_playing_harp', 'winged_maiden',
        'satyr_playing_flute', 'forest_guard_bow'),
    'dwarf': (
        'geometric_pattern', 'runic_ligature', 'hammer_and_crown', 'dwarfs_holding_over_his_head_anvil',
        'armed_dwarfs_tramples_goblin', 'crossed_axes', 'entwined_rings', 'helmet_with_horns',
        'krotocherv', 'dwarfs', 'urist_makdvarf', 'dragon_smaug'),
    'merman': (
        'wavy_pattern', 'frolicking_fish', 'seahorse', 'newt_lifting_trident', 'triton_and_siren_holding_hands',
        'mermaid_brushing_hair', 'playing_mermaid', 'mermaid_playing_with_pearl', 'awesome_sea_serpent',
        'flying_seagull', 'wriggling_octopus', 'kraken_drowning_sea_vessel', 'sailing_ship'),
}
"""словарь для описания изображений,
ключ - вариант изображения,
значение - словарь из рода изображения и описания изображения в различных падежах"""
image_description_rus = {
    'abstract_ornament': u'an abstract decoration',
    'concentric_circles': u'concentric circles',
    'round_dance': u'a ring dance',
    'fire-breathing_dragon': u'a fire-breathing dragon',
    'flying_dragon': u'a flying dragon',
    'wingless_dragon': u'a wingless dragon',
    'snake_with_a_crown': u'a crowned snake',
    'winged_serpent': u'a winged serpent',
    'cocatrice': u'a cocatrice',
    'basilisk': u'a basilisk',
    'dragon_entwine_naked_girl': u'a dragon entwined with a naked girl',
    'battle_dragon_with_knight': u'a dragon battling a knight',
    'dancing_girls': u'dancing girls',
    'bathing_girl': u'bathing girls',
    'children_playing': u'children playing',
    'rider_with_bow': u'a rider with a bow',
    'horseman_with_spear_and_shield': u'a horseman with a shield and spear',
    'dead_knight_with_sword': u'a dead knight with a sword',
    'proud_motto': u'a proud motto',
    'battle_scene': u'a battle scene',
    'coat_of_arms_with_rearing_unicorn': u'a coat of arms with a rearing unicorn',
    'coat_of_arms_with_head_of_boar': u'a coat of arms with a boar\'s head',
    'coat_of_arms_with_three_lilies': u'a coat of arms with three lilies',
    'coat_of_arms_with_roaring_lion': u'a coat of arms with a rearing lion',
    'coat_of_arms_with_proud_eagle': u'a coat of arms with a proud eagle',
    'coat_of_arms_with_procession_giraffe': u'a coat of arms with a processing giraffe',
    'coat_of_arms_with_crossed_swords': u'a coat of arms with a crossed swords',
    'coat_of_arms_with_shield_and_sword': u'a coat of arms with a sword and shield',
    'saying_of_holy_scriptures': u'a verse from holy scripture',
    'scene_of_holy_scriptures': u'a scene from holy scripture',
    'saint_with_halo': u'a saint with a halo',
    'angel_with_flaming_sword': u'an angel with a flaming sword',
    'angel_winning_serpent': u'an angel defeating a serpent',
    'raising_hands_angel': u'an angel raising his hands',
    'six-winged_seraph': u'a six-winged seraph',
    'holy_maiden_and_child': u'a holy maiden and child',
    'holy_maiden_stretches_hands': u'a holy maiden with outstretched hands',
    'weeping_maiden': u'a weeping maiden',
    'floral_ornament': u'a floral pattern',
    'elegant_runes': u'elegant runes',
    'running_deer': u'a running deer',
    'bear_with_raised_legs': u'a bear with raised legs',
    'wolf_hunting': u'a wolf hunting',
    'sneaking_manul': u'a crouching cat',
    'two_songbirds': u'two songbirds',
    'moon_and_stars': u'the moon and stars',
    'branched_oak': u'a branched oak',
    'blooming_vine': u'a blooming vine',
    'spreading_maple': u'a spreading maple',
    'weeping_willow': u'a weeping willow',
    'dancing_nymphs': u'dancing nymphs',
    'nymph_with_cup': u'a nymph with a cup',
    'nymph_collecting_fruits': u'a nymph collecting fruits',
    'nymph_playing_harp': u'a nymph playing a harp',
    'winged_maiden': u'a winged maiden',
    'satyr_playing_flute': u'a satyr playing a flute',
    'forest_guard_bow': u'a forest guard with a bow',
    'geometric_pattern': u'a geometric pattern',
    'runic_ligature': u'runic patterns',
    'hammer_and_crown': u'a hammer and crown',
    'dwarfs_holding_over_his_head_anvil': u'a dwarf holding an anvil over his head',
    'armed_dwarfs_tramples_goblin': u'armed dwaves trampling a goblin',
    'crossed_axes': u'crossed axes',
    'entwined_rings': u'entwined rings',
    'helmet_with_horns': u'a horned helmet',
    'krotocherv': u'a moleworm',
    'dwarfs': u'dwarves. The dwarves are working',
    'urist_makdvarf': u'Urist McDwarf. Urist McDwarf is eating a masterwork yak cheese. ' u'The artwork relates to the eating of yak cheese by the dwarf Urist McDwarf ' u'in the early spring of 1076',
    'dragon_smaug': u'the dragon Smaug and the dwarf Thorin. Thorin clasps his hands. Smaug is in a threatening posture.' u'This artwork relates to the murder of the King Under the Mountain in Erebor in the late summer of 2770',
    'wavy_pattern': u'a wavy pattern',
    'frolicking_fish': u'a frolicking fish',
    'seahorse': u'a seahorse',
    'newt_lifting_trident': u'a newt lifting a trident',
    'triton_and_siren_holding_hands': u'a triton and siren holding hands',
    'mermaid_brushing_hair': u'a mermaid brushing her hair',
    'playing_mermaid': u'a playing mermaid',
    'mermaid_playing_with_pearl': u'a mermaid playing with a pearl',
    'awesome_sea_serpent': u'a mighty sea serpent',
    'flying_seagull': u'a flying seagull',
    'wriggling_octopus': u'a wriggling octopus',
    'kraken_drowning_sea_vessel': u'a kraken drowning a sea vessel',
    'sailing_ship': u'a sailing ship and waves',
}
"""словарь для описания качества драгоценности,
 ключ - качество,
 значение - словарь с русским названием качества в разных родах"""
quality_description_rus = { 
    'rough': u"rough ",
    'common': u"",
    'skillfully': u"skillfully made ",
    'mastery': u"masterfully made ",
}
"""словарь для описания украшения, ключ - тип украшения, значение - словарь с русским словом в разных родах"""
decoration_description_rus = {
    'decoration': u"decorated with",
    'spangled': u"spangled with",
    'inlaid': u"inlaid with",
    'image': u"depicts",
}
"""словарь для описания типа украшения на русском"""
decorate_types_description_rus = {
    'incuse': u"engravings", #Todo: I don't know of a better word to go here
    'engrave': u"engravings",
    'etching': u"etchings",
    'carving': u"carvings",
}
"""словарь для вывода описаний массы сокровищ на русском"""
treasures_mass_description_rus = {
    'coin': {
        0: u"Coins",
        100: u"Handful of coins",
        1000: u"Pile of coins",
        10000: u"Mountain of coins",
        100000: u"Mountains of coins",
    },
    'material': {
        0: u"Materials",
        100: u"Handful of materials",
        1000: u"Pile of materials",
        10000: u"Mountain of materials",
        100000: u"Mountains of materials",
    },
    'gem': {
        0: u"Gemstones",
        100: u"Handful of gems",
        1000: u"Pile of gems",
        10000: u"Mountain of gems",
        100000: u"Mountains of gems",
    },
    'jewelry': {
        0: u"Trinkets",
        100: u"Handful of trinkets",
        1000: u"Pile of trinkets",
        10000: u"Mountain of treasure",
        100000: u"Mountains of treasure",
    },
    'wealth': {
        0: u"The treasury is virtually empty. ",
        100: u"In the treasury is a pittance that any respectable dragon would be ashamed of. ",
        1000: u"In the treasury there is not much to look at. ",
        10000: u"In the treasury is quite a decent pile of treasure, no longer something to be ashamed of. ",
        100000: u"There is reason to be proud of the treasury. Only the best dragons manage to collect such a mountain of wealth.",
        1000000: u"Mountains of treasure - the pride of the richest dragon in the world. ",
    },
}

def number_pluralizer(num):
    if num > 1:
        return "s"
    else:
        return ""

def number_conjugation_rus(num, word): #Input 5, "ingot", output "5 ingots"
    if num > 1:
        return u"%d %ss" % (num,word)
    else:
        return u"%d %s"% (num,word)
        

def capitalize_first(string):
    return string.capitalize()


def weighted_select(d):
    weight = random.random() * sum(v[0] for k, v in d.items())
    for k, v in d.items():
        if weight < v[0]:
            return k
        weight -= v[0]
    return d.keys()[random.randint(0, len(d.keys()))]


class Ingot(object):  # Class for generating ingots
    weights = (1, 4, 8, 16)
    weights_description_rus = {1: u"tiny", 4: u"small", 8: u"heavy", 16: u"massive"}

    def __init__(self, metal_type):
        self.metal_type = metal_type
        self.metal_cost = metal_types[metal_type]
        self.weight = random.choice(self.weights)

    @property
    def cost(self):
        return self.metal_cost * self.weight

    def __repr__(self):
        return "a %s pound %s ingot" % (self.weight, self.metal_type)

    def description(self):
        if self.weight in self.weights:
            return u"a %s %s ingot" % (
                    self.weights_description_rus[self.weight], metal_description_rus[self.metal_type])
        else:
            return u"The gross weight of the %s ingots is %d pounds" % (
                    metal_description_rus[self.metal_type], self.weight)
                    
    @staticmethod
    def number_conjugation(metal_type, metal_weight):
        """
        Функция для вывода описания слитков металла по типу металла и его количеству
        """
        if metal_weight in Ingot.weights:
            return u"%s %s bar" % (
                Ingot.weights_description_rus[metal_weight], metal_description_rus[metal_type])
        else:
            return u"Some %s bars weighing %d pound%s" % (
                metal_description_rus[metal_type], metal_weight, number_pluralizer(metal_weight))

                
    


class Coin(object):
    coin_types = {"farthing": (1, 1), "taller": (1, 10), "dubloon": (1, 100)}
    coin_description_rus = {"farthing": u"farthing", "taller": u"taller", "dubloon": u"dubloon"}
    """
    Монеты.
    """

    def __init__(self, name, amount):
        self.amount = amount  # количество монеток
        self.name = name
        self.value = Coin.coin_types[self.name][1]

    @property
    def cost(self):
        return self.amount * self.value

    def __repr__(self):
        return str(self.amount) + " " + "%s(s)" % self.name

    def description(self):
        return "%d %s%s" % (self.amount, Coin.coin_description_rus[self.name], number_pluralizer(self.amount))

    
        
        
        
        
        
class Gem(object):   
    cut_dict = {
        " ": (0, 1),
        "polished": (50, 2),
        "rough": (30, 1),
        "faceted": (20, 3)
    } # %chance, value multiplier 
    size_dict = {
        "small": (40, 1),
        "common": (50, 5),
        "large": (8, 25),
        "exceptional": (2, 100)
    } # %chance, size modifier

    def __init__(self, g_type, size, cut):
        self.g_type = g_type  # Тип камня
        self.size = size  # размер
        self.size_mod = Gem.size_dict[size][1]  # size modifier
        """степень обработки"""
        if self.g_type == "pearl" or self.g_type == "black_pearl":
            self.cut = " "
        else:
            self.cut = cut
        self.cut_mod = Gem.cut_dict[cut][1]  # value multiplier
        self.base = gem_types[self.g_type][1]  # base value from type dict
        # проверяем возможность инкрустации:
        if self.size == 100:
            self.can_be_incrusted = False
        else:
            self.can_be_incrusted = True
        if self.size_mod >= 25:
            self.amount = 1
        else:
            if self.size_mod == 5:
                self.amount = 5
            else:
                self.amount = 20

    @property
    def cost(self):
        return self.base * self.size_mod * self.cut_mod * self.amount

    def __repr__(self):
        return "%s %s %s" % (self.size, self.cut, self.g_type)

    def __eq__(self, other):
        if isinstance(other, Gem):
            return other and self.g_type == other.g_type and self.cut == other.cut \
                and self.size == other.size
        else:
            return

    def description(self, custom=False):
        if not custom and (self.size == 'small' or self.size == 'common'):
            if self.size == 'small':
                case = 'plural'
                return u"a handful of small %s%s" % (
                    gem_cut_description_rus[self.cut],
                    gem_description_rus[self.g_type][case])
            else:
                case = 'plural'
                return u"several %s%s" % (
                    gem_cut_description_rus[self.cut],
                    gem_description_rus[self.g_type][case])
        else:
            case = 'plural'
            return u"%s%s%s" % (
                material_size_description_rus[self.size],
                gem_cut_description_rus[self.cut],
                gem_description_rus[self.g_type][case])
                
                
    @staticmethod
    def number_conjugation(gem_type, gem_count):
        """
        Функция для вывода описания камней по типу (в формате тип/размер/огранка)
        и количеству (без учета умножения мелких/обычных камней)
        """
        gem_param = gem_type.split(';')
        if gem_param[1] == 'small' or gem_param[1] == 'common':  # умножаем мелкие/обычные камни
            if gem_param[1] == 'small':
                gem_count *= 25
            else:
                gem_count *= 5
                
        if gem_count != 1:  
            return u"%s %s%s%s" % (gem_count, material_size_description_rus[gem_param[1]],
                                   gem_cut_description_rus[gem_param[2]],
                                   gem_description_rus[gem_param[0]]['plural'])
        else:
            return u"%s%s%s" % (material_size_description_rus[gem_param[1]],
                                gem_cut_description_rus[gem_param[2]],
                                gem_description_rus[gem_param[0]]['singular'])
  

def generate_gem(count, *args):
    """One required argument - number of stones that you need to generate.
    Other arguments specify the size/quantity. Called with 
    {"size" : ("size", size, ...)} or {"cut" :("quality", "quality",...)}
    For example
    generate_gem (5, {"size" :( "common", "small")}, ["ruby", "star", "aqua"], "diamond")
    
    """
    gems = []
    if len(args) != 0:
        cut = {}
        size = {}
        new_dict = {}
        for i in args:
            if isinstance(i, dict):
                if i.keys()[0] == "size":
                    for v in i["size"]:
                        if v in Gem.size_dict:
                            size[v] = Gem.size_dict[v]
                elif i.keys()[0] == "cut":
                    for v in i["cut"]:
                        if v in Gem.cut_dict:
                            cut[v] = Gem.cut_dict[v]
            elif isinstance(i, list):
                for item in i:
                    if item in gem_types:
                        new_dict[item] = gem_types[item]
            elif isinstance(i, basestring):
                if i in gem_types:
                    new_dict[i] = gem_types[i]
        while count > 0:
            if len(cut) == 0:
                cut = Gem.cut_dict
            if len(size) == 0:
                size = Gem.size_dict
            if len(new_dict) == 0:
                new_dict = gem_types
            gems.append(Gem(weighted_select(new_dict), weighted_select(size), weighted_select(cut)))
            count -= 1
        return gems
    for i in xrange(count):
        gems.append(Gem(weighted_select(gem_types), weighted_select(Gem.size_dict), weighted_select(Gem.cut_dict)))
    return gems



class Material(object):  # класс для генерации материалов
    size_dict = {"small": (40, 1), "common": (50, 5), "large": (8, 25), "exceptional": (2, 100)}

    def __init__(self, m_type, size):
        self.m_type = m_type  # название
        self.base = material_types[m_type][1]  # базовая цена
        self.size = size  # размер
        self.size_mod = Material.size_dict[size][1]  # модификатор размера

    @property
    def cost(self):  # определяем цену материала(зависит от размера и типа)
        return self.size_mod * self.base

    def __repr__(self):
        return "%s %s" % (self.size, self.m_type)

    def __eq__(self, other):
        if isinstance(other, Material):
            return other and self.m_type == other.m_type and self.size == other.size
        else:
            return

    def description(self):
        return u"%spieces of %s" % (material_size_description_rus[self.size],material_description_rus[self.m_type])

    @staticmethod
    def number_conjugation(material_type, material_count):
        """
        Функция для вывода описания камней по типу (в формате тип/размер) и количеству
        """
        material_param = material_type.split(';')
        # выводим результат для каждого типа сопряжения
        if material_count != 1:  # если материал один - не ставим число
            return u"%s %spieces of %s" % (
                material_count, material_size_description_rus[material_param[1]], material_description_rus[material_param[0]])
        else:
            return u"%spiece of %s" % (material_size_description_rus[material_param[1]], material_description_rus[material_param[0]])


def generate_mat(count, *args):
    """принцип работы такойже как для драг.камней"""
    mats = []
    if len(args) != 0:
        size = {}
        new_dict = {}
        for i in args:
            if isinstance(i, dict):
                if i.keys()[0] == "size":
                    # size = {v: Material.size_dict[v] for v in i["size"] if v in Material.size_dict}
                    for v in i["size"]:
                        if v in Material.size_dict:
                            size[v] = Material.size_dict[v]
            elif isinstance(i, list):
                for item in i:
                    if item in material_types:
                        new_dict[item] = material_types[item]
            elif isinstance(i, basestring):
                if i in material_types:
                    new_dict[i] = material_types[i]
        for i in xrange(count):
            if len(size) == 0:
                size = Material.size_dict
            if len(new_dict) == 0:
                new_dict = material_types
            mats.append(Material(weighted_select(new_dict), weighted_select(size)))
        return mats
    for i in xrange(count):
        mats.append(Material(weighted_select(material_types), weighted_select(Material.size_dict)))
    return mats



class Treasure(object):  # класс для сокровищ
    decorate_types = {"incuse": (33,), "engrave": (33,), "etching": (33,), "carving": (0,)}
    quality_types = {"common": (60, 2), "skillfully": (20, 3), "rough": (10, 1), "mastery": (10, 5)}

    def __init__(self, treasure_type, alignment): #alignment = "dwarf", "elf", etc
        """все значения заносятся из словаря treasure_types"""
        self.treasure_type = treasure_type
        self.base_price = treasure_types[self.treasure_type][0]
        self.metal = treasure_types[self.treasure_type][1]
        self.nonmetal = treasure_types[self.treasure_type][2]
        self.image = treasure_types[self.treasure_type][3]
        self.incrustable = treasure_types[self.treasure_type][4]
        self.decorable = treasure_types[self.treasure_type][5]
        self.alignment = alignment
        """дальше генерируем характеристики в зависимости от типа сокровища"""
        self.random_mod = random.randint(0, self.base_price * 10)
        if random.randint(1, 100) <= 50 and self.incrustable:
            self.spangled = generate_gem(1, {"size": ('common',)})[0]
            # размер 'common' - хак, чтобы не писалось "мелкими":
        else:
            self.spangled = None
        if random.randint(1, 100) <= 15 and self.incrustable:
            self.inlaid = generate_gem(1, {"size": ('common',)})[0]
        else:
            self.inlaid = None
        if random.randint(1, 100) <= 5 and self.incrustable:
            self.huge = generate_gem(1, {"size": ('large',)})[0]
        else:
            self.huge = None

        def metals_available():  # проверяем принадлежность к расе(из каких металов может быть сделано)
            if self.alignment == "human" or self.alignment == "cleric" or self.alignment == "knight":
                return {"silver": (70,), "gold": (30,)}
            elif self.alignment == "elf" or self.alignment == "merman":
                return {"gold": (70,), "mithril": (30,)}
            elif self.alignment == "dwarf":
                return {"gold": (70,), "adamantine": (30,)}

        def material():
            if self.metal and self.nonmetal:
                rnd = random.randint(1, 100)
                if rnd > 50:
                    return weighted_select(material_types)
                else:
                    return weighted_select(metals_available())
            elif self.metal:
                return weighted_select(metals_available())
            else:
                return weighted_select(material_types)

        self.material = material()  # выбираем материал

        def decorate():
            if self.decorable:
                rnd = random.randint(1, 100)
                if rnd <= 15:
                    rnd = random.randint(1, 100)
                    if rnd <= 50:
                        self.decoration_image = random.choice(image_types[self.alignment])
                        if self.material in material_types:
                            return "carving"
                        else:
                            return weighted_select(Treasure.decorate_types)
                    else:
                        return None
                else:
                    return None

        self.decoration = decorate()  # выбираем орнамент
        if self.image:
            self.decoration_image = random.choice(image_types[self.alignment])

        def q_choice():  # прокидываем качество вещи
            if self.alignment == "human" or self.alignment == "cleric" or self.alignment == "knight":
                return weighted_select(Treasure.quality_types)
            else:
                holder = deepcopy(Treasure.quality_types)
                holder.__delitem__('rough')
                return weighted_select(holder)

        self.quality = q_choice()
        self.obtained = u""

    def incrustation(self, gem):  # метод для икрустации камней
        if not self.incrustable:
            return "Can't be incrusted"
        if gem.size == "small":
            if self.spangled is None:
                self.spangled = gem
            return
        if gem.size[1] == "common":
            if self.inlaid is None:
                self.inlaid = gem
            return
        if gem.size[1] == "huge":
            if self.huge is None:
                self.huge = gem
            return

    @property  # качество вещи
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, value):
        self._quality = value
        if value in Treasure.quality_types:
            self.quality_mod = Treasure.quality_types[value][1]

    @property  # тип материала
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value
        if self.material in material_types:
            self.mat_price = material_types[self._material][1]
        else:
            self.mat_price = metal_types[self._material]

    @property  # тип орнамента
    def decoration(self):
        return self._decoration

    @decoration.setter
    def decoration(self, value):
        self._decoration = value
        if value is None:
            self.dec_mod = 1
        else:
            self.dec_mod = 2  # равен двум если есть орнамент

    @property  # цена вставленных камней
    def incrustation_cost(self):
        holder = 0
        if self.spangled is not None:
            # из-за хака с размерами нужно умножить на реальный размер и поделить на "хакнутый"
            holder += self.spangled.cost * Gem.size_dict['small'][1] // Gem.size_dict['common'][1]
        if self.inlaid is not None:
            holder += self.inlaid.cost
        if self.huge is not None:
            holder += self.huge.cost
        return holder

    def craft_cost(self, base_cost, price_multiplier):  
        """
        Цена создания/покупки
        :param base_cost: базовая стоимость работы (для ремесла)
        :param price_multiplier: увеличение цены (для покупки, в процентах)
        :return: созданная вещь либо None в случае отмены
        """
        price = self.cost * price_multiplier // 100
        price += base_cost
        if self.spangled:
            price += base_cost
        if self.inlaid:
            price += base_cost
        if self.huge:
            price += base_cost
        if self.decoration:
            price += 2 * base_cost
        return price

    @property
    def cost(self):  # цена сокровища
        return \
            self.base_price * self.quality_mod * self.dec_mod * self.mat_price + \
            self.incrustation_cost + self.random_mod

    def __repr__(self):
        return "%s%s" % (self.material, self.treasure_type)

    def description(self):
        quality_str = quality_description_rus[self.quality]  # мастерство исполнения
        treasure_str = treasure_description_rus[self.treasure_type]  # тип драгоценности
        # совмещаем мастерство исполнения, тип и материал, из которого изготовлено
        if self.material in metal_types.keys():
            if self.treasure_type == 'tome':
                desc_str = u"%s%s bound with %s" %(
                    quality_str, treasure_str, metal_description_rus[self.material])
            else:
                desc_str = u"%s%s %s" % (
                    quality_str, metal_description_rus[self.material], treasure_str)
        else:
            desc_str = u"%s%s %s" % (
                quality_str, material_description_rus[self.material], treasure_str)

        if self.image:
            desc_str += u", depicting %s" % image_description_rus[self.decoration_image]  
            # только изображение
        else:
            # добавляем различные украшения
            enchant_list = []
            if self.spangled:  # усыпанное камнями
                enchant_list.append(u"%s %s" % (decoration_description_rus['spangled'], self.spangled.description(True)))
            if self.inlaid:  # инкрустированное камнями
                enchant_list.append(u"%s %s" % (decoration_description_rus['inlaid'], self.inlaid.description(True)))
            if self.huge:  # с крупным камнем
                # только ради "крупной (чёрной) жемчужины":
                enchant_list.append(u"with %s" % self.huge.description(True))
            if self.decoration:  # украшенное чеканкой/гравировкой/травлением/резьбой
                enchant_list.append(u"%s %s" % (decoration_description_rus['decoration'], decorate_types_description_rus[self.decoration]))
            if len(enchant_list) == 1:
                if not self.huge:
                    desc_str += u","  # добавляем "с крупным камнем" без запятой
                desc_str += u" %s" % enchant_list[0]
            elif len(enchant_list) > 1:
                while len(enchant_list) > 1:
                    desc_str += u", %s" % enchant_list[0]  # добавляем через запятую украшения
                    del enchant_list[0]
                desc_str += u" and %s" % enchant_list[0]  # последнее добавляется союзом "и"
            if self.decoration:  # если есть изображение - ставим точку и описываем его
                image_description = image_description_rus[self.decoration_image]  # упрощение доступа к свойству
                desc_str = u"%s. The %s %s %s" % (desc_str, treasure_description_rus[self.treasure_type],decoration_description_rus['image'],image_description)
        return desc_str


def gen_treas(count, t_list, alignment, min_cost, max_cost, obtained):
    """Генерируем рандомное сокровище
    функция генерации сокровищ,
    count - number of treasures
    t_list - list of strings, the names of the treasures
    alignmet - human, cleric, knight, merman, elf, dwarf
    min_cost - минимальная цена сокровища,
    max_cost - максимальная цена сокровища"""
    treasures_list = []
    while count > 0:
        treas_holder = random.choice(t_list)
        if treas_holder in gem_types:
            treasures_list.extend(generate_gem(1, treas_holder))
        elif treas_holder in material_types:
            treasures_list.extend(generate_mat(1, treas_holder))
        elif treas_holder in metal_types:
            treasures_list.append(Ingot(treas_holder))
        elif treas_holder in Coin.coin_types:
            rnd = random.randint(min_cost, max_cost)
            treasures_list.append(Coin(treas_holder, rnd / Coin.coin_types[treas_holder][1]))
        elif treas_holder in treasure_types:
            t = Treasure(treas_holder, alignment)
            t.obtained = obtained
            treasures_list.append(t)
        else:
            raise Exception("No treasure")
        if not min_cost < treasures_list[-1].cost < max_cost:
            treasures_list.pop()
            count += 1
        count -= 1
    return treasures_list
        
        
        
        
class Treasury(store.object):
    def __init__(self):
        self.farthing = 0  # медная монетка
        self.taller = 0  # серебряная монетка
        self.dubloon = 0  # золотая монетка
        # списки строк
        self.materials = {}  # словарь с количеством материала
        self.metals = {}  # словарь с количеством металла
        self.jewelry = []  # список драгоценностей
        self.equipment = []
        self.gems = {}  # словарь с количеством драгоценных камней
        # TODO: multiple same equipment
        self.thief_items = []

    @property
    def money(self):
        return self.farthing + 10 * self.taller + 100 * self.dubloon

    @money.setter
    def money(self, value):
        if value < 0:  # Защита от ухода денег в минус
            raise NotImplementedError(u"Error: Not enough money")
        money_diff = value - self.money  # считаем разницу между прошлым значением и новым
        if money_diff < 0:
            # разница отрицательна или ноль - производим вычитание
            money_diff = -money_diff  # для удобства получаем число, которое необходимо вычесть
            if self.farthing < money_diff % 10:
                # медных монет недостаточно для выплаты, меняем серебряную
                self.taller -= 1
                self.farthing += 10
            self.farthing -= money_diff % 10
            money_diff //= 10
            if self.taller < money_diff % 10:
                if (self.farthing // 10 + self.taller) < money_diff % 10:
                    # серебряных монет даже с учетом медных недостаточно для выплаты, меняем золотую
                    self.dubloon -= 1
                    self.taller += 10
                else:
                    # серебряных монет с учетом медных достаточно для выплаты, меняем по максимуму медные на серебряные
                    self.taller += self.farthing // 10
                    self.farthing %= 10
            self.taller -= money_diff % 10
            money_diff //= 10
            if self.dubloon < money_diff % 10:
                # золотых монет недостаточно для выплаты
                self.taller += self.farthing // 10  # меняем по максимуму медные на серебряные
                self.farthing %= 10
                self.dubloon += self.taller // 10  # меняем по максимуму серебряные на золотые
                self.taller %= 10
            self.dubloon -= money_diff
        else:
            # разница положительна - производим добавление монет по разрядам
            self.dubloon += money_diff // 100
            money_diff %= 100
            self.taller += money_diff // 10
            self.farthing += money_diff % 10

    @property
    def wealth(self):
        """
        Стоимость всех сокровищ дракона
        """
        calc_wealth = self.money  # деньги
        for metal in self.metals.iterkeys():  # металлы
            calc_wealth += self.metals[metal] * metal_types[metal]
        for material_i in self.materials.iterkeys():  # материалы
            material = material_i.split(';')
            calc_wealth += self.materials[material_i] * material_types[material[0]][1] * \
                           Material.size_dict[material[1]][1]
        for gem_i in self.gems.iterkeys():  # драгоценные камни
            gem = gem_i.split(';')
            calc_wealth += self.gems[gem_i] * gem_types[gem[0]][1] * Gem.size_dict[gem[1]][1] * Gem.cut_dict[gem[2]][1]
        for treas_i in xrange(len(self.jewelry)):  # украшения
            calc_wealth += self.jewelry[treas_i].cost
        return calc_wealth

    def receive_treasures(self, treasure_list):
        """
        Помещает сокровища в сокровищницу
        :param treasure_list: Список сокровищ, помещаемых в сокровищницу
        """
        for treas in treasure_list:
            achieve_target(treas.cost, "treasure")#Событие для ачивок
            if isinstance(treas, Coin):
                # сохраняется число медных, серебряных и золотых монет в соответствующих переменных
                if treas.name == 'farthing':
                    self.farthing += treas.amount
                elif treas.name == 'taller':
                    self.taller += treas.amount
                else:
                    self.dubloon += treas.amount
            elif isinstance(treas, Ingot):
                # сохраняется в словаре metals, где ключ - название металла, а значение - его вес в фунтах
                if treas.metal_type in self.metals:
                    self.metals[treas.metal_type] += treas.weight
                else:
                    self.metals[treas.metal_type] = treas.weight
            elif isinstance(treas, Material):
                # сохраняется в словаре materials, где
                # ключ - "название материала;размер материала", а
                # значение - число материалов такого типа и размера
                type_str = treas.m_type + ';' + treas.size
                if type_str in self.materials:
                    self.materials[type_str] += 1
                else:
                    self.materials[type_str] = 1
            elif isinstance(treas, Gem):
                # сохраняется в словаре gems, где
                # ключ - "название драгоценности;размер драгоценности;обработка драгоценности", а
                # значение - число камней такого типа, размера и обработки
                type_str = treas.g_type + ';' + treas.size + ';' + treas.cut
                if type_str in self.gems:
                    self.gems[type_str] += 1
                else:
                    self.gems[type_str] = 1
            elif isinstance(treas, Treasure):
                self.jewelry.append(treas)
        achieve_target(self.wealth, "wealth")#Событие для ачивок
    @staticmethod
    def treasures_description(treasure_list):
        """
        :param treasure_list: Список сокровищ, для которых требуется получить описание
        :return: Возвращает список с описанием сокровищ
        """
        treas_list = deepcopy(treasure_list)
        description_list = []
        # Группируем монеты, слитки, драгоценные камни и материалы
        coin_list = {}
        ingot_list = {}
        gem_list = {}
        material_list = {}
        for treas_i in reversed(xrange(len(treasure_list))):
            treas = treas_list[treas_i]
            if isinstance(treas, Coin):
                if treas.name in coin_list:
                    coin_list[treas.name] += treas.amount
                else:
                    coin_list[treas.name] = treas.amount
                del treas_list[treas_i]
            elif isinstance(treas, Ingot):
                if treas.metal_type in ingot_list:
                    ingot_list[treas.metal_type] += treas.weight
                else:
                    ingot_list[treas.metal_type] = treas.weight
                del treas_list[treas_i]
            elif isinstance(treas, Gem):
                type_str = treas.g_type + ';' + treas.size + ';' + treas.cut
                if type_str in gem_list:
                    gem_list[type_str] += 1
                else:
                    gem_list[type_str] = 1
                del treas_list[treas_i]
            elif isinstance(treas, Material):
                type_str = treas.m_type + ';' + treas.size
                if type_str in material_list:
                    material_list[type_str] += 1
                else:
                    material_list[type_str] = 1
                del treas_list[treas_i]
        for treas in coin_list.iterkeys():
            description_list.append("%d %s%s." % ((coin_list[treas]), treas, number_pluralizer((coin_list[treas]))))
        for treas in ingot_list.iterkeys():
            description_list.append(capitalize_first(Ingot.number_conjugation(treas, ingot_list[treas])) + '.')
        for treas in gem_list.iterkeys():
            if gem_list[treas] > 1:
                description_list.append(capitalize_first(Gem.number_conjugation(treas, gem_list[treas])) + '.')
            else:
                description_list.append(capitalize_first(Gem(*treas.split(';')).description()) + '.')
        for treas in material_list.iterkeys():
            if material_list[treas] > 1:
                description_list.append(capitalize_first(Material.number_conjugation(treas, material_list[treas])) + '.')
            else:
                description_list.append(capitalize_first(Material(*treas.split(';')).description()) + '.')
            # Выводим остальное
        for treas in treas_list:
            # TODO: найти откуда в списке сокровищ при воровстве может быть None
            if treas:
                description_list.append(capitalize_first(treas.description()) + '.')
        return description_list

    def take_ingot(self, ingot_type, weight=1):
        """
        :param ingot_type: название металла
        :param weight: вес, который мы хотели бы взять 
        :return: Возвращает тип Ingot с указанным весом или максимально возможным, либо None,
            если такого металла в сокровищнице нет
        """
        if ingot_type in self.metals and self.metals[ingot_type] > 0:  # проверяем есть ли такой металл в сокровищнице
            ingot = Ingot(ingot_type)  # создаем ingot
            # делаем вес слитка равным указанному весу или максимуму в сокровищнице:
            if weight < self.metals[ingot_type]:
                ingot.weight = weight
            else:
                ingot.weight = self.metals[ingot_type]
            self.metals[ingot_type] -= ingot.weight  # вычитаем вес слитка из сокровищницы
            if self.metals[ingot_type] == 0:
                del self.metals[ingot_type]  # удаляем тип материала из списка сокровищницы
            return ingot
        elif ingot_type in self.metals:
            del self.metals[ingot_type]  # удаляем тип металла из списка сокровищницы
        return None

    def take_material(self, material_name):
        """
        :param material_name: описание материала в формате 'тип;размер'
        :return: Возвращает тип Material или None, если такого материала в сокровищнице нет
        """
        # проверяем есть ли такой материал в сокровищнице
        if material_name in self.materials and self.materials[material_name] > 0:
            material_param = material_name.split(';')  # парсим строку
            material = Material(*material_param)  # получаем экземпляр класса с нужными параметрами
            self.materials[material_name] -= 1  # вычитаем один материал из списка сокровищницы
            if self.materials[material_name] == 0:
                del self.materials[material_name]  # удаляем тип материала из списка сокровищницы
            return material
        elif material_name in self.materials:
            del self.materials[material_name]  # удаляем тип материала из списка сокровищницы
        return None

    def take_gem(self, gem_name):
        """
        :param gem_name: описание камня в формате 'тип;размер;обработка'
        :return: Возвращает тип Gem или None, если таких камней в сокровищнице нет
        """
        if gem_name in self.gems and self.gems[gem_name] > 0:  # проверяем есть ли такой камень в сокровищнице
            gem_param = gem_name.split(';')  # парсим строку
            gem = Gem(*gem_param)  # получаем экземпляр класса с нужными параметрами
            self.gems[gem_name] -= 1  # вычитаем один камень из списка сокровищницы
            return gem
        elif gem_name in self.gems:
            del self.gems[gem_name]  # удаляем тип камня из списка сокровищницы
        return None

    def take_coin(self, coin_name, coin_count=1):
        """
        :param coin_name: название монеты
        :param coin_count: сколько монет нам бы хотелось взять
        :return: Возвращает тип Coin с указанным числом монет или максимально возможным, либо None,
            если таких монет в сокровищнице нет
        """
        if coin_name == 'farthing' and self.farthing > 0:
            if coin_count > self.farthing:
                coin_count = self.farthing
            self.farthing -= coin_count
        elif coin_name == 'taller' and self.taller > 0:
            if coin_count > self.taller:
                coin_count = self.taller
            self.taller -= coin_count
        elif coin_name == 'dubloon' and self.dubloon > 0:
            if coin_count > self.dubloon:
                coin_count = self.dubloon
            self.dubloon -= coin_count
        else:
            return None
        return Coin(coin_name, coin_count)

    def rob_treasury(self, treasure_count=1):
        """
        :param treasure_count: Количество сокровищ, которые необходимо взять из сокровищницы
        :return: Список самых дорогих сокровищ, взятых из сокровищницы
        """
        treasure_list = []  # список сокровищ, которые не приглянулись вору
        abducted_list = []  # список награбленного
        threshold_value = 0  # минимальная стоимость, которая будет взята

        def update_list(test_treasure):  
            """
            функция добавления награбленного в список, возвращает истину в случае успешного добавления
            """
            if not test_treasure:
                return False  # попытка взять несуществующую вещь
            elif threshold_value < test_treasure.cost:
                test_cost = test_treasure.cost  # сохраняем цену для скорости
                test_i = len(abducted_list)  # новый индекс - последний в списке
                while test_i > 0 and abducted_list[test_i - 1].cost < test_cost:
                    test_i -= 1  # сортировка
                abducted_list.insert(test_i, test_treasure)  # вставляем в нужную позицию
                if len(abducted_list) > treasure_count:  # убираем из списка вещь с наименьшей ценой
                    treasure_list.append(abducted_list.pop())
                    self.threshold_value = abducted_list[-1].cost
                return True
            else:
                # стоимость добавляемого меньше пороговой, возвращаем сокровище обратно в сокровищницу
                treasure_list.append(test_treasure)
                return False

        # цикл по всем сокровищам, начиная с конца списка, для соответствия индекса количеству вещей в списке
        for _ in reversed(xrange(len(self.jewelry))):
            # достаем сокровище из конца списка - там должны быть более дорогие сокровища и
            # пробуем добавить их в список награбленного
            update_list(self.jewelry.pop())
        self.jewelry.extend(treasure_list)  # возвращаем сокровища в сокровищницу после поиска самых дорогих
        treasure_list = []  # очищаем список возвращаемого
        for gem_type in self.gems.keys():  # просматриваем список типов камней
            while update_list(self.take_gem(gem_type)):
                pass  # пока в список добавляются камни - добавляем
        for metal_type in self.metals.keys():  # аналогично, просматриваем список типов слитков
            while update_list(self.take_ingot(metal_type, 8)):
                pass  # пока в список добавляются слитки - добавляем
        for coin_type in Coin.coin_types.keys():  # аналогично, просматриваем список типов монет
            while update_list(self.take_coin(coin_type, 100)):
                pass  # пока в список добавляются монеты - добавляем
        for material_type in self.materials.keys():  # аналогично, просматриваем список типов материалов
            while update_list(
                    self.take_material(material_type)):
                pass  # пока в список добавляются материалы - добавляем
        self.receive_treasures(treasure_list)  # возвращаем сокровища в сокровищницу
        return abducted_list

    def gem_name_count(self, gem_name):
        """
        :param gem_name: Тип драгоценных камней (в формате 'тип;размер;обработка'), для которого необходимо подсчитать
            количество камней в сокровищнице
        :return: количество камней такого типа в сокровищнице с учетом того, что мелкие идут группами по 25, а
            обычные - по 5
        """
        gem_count = self.gems[gem_name]  # берем данные о количестве из словаря
        gem_param = gem_name.split(';')  # парсим строку
        if gem_param[1] == 'small':
            gem_count *= 25
        elif gem_param[1] == 'common':
            gem_count *= 5
        return gem_count

    @property
    def gems_list(self):
        """
        :return: строка с описанием количества драгоценных камней в сокровищнице
        """
        gem_str = u"In the treasury is:\n"
        gem_list = sorted(self.gems.keys())  # список драгоценных камней, отсортированных по типу/размеру/огранке
        for gem_name in gem_list:
            if self.gems[gem_name]:  # проверка наличия камней такого типа в сокровищнице
                gem_str += u"%s.\n" % capitalize_first(Gem.number_conjugation(gem_name, self.gems[gem_name]))
        return gem_str

    @property
    def materials_list(self):
        """
        :return: строка с описанием количества материалов в сокровищнице
        """
        material_str = u"In the treasury is:\n"
        metal_list = sorted(self.metals.keys())
        for metal_name in metal_list:
            metal_weight = self.metals[metal_name]
            if metal_weight:
                material_str += u"%s.\n" % capitalize_first(Ingot.number_conjugation(metal_name, metal_weight))
        mat_list = sorted(self.materials.keys())
        for mat_name in mat_list:
            if self.materials[mat_name]:
                material_str += u"%s.\n" % capitalize_first(
                    Material.number_conjugation(mat_name, self.materials[mat_name]))
        return material_str

    @property
    def most_expensive_jewelry_index(self):
        """
        Индекс самого дорогого украшения в сокровищнице
        """
        if len(self.jewelry):
            most_expensive_i = 0
            most_expensive_cost = self.jewelry[most_expensive_i].cost
            for jewelry_i in xrange(len(self.jewelry)):
                if self.jewelry[jewelry_i].cost > most_expensive_cost:
                    most_expensive_cost = self.jewelry[jewelry_i].cost
                    most_expensive_i = jewelry_i
            return most_expensive_i
        else:
            return -1

    @property
    def cheapest_jewelry_index(self):
        """
        Индекс самого дешёвого украшения в сокровищнице
        """
        if len(self.jewelry):
            cheapest_i = 0
            cheapest_cost = self.jewelry[cheapest_i].cost
            for jewelry_i in xrange(len(self.jewelry)):
                if self.jewelry[jewelry_i].cost < cheapest_cost:
                    cheapest_cost = self.jewelry[jewelry_i].cost
                    cheapest_i = jewelry_i
            return cheapest_i
        else:
            return -1

    @property
    def most_expensive_jewelry_cost(self):
        """
        Стоимость самого дорогого украшения в сокровищнице
        """
        if len(self.jewelry):
            return self.jewelry[self.most_expensive_jewelry_index].cost
        else:
            return 0

    @property
    def most_expensive_jewelry(self):
        """
        Описание самого дорогого украшения в сокровищнице
        """
        if len(self.jewelry):
            most_expensive_i = self.most_expensive_jewelry_index
            return u"%s.\nValue of trinket: %d farthing%s.\n%s" % (
                capitalize_first(self.jewelry[most_expensive_i].description()),
                self.jewelry[most_expensive_i].cost,
                number_pluralizer(self.jewelry[most_expensive_i].cost),
                self.jewelry[most_expensive_i].obtained)
        else:
            return u"No ornaments in the treasury."

    @property
    def cheapest_jewelry(self):
        """
        Описание самого дешёвого украшения в сокровищнице
        """
        if len(self.jewelry):
            cheapest_i = self.cheapest_jewelry_index
            return u"%s.\nValue of trinket: %d farthing%s.\n%s" % (
                capitalize_first(self.jewelry[cheapest_i].description()),
                self.jewelry[cheapest_i].cost,
                number_pluralizer(self.jewelry[cheapest_i].cost),
                self.jewelry[cheapest_i].obtained)
        else:
            return u"No ornaments in the treasury."

    @property
    def random_jewelry(self):
        if len(self.jewelry):
            random_jewelry = random.choice(self.jewelry)
            return u"%s.\nValue of trinket: %d farthing%s.\n%s" % (
                capitalize_first(random_jewelry.description()),
                random_jewelry.cost,
                number_pluralizer(random_jewelry.cost),
                random_jewelry.obtained)
        else:
            return u"No ornaments in the treasury."

    @property
    def all_jewelries(self):
        """
        Стоимость всех украшений дракона
        """
        calc_all_jewelries = 0
        for treas_i in xrange(len(self.jewelry)):  
            calc_all_jewelries += self.jewelry[treas_i].cost
        return calc_all_jewelries

    @staticmethod
    def get_mass_description(description_key, mass):
        """ 
        :param description_key: ключ для словаря treasures_mass_description_rus
        :param mass: число, для которой нужно подобрать описание
        :return: описание массы в сокровищнице
        """
        if mass > 0:
            return get_description_by_count(treasures_mass_description_rus[description_key], mass)
        else:
            return u""

    @property
    def coin_mass(self):
        """
        :return: масса монет в сокровищнице
        """
        return self.farthing + self.taller + self.dubloon

    @property
    def coin_mass_description(self):
        """
        :return: описание массы монет в сокровищнице
        """
        return Treasury.get_mass_description('coin', self.coin_mass)

    @property
    def metal_mass(self):
        """
        :return: вес металла в сокровищнице
        """
        metal_weight = 0
        for metal_i in self.metals.values():
            metal_weight += metal_i
        return metal_weight

    @property
    def materials_mass_description(self):
        """
        :return: описание массы материалов и металлов в сокровищнице
        """
        return Treasury.get_mass_description('material', self.metal_mass + self.material_mass)

    @property
    def gem_mass(self):
        """
        :return: масса драгоценных камней в сокровищнице
        """
        gem_summ = 0
        for gem_i in self.gems.keys():
            gem_size = gem_i.split(';')
            gem_size = gem_size[1]
            if gem_size == 'small':
                gem_summ += 25
            elif gem_size == 'common':
                gem_summ += 15
            elif gem_size == 'large':
                gem_summ += 5
            else:
                gem_summ += 7
        return gem_summ

    @property
    def gems_mass_description(self):
        """
        :return: описание массы драгоценных камней в сокровищнице
        """
        return Treasury.get_mass_description('gem', self.gem_mass)

    @property
    def material_mass(self):
        """
        :return: масса материала в сокровищнице
        """
        mat_summ = 0
        for mat_i in self.materials.keys():
            mat_size = mat_i.split(';')
            mat_size = mat_size[1]
            mat_summ += Material.size_dict[mat_size][1]
        return mat_summ

    @property
    def jewelry_mass(self):
        """
        :return: масса украшений в сокровищнице
        """
        jewelry_summ = 0
        for jewelry_i in self.jewelry:
            jewelry_summ += jewelry_i.base_price
        return jewelry_summ

    @property
    def jewelry_mass_description(self):
        """
        :return: описание массы драгоценных камней в сокровищнице
        """
        return Treasury.get_mass_description('jewelry', self.jewelry_mass)
        
    @property
    def wealth_description(self):
        """
        :return: описание всех сокровищ в сокровищнице
        """
        wealth = self.wealth
        if wealth > 0:
            wealth_str = Treasury.get_mass_description('wealth', wealth)
            wealth_str += u"Total treasure value: %d farthing%s." % (wealth, number_pluralizer(wealth))
            return wealth_str 
        else:
            return u"Treasury is empty."

    def get_salary(self, amount):
        """
        :param amount: требуемая сумма, farthings
        :return: список того, что взяли, чтобы получить сумму, либо None, если в сокровищнице недостаточно денег.
        """
        # TODO: Сделать рефакторинг без использования `self`
        self.salary_list = []  # список сокровищ, которые можно взять в качестве платы
        self.salary_item = None  # предмет, который можно взять в качестве платы
        self.min_salary_value = 0  # цена предмета
        self.max_salary_value = 0  # цена списка сокровищ
        self.treasure_list = []  # список сокровищ, которые не приглянулись гремлинам

        def update_list(test_treasure):
            """
            функция добавления в список, возвращает истину если нужно добавить такую же вещь
            """
            if not test_treasure:
                return False  # попытка взять несуществующую вещь
            elif test_treasure.cost >= amount:
                # стоимость сокровища больше или равно необходимой суммы, можно взять только его в качестве оплаты
                if self.min_salary_value == 0:
                    # это первая вещь, которая стоит дороже, чем нам нужно - берём её
                    self.min_salary_value = test_treasure.cost
                    self.salary_item = test_treasure
                elif self.min_salary_value > test_treasure.cost:
                    # это не первая вещь, которая стоит дороже, чем нам нужно - берём её только если она дешевле прошлой
                    self.treasure_list.append(self.salary_item)  # возвращаем прошлую вещь в сокровищницу
                    self.min_salary_value = test_treasure.cost  # берём новую
                    self.salary_item = test_treasure
                else:
                    self.treasure_list.append(test_treasure)  # возвращаем вещь в сокровищницу
                return False  # больше такой не нужно
            else:
                # стоимость сокровища меньше необходимой суммы, придётся "скрести по сусекам"
                if self.max_salary_value < amount:
                    # стоимость списка недостаточно, добавляем ещё
                    self.max_salary_value += test_treasure.cost
                    self.salary_list.append(test_treasure)
                    return True
                else:
                    # стоимость списка достаточно, больше ничего не нужно
                    self.treasure_list.append(test_treasure)  # возвращаем вещь в сокровищницу
                    return False

        if self.wealth >= amount:
            if self.money >= amount:
                self.money -= amount
                self.salary_list.append(Coin('farthing', amount))
                return self.salary_list  # взяли деньгами сколько нужно
            else:
                for coin_type in Coin.coin_types.keys():  # просматриваем список типов монет
                    while update_list(self.take_coin(coin_type)):
                        pass  # пока в список добавляются монеты - добавляем
                # цикл по всем сокровищам, начиная с конца списка, для соответствия индекса количеству вещей в списке
                for _ in reversed(xrange(len(self.jewelry))):
                    # достаем сокровище из конца списка - там должны быть более дорогие сокровища и
                    # пробуем добавить их в список
                    update_list(self.jewelry.pop())
                for gem_type in self.gems.keys():  # просматриваем список типов камней
                    while update_list(self.take_gem(gem_type)):
                        pass  # пока в список добавляются камни - добавляем
                for metal_type in self.metals.keys():  # аналогично, просматриваем список типов слитков
                    while update_list(self.take_ingot(metal_type)):
                        pass  # пока в список добавляются слитки - добавляем
                for material_type in self.materials.keys():  # аналогично, просматриваем список типов материалов
                    while update_list(self.take_material(material_type)):
                        pass  # пока в список добавляются материалы - добавляем
                if self.max_salary_value > self.min_salary_value:
                    if self.salary_list:
                        self.treasure_list.extend(self.salary_list)  # возвращаем список в сокровищницу - не пригодился
                    self.salary_list = [self.salary_item]
                elif self.salary_list:
                    self.treasure_list.append(self.salary_item)  # возвращаем предмет в сокровищницу - не пригодился
                self.receive_treasures(self.treasure_list)  # возвращаем сокровища в сокровищницу
                return self.salary_list
        else:
            return None

    def check_gem_size(self, gem_size):
        """
        Функция для проверки есть ли в сокровищнице камень требуемого размера
        :param gem_size: размер камня для проверки
        :return: есть (True) или нет (False) в сокровищнице камень указанного размера
        """
        for gem_type in self.gems:
            if gem_type.split(';')[1] == gem_size:
                return True
        return False

    def available_materials(self, is_crafting, item_type):
        """
        Функция для проверки есть ли материал, из которого можно сделать вещь такого типа
        :param item_type: тип вещи, который хочется смастерить
        :param is_crafting: материалы дракона (True) или все доступные (False)
        :return: список материалов, из которых можно сделать вещь
        """
        materials = []
        if treasure_types[item_type][1]:
            # вещь можно сделать из металла, добавляем доступный список металлов
            if is_crafting:
                # все типы металлов у дракона
                materials += self.metals.keys()
            else:
                # все типы металлов в игре
                materials += metal_types.keys()
        if treasure_types[item_type][2]:
            # вещь можно сделать из поделочного материала, добавляем доступный список материалов
            if is_crafting:
                # все типы материалов у дракона
                for material_type in self.materials.keys():
                    # убираем повторы из-за возможной разницы в размерах поделочных материалов
                    material_name = material_type.split(';')[0]
                    if material_name not in materials:
                        materials.append(material_name)
            else:
                # все типы материалов в игре
                materials += material_types.keys()
        return materials

    def is_craft_possible(self, item_type, alignment):
        """
        Функция для проверки достаточно ли материалов в сокровищнице для изготовления вещи
        :param item_type: тип вещи, который хочется смастерить
        :param alignment: стиль вещи, которую хочется смастерить
        :return: достаточно (True) или нет (False) материалов для создания вещи
        """
        craft_possible = self.available_materials(True, item_type)
        if treasure_types[item_type][3]:
            # если сам предмет - изображение - нужен какой-то стиль
            craft_possible = craft_possible and alignment
        return craft_possible
 
    def craft_select_item(self, is_crafting, alignment):
        """
        Функция для вывода меню выбора типа покупаемой/создаваемой вещи
        :param is_crafting: создаётся из материалов дракона (True) или покупается (False)
        :return: выбранный тип вещи либо None в случае отмены
        """
        treasure_list = sorted(treasure_types.keys(), key=lambda treas: treasure_description_rus[treas])
        # получаем список возможных сокровищ
        if is_crafting:
            # если идёт создание вещи - ставим первыми в списке вещи, которые можем сделать
            craft_possible = []
            craft_impossible = []
            for treasure_type in treasure_list:
                if self.is_craft_possible(treasure_type, alignment):
                    craft_possible.append(treasure_type)
                else:
                    craft_impossible.append(treasure_type)
            treasure_list = craft_possible + craft_impossible
        menu_choice = None
        row_count = 10  # количество кнопок с отображаемым типом сокровища для создания/покупки
        position = 0  # начальное значение 
        while menu_choice not in treasure_list:
            # цикл для выбора типа сокровища для создания/покупки
            if row_count < len(treasure_list):
                menu_options = [(u"Back to previous page", 'dec', True, position > 0)]
            else:
                menu_options = [(u"", 'blank', True, False)]
            for i in xrange(position, min(position + row_count, len(treasure_list))):
                treasure_type = treasure_list[i]
                treas_name = treasure_description_rus[treasure_type].capitalize()
                if is_crafting:
                    menu_options.append((treas_name, treasure_type, True, self.is_craft_possible(treasure_type, alignment)))
                else:
                    menu_options.append((treas_name, treasure_type, True, True))
            while len(menu_options) < row_count + 1:
                # заполняем пустыми вариантами для выравнивания меню
                menu_options += [(u"", 'blank', True, False)]
            if row_count < len(treasure_list):
                menu_options += [(u"Go to next page", 'inc', True, position + row_count < len(treasure_list))]
            else:
                menu_options += [(u"", 'blank', True, False)]
            menu_options += [(u"cancel", 'return', True, True)]
            menu_choice = call_screen("dw_choice", menu_options)
            if menu_choice == 'dec':
                position -= row_count
            elif menu_choice == 'inc':
                position += row_count
            elif menu_choice == 'return':
                return None
        return menu_choice

    def craft_select_material(self, materials):
        """
        Функция для вывода меню выбора из списка
        :param materials: список материалов для выбора
        :return: выбранный вариант из списка либо None в случае отмены
        """
        menu_choice = None
        row_count = 10  # количество кнопок для отображения списка материалов
        position = 0  # начальное значение 
        while menu_choice not in materials:
            # цикл для выбора типа материала
            if row_count < len(materials):
                menu_options = [(u"Back to previous page", 'dec', True, position > 0)]
            else:
                menu_options = [(u"", 'blank', True, False)]
            for i in xrange(position, min(position + row_count, len(materials))):
                material_type = materials[i]
                if material_type in metal_types.keys():
                    # получаем название материала на русском
                    option_name = u"From %s" % metal_description_rus[material_type]
                else:
                    option_name = u"From %s" % material_description_rus[material_type]
                menu_options.append((option_name, material_type, True, True))
            while len(menu_options) < row_count + 1:
                # заполняем пустыми вариантами для выравнивания меню
                menu_options += [(u"", 'blank', True, False)]
            if row_count < len(materials):
                menu_options += [(u"Go to next page", 'inc', True, position + row_count < len(materials))]
            else:
                menu_options += [(u"", 'blank', True, False)]
            menu_options += [(u"", 'blank', True, False)]
            menu_choice = call_screen("dw_choice", menu_options)
            if menu_choice == 'dec':
                position -= row_count
            elif menu_choice == 'inc':
                position += row_count
        return menu_choice

    def craft_select_gem(self, is_crafting, gem_size):
        """
        Функция для вывода меню выбора камня для инкрустации из всех доступных вариантов
        После выбора автоматически вставляет (или убирает) камень нужного размера
        :param gem_size: размер камня для инкрустации
        :param is_crafting: из сокровищницы дракона (True) или покупается (False)
        :return: камень для инкрустации
        """
        menu_choice = None
        row_count = 10  # количество кнопок для отображения списка материалов
        position = 0  # начальное значение
        gem_list = []
        if is_crafting:
            # подходящие камни из сокровищницы дракона
            for gem_type in self.gems:
                # добавляем камни требуемого размера в список
                gem_params = gem_type.split(';')
                if gem_params[1] == gem_size:
                    if gem_size == 'small':
                        # изменение размера для хака описания
                        gem_params[1] = 'common'
                    gem_list.append(Gem(*gem_params))
        else:
            # все типы камней в игре
            gem_params = [None, gem_size, None]
            if gem_size == 'small':
                # изменение размера для хака описания
                gem_params[1] = 'common'
            gem_types_keys = sorted(gem_types.keys(), key=lambda gt: gem_description_rus[gt]['singular'])
            for gem_type in gem_types_keys:
                gem_params[0] = gem_type
                if gem_type == "pearl" or gem_type == "black_pearl":
                    gem_params[2] = " "
                    gem_list.append(Gem(*gem_params))
                else:
                    for gem_cut in ('rough', 'polished', 'faceted'):
                        gem_params[2] = gem_cut
                        gem_list.append(Gem(*gem_params))
        while menu_choice is None or (menu_choice == 'inc') or (menu_choice == 'dec'):
            # цикл для выбора типа камня
            if row_count < len(gem_list):
                menu_options = [(u"Back to previous page", 'dec', True, position > 0)]
            else:
                menu_options = [(u"", 'blank', True, False)]
            for i in xrange(position, min(position + row_count, len(gem_list))):
                menu_options.append((gem_list[i].description(custom=True).capitalize(), i, True, True))
            while len(menu_options) < row_count + 1:
                # заполняем пустыми вариантами для выравнивания меню
                menu_options += [(u"", 'blank', True, False)]
            if row_count < len(gem_list):
                menu_options += [(u"Go to next page", 'inc', True, position + row_count < len(gem_list))]
            else:
                menu_options += [(u"", 'blank', True, False)]
            menu_options += [(u"No stone", 'clear', True, True)]
            menu_choice = call_screen("dw_choice", menu_options)
            if menu_choice == 'dec':
                position -= row_count
            elif menu_choice == 'inc':
                position += row_count
        if menu_choice == 'clear':
            return None
        else:
            return gem_list[menu_choice]

    def craft(self, is_crafting=False, quality=['random'], alignment=['random'], base_cost=0, price_multiplier=100):
        """
        Функция для вывода меню покупки/создания вещи
        :param is_crafting: создаётся из материалов дракона (True) или покупается (False)
        :param quality: список для выбора возможного качества создаваемой вещи, 
            может быть rough, common, skillfully, mastery, 
            либо random для случайного выбора из этих вариантов с весовыми коэффициентами
        :param alignment: список для выбора возможного стиля декорации создаваемой вещи, 
            может быть human, knight, cleric, elf, dwarf, merman,
            либо random для случайного выбора из этих вариантов,
            либо None, если сделать орнамент невозможно
        :param base_cost: базовая стоимость работы (для ремесла)
        :param price_multiplier: увеличение цены (для покупки, в процентах)
        :return: созданная вещь либо None в случае отмены
        """
        if 'random' in alignment or not alignment:
            alignment = image_types.keys()
        alignment = random.choice(alignment)
        treasure_type = self.craft_select_item(is_crafting, alignment)
        if treasure_type is None:
            return None
        # случайный выбор стиля вещи из списка
        item = Treasure(treasure_type, alignment)
        quality_options = {
            'rough': u"Rough crafting",
            'common': u"Normal crafting",
            'skillfully': u"Skillful crafting",
            'mastery': u"Masterful crafting",
            'random': u"Random quality"
        }
        item.quality = quality[0]
        # первоначальный выбор качества - первый в списке
        materials = self.available_materials(is_crafting, treasure_type)
        item.material = self.craft_select_material(materials)
        item.spangled = None
        item.inlaid = None
        item.huge = None
        item.decoration = None
        item.decoration_image = None
        menu_choice = None
        while menu_choice is not 'create':
            menu_options = [(u"cancel", 'return', True, True)]
            treasure_name = treasure_description_rus[treasure_type].capitalize()
            menu_options += [(treasure_name, treasure_type, True, False)]
            # тип вещи - не может быть изменен
            menu_options += [(quality_options[item.quality], 'quality', True, len(quality) > 1)]
            # качество вещи
            if item.material in metal_types.keys():
                material_name = u"from %s" % metal_description_rus[item.material]
            else:
                material_name = u"from %s" % material_description_rus[item.material]
            menu_options += [(material_name, 'material', True, True)]
            # материал вещи
            if treasure_types[treasure_type][4]:
                # проверка на возможность инкрустации
                if item.spangled:
                    spangled_description = decoration_description_rus['spangled']
                    spangled_description += u" " + item.spangled.description(True)
                    menu_options += [(spangled_description, 'spangled', True, True)]
                else:
                    menu_options += [(u"no spangles", 'spangled', True, not is_crafting or self.check_gem_size('small'))]
                if item.inlaid:
                    inlaid_description = decoration_description_rus['inlaid'] 
                    inlaid_description += u" " + item.inlaid.description(True)
                    menu_options += [(inlaid_description, 'inlaid', True, True)]
                else:
                    menu_options += [(u"no inlay", 'inlaid', True, not is_crafting or self.check_gem_size('common'))]
                if item.huge:
                    huge_description = u"with " + item.huge.description(True)
                    menu_options += [(huge_description, 'huge', True, True)]
                else:
                    menu_options += [(u"no large gem", 'huge', True, not is_crafting or self.check_gem_size('large'))]
            if alignment and item.decorable:
                if item.decoration:
                    decor_image = decoration_description_rus['image']
                    decor_image += u" " + image_description_rus[item.decoration_image]
                else:
                    decor_image = u"no image"
                menu_options += [(decor_image, 'decoration', True, True)]
            if is_crafting:
                if item.craft_cost(base_cost, price_multiplier) > 0:
                    craft_msg = u"Craft for %d farthing%s (you have %s)" % (item.craft_cost(base_cost, price_multiplier), number_pluralizer((item.craft_cost(base_cost, price_multiplier))), self.money)
                else:
                    craft_msg = u"Craft"
            else:
                craft_msg = u"Craft for %d farthing%s (you have %s)" % (item.craft_cost(base_cost, price_multiplier), number_pluralizer((item.craft_cost(base_cost, price_multiplier))), self.money)
            menu_options += [(craft_msg, 'create', True, item.craft_cost(base_cost, price_multiplier) <= self.money)]
            menu_choice = call_screen("dw_choice", menu_options)
            # показ меню
            if menu_choice == 'return':
                return None
            elif menu_choice == 'quality':
                menu_options = []
                for quality_type in quality:
                    menu_options += [(quality_options[quality_type], quality_type, True, True)]
                item.quality = call_screen("dw_choice", menu_options)
            elif menu_choice == 'material':
                item.material = self.craft_select_material(materials)
            elif menu_choice == 'spangled':
                item.spangled = self.craft_select_gem(is_crafting, 'small')
            elif menu_choice == 'inlaid':
                item.inlaid = self.craft_select_gem(is_crafting, 'common')
            elif menu_choice == 'huge':
                item.huge = self.craft_select_gem(is_crafting, 'large')
            elif menu_choice == 'decoration':
                menu_options = [(u"Decorate with image", 'yes', True, True)]
                menu_options += [(u"No image", 'no', True, True)]
                menu_choice = call_screen("dw_choice", menu_options)
                if menu_choice == 'yes':
                    item.decoration_image = random.choice(image_types[item.alignment])
                    if item.material in material_types:
                        item.decoration = 'carving'
                    else:
                        item.decoration = weighted_select(Treasure.decorate_types)
                else:
                    item.decoration = None
                    item.decoration_image = None
        if item.quality =='random':
            # случайный выбор качества вещи
            quality_list = (('rough', 25), ('common', 50), ('skillfully', 20), ('mastery', 10),)
            item.quality = weighted_random(quality_list)
        self.money -= item.craft_cost(base_cost, price_multiplier)
        if is_crafting:
            # если делается из материалов дракона - убираем материалы из сокровищницы
            if item.material in material_types:
                material = None
                materials_size = sorted(Material.size_dict.keys(), key=lambda mat_size: Material.size_dict[mat_size][1]) 
                # сортировка по размеру, т.к. дракон жадный - зачем отдавать большой кусок, если можно сделать из любого?
                for material_size in materials_size:
                    # ищем из какого бы куска изготовить вещь
                    if not material:
                        material = self.take_material(item.material + u";" + material_size)
            else:
                self.take_ingot(item.material)
            if item.spangled:
                self.take_gem(item.spangled.g_type + u';small;' + item.spangled.cut)
            if item.inlaid:
                self.take_gem(item.inlaid.g_type + u';common;' + item.inlaid.cut)
            if item.huge:
                self.take_gem(item.huge.g_type + u';large;' + item.huge.cut)
            if item.image:
                item.decoration_image = random.choice(image_types[item.alignment])
        return item