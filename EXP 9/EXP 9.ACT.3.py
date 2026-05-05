# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:48:32 2026

@author: indrajeet
"""

import random
import string

def generate_otp(length=6):
   
    characters = string.digits
   
    otp = ''.join(random.choice(characters) for _ in range(length))
   
    return otp

new_otp = generate_otp(6)

print("--- Secure Authentication ---")
print(f"Your mobile verification code is: {new_otp}")
print("This code expires in 5 minutes.")
