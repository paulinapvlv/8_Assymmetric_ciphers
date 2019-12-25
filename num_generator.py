# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 21:13:14 2019

@author: polin
"""

import random 

def mod_num(g,p,n):
    return (g^n) % p

def big_prime_num(lower_bound=10e+10,upper_bound=10e+50):
    num=int()
    while not is_prime(num):
        num=random.randint(lower_bound,upper_bound)
    return num
    
def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True