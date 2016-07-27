from random import randint
from random import random

###################################################################

#list of weapon lists (names)
low_damage_short_weapons_names = ("Rusted_Dagger", "Broken_Dagger", "Rusted_Knife", "Broken_Knife")
low_damage_medium_weapons_names = ("Rusted_Iron_Sword", "Broken_Iron_Sword", "Rusted_Short_Sword", "Broken_Short_Sword")
low_damage_long_weapons_names = ("Rusted_Rapier", "Broken_Rapier", "Rusted_Long_Sword", "Broken_Long_Sword")
medium_damage_short_weapons_names = ("Dagger", "Cracked_Dagger", "Shimmering_Knife", "Knife")
medium_damage_medium_weapons_names = ("Iron_Sword", "Mediocre_Iron_Sword", "Short_Sword_Of_Hercules", "Average_Short_Sword")
medium_damage_long_weapons_names = ("Chrome_Plated_Rapier", "Superior_Rapier", "Fiery_Long_Sword", "Icy_Long_Sword")
high_damage_short_weapons_names = ("Diamond_Plated_Dagger", "Sturdy_Dagger", "Glistening_Knife", "Hunting_Knife")
high_damage_medium_weapons_names = ("Prestine_Iron_Sword", "Broadsword", "Xiphos", "Moon_Lit_Short_Sword")
high_damage_long_weapons_names = ("Falchion", "Sabre", "Scimitar", "Claymore")
broken_weapons_names = ("Golden_Rapier", "Dawn_Lit_Rapier", "Double_Edged_Long_Sword", "Bastard_Sword")
dumb_weapons_names = ("Stick", "Rock")
ranged_weapons_names = ("Short_Bow", "Long_Bow", "Cross_Bow")
broken_ranged_weapons_names = "Marksman_Pistol"

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

###################################################################

#list of weapon lists (values)
low_damage_short_weapons = (Rusted_Dagger, Broken_Dagger, Rusted_Knife, Broken_Knife)
low_damage_medium_weapons = (Rusted_Iron_Sword, Broken_Iron_Sword, Rusted_Short_Sword, Broken_Short_Sword)
low_damage_long_weapons = (Rusted_Rapier, Broken_Rapier, Rusted_Long_Sword, Broken_Long_Sword)
medium_damage_short_weapons = (Dagger, Cracked_Dagger, Shimmering_Knife, Knife)
medium_damage_medium_weapons = (Iron_Sword, Mediocre_Iron_Sword, Short_Sword_Of_Hercules, Average_Short_Sword)
medium_damage_long_weapons = (Chrome_Plated_Rapier, Superior_Rapier, Fiery_Long_Sword, Icy_Long_Sword)
high_damage_short_weapons = (Diamond_Plated_Dagger, Sturdy_Dagger, Glistening_Knife, Hunting_Knife)
high_damage_medium_weapons = (Prestine_Iron_Sword, Broadsword, Xiphos, Moon_Lit_Short_Sword)
high_damage_long_weapons = (Falchion, Sabre, Scimitar, Claymore)
broken_weapons = (Golden_Rapier, Dawn_Lit_Rapier, Double_Edged_Long_Sword, Bastard_Sword)
dumb_weapons = (Stick, Rock)
ranged_weapons = (Short_Bow, Long_Bow, Cross_Bow)
broken_ranged_weapons = Marksman_Pistol

###################################################################

time = True
battle = False
weapon_equip_1_inventory = low_damage_short_weapons_names[0]
weapon_equip_2_inventory = low_damage_short_weapons_names[3]
weapon_equip_1 = low_damage_short_weapons[0]
weapon_equip_2 = low_damage_short_weapons[3]
player_inventory = [weapon_equip_1_inventory, weapon_equip_2_inventory, "Health Potion"]
Coins = 0
player_bag = []
player_lvl = 1
player_damage = (int(player_lvl) + int(weapon_equip_1) + int(weapon_equip_2))*-.5
player_kills = 0
player_num_of_equiped = 0
player_health = 10
player_health_max = 10
genEnemyDamage = int(player_damage)*.6
genEnemyHealth = ""
enemyNameGen = ""
enemyName = randint(1, 2)
if enemyName == 1:
    enemyName = "a nord"
if enemyName == 2:
    enemyName = "a senile, old man"
enemy_health = int(player_health_max * .5)
enemy_health_max = int(player_health_max * .5)
damage_from_enemy = int(player_damage)*-.5
hard_enemyName = randint(1, 2)
if hard_enemyName == 1:
    hard_enemyName = "a body-builder"
if hard_enemyName == 2:
    hard_enemyName = "a child on crystal meth"
hard_enemy_health = int(player_health_max *.9)
hard_enemy_health_max = int(player_health_max *.9)
damage_from_hard_enemy = int(player_damage)*-.6
bossName = randint(1, 2)
if bossName == 1:
    bossName = "a Dragon"
if bossName == 2:
    bossName = "a Hydra"
boss_health = player_health_max*1.1
boss_health_max = player_health_max*1.1
damage_from_boss = int(player_damage)*-.75


if player_health <= 0:
    "%s died! Better luck next time!" % (charName)
    playerChoice = "quit"
    time = False


###################################################################



charName = raw_input("\nWelcome fellow adventurer... What is your name?\n > ")

print "(Type 'help' for a list of commands.)"

while time is True:
    playerChoice1 = raw_input("Ahh... I see.\nYou do look quite like a %s to me..."
                         " So %s what would you like to do now?\n > " % (charName, charName))
    if playerChoice1 == "stats":
        print "%s's Level: %s\n%s's Health: %s\n"
        break
    if playerChoice1 == "help":
        print "['explore','attack', 'special attack', 'block', 'evade', 'flee', 'stats','inventory', 'help','quit']"
        break
    if playerChoice1 == "inventory":
        print player_inventory
        break
    if playerChoice1 == "quit":
        player_health = 0
        break
    else: print "Command not recognized."
    break

if player_health > 0:
    while time is True:
        if player_health > 0:
            if player_kills is player_lvl:
                player_lvl = player_lvl + 1
                player_health_max = int(player_health_max + int(player_health_max) * 1.25)
                player_kills = 0
            if player_lvl == 25:
                player_inventory = player_inventory + ["Marksman_Pistol"]
            playerChoice = raw_input("What will you do?\n > ")
            if playerChoice == "explore":
                randomEncounter = randint(1, 2)
                if randomEncounter == 1:
                    print "%s explores..." % charName
                if randomEncounter == 2:
                    randomEncounter = randint(2, 3)
                    if randomEncounter == 2:
                        print "%s explores and encounters %s!" % (charName,enemyName)
                    if randomEncounter == 3:
                        randomEncounter = randint(2, 3)
                        if randomEncounter == 2:
                            print "%s explores and discovers %s!" % (charName, enemyName)
                        if randomEncounter == 3:
                            randomEncounter = randint(2, 3)
                            if randomEncounter == 2:
                                print "%s explores and finds %s!" % (charName, enemyName)
                            if randomEncounter == 3:
                                randomEncounter = randint(2, 3)
                                if randomEncounter == 2:
                                    print "%s explores and is attacked by %s!" % (charName, enemyName)
                                if randomEncounter == 3:
                                    randomEncounter = randint(2, 3)
                                    if randomEncounter == 2:
                                        print "%s explores and is discovered by %s!" % (charName, enemyName)
                                    if randomEncounter == 3:
                                        randomEncounter = randint(2, 3)
                                        if randomEncounter == 2:
                                            print "%s explores and is encountered by %s!" % (charName, enemyName)
                                        if randomEncounter == 3:
                                                randomEncounter = randint(4, 5)
                                                if randomEncounter == 4:
                                                    print "%s explores and encounters %s!" % (charName, hard_enemyName)
                                                if randomEncounter == 5:
                                                    randomEncounter = randint(4, 5)
                                                    if randomEncounter == 4:
                                                        print "%s explores and discovers %s!" % (charName, hard_enemyName)
                                                    if randomEncounter == 5:
                                                        randomEncounter = randint(4, 5)
                                                        if randomEncounter == 4:
                                                            print "%s explores and finds %s!" % (charName, hard_enemyName)
                                                        if randomEncounter == 5:
                                                            randomEncounter = randint(4, 5)
                                                            if randomEncounter == 4:
                                                                print "%s explores and is attacked by %s!" % (charName, hard_enemyName)
                                                            if randomEncounter == 5:
                                                                randomEncounter = randint(4, 5)
                                                                if randomEncounter == 4:
                                                                    print "%s explores and is discovered by %s!" % (charName, hard_enemyName)
                                                                if randomEncounter == 5:
                                                                    randomEncounter = randint(4, 5)
                                                                    if randomEncounter == 4:
                                                                        print "%s explores and is encountered by %s!" % (charName, hard_enemyName)
                                                                    if randomEncounter == 5:
                                                                        randomEncounter = randint(6, 7)
                                                                        if randomEncounter == 6:
                                                                            print "%s explores and encounters %s!" % (charName, bossName)
                                                                        if randomEncounter == 7:
                                                                            randomEncounter = randint(6, 7)
                                                                            if randomEncounter == 6:
                                                                                print "%s explores and discovers %s!" % (charName, bossName)
                                                                            if randomEncounter == 7:
                                                                                randomEncounter = randint(6, 7)
                                                                                if randomEncounter == 6:
                                                                                    print "%s explores and finds %s!" % (charName, bossName)
                                                                                if randomEncounter == 7:
                                                                                    randomEncounter = randint(6, 7)
                                                                                    if randomEncounter == 6:
                                                                                        print "%s explores and is attacked by %s!" % (charName, bossName)
                                                                                    if randomEncounter == 7:
                                                                                        randomEncounter = randint(6, 7)
                                                                                        if randomEncounter == 6:
                                                                                            print "%s explores and is discovered by %s!" % (charName, bossName)
                                                                                        if randomEncounter == 7:
                                                                                            randomEncounter = randint(6, 7)
                                                                                            if randomEncounter == 6:
                                                                                                print"%s explores and is encountered by %s!" % (charName, bossName)
                    playerChoice = ""
                    if randomEncounter == 2:
                        genEnemyHealth = enemy_health
                    if randomEncounter == 3:
                        genEnemyHealth = enemy_health
                    if randomEncounter == 4:
                        genEnemyHealth = hard_enemy_health
                    if randomEncounter == 5:
                        genEnemyHealth = hard_enemy_health
                    if randomEncounter == 6:
                        genEnemyHealth = boss_health
                    if randomEncounter == 7:
                        genEnemyHealth = boss_health
                    else: playerChoice = ""
                    battle = True

                if battle is True:
                    print "['attack', 'special attack', 'block', 'evade', 'flee', 'stats', 'help','quit']"
                    while battle is True:
                        playerChoice = raw_input("What will you do?\n > ")
                        if playerChoice == "attack":
                            battle = True
                            if enemyNameGen == enemyName:
                                genEnemyHealth = enemy_health
                                genEnemyDamage = damage_from_enemy
                            if enemyNameGen == hard_enemyName:
                                genEnemyHealth = hard_enemy_health
                                genEnemyDamage = damage_from_hard_enemy
                            if enemyNameGen == bossName:
                                genEnemyHealth = boss_health
                                genEnemyDamage = damage_from_boss
                            one_sided = randint(3, 4)
                            if one_sided == 3:
                                genEnemyHealth = genEnemyHealth + player_damage
                                print "The Enemy has been damaged!\n%s's Health: %s\nEnemy's Health: %s" % (charName, player_health, genEnemyHealth)
                            if one_sided == 4:
                                player_health = player_health + genEnemyDamage
                                print "%s has been damaged!\n%s's Health: %s\nEnemy's Health: %s" % (charName, charName, player_health, genEnemyHealth)
                            if player_health > 0:
                                if genEnemyHealth <= 0:
                                    Coins = int(Coins) + 10
                                    print "The enemy has been defeated!\nCoins Acquired: 10"
                                    battle = False
                                    playerChoice = ""
                            else: "%s died! Better luck next time!" % (charName)
                            battle = True
                        if playerChoice == "special attack":
                            double = randint(1, 2)
                            if double == 1:
                                player_health = int(player_health) + int(genEnemyDamage)
                                genEnemyHealth = genEnemyHealth + player_damage
                                print "Everyone is damaged!\n%s's Health: %s\nEnemy's Health: %s" % (
                                charName, player_health, genEnemyHealth)
                                battle = True
                            if double == 2:
                                print "No one is damaged!\n%s's Health: %s\nEnemy's Health: %s" % (
                                    charName, player_health, genEnemyHealth)
                                battle = True
                            if player_health > 0:
                                if genEnemyHealth <= 0:
                                    Coins = int(Coins) + 10
                                    print "The enemy has been defeated!\nCoins Acquired: 10"
                                    battle = False
                                    playerChoice = ""
                            else: "%s died! Better luck next time!" % (charName)
                            playerChoice = "quit"
                        if playerChoice == "block":
                            print "%s bolsters their defenses and takes no damage" % (charName, charName)
                        if playerChoice == "evade":
                            print "%s rolls past the enemy. No damage was taken." % charName
                        if playerChoice == "flee":
                            print "You ran away and it looks like your dignity wasn't the only thing to come out unscathed!"
                            player_health = int(player_health - 1)
                            print "%s's Health: %s" % (charName, player_health)
                            if player_health <= 0:
                                "%s died! Better luck next time!" % (charName)
                                playerChoice = "quit"
                        if playerChoice == "stats":
                            print "%s's Level: %s\n%s's Health: %s\nEnemy's Health:" % (charName, player_lvl, charName, player_health,)
                        if playerChoice == "help":
                            print "['attack', 'special attack', 'block', 'evade', 'flee', 'stats', 'help','quit']"
                        if player_health <= 0:
                            "%s was killed by a %s! Better luck next time!" % (charName, enemyNameGen)
                            playerChoice = "quit"
                            time = False
                            battle = False
                        if playerChoice == "quit":
                            time = False
                            battle = False
                            break
                        while battle = True:
                            if playerChoice == "":
                                playerChoice = ""
                            playerChoice = raw_input("What will you do?\n > ")
                        else
            if playerChoice == "":
                playerChoice = ""
            if playerChoice == "rest":
                player_health = int(player_health_max)
            if playerChoice == "attack":
                print "%s swats at the air, looking quite stupid." % charName
            if playerChoice == "special attack":
                print "%s is an idiot..." % charName
            if playerChoice == "block":
                print "%s bolsters their defenses without any reason to. %s looks quite stupid." % (charName, charName)
            if playerChoice == "evade":
                print "%s rolls on the floor, looking quite stupid." % charName
            if playerChoice == "flee":
                print "You ran away and it looks like your dignity wasn't the only thing to come out unscathed!"
                player_health = int(player_health - 1)
                print "%s's Health: %s" % (charName, player_health)
                if player_health <= 0:
                    "%s died! Better luck next time!" % (charName)
                    playerChoice = "quit"
                if battle is False:
                    print "%s runs from nothing in particular!" % charName

            if playerChoice == "stats":
                print "%s's Level: %s\n%s's Health: %s\n" % (charName, player_lvl, charName, player_health)
            if playerChoice == "inventory":
                print player_inventory
                equip = raw_input("Would you like to equip something?\n(yes/no)")
                if equip == "yes":
                    print player_inventory
                    switch_inventory_slot_1 = raw_input("Would you like to equip something in weapon slot one?\n(yes/no)")
                    if switch_inventory_slot_1 == "yes":
                        print "Select a weapon."
                if equip == "no":
                    break
                else: print "Command not recognized."



            if playerChoice == "help":
                print "['explore', 'rest', 'attack', 'special attack', 'block', 'evade', 'flee', 'stats','inventory', 'help','quit']"
            if playerChoice == "quit":
                break
            else: print "Command not recognized."
        else: "%s died! Better luck next time!" % (charName)
    time = False
#Stats Of Weapons Vary On Player Level (Health) and Base Weapon Stats
#random chance to drop low and medium damage weapons on normal mobs
#random chance to drop high damage weapons on "Hard" mobs
#random chance to drop broken weapons on bosses
#random chance to drop ranged weapons on "Hard" mobs
#random chance to drop broken ranged weapons on bosses
#if player_level = 25 then player_inventory = player inventory + "Marksman's Pistol"
#player can only equip two short weapons or one long weapon with one ranged weapon
#specify with 'battle' command to battle an enemy of a certain difficulty
#'explore' gives player coins to spend in a shop
#fix inventory