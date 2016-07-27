from random import randint
from random import random

###################################################################

#list of weapon lists
low_damage_short_weapons = ("Rusted_Dagger", "Broken_Dagger", "Rusted_Knife", "Broken_Knife")
low_damage_medium_weapons = ("Rusted_Iron_Sword", "Broken_Iron_Sword", "Rusted_Short_Sword", "Broken_Short_Sword")
low_damage_long_weapons = ("Rusted_Rapier", "Broken_Rapier", "Rusted_Long_Sword", "Broken_Long_Sword")
medium_damage_short_weapons = ("Dagger", "Cracked_Dagger", "Shimmering_Knife", "Knife")
medium_damage_medium_weapons = ("Iron_Sword", "Mediocre_Iron_Sword", "Short_Sword_Of_Hercules", "Average_Short_Sword")
medium_damage_long_weapons = ("Chrome_Plated_Rapier", "Superior_Rapier", "Fiery_Long_Sword", "Icy_Long_Sword")
high_damage_short_weapons = ("Diamond_Plated_Dagger", "Sturdy_Dagger", "Glistening_Knife", "Hunting_Knife")
high_damage_medium_weapons = ("Prestine_Iron_Sword", "Broadsword", "Xiphos", "Moon_Lit_Short_Sword")
high_damage_long_weapons = ("Falchion", "Sabre", "Scimitar", "Claymore")
broken_weapons = ("Golden_Rapier", "Dawn_Lit_Rapier", "Double_Edged_Long_Sword", "Bastard_Sword")
dumb_weapons = ("Stick", "Rock")
ranged_weapons = ("Short_Bow", "Long_Bow", "Cross_Bow")
broken_ranged_weapons = "Marksman_Pistol"

###################################################################

#list of all weapons' damage
    #low_damage_short_weapons (scale = basic)
Rusted_Dagger = 4
Broken_Dagger = 3
Rusted_Knife = 3
Broken_Knife = 2
    #low_damage_medium_weapons (scale = basic)
Rusted_Iron_Sword = 5
Broken_Iron_Sword = 4
Rusted_Short_Sword = 6
Broken_Short_Sword = 5
    #low_damage_long_weapons (scale = basic)
Rusted_Rapier = 7
Broken_Rapier = 6
Rusted_Long_Sword = 9
Broken_Long_Sword = 8
    #medium_damage_short_weapons (scale = *2+2)
Dagger = 8
Cracked_Dagger = 6
Shimmering_Knife = 7
Knife = 6
    #medium_damage_medium_weapons (scale = *2+2)
Iron_Sword = 12
Mediocre_Iron_Sword = 10
Short_Sword_Of_Hercules = 14
Average_Short_Sword = 12
    #medium_damage_long_weapons (scale = *2+2)
Chrome_Plated_Rapier = 16
Superior_Rapier = 14
Fiery_Long_Sword = 20
Icy_Long_Sword = 18
    #high_damage_short_weapons (scale = *2+4)
Diamond_Plated_Dagger = 20
Sturdy_Dagger = 16
Glistening_Knife = 18
Hunting_Knife = 16
    #high_damage_medium_weapons (scale = *2+4)
Prestine_Iron_Sword = 28
Broadsword = 24
Xiphos = 32
Moon_Lit_Short_Sword = 29
    #high_damage_long_weapons (scale = *2+4)
Falchion = 36
Sabre = 32
Scimitar = 44
Claymore = 40
    #broken_weapons (scale = *2.25)
Golden_Rapier = 81
Dawn_Lit_Rapier = 72
Double_Edged_Long_Sword = 99
Bastard_Sword = 90
    #dumb_weapons (scale = basic)
Stick = 3
Rock = 5
    #ranged_weapons (scale = basic)
Short_Bow = 16
Long_Bow = 18
Cross_Bow = 14
    #broken_ranged_weapons (scale = broken)
Marksman_Pistol = 100

print broken_ranged_weapons
