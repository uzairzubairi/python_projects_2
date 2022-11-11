#!/usr/bin/env python3
import string

def convert_to_feet(p_entered_miles):     #converts the p_entered_miles to feet, converts it to int, then returns it
    result=5280*p_entered_miles
    result_int=int(result)
    return result_int

def main():
    print("Hike Calculator")
    entered_miles=float(input("How many miles did you walk:\t"))  #user inputs the number of miles
    result_in_feet=convert_to_feet(entered_miles)        #call the function convert_to_feet to convert the above number to feet
    print(f"You walked {result_in_feet} feet.")         #print the result

if __name__ == "__main__":
    main()