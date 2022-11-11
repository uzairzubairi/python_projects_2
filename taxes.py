#!/usr/bin/env python3
import string
TAX_RATE=0.06

def tax_calculator(total_amt):
    tax_amount=total_amt*TAX_RATE
    return tax_amount

def total_after_tax_calculator(total_amt, tax_amt):
    total_after_tax=total_amt+tax_amt
    return total_after_tax