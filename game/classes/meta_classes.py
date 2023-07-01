class Player:
    def __init__(self, name, user_id=None):
        self.name = name
        self.user_id = user_id
        self.characters = []
        self.stats = {
            'health': 100,
            'mana': 100,
            'phys_dmg': 10,
            'magic_dmg': 10,
            'phys_def': 10,
            'magic_def': 10,
        }
        self.achievement_count = 0
    
    def create_character(self, character_name, class_type):
        character = Char(character_name, class_type)
        self.characters.append(character)
        self.update_stats(character.cls)
        print(f"Created a new character: {character_name}")
    
    def update_stats(self, class_obj):
        self.stats['health'] += class_obj.health_bonus
        self.stats['mana'] += class_obj.mana_bonus
        self.stats['phys_dmg'] += class_obj.phys_dmg_bonus
        self.stats['magic_dmg'] += class_obj.magic_dmg_bonus
        self.stats['phys_def'] += class_obj.phys_def_bonus
        self.stats['magic_def'] += class_obj.magic_def_bonus

class Char:
    def __init__(self, name, class_type):
        self.name = name
        self.cls = class_type
        self.level = 1
        self.equipment = {
            'helmet': None,
            'boots': None,
            'chest': None,
            'legs': None,
            'gloves': None,
            'weapon': None,
        }
        self.equip_mod = {
            'health': 0,
            'mana': 0,
            'phys_dmg': 0,
            'magic_dmg': 0,
            'phys_def': 0,
            'magic_def': 0,
        }
        self.stats = {
            'health': (100 + self.cls.health_bonus) + self.equip_mod['health'],
            'mana': (100 + self.cls.mana_bonus) + self.equip_mod['mana'],
            'phys_dmg': (10 + self.cls.phys_dmg_bonus) + self.equip_mod['phys_dmg'],
            'magic_dmg': (10 + self.cls.magic_dmg_bonus) + self.equip_mod['magic_dmg'],
            'phys_def': (10 + self.cls.phys_def_bonus) + self.equip_mod['phys_def'],
            'magic_def': (10 + self.cls.magic_def_bonus) + self.equip_mod['magic_def'],
        }
        
    def equip_item(self, slot, item):
        if slot in self.equipment:
            self.equipment[slot] = item
            print(f"{self.name} equipped {item.name} in the {slot} slot.")
            if isinstance(item, Item_Armor):
                for mod in ['health', 'mana', 'phys_def', 'magic_def']:
                    modifier = self.equip_mod[mod]
                    self.equip_mod[mod] += item.modifiers[f'{mod}_mod']
                    if modifier != self.equip_mod[mod]:
                        print(f"{self.name}'s {mod} changed from {modifier} to {self.equip_mod[mod]}.")
            elif isinstance(item, Item_Weapon):
                for mod in ['phys_dmg', 'magic_dmg']:
                    self.equip_mod[mod] += item.modifiers[f'{mod}_mod']
        else:
            print(f"{self.name} cannot equip items in the {slot} slot.")

    def unequip_item(self, slot):
        if slot in self.equipment:
            item = self.equipment[slot]
            self.equipment[slot] = None
            print(f"{self.name} unequipped {item.name} from the {slot} slot.")
        else:
            print(f"{self.name} does not have an item equipped in the {slot} slot.")


class Item_Armor:
    def __init__(self, name, slot, health_mod=0, mana_mod=0, phys_def_mod=0, magic_def_mod=0):
        self.name = name
        self.slot = slot
        self.modifiers = {'health_mod': health_mod, 'mana_mod': mana_mod, 'phys_def_mod': phys_def_mod, 'magic_def_mod': magic_def_mod}


class Item_Weapon:
    def __init__(self, name, weapon_type, phys_dmg_mod=0, magic_dmg_mod=0):
        self.name = name
        self.weapon_type = weapon_type
        self.modifiers = {'phys_dmg_mod': phys_dmg_mod, 'magic_dmg_mod': magic_dmg_mod}


class Char_Class:
    def __init__(self, name, health_bonus=0, mana_bonus=0, phys_dmg_bonus=0, magic_dmg_bonus=0, phys_def_bonus=0, magic_def_bonus=0):
        self.name = name
        self.health_bonus = health_bonus
        self.mana_bonus = mana_bonus
        self.phys_dmg_bonus = phys_dmg_bonus
        self.magic_dmg_bonus = magic_dmg_bonus
        self.phys_def_bonus = phys_def_bonus
        self.magic_def_bonus = magic_def_bonus