#!/usr/bin/env python3
import string

def checker(p_entered_num):          #this function checks if the p_entered_num is odd or even, using the modulus function
    result=""                           #the variable to store the check's result
    if p_entered_num%2 == 0:                #checks if theres a remainder or not, if there is, its an odd number, otherwise its even
        result="The number is even."
    else:
        result="This is an odd number."
    return result                          #returns the result


def main():
    print("Odd or Even Checker")
    entered_num=int(input("Enter an integer:\t"))   #asks the user to input a number
    check_result=checker(entered_num)                #calls the check function and passes to it entered_num to check if its even or odd
    print(check_result)                             #prints the saved result from the checker function

if __name__ == "__main__":
    main()