import random
import time
dice_min = 1
dice_max = 6
roll_again = "y"
while  roll_again == "yes" or roll_again == "y":
    print("Rolling dice .. ")
    time.sleep(random.randint(dice_min, 4))
    print("Dice value : ")
    print(random.randint(dice_min, dice_max))
    roll_again = str(input("Enter y or yes to roll again: "))