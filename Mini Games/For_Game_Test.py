#imports
from random import randint

#list
player_inventory = "\nStick"

#variables and starting commands
player_lvl = 59
random_event_3 = randint(0, 1)
bossName = ""
if random_event_3 == 0:
    bossName = "A dragon"
if random_event_3 == 1:
    bossName = "A hydra"
boss_health = int(player_lvl)
battle = "False"
constant = battle
game = "on"
system = "on"
eName = ""
player_health_max = int(player_lvl) + 20
player_health = int(player_health_max)
enemy_health_max = int(player_health_max)*.85
player_damage = int(enemy_health_max)*-.4
init_player_damage = -5
enemy_health = int(enemy_health_max)
enemy_lvl = int(player_lvl) + 1
enemy_damage = int(player_health_max)*.1
init_enemy_damage = -2
boss_damage = int(player_health_max)*.45

#encountering system
andDiscoversEnemy = " and discovers an enemy!"

#keeps game running
while system == "on":

    #character name raw_input
    charName = raw_input("What would you like to name your character?\n > ")

    #keeps current save
    while game == "on":

        #commands while not battling an enemy
        while battle == "False":
            constant = "True"
            exploreChoice = raw_input("\nIt seems no enemies are near. What will you do?\n(Type 'help' for a list of commands.)\n > ")

            #when player types 'explore' outside of a battle
            if exploreChoice == "explore":
                random_event_1 = randint(0, 1)
                if random_event_1 == 0:
                    print "\n%s explores...\n" % charName
                if random_event_1 == 1:
                    print "\n%s explores and discovers an enemy!\n" % charName
                    battle = "True"

            # when player types 'explore' outside of a battle
            if exploreChoice == "fight boss":
                if player_lvl >= 20:
                    battle = "True"
                    constant = "True"
                    while constant == "True":
                        bossChoice = raw_input(
                            "\n%s is present... What will you do?\n(Type 'help' for a list of commands.)\n > " % bossName)

                        # when player types 'attack' inside of a battle
                        if bossChoice == "attack":
                            random_event_2 = randint(0, 1)
                            if random_event_2 == 0:
                                boss_damage = int(player_damage) * .9
                                player_health = int(player_health) + int(boss_damage)
                            if random_event_2 == 1:
                                boss_damage = int(player_damage) * 1.1
                                player_health = int(player_health) + int(boss_damage)
                            boss_health = int(boss_health) + int(player_damage)
                            if player_health > 0:
                                player_lvl = int(player_lvl) + 1
                                print "%s damages enemy!\n%s's Health: %s\n Enemy's Health: %s" % (
                                charName, charName, player_health, boss_health)
                                if boss_health <= 0:
                                    player_health_max = int(player_health_max) + int(player_health_max) * .15
                                    print "Enemy has been vanquished!"
                                    if player_lvl == 5:
                                        print "\nLevel up bonus, %s recieved a Dagger!" % charName
                                        player_inventory = str(player_inventory) + ", Dagger"
                                    if player_lvl == 10:
                                        print "\nLevel up bonus, %s recieved a Knife!" % charName
                                        player_inventory = str(player_inventory) + ", Knife"
                                    if player_lvl == 15:
                                        print "\nLevel up bonus, %s recieved an Iron Dagger!" % charName
                                        player_inventory = str(player_inventory) + ", Iron Dagger"
                                    if player_lvl == 20:
                                        print "\nLevel up bonus, %s recieved an Iron Sword!" % charName
                                        player_inventory = str(player_inventory) + ", Iron Sword"
                                    if player_lvl == 25:
                                        print "\nLevel up bonus, %s recieved a Silver Xiphos!" % charName
                                        player_inventory = str(player_inventory) + ", Silver Xiphos"
                                    if player_lvl == 30:
                                        print "\nLevel up bonus, %s recieved a Steel Sword!" % charName
                                        player_inventory = str(player_inventory) + ", Steel Sword"
                                    if player_lvl == 35:
                                        print "\nLevel up bonus, %s recieved a Gnarly Schmitar!" % charName
                                        player_inventory = str(player_inventory) + ", Gnarly Schmitar"
                                    if player_lvl == 40:
                                        print "\nLevel up bonus, %s recieved a Bastard Sword!" % charName
                                        player_inventory = str(player_inventory) + ", Bastard Sword"
                                    if player_lvl == 45:
                                        print "\nLevel up bonus, %s recieved a Chrome-plated Rapier!" % charName
                                        player_inventory = str(player_inventory) + ", Chrome-plated Rapier"
                                    if player_lvl == 50:
                                        print "\nLevel up bonus, %s recieved a Golden Rapier!" % charName
                                        player_inventory = str(player_inventory) + ", Golden Rapier"
                                    if player_lvl == 55:
                                        print "\nLevel up bonus, %s recieved a Diamond-plated Rapier!" % charName
                                        player_inventory = str(player_inventory) + ", Diamond-plated Rapier"
                                    if player_lvl == 60:
                                        print "\nLevel up bonus, %s recieved 'Marksman's Rifle'!" % charName
                                        player_inventory = str(player_inventory) + ", Marksman's Rifle"

                                    constant = "False"
                                    battle = "False"
                            if player_health <= 0:
                                play_again = raw_input("\nGame over!\n\nWould you like to play again?\n(yes/no)\n > ")
                                if play_again == "yes":
                                    constant = "False"
                                    battle = "False"
                                    game = "restart"
                                if play_again == "no":
                                    game = "off"
                                    system = "off"
                                    constant = "False"
                                    battle = "False"

                        # when player types 'block' inside of a battle
                        if bossChoice == "block":
                            print "\n%s bolsters their defenses and avoids damage!\n" % charName

                        # when player types 'evade' inside of a battle
                        if bossChoice == "evade":
                            print "\n%s rolls out of harm's way!\n" % charName

                        # when player types 'stats' inside of a battle
                        if bossChoice == "stats":
                            print "%s's Health: %s\n %s's Level: %s\n  %s's Damage: %s" % (
                            charName, player_health, charName, player_lvl, charName, player_damage)

                        # when player types 'flee' inside of a battle
                        if bossChoice == "flee":
                            battle = "False"
                            constant = "False"
                            print "\n%s ran away from the enemy!\n" % charName

                        # when player types 'help' inside of a battle
                        if bossChoice == "help":
                            print "\n['attack', 'block', 'evade', 'flee', 'stats', 'help', 'restart', 'quit']\n"

                        # when player types 'restart' inside of a battle
                        if bossChoice == "restart":
                            game = "restart"
                            print ""

                        # 'breaking' out of the loop
                        if game == "restart":
                            constant = "False"
                            battle = "restart"

                        # when player types 'quit' inside of a battle
                        if bossChoice == "quit":
                            constant = "False"
                            battle = "return"
                            print "See you next time!"

                else: print "Sorry, please come back when you've reached level 20!"

            if exploreChoice == "inventory":
                print player_inventory

            #when player types 'attack' outside of a battle
            if exploreChoice == "attack":
                print "%s swats at the air, looking quite stupid." % charName

            #when player types 'block' outside of a battle
            if exploreChoice == "block":
                print "\n%s appears defensive and looks quite stupid.\n" % charName

            # when player types 'evade' outside of a battle
            if exploreChoice == "evade":
                print "\n%s rolls around on the ground for no reason.\n" %charName

            # when player types 'stats' outside of a battle
            if exploreChoice == "stats":
                print "%s's Health: %s\n %s's Level: %s\n  %s's Damage: %s" % (charName, player_health, charName, player_lvl, charName, player_damage)

            # when player types 'flee' outside of a battle
            if exploreChoice == "flee":
                print "\n%s runs from nothing in particular.\n" % charName

            # when player types 'restart' outside of a battle
            if exploreChoice == "rest":
                player_health = player_health_max
                print "Health restored!"
                print "%s's Health: %s\n %s's Level: %s" % (charName, player_health, charName, player_lvl)

            # when player types 'help' outside of a battle
            if exploreChoice == "help":
                print "\n['explore', 'fight boss', 'inventory', 'attack', 'block', 'evade', 'flee', 'rest', 'stats', 'help', 'restart', 'quit']\n"

            # when player types 'restart' outside of a battle
            if exploreChoice == "restart":
                game = "restart"
                print ""

            #'breaking' out of loop
            if game == "restart":
                constant = "false"
                battle = "restart"
                print "Re-rollin' it like a boss.\n"

            # when player types 'quit' outside of a battle
            if exploreChoice == "quit":
                constant = "false"
                battle = "return"
                print "See you next time!"

        #console rebooting the file
        if battle == "restart":
            game = "restart"

        #console closing the file
        if battle == "return":
            game = "off"

        #commands while battling an enemy
        while battle == "True":
            constant = battle

            #randomize name between two names
            randomEName = randint(0, 1)

            #first possible 'eName'
            if randomEName == 0:
                eName = "A goblin"

            #second possible 'eName'
            if randomEName == 1:
                eName = "An angry dwarf"

            #prevents player from leaving/restarting the actual encounter/fight
            while constant == "True":
                battleChoice = raw_input("\n%s is present... What will you do?\n(Type 'help' for a list of commands.)\n > " % eName)

                # when player types 'attack' inside of a battle
                if battleChoice == "attack":
                    random_event_2 = randint(0, 1)
                    if random_event_2 == 0:
                        enemy_damage = int(player_damage) * .9
                        player_health = int(player_health) + int(enemy_damage)
                    if random_event_2 == 1:
                        enemy_damage = int(player_damage) * 1.1
                        player_health = int(player_health) + int(enemy_damage)
                    enemy_health = int(enemy_health) + int(player_damage)
                    if player_health > 0:
                        player_lvl = int(player_lvl) + 1
                        print "%s damages enemy!\n%s's Health: %s\n Enemy's Health: %s" % (charName, charName, player_health, enemy_health)
                        if enemy_health <= 0:
                            player_health_max = int(player_health_max) + int(player_health_max) *.15
                            print "Enemy has been vanquished!"
                            if player_lvl == 5:
                                print "\nLevel up bonus, %s recieved a Dagger!" % charName
                                player_inventory = str(player_inventory) + ", Dagger"
                            if player_lvl == 10:
                                print "\nLevel up bonus, %s recieved a Knife!" % charName
                                player_inventory = str(player_inventory) + ", Knife"
                            if player_lvl == 15:
                                print "\nLevel up bonus, %s recieved an Iron Dagger!" % charName
                                player_inventory = str(player_inventory) + ", Iron Dagger"
                            if player_lvl == 20:
                                print "\nLevel up bonus, %s recieved an Iron Sword!" % charName
                                player_inventory = str(player_inventory) + ", Iron Sword"
                            if player_lvl == 25:
                                print "\nLevel up bonus, %s recieved a Silver Xiphos!" % charName
                                player_inventory = str(player_inventory) + ", Silver Xiphos"
                            if player_lvl == 30:
                                print "\nLevel up bonus, %s recieved a Steel Sword!" % charName
                                player_inventory = str(player_inventory) + ", Steel Sword"
                            if player_lvl == 35:
                                print "\nLevel up bonus, %s recieved a Gnarly Schmitar!" % charName
                                player_inventory = str(player_inventory) + ", Gnarly Schmitar"
                            if player_lvl == 40:
                                print "\nLevel up bonus, %s recieved a Bastard Sword!" % charName
                                player_inventory = str(player_inventory) + ", Bastard Sword"
                            if player_lvl == 45:
                                print "\nLevel up bonus, %s recieved a Chrome-plated Rapier!" % charName
                                player_inventory = str(player_inventory) + ", Chrome-plated Rapier"
                            if player_lvl == 50:
                                print "\nLevel up bonus, %s recieved a Golden Rapier!" % charName
                                player_inventory = str(player_inventory) + ", Golden Rapier"
                            if player_lvl == 55:
                                print "\nLevel up bonus, %s recieved a Diamond-plated Rapier!" % charName
                                player_inventory = str(player_inventory) + ", Diamond-plated Rapier"
                            if player_lvl == 60:
                                print "\nLevel up bonus, %s recieved 'Marksman's Rifle'!" % charName
                                player_inventory = str(player_inventory) + ", Marksman's Rifle"

                            constant = "False"
                            battle = "False"
                    if player_health <= 0:
                        play_again = raw_input("\nGame over!\n\nWould you like to play again?\n(yes/no)\n > ")
                        if play_again == "yes":
                            constant = "False"
                            battle = "False"
                            game = "restart"
                        if play_again == "no":
                            game = "off"
                            system = "off"
                            constant = "False"
                            battle = "False"


                # when player types 'block' inside of a battle
                if battleChoice == "block":
                    print "\n%s bolsters their defenses and avoids damage!\n" % charName

                # when player types 'evade' inside of a battle
                if battleChoice == "evade":
                    print "\n%s rolls out of harm's way!\n" % charName

                # when player types 'stats' inside of a battle
                if battleChoice == "stats":
                    print "%s's Health: %s\n %s's Level: %s\n  %s's Damage: %s" % (charName, player_health, charName, player_lvl, charName, player_damage)

                # when player types 'flee' inside of a battle
                if battleChoice == "flee":
                    battle = "False"
                    constant = "False"
                    print "\n%s ran away from the enemy!\n" % charName

                # when player types 'help' inside of a battle
                if battleChoice == "help":
                    print "\n['attack', 'block', 'evade', 'flee', 'stats', 'help', 'restart', 'quit']\n"

                # when player types 'restart' inside of a battle
                if battleChoice == "restart":
                    game = "restart"
                    print ""

                #'breaking' out of the loop
                if game == "restart":
                    constant = "False"
                    battle = "restart"
                    print "Re-rollin' it like a boss.\n"

                # when player types 'quit' inside of a battle
                if battleChoice == "quit":
                    constant = "False"
                    battle = "return"
                    print "See you next time!"

        # loop from while battle == "False"
        if battle == "False":
            execfile("/Users/palihighcomputerclub/Desktop/Digital_Signals/helper.py")

        #console rebooting the file
        if battle == "restart":
            game = "restart"

        #console closing the file
        if battle == "return":
            game = "off"

    #ends all above 'whiles' and other such loops
    if game == "off":
        system = "off"

    # loop from the top
    if game == "restart":
        system = "off"
        execfile("/Users/palihighcomputerclub/Desktop/Digital_Signals/For_Game_Test.py")


################################################

#EXTRA COMMENTS HERE
#finish 'helper.py' by copying and pasting finished file into helper.py and getting rid of the charName raw_input and the note above it and the variables above that
#add music and gui