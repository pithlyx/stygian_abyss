
def seed_weapons():
    from db.db_models import Weapon
    from db.db_menu import create_entry, create_table
    create_table(Weapon, True)
    weapon_data = [
        # Sword
        ["Sword of Valor", 1.2, 0.2, 10, "sword"],
        ["Blade of Shadows", 1.1, 0.6, 8, "sword"],
        ["Flamebrand", 1.4, 0.4, 12, "sword"],
        ["Frostbite", 1.3, 0.5, 11, "sword"],
        ["Soulreaver", 1.5, 0.3, 13, "sword"],
        ["Thunderstrike", 1.6, 0.2, 15, "sword"],
        ["Vorpal Sword", 1.4, 0.6, 14, "sword"],
        ["Divine Blade", 1.2, 0.8, 11, "sword"],
        ["Doomblade", 1.3, 0.7, 12, "sword"],
        ["Runeblade", 1.1, 0.9, 10, "sword"],

        # Staff
        ["Staff of Arcane Power", 0.4, 1.6, 15, "staff"],
        ["Twilight Rod", 0.5, 1.5, 12, "staff"],
        ["Nature's Embrace", 0.6, 1.4, 11, "staff"],
        ["Inferno Staff", 0.3, 1.7, 14, "staff"],
        ["Frostwood Staff", 0.4, 1.6, 13, "staff"],
        ["Scepter of Radiance", 0.5, 1.5, 10, "staff"],
        ["Celestial Wand", 0.7, 1.3, 16, "staff"],
        ["Void Staff", 0.6, 1.4, 12, "staff"],
        ["Thunderbolt Rod", 0.5, 1.6, 13, "staff"],
        ["Druidic Staff", 0.6, 1.5, 14, "staff"],

        # Bow
        ["Bow of Precision", 1.4, 0.2, 9, "bow"],
        ["Shadowstrike Bow", 1.3, 0.3, 8, "bow"],
        ["Flameflight Bow", 1.5, 0.4, 11, "bow"],
        ["Frostwind Bow", 1.4, 0.5, 10, "bow"],
        ["Venomstrike Bow", 1.6, 0.2, 12, "bow"],
        ["Thunderstorm Bow", 1.7, 0.1, 13, "bow"],
        ["Moonshot Bow", 1.6, 0.3, 12, "bow"],
        ["Divine Archer Bow", 1.3, 0.7, 10, "bow"],
        ["Doomshadow Bow", 1.4, 0.6, 11, "bow"],
        ["Windforce Bow", 1.2, 0.8, 9, "bow"],

        # Dagger
        ["Dagger of Shadows", 1.1, 0.6, 6, "dagger"],
        ["Venomstrike Dagger", 1.2, 0.5, 7, "dagger"],
        ["Frostbite Dagger", 1.3, 0.4, 8, "dagger"],
        ["Silent Blade", 1.0, 0.8, 5, "dagger"],
        ["Soulthief Dagger", 1.4, 0.3, 9, "dagger"],
        ["Swiftstrike Dagger", 1.2, 0.6, 7, "dagger"],
        ["Shadowfang Dagger", 1.3, 0.5, 8, "dagger"],
        ["Doomblade Dagger", 1.5, 0.2, 10, "dagger"],
        ["Viperstrike Dagger", 1.1, 0.7, 6, "dagger"],
        ["Assassin's Blade", 1.4, 0.4, 9, "dagger"],

        # Mace
        ["Mace of Justice", 1.4, 0.2, 12, "mace"],
        ["Cursed Mace", 1.2, 0.4, 10, "mace"],
        ["Flamestrike Mace", 1.5, 0.3, 13, "mace"],
        ["Frostshard Mace", 1.3, 0.5, 11, "mace"],
        ["Skullcrusher", 1.6, 0.2, 15, "mace"],
        ["Thundering Mace", 1.7, 0.1, 16, "mace"],
        ["Holy Hammer", 1.5, 0.4, 14, "mace"],
        ["Doombringer", 1.4, 0.6, 13, "mace"],
        ["Wrathful Mace", 1.3, 0.7, 12, "mace"],
        ["Soulburn Mace", 1.6, 0.3, 15, "mace"],

        # Wand
        ["Wand of the Arcanist", 0.4, 1.6, 9, "wand"],
        ["Shadowmire Wand", 0.5, 1.5, 8, "wand"],
        ["Flamecore Wand", 0.6, 1.4, 7, "wand"],
        ["Frostwind Wand", 0.3, 1.7, 10, "wand"],
        ["Soulspark Wand", 0.4, 1.6, 11, "wand"],
        ["Thunderstrike Wand", 0.5, 1.5, 12, "wand"],
        ["Celestial Wand", 0.7, 1.3, 14, "wand"],
        ["Void Wand", 0.6, 1.4, 13, "wand"],
        ["Stormcaller Wand", 0.5, 1.6, 11, "wand"],
        ["Druidic Wand", 0.6, 1.5, 12, "wand"],

        # Axe
        ["Axe of Might", 1.3, 0.2, 11, "axe"],
        ["Shadowcleaver", 1.2, 0.4, 10, "axe"],
        ["Flamebiter", 1.5, 0.3, 13, "axe"],
        ["Frostbite Axe", 1.4, 0.5, 12, "axe"],
        ["Skullsplitter", 1.6, 0.2, 15, "axe"],
        ["Thunderaxe", 1.7, 0.1, 16, "axe"],
        ["Warlord's Axe", 1.4, 0.6, 14, "axe"],
        ["Divine Executioner", 1.3, 0.7, 11, "axe"],
        ["Doomcleaver", 1.5, 0.4, 13, "axe"],
        ["Ragefire Axe", 1.2, 0.8, 10, "axe"],

        # Spear
        ["Spear of the Vanguard", 1.3, 0.2, 12, "spear"],
        ["Shadowpiercer", 1.2, 0.4, 10, "spear"],
        ["Flamespear", 1.5, 0.3, 13, "spear"],
        ["Frostbite Spear", 1.4, 0.5, 12, "spear"],
        ["Skullseeker", 1.6, 0.2, 15, "spear"],
        ["Thunderstrike Spear", 1.7, 0.1, 16, "spear"],
        ["Divine Halberd", 1.4, 0.6, 14, "spear"],
        ["Doomspike", 1.3, 0.7, 11, "spear"],
        ["Vengeful Lance", 1.5, 0.4, 13, "spear"],
        ["Windborne Pike", 1.2, 0.8, 10, "spear"],

        # Crossbow
        ["Crossbow of Precision", 1.4, 0.2, 9, "crossbow"],
        ["Shadowstrike Crossbow", 1.3, 0.3, 8, "crossbow"],
        ["Flameflight Crossbow", 1.5, 0.4, 11, "crossbow"],
        ["Frostwind Crossbow", 1.4, 0.5, 10, "crossbow"],
        ["Venomstrike Crossbow", 1.6, 0.2, 12, "crossbow"],
        ["Thunderstorm Crossbow", 1.7, 0.1, 13, "crossbow"],
        ["Moonshot Crossbow", 1.6, 0.3, 12, "crossbow"],
        ["Divine Archer Crossbow", 1.3, 0.7, 10, "crossbow"],
        ["Doomshadow Crossbow", 1.4, 0.6, 11, "crossbow"],
        ["Windforce Crossbow", 1.2, 0.8, 9, "crossbow"],

        # Hammer
        ["Hammer of Justice", 1.4, 0.2, 12, "hammer"],
        ["Cursed Hammer", 1.2, 0.4, 10, "hammer"],
        ["Flamestrike Hammer", 1.5, 0.3, 13, "hammer"],
        ["Frostshard Hammer", 1.3, 0.5, 11, "hammer"],
        ["Skullcrusher", 1.6, 0.2, 15, "hammer"],
        ["Thundering Hammer", 1.7, 0.1, 16, "hammer"],
        ["Holy Hammer", 1.5, 0.4, 14, "hammer"],
        ["Doombringer", 1.4, 0.6, 13, "hammer"],
        ["Wrathful Hammer", 1.3, 0.7, 12, "hammer"],
        ["Soulburn Hammer", 1.6, 0.3, 15, "hammer"]
    ]

    for weapon in weapon_data:
        create_entry(Weapon, weapon)


def seed_armors():
    from db.db_models import Armor
    from db.db_menu import create_entry, create_table
    create_table(Armor, True)
    armor_data = [
        # Helms
        ["Steel Helm", 15, 8, 3, "helmet"],
        ["Leather Helm", 8, 5, 2, "helmet"],
        ["Iron Helm", 12, 6, 4, "helmet"],
        ["Chain Coif", 10, 7, 3, "helmet"],
        ["Plate Helm", 18, 10, 5, "helmet"],
        ["Silk Hood", 6, 12, 2, "helmet"],
        ["Scale Helmet", 13, 7, 4, "helmet"],
        ["Bronze Helm", 14, 8, 4, "helmet"],
        ["Horned Helm", 16, 9, 5, "helmet"],
        ["Cloth Cap", 5, 10, 2, "helmet"],
        ["Copper Helm", 10, 6, 3, "helmet"],
        ["Bone Helm", 8, 4, 2, "helmet"],
        ["Silver Helm", 20, 12, 6, "helmet"],
        ["Golden Crown", 12, 18, 4, "helmet"],
        ["Platinum Helm", 25, 15, 7, "helmet"],
        ["Diamond Circlet", 8, 25, 3, "helmet"],
        ["Shadow Hood", 18, 10, 8, "helmet"],
        ["Ancient Helm", 22, 16, 6, "helmet"],
        ["Crystal Crown", 14, 22, 5, "helmet"],
        ["Dragon Helm", 30, 20, 10, "helmet"],

        # Chestplates
        ["Plate Mail", 25, 12, 6, "chestplate"],
        ["Leather Tunic", 12, 6, 3, "chestplate"],
        ["Chainmail", 20, 10, 5, "chestplate"],
        ["Silk Robe", 8, 15, 3, "chestplate"],
        ["Scale Armor", 18, 9, 5, "chestplate"],
        ["Bronze Chestplate", 22, 11, 6, "chestplate"],
        ["Steel Plate", 28, 14, 7, "chestplate"],
        ["Cloth Garments", 10, 12, 3, "chestplate"],
        ["Iron Cuirass", 24, 12, 6, "chestplate"],
        ["Copper Armor", 15, 8, 4, "chestplate"],
        ["Bone Chestplate", 14, 6, 4, "chestplate"],
        ["Silver Plate", 32, 16, 8, "chestplate"],
        ["Golden Armor", 20, 28, 5, "chestplate"],
        ["Platinum Plate", 40, 20, 10, "chestplate"],
        ["Diamond Vest", 12, 35, 4, "chestplate"],
        ["Shadow Robe", 28, 15, 8, "chestplate"],
        ["Ancient Armor", 35, 18, 10, "chestplate"],
        ["Crystal Mail", 18, 30, 6, "chestplate"],
        ["Dragon Plate", 50, 25, 12, "chestplate"],

        # Leggings
        ["Steel Greaves", 18, 9, 4, "leggings"],
        ["Leather Leggings", 10, 5, 2, "leggings"],
        ["Iron Legplates", 15, 7, 3, "leggings"],
        ["Chain Leggings", 14, 8, 3, "leggings"],
        ["Plate Legguards", 20, 10, 5, "leggings"],
        ["Silk Pants", 7, 12, 2, "leggings"],
        ["Scale Leggings", 16, 8, 4, "leggings"],
        ["Bronze Legplates", 17, 9, 4, "leggings"],
        ["Horned Greaves", 19, 9, 5, "leggings"],
        ["Cloth Legwraps", 6, 10, 2, "leggings"],
        ["Copper Legguards", 12, 6, 3, "leggings"],
        ["Bone Legplates", 10, 4, 2, "leggings"],
        ["Silver Greaves", 22, 11, 6, "leggings"],
        ["Golden Leggings", 14, 20, 4, "leggings"],
        ["Platinum Greaves", 28, 14, 7, "leggings"],
        ["Diamond Legguards", 8, 25, 3, "leggings"],
        ["Shadow Pants", 20, 10, 8, "leggings"],
        ["Ancient Legplates", 24, 16, 6, "leggings"],
        ["Crystal Greaves", 16, 22, 5, "leggings"],
        ["Dragon Legguards", 30, 18, 10, "leggings"],

        # Boots
        ["Steel Boots", 12, 6, 3, "boots"],
        ["Leather Boots", 6, 3, 1, "boots"],
        ["Iron Boots", 10, 5, 2, "boots"],
        ["Chain Boots", 9, 4, 2, "boots"],
        ["Plate Boots", 14, 7, 4, "boots"],
        ["Silk Slippers", 4, 8, 1, "boots"],
        ["Scale Boots", 8, 4, 3, "boots"],
        ["Bronze Boots", 9, 5, 3, "boots"],
        ["Horned Boots", 11, 6, 4, "boots"],
        ["Cloth Shoes", 3, 6, 1, "boots"],
        ["Copper Boots", 7, 3, 2, "boots"],
        ["Bone Boots", 5, 2, 1, "boots"],
        ["Silver Boots", 16, 8, 5, "boots"],
        ["Golden Boots", 10, 15, 3, "boots"],
        ["Platinum Boots", 20, 10, 6, "boots"],
        ["Diamond Boots", 6, 18, 2, "boots"],
        ["Shadow Boots", 14, 8, 7, "boots"],
        ["Ancient Boots", 18, 10, 6, "boots"],
        ["Crystal Boots", 12, 16, 4, "boots"],
        ["Dragon Boots", 25, 14, 8, "boots"],

        # Gloves
        ["Steel Gauntlets", 8, 4, 2, "gloves"],
        ["Leather Gloves", 4, 2, 1, "gloves"],
        ["Iron Gauntlets", 6, 3, 2, "gloves"],
        ["Chain Gloves", 5, 2, 1, "gloves"],
        ["Plate Gauntlets", 10, 5, 3, "gloves"],
        ["Silk Gloves", 3, 6, 1, "gloves"],
        ["Scale Gauntlets", 6, 3, 2, "gloves"],
        ["Bronze Gauntlets", 7, 4, 2, "gloves"],
        ["Horned Gauntlets", 9, 4, 3, "gloves"],
        ["Cloth Handwraps", 2, 4, 1, "gloves"],
        ["Copper Gauntlets", 5, 3, 1, "gloves"],
        ["Bone Gloves", 3, 2, 1, "gloves"],
        ["Silver Gauntlets", 12, 6, 4, "gloves"],
        ["Golden Gauntlets", 8, 10, 2, "gloves"],
        ["Platinum Gauntlets", 15, 8, 5, "gloves"],
        ["Diamond Gauntlets", 4, 12, 1, "gloves"],
        ["Shadow Gloves", 10, 6, 5, "gloves"],
        ["Ancient Gauntlets", 14, 8, 4, "gloves"],
        ["Crystal Gloves", 9, 10, 3, "gloves"],
        ["Dragon Gauntlets", 18, 12, 6, "gloves"]
    ]
    for armor in armor_data:
        create_entry(Armor, armor)


def seed_classes():
    from db.db_models import Char_Class
    from db.db_menu import create_entry, create_table
    create_table(Char_Class, True)
    classes = [
        # Sword
        ["Swordmaster", "A master of the blade, the Swordmaster combines precision and strength to deliver lethal sword strikes.",
            120, 80, 1.2, 0.4, 1.1, 0.8, "sword"],
        # Staff
        ["Archmage", "The Archmage commands immense magical power, wielding a staff to channel arcane energies and reshape reality itself.",
            80, 120, 0.5, 1.5, 0.8, 1.2, "staff"],
        # Bow
        ["Sharpshooter", "The Sharpshooter is an unparalleled marksman, striking down enemies with deadly accuracy using their trusty bow.",
            100, 80, 1.3, 0.8, 0.9, 0.7, "bow"],
        # Dagger
        ["Shadowblade", "Swift and deadly, the Shadowblade strikes from the shadows with lightning-fast dagger attacks, leaving no trace behind.",
            90, 60, 1.2, 0.9, 0.8, 0.9, "dagger"],
        # Mace
        ["Crusader", "The Crusader wields a mighty mace, bringing divine justice upon evildoers and protecting the weak with unwavering resolve.",
            140, 80, 1.1, 0.7, 1.2, 1.1, "mace"],
        # Wand
        ["Spellweaver", "The Spellweaver harnesses the raw power of magic through their enchanted wand, casting devastating spells to vanquish foes.",
            70, 140, 0.7, 1.3, 0.6, 1.4, "wand"],
        # Axe
        ["Berserker", "The Berserker is a raging force of destruction, wielding a massive axe to cleave through enemies with unstoppable fury.",
            130, 40, 1.4, 0.6, 1.3, 0.5, "axe"],
        # Spear
        ["Lancer", "The Lancer is a skilled warrior who dominates the battlefield with their swift spear strikes and precise martial techniques.",
            110, 70, 1.2, 0.8, 1.1, 0.9, "spear"],
        # Crossbow
        ["Sniper", "The Sniper is a patient and deadly hunter, taking down targets from a distance with their trusty crossbow and unmatched accuracy.",
            90, 60, 1.3, 0.7, 0.9, 0.8, "crossbow"],
        # Hammer
        ["Warhammer", "Wielding a colossal warhammer, this powerful warrior delivers bone-crushing blows and leaves a trail of destruction in their wake.",
            150, 50, 1.5, 0.4, 1.4, 0.6, "hammer"]
    ]
    for char_data in classes:
        create_entry(Char_Class, char_data)
