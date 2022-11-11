#!/usr/bin/env python3
import string

"""
Converter can be used to convert feet to meters and meters to feet.
"""

def feet_to_meters(feet=1.00):
    meters = feet * 0.3048
    return meters

def meters_to_feet(meters=1.00):
    feet = meters / 0.3048
    return feet