#!/usr/bin/env python3
import string
import converter

def display_title():
    print("Feet and Meters converter\n\n")

def display_menu():
    print("Conversions Menu")
    print("a. Feet to Meters")
    print("b. Meters to feet")
    chosen=input("Pick an option (a/b):\t")
    return chosen


def main():
    display_title()                         #calls the display title function
    repeat="y"

    while repeat == "y" or repeat == "Y":   #while loop to repeat the whole process over and over till the user selects not to continue
        chosen_opt=display_menu()               #calls the dispaly_menu function to display the menu and save the user's choice in a var
        if chosen_opt=="a":                     #if the user chose to convert feet to meters, the feet_to_meters function will be called and the result will be displayed
            result=converter.feet_to_meters(float(input("Enter feet:\t")))
            result=round(result,2)              #rounds the result to two decimal places
            print(f"{result} meters")
        elif chosen_opt=="b":   #if the user chose to convert meters to feet, then the meters to feet function will be called and the result will shown to the user
            result=converter.meters_to_feet(float(input("Enter meters:\t")))
            result=round(result,2)      #rounds the result to two decimal places
            print(f"{result} feet")
        repeat=input("Continue? (y/n): \t")
    print("Thanks, bye!")
   
if __name__ == "__main__":
    main()