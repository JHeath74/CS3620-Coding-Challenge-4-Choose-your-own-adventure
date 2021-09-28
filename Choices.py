from Battles import Battles
from EndBattle import EndBattle
from Cast import Cast
from Colors import Colors
from Hero import Hero
from Locations import Locations
from Monsters import Monsters
from Reward import Reward

Reward = Reward()
answer = ""
cities = ""


class Choices:
    # ------------------------One of two final battles possible outcomes------------------------------------------------
    def endBattleLordBritish(self):
        print(Colors.BLUE + Cast.King + "After all I've done for you,  I can't believe you would do this to " +
              "me, my friends or your kingdom\n")
        print("We will not stand for this,  prepare to defend yourself.")

        input("Press Enter when Ready to Fight")
        EndBattle.fightlordbritish()

    # ------------------------One of two final battles possible outcomes------------------------------------------------
    def endBattleLordBlackthorne(self):
        print(Colors.BLUE + Hero.name + Colors.Reset + " and " + Colors.CYAN + Hero.friend2 + Colors.Reset)
        print("Rush to " + Colors.LIGHT_RED + Locations.Lord_BlackThornsCastle + Colors.Reset + " you fight your way "+
              "to the throne room to find " + Cast.MainBadGuy)
        print("You shout out 'After everything you did to kill me,  I am still alive.'\n")
        print("With everything I've seen and done,  nothing you do will stop me and my two friends from stopping " +
              "you!!\n")
        input("Press Enter When Ready to Fight")
        EndBattle.fightlordblackthorne()

    # ------------------------------------------------------------------------------------------------------------------
    def skaraBraeChoice10(self):  # ----- For the king --- Need to finish after Buc's Den
        print("As you " + Colors.CYAN + Hero.friend1 + Colors.Reset + "enter the town of " + Locations.Skae_Brae +
              "you remember why it's also known as the town of the dead.\n")
        print("No living people,  only the dead having who have no place else to go")
        print("You see " + Colors.GREEN + Hero.friend2 + Colors.Reset + "waiting for you as you get closer.  They shout"
              + "'Hail,  it is good to see you two again'.  And you both reply 'To you as well.")
        print(" We need to enter and find the Jeweller,  once we get the name of the who was recieving " +
              "the package and who murdered him and why,  maybe we can find out who is responsible for the whole thing")
        print("So,  we travel through out " + Colors.BLINK + Locations.Skae_Brae + Colors.Reset + " doing the best " +
              "we can to talk to the dead inhabitants of this town.  When we finally find the Jeweller")
        print("Having recently died,  he was more than anxious to discuss what happened")
        input("Press Enter to Continue")
        print("I was delivering a package of medallions for " + Colors.BROWN + Cast.BadGroup + Colors.Reset +
              "While I was there one late night,  I overheard a conversation between two people, that I wasn't " +
              "suppose to hear\n ")
        print("They were talking about overthrowing " + Colors.CYAN + Cast.King + Colors.Reset + "I tried to hurry " +
              "away,  but was caught.")
        print("It was then that I was taken out of the city and was murdered.")
        print(Colors.BLUE + Hero.friend2 + Colors.Reset + ", please tell us whom you overheard talking?")
        print("The Jeweller said it was " + Colors.RED + Cast.Jester + Colors.Reset + " and " + Colors.YELLOW +
              Cast.MainBadGuy + Colors.Reset + ".  They plan to kill the king.")
        input("Please Press enter to Continue")
        print(Colors.LIGHT_RED + Hero.friend1 + Colors.Reset + ", quick make for " + Colors.CYAN + Locations.Britain +
              Colors.Reset + " and save " + Colors.LIGHT_BLUE + Cast.King + Colors.Reset + " while the two of us "+
              "make for " + Colors.YELLOW + Locations.Lord_BlackThornsCastle + Colors.Reset + "to stop " +
              Colors.BROWN + Cast.MainBadGuy + Colors.Reset)
        Hero.moves += 1
        Hero.virtue += 10
        self.endBattleLordBlackthorne(self)

    # -----------------------------------------------------------------------------------------------------------------
    def pawsChoice10(self):  # ----- For the Lord BlackThorne
        print("To be Continued in the town of Paws")

    # ------------------------------------------------------------------------------------------------------------------
    def empvilleChoice7(self):  # ----- For the Lord BlackThorne
        print("To be Continued in the town of Empville")

    # ------------------------------------------------------------------------------------------------------------------
    def bucDenChoice8(self):  # ----- For the Lord British
        print("After you pull your attacker up " + Colors.GREEN + Hero.friend1 + Colors.Reset + " comes running up" +
              " to help.\n")
        print("I just caught the tail end of your little wrestling match.  Let's interrogate my attacker and find" +
              " out who he is and where the necklace comes from?")
        print("As the three of you talk,  your prisoner is not forth coming with information." +
              "  All you find out is the medallion is made by a jeweller in " + Colors.CYAN + Locations.Buccaneers_Den +
              Colors.Reset + ".  " + Colors.BROWN + Hero.friend1 + Colors.Reset + " well it's a good thing we are" +
              " are on our way there.")
        input("Press Enter to Continue")
        print("After 3 more days of travelling, you finally arrive in " + Colors.BROWN + Locations.Buccaneers_Den +
              Colors.Reset + " and quickly leave your boat.")
        print("You are able to quickly find the jeweller,  but the store is closed. You both wonder where he is " +
              "You talk to a kindly old lady near the story and are able to discover that the jeweller was murdered" +
              " recently on a trip to \n" +
              Colors.YELLOW + Locations.Trinsic + Colors.Reset + ".  You ask what he was doing in Trinsic, " +
              " He was making a large delivery,  but of what we don't know.")
        print("So,  this was a dead end?  Not exactly the kind old lady tells you.  Because of his life, and how he " +
              " died,  his spirit would be in " + Colors.YELLOW + Locations.Skae_Brae + Colors.Reset)
        print("Thank you for your help,  as you walk away you tell " + Colors.YELLOW + Hero.friend1 + Colors.Reset +
              "Now, we need to contact " + Colors.CYAN + Hero.friend2 + Colors.Reset + "who is waiting at " +
              Colors.RED + Locations.The_Dungeon_Destard + Colors.Reset + " to meet us just outside of " +
              Colors.LIGHT_BLUE + Locations.Skae_Brae + Colors.Reset + "and get some answers.")
        Hero.moves += 1
        Hero.virtue += 1
        self.skaraBraeChoice10(self)

    # -----------------------------------------------------------------------------------------------------------------
    def dropOverboardChoice9(self):  # ----- For the Lord British
        print("After your attacker falls into the ocean,  your seen by a few crew members that just came on desk." +
              "They shout, 'Hey, what are you doing?  Why did you throw him overboard\n")
        print("Assuming you to be a robber,  they crew members take you before the captain and announce what " +
              "you've done.\n" + "When you get before the captain,  he asks for your name?  My Name is "
              + Colors.CYAN + Hero.virtue + Colors.Reset + " and I am here in the name of "
              + Colors.BROWN + Cast.King + Colors.Reset + " I demand you release me.\n")
        print("We all know who you are and what you've done for our lands,  but these are perilous times and crimes "
              + "must be punished quickly for we do not take murder lightly.\n")
        print("Throw him overboard, the Captain yells!  You are then lost into the seas, never to return")
        print("Better Luck Next Time")
        Reward.Reward(self)

    # ------------------------------------------------------------------------------------------------------------------

    def destardChoice5(self):  # ----- For the king
        print("As you arrive at the entrance of " + Colors.CYAN + Locations.The_Dungeon_Destard + Colors.Reset +
              "you see your friend " + Colors.LIGHT_PURPLE + Hero.friend1 + Colors.Reset + ".\n" +
              "You ask " + Colors.LIGHT_PURPLE + Hero.friend2 + Colors.Reset + "why the King believes what they seek" +
              " is here,  your friend responds.  The king didn't say only that we need to take a look.\n" +
              "So you enter the dark dungeon and spend time looking around, seeing on scrapes walls and floor,  makes" +
              " you both nervous,  but it's important that you keep searching.\n" +
              "Just before you walk into a large chamber, " + Colors.BLUE + Hero.friend2 + Colors.Reset +
              "this place isn't safe and says they they will wait here. \n")

        input("Press Enter to Continue")

        print(" As you walk in the door, your way behind you collapses.  You feel and hear the sound " +
              "of a hot flame and see a " + Colors.GREEN + Cast.GiantDragon + Colors.Reset + " enter the room.\n" +
              "with no way out except for behind the dragon or back through the collapsed doorway," +
              "  your prepare to fight.")

        Battles.fightGiantDragon(self)

    # --------------------------------------------------------------------------------------------------------------------
    def bucDenChoice6(self):  # ----- For the king
        print(Colors.BLUE + Locations.Buccaneers_Den + Colors.Reset + " is on an island so we must find a boat "
                                                                      "to take us there.\n")
        print(Colors.BLUE + Hero.friend2 + Colors.Reset + " there is a port in " + Colors.CYAN + Locations.Trinsic +
              Colors.Reset + " with a boat that will get us to " + Locations.Buccaneers_Den + "\n")
        print("When you arrive at " + Colors.YELLOW + Locations.Trinsic + Colors.Reset +
              "you first head to the docks to buy passage on a ship\n")
        print("As you walk to the docks,  an individual follows you to the docks trying not to be noticed." +
              "He purchases a ticket and follow you on to the boat.\n")
        print("After the boat gets underway " + Colors.YELLOW + Hero.friend2 + Colors.Reset + "turns to you and says" +
              " while it's not a long trip to " + Colors.BLUE + Locations.Buccaneers_Den + Colors.Reset +
              "this time of year, storms tend to arise, and the seas can be rough,  let's just hope that" +
              " nothing happens along the way\n")
        input("Press Enter to Continue")
        print("Later that day,  you go to walk the deck.\n" +
              "While standing looking out over the water, someone suddenly rushes you trying to " +
              "throw you overboard.\n")
        print("After a brief but intense struggle,  your push her attacker up against the railing, over the water " +
              " while holding him over the water,  you take his medallion around his neck\n" +
              "asking him 'Where did you get this from?'.  He yells in response, ' We won't let you stop us!' " +
              "we'll kill you if we have too\n")
        fellowshipResponse = input("Do you " + Colors.RED + "drop" + Colors.Reset + "your attacker from the boat"
                                                                                    "or " + Colors.RED + "bring " + Colors.Reset + " him for further questioning?")
        Hero.moves += 1

        fellowshipResponse.lower()

        if fellowshipResponse == "drop":
            Hero.virtue -= 1
            self.dropOverboardChoice9()
        if fellowshipResponse == "bring":
            Hero.virtue += 1
            self.bucDenChoice8()

    # --------------------------------------------------------------------------------------------------------------------
    def friendsChoice4(self):
        print("I am sorry,  I wish I could go with you.  However, I must continue on to the Capital town of " +
              Colors.BLUE + Locations.Britain + Colors.Reset + "\nI have been summoned by my friends to appear" +
              " before " + Cast.King + " I must hurry." + "You say your good byes and leave for the distance" +
              " is great.\n")
        print("You arrive quickly in " + Colors.BLUE + Locations.Britain + Colors.Reset + "  and appear before " +
              "the king\n" + "Thank you for appearing so quickly " + Colors.BLUE + Hero.name + Colors.Reset +
              "The Kingdom of " + Colors.CYAN + Locations.Britannia + Colors.Reset + "and it's people need your help.\n"
              + "There is a an unknown group that is begun to undermine the kingdom,  we need to find " +
              "them and stop them.\n" + " We believe they are working out of the locations of " +
              Colors.LIGHT_CYAN + Locations.The_Dungeon_Destard + Colors.Reset + " or " + Colors.LIGHT_CYAN +
              Locations.Buccaneers_Den + Colors.Reset + " Your friends each went to one of the cities,\n  meet" +
              " them and see what you can find\n")
        print("As you walk out of the throne room, you hear " + Colors.BLINK + Cast.Jester + Colors.Reset +
              "runs up to you cackling saying 'You'll be lucky to make it back alive!\n")
        cities = input("\nShould you go to the Dungeon " + Colors.LIGHT_CYAN + "Destard" + Colors.Reset +
                       " or " + Colors.LIGHT_CYAN + "Buccaneers Den" + Colors.Reset + "?")
        cities.lower()
        Hero.moves += 1
        # ----- For the king
        if cities == "destard":
            self.destardChoice5()
            Hero.virtue -= 1
        elif cities == "buccaneers den":
            Hero.virtue += 1
            self.bucDenChoice6()

    # --------------------------------------------------------------------------------------------------------------------
    def goChoice3(self):
        print(
            "I appreciate you saving my life,  while I should be going to see "
            + Colors.BLUE + Cast.King + Colors.Reset + " it wouldn't hurt to see how things" +
            " have changed while I've been gone.\n" + "Please lead the way to " + Colors.LIGHT_PURPLE +
            Locations.Trinsic + Colors.Reset + " and let me here what you have to say.")
        print("After a quick journey to " + Colors.LIGHT_PURPLE + Locations.Trinsic + Colors.Reset +
              "You travel to their Fellowship hall and meet with \n " + Colors.CYAN + Cast.MainBadGuy +
              Colors.Reset + " The leader of the " + Colors.LIGHT_PURPLE + Cast.BadGroup + Colors.Reset +
              "After talking you ask You ask what you can do to to help? " + "We need you to visit either "
              + Colors.LIGHT_CYAN + Locations.Paws + Colors.Reset + " or "
              + Colors.LIGHT_PURPLE + Locations.Empville + Colors.Reset)

        location = input("Do you wish to travel to " + Colors.RED + "Paws" + Colors.Reset +
                         " or " + Colors.RED + " Empville " + Colors.Reset)
        location.lower()
        Hero.moves += 1

        if location == "paws":
            Hero.virtue -= 1
            self.pawsChoice10()

        elif location == "empville":
            Hero.virtue += 1
            self.empvilleChoice7()

    # --------------------------------------------------------------------------------------------------------------------
    def initGame(self):
        Hero.hero = input("Please Enter your Name for this adventure: ")
        Hero.friend1 = input("Enter a friends name: ")
        Hero.friend2 = input("Enter another friends name: ")
        print("\n")

        print("You wake up to a bright light outside your window.\n "
              "You get out of bed,  get dressed and go outside\n"
              " to see if it's what you expected.As you enter your yard, \n"
              " you see if a bright portal before you. You hear the sound of your\n"
              "friends " + Colors.CYAN + Hero.friend1 + Colors.Reset + " and " + Colors.CYAN + Hero.friend2 +
              Colors.Reset + " asking you to enter and find them and help " + Colors.BLUE + Cast.King + Colors.Reset +
              ". Wondering if you should enter \n" +
              "and  wondering what adventure awaits you? So you enter the Moongate and vanish.\n")

        print("\n")
        print("After entering the Moongate, You instantly come under" +
              " attack by a " + Colors.RED + "" + Monsters.Gargoyle + "" + Colors.Reset + ". " +
              "You look, down and see a broken sword at your feet\n")

        response1 = input("Do you grab the sword to " + Colors.LIGHT_RED + "defend " + Colors.Reset +
                          "yourself or try and " + Colors.BLUE + "run" + Colors.Reset + " away?\n")

        Hero.moves += 1
        response1.lower()

        if response1 == "defend":
            Hero.virtue += 1
            self.defendChoice1()
        if response1 == "run":
            Hero.virtue -= 1
            self.runChoice2()

    # --------------------------------------------------------------------------------------------------------------------
    def runChoice2(self):

        print("\n")
        print("You get up to run, but slip on the mud and fall and realize you can't get away" +
              " from the " + Colors.RED + "" + Monsters.GiantGargoyle + "" + Colors.Reset + " you sadly die.\n")

        Hero.moves += 1
        Reward.Reward()

    # --------------------------------------------------------------------------------------------------------------------
    def defendChoice1(self):
        print("You grab the sword at your feet and parries the blow from the " +
              Colors.RED + "" + Monsters.GiantGargoyle + "" + Colors.Reset + " after a few minutes" +
              " of battle you are final able to defeat your attacker.\n"
              "You hear a sound and when you look up, you see three " + Colors.RED + Monsters.Headless
              + Colors.Reset + " creatures running at you. Not sure if you will survive this attack\n" +
              "As " + Colors.BLUE + Hero.name + Colors.Reset + "you raise your sword to defend yourself" +
              " You hear a voice that shouts at the " + Colors.RED + Monsters.Headless + Colors.Reset +
              "\nPrepare to Die! You see two people running toward you\n, and in short order your attackers are " +
              "gone.\n")
        print("\n")
        print("Your two defenders introduce themselves as " + Colors.LIGHT_RED + Cast.BadGuy2 + Colors.Reset +
              " and " + Colors.LIGHT_RED + Cast.BadGuy3 + Colors.Reset + " We belong to "
              + Colors.RED + Cast.BadGroup + Colors.Reset + " \n We help the poor and others in need," +
              "  why don't you come with us to our fellowship hall in " + Colors.LIGHT_GREEN + Locations.Trinsic +
              Colors.Reset + " and learn more about what we do?")

        answer = input(
            "Do you " + Colors.CYAN + "Go" + Colors.Reset + "with your defenders or " + Colors.CYAN + "Continue "
            + Colors.Reset + "to your friends?")

        answer.lower()
        Hero.moves += 1

        if answer == "go":
            Hero.virtue -= 1
            Choices.goChoice3(self)
        elif answer == "continue":
            Hero.virtue += 1
            Choices.friendsChoice4(self)
    # --------------------------------------------------------------------------------------------------------------------
