#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 14:58:20 2018

@author: Will
"""
import time,os,sys

all_data = '/Users/Will/Documents/Engineering/Robot/RandomData.txt'
dis_log = '/Users/Will/Documents/Engineering/Robot/dis_log.txt'
hum_log = '/Users/Will/Documents/Engineering/Robot/hum_log.txt'
temp_log = '/Users/Will/Documents/Engineering/Robot/temp_log.txt'

f = open(all_data,'r')
d = open(dis_log,'w',1)
h = open(hum_log, 'w',1)
t = open(temp_log,'w',1)
section_size = 2

line_yield = 0

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

count = 0
def follow(file):
    global line_yield , count
    print(count)
    file.seek(0,2)
    while True:
        line = file.read(section_size)
        print(line)
        if(count>20):
           sys.exit()
        else:
            if not line :
                time.sleep(0.1)
                print('Waiting...')
                count += 1
                
            else:
                yield str(line)
                print(line)
                line_yield += 1
                count = 0
            
      

data = follow(f)   
loop_count = 0 
sorted_count = 0
alphaIdx = []
letter_list = []
InputFileSize = convert_bytes(os.stat(all_data).st_size) 
print('Input File Size: ' + str(InputFileSize))
while True:
    InputFileSize = convert_bytes(os.stat(all_data).st_size)        
    dataSection = next(data)
    #print('\n\n' + dataSection)
    loop_count += 1
    print('Loop number: ' + str(loop_count))
    print('Input File Size: ' + str(InputFileSize))
    #alphaIdx = [dataSection.index(ch) for ch in dataSection if ch.isalpha() ] #indexes of all letters in section
    for i in range(0, len(dataSection) - 1):
        if dataSection[i].isalpha():
            alphaIdx.append(i)
            
    #print('length of alphaIdx : ' + str(len(alphaIdx)))
    for i in alphaIdx:
        letter_list.append(dataSection[int(i)])
    #print(alphaIdx)   
    #print(letter_list)
    try:
        dataSection = dataSection[:alphaIdx[-1]+1] #clips anything after last letter 
     #   print('clipped : ' + str(dataSection))
        for i in range(0,len(alphaIdx)-1):
            if dataSection[alphaIdx[i]] == 'd':
                dis_data = dataSection[alphaIdx[i]+1:alphaIdx[i+1]]#slices section after letter and before next letter
                d.write(dis_data  + '\n')
                sorted_count += 1
            elif dataSection[alphaIdx[i]] == 'h':
                hum_data = dataSection[alphaIdx[i]+1:alphaIdx[i+1]]
                h.write(hum_data  + '\n')
                sorted_count += 1
            elif dataSection[alphaIdx[i]] == 't':
                temp_data = dataSection[alphaIdx[i]+1:alphaIdx[i+1]]
                t.write(temp_data  + '\n')
                sorted_count += 1
        print('numbers sorted: ' + str(sorted_count))
        letter_list = []
        alphaIdx = []
        sorted_count = 0
    except IndexError:
        print('\n\n**********\nFile sorted\n**********')
        exit()
            

