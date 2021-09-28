from Colors import Colors
from Monsters import Monsters
from Cast import Cast
from Hero import Hero
from Choices import Choices


class main:
    Color = Colors()
    Monsters = Monsters()
    Cast = Cast()
    Choices = Choices()
    Hero = Hero()

    menu = input("What do you wish to do, My Lord?\n"
                 + Colors.RED + "Play " + Colors.Reset + "Game\n"
                 + "View " + Colors.YELLOW + "Help " + Colors.Reset + "Files\n"
                 + Colors.BLUE + "Exit " + Colors.Reset + "Game\n"
                 + "What Do You Wish To Do?:")
    menu = str(menu)
    menu.lower()

    def exitProgram(self):
        exit(0)

    def helpfiles(self):
        print("When making a choice after being asked.  The correct word or words are listed in a "
              "different color. Make sure to enter them as input exactly as shown")

    menuDict = {
        "play": Choices.initGame(),
        # "help": helpfiles(),
        # "exit": exitProgram(),
    }

    if menu == "play":
        print("Play")
        menuDict["play"]
    # elif menu == "help":
    #     print("help")
    #     menuDict["help"]
    # elif menu == "exit":
    #     print("exit")
    #     menuDict["exit"]
