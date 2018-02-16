#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:38:39 2018

@author: Will

This program is to plot the graphs in real time by taking the data from the updating log list
and using matplotlib to extend and display the graph.
"""
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


data_log_file = '' 

def follow(file):
    file.seek(0,2)  #goes to the end of the file
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
        else:
            yield line
            
            
dataLog = open(data_log_file) 
data = follow(dataLog) # creates generator object, iterating through this pops the last distance 

style.use('fivethirtyeight')

fig = plt.figure() #like MATLABs figure creator 
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    xs = []
    ys = []
    x = 1 
    for dt in data:
            xs.append(x)
            ys.append(dt)
            x += 1
    ax1.clear()
    ax1.plot(xs, ys)
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()