#!/usr/bin/env python3
import string
import io_display
import taxes


def main():
   print("Tax Calculator\n")
   will_continue="y"

   while will_continue == "y" or will_continue== "Y":       #While loop to repeat the code over and over till the user wants to stop
    total=io_display.inputter()                             #call inputter to recieve prices from the user
    tax_amount=taxes.tax_calculator(total)                  #call tax calculator to calculate the tax amount
    total_after_tax=taxes.total_after_tax_calculator(total, tax_amount)     #this function will calculate the total after tax
    io_display.outputter(total, tax_amount, total_after_tax)            #this function will display the calculated amounts to the user
    will_continue=input("Again? (y/n)\t")                               #ask if the user is done, or would like to repeat the process
   
   print("Thanks, bye!")

if __name__ == "__main__":
    main()