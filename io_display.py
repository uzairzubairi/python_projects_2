#!/usr/bin/env python3
import string
"""
io_display module has two functions, inputter and outputter. The inputter recieves input from the user and outputter displays
calcaulated taxes and total amount back to the user
"""
def inputter():
    print("ENTER ITEMS (ENTER 0 TO END)")
    total=0.00
    will_continue=True
    while will_continue == True:
        item_price=float(input("Cost of the item:\t"))
        if item_price>0.00:
            will_continue=True
        else:
            will_continue=False
        total+=item_price
    return total

def outputter(total, tax_amt, tot_aft_tax):
    print(f"Total:\t\t{total}")
    print(f"Tax amount:\t\t{tax_amt}")
    print(f"Total after tax:\t{tot_aft_tax}")

