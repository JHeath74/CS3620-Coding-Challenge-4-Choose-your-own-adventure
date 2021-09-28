from Hero import Hero
from Colors import Colors


class Reward:
    Hero = Hero()

    def Reward(self):
        if Hero.virtue < 10:
            moves = str(Hero.moves)
            virtue = str(Hero.virtue)

            reward = open("Reward.txt", "w")
            reward.write("With a virtue of " + Colors.RED + virtue + Colors.Reset + " you will go home in shame, " +
                         "never being the adventurer we all hoped you would be.\n " +
                         "Learn from your time in our lands and strive for excellence.\n" +
                         "You completed your adventure in " + Colors.BLUE + moves + Colors.Reset + " moves")
            reward = open("Reward.txt", "r")
            print(reward.read())
            reward.close()
            # -------------------------------------------------------------------------------------------------------------------------------
            reward.close()
        if 10 < Hero.virtue < 20:
            reward = open("Reward.txt", "w")
            reward.write(
                "With a virtue of " + Hero.virtue +
                "you have worked hard but have learned very little.\n" +
                " But we see you are full of promise and hope to see you "
                "continue to grow.  You completed your adventure in " + Hero.moves + " moves")
            reward = open("Reward.txt", "r")
            print(reward.read())
            reward.close()
            # -------------------------------------------------------------------------------------------------------------------------------
            if 20 < Hero.virtue < 30:
                reward = open("Reward.txt", "w")
                reward.write(
                    "With a virtue of " + Hero.virtue + " you have worked hard to " +
                    "set example \nfor us to follow but still have much to learn. " +
                    " You completed your adventure in " + Hero.moves + " moves")
                reward = open("Reward.txt", "r")
                print(reward.read())
                reward.close()
            # -------------------------------------------------------------------------------------------------------------------------------
            if 30 < Hero.virtue < 40:
                reward = open("Reward.txt", "w")
                reward.write(
                    "With a virtue of " + Hero.virtue + " you have " +
                    "worked hard and have accomplished much" +
                    " you have taught us much\n" +
                    " You completed your adventure in " + Hero.moves + " moves")
                reward = open("Reward.txt", "r")
                print(reward.read())
                reward.close()
            # -------------------------------------------------------------------------------------------------------------------------------
            if 40 < Hero.virtue <= 50:
                reward = open("Reward.txt", "w")
                reward.write(
                    "With a virtue of " + Hero.virtue + " you truly are a man of virtue " +
                    "and an inspiration to all of us you are loved by all and always welcome here." +
                    " You completed your adventure in " + Hero.moves + " moves")
                reward = open("Reward.txt", "r")
                print(reward.read())
                reward.close()
