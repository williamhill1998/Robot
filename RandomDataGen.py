#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 17:08:15 2018

@author: Will
"""
from random import randint
from time import sleep
data_log_file = '/Users/Will/Documents/Robot/RandomData.txt' 
with open(data_log_file,'a') as log:
    while True:
        log.write('d')
        log.write(str(randint(0,100)))
        log.write('h')
        log.write(str(randint(0,100)))
        log.write('t')
        log.write(str(randint(0,100)))
        sleep(1)
    

