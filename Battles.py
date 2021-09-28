from Hero import Hero
from Cast import Cast
from Reward import Reward
from Colors import Colors
import random
import time


class Battles:
    Hero = Hero()

    def fightGiantDragon(self):
        GiantDragon = random.randint(0, 15)
        Hero = random.randint(0, 6)

        while int(Hero.virtue) > 0 or int(Cast.GiantDragonHP) > 0:

            if Hero > GiantDragon:
                Cast.LordBritishHP = Cast.GiantDragonHP - (Hero - GiantDragon)
                print(Cast.GiantDragon + " Hit Points: " + Hero.virtue + " " + Hero.name + " Hit Points: " +
                      Hero.virtue)
            elif GiantDragon > Hero:
                Hero.virtue = Hero.virtue - (GiantDragon - Hero)
                print(Cast.GiantDragon + " Hit Points: " + Hero.virtue + " " + Hero.name + " Hit Points: " +
                      Hero.virtue)

        if Hero.virtue < 1:
            print("I am sorry,  " + Colors.BLINK + Colors.BackgroundBrightGreen + Colors.LIGHT_RED +
                  "You Died!" + Colors.Reset + "Did you really expect to beat a dragon?")
            time.sleep(5)
            Hero.virtue == 15
            Reward.Reward(Hero.virtue)
        elif Cast.GiantDragonHP < 1:
            print("You've won! Still not sure how you did it.")
            time.sleep(5)
            Hero.virtue == 20
            Reward.Reward(Hero.virtue)
