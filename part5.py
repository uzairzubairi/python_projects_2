#!/usr/bin/env python3
import string
import random

def dice_roller():
    num=random.randint(1,6)
    return num

def main():
   print("Dice Roller\n")
   roll_dice_yn=input("Roll the dice? (y/n)\t")

   while roll_dice_yn == "y" or roll_dice_yn== "Y":       #While loop to repeat the code over and over till the user wants to stop
     val_1=dice_roller()                                    #call the dice roller function two times to get 2 values
     val_2=dice_roller()
     total=val_2+val_1                                      #calculate the sum
     print(f"Die 1: {val_1}")
     print(f"Die 2: {val_2}")
     print(f"Total: {total}")
     if val_1 == 1 and val_2 == 1:                          #if both are 1, print snake eyes
        print(f"snake eyes!")
     elif val_1 == 6 and val_2 == 6:                        #if both are 6, print boxcars
        print(f"boxcars!")

     roll_dice_yn=input("Roll the dice? (y/n)\t")                               #ask if the user is done, or would like to roll again
   
   print("Thanks, bye!")

if __name__ == "__main__":
    main()