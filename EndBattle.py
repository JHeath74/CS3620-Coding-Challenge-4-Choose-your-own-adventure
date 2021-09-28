from Cast import Cast
from Reward import Reward
from Colors import Colors
from Hero import Hero

import random


class EndBattle:

    def fightlordbritish(self):

        LordBritish = random.randint(0, 6)
        Hero = random.randint(0, 6)

        LordBritish = int(LordBritish)
        Hero = int(Hero)

        while Hero.virtue > 0 or Cast.LordBritishHP > 0:

            if Hero > LordBritish:
                Cast.LordBritishHP = Cast.LordBritishHP - (Hero - LordBritish)
                print(Cast.King + " Hit Points: " + Cast.LordBritishHP + " " + Hero.name + " Hit Points: " +
                      Hero.virtue)
            elif LordBritish > Hero:
                Hero.virtue = Hero.virtue - (LordBritish - Hero)
                print(Cast.King + " Hit Points: " + Cast.LordBritishHP + " " + Hero.name + " Hit Points: " +
                      Hero.virtue)

        if Hero.virtue < 1:
            print("I am sorry,  but you have lost. But evil shall not triumph ")
            Reward.Reward(Hero.virtue)
        elif Cast.LordBritishHP < 1:
            print("You've won,  but at what cost to yourself?")
            Reward.Reward(Hero.virtue)

    def fightlordblackthorne(self):

        LordBlackthorne = random.randint(0, 6)
        Hero = random.randint(0, 6)

        LordBlackthorne = int(LordBlackthorne)
        Hero = int(Hero)

        while Hero.virtue > 0 or Cast.LordBritishHP > 0:

            if Hero > LordBlackthorne:
                Cast.LordBlackthorneHP = Cast.LordBlackthorneHP - (Hero - LordBlackthorne)
            elif LordBlackthorne > Hero:
                Hero.virtue = Hero.virtue - (LordBlackthorne - Hero)

        if Hero.virtue < 1:
            print("I am sorry,  but you have lost. But" + Colors.BROWN + Cast.MainBadGuy + Colors.Reset +
                  "evil shall not triumph ")
            Hero.virtue = 25
            Reward.Reward(self)
        elif Cast.LordBlackthorneHP < 1:
            print("You've won,  You've beaten " + Colors.BROWN + Cast.MainBadGuy + Colors.Reset +
                  "the people seeing his evil appreciate your efforts")
            Hero.virtue = 25
            Reward.Reward(self)
