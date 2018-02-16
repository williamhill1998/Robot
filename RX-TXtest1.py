# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 18:37:12 2018

@author: Will

Program to switch between tx and rx:
        *We need to send keypresses(done)
        *and recieve data.(done)
            *This data needs to be sorted an written to appropriate log files
            *This data needs to be signed by the sensor type
        * The switching mechanism will be to recieve when the keypress hasnt changed
"""

import keyboard, serial ,threading,time 

file = 'D:\Documents\Programs\IncomingData'
f = open(file,'w')
key_list = ['w','a','s','d']
timeout = 100
ser = 0
current_inst = 'x'
current_key = 'x'

class write_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.paused = False
        self.pause_cond = threading.Condition(threading.Lock())

    def run(self):
        while True:
            with self.pause_cond:
                while self.paused:
                    self.pause_cond.wait()

                #thread should do the thing if
                #not paused
                write_data()
            time.sleep(0.001)

    def pause(self):
        self.paused = True
        self.pause_cond.acquire()

    def resume(self):
        self.paused = False
        self.pause_cond.notify()
        self.pause_cond.release()
        
def init_serial():
    global ser
    ser = serial.Serial('COM4')
    ser.baudrate = 9600
    ser.timeout=1
    
    if ser.isOpen():
        print('Open: ' + ser.portstr)
    else:
        ser.open()

def write_check(encoded_inst):
    
    global current_inst
    if encoded_inst != current_inst: #only send key if it has changed or is stop
        data_write.pause()
        ser.write(encoded_inst)
    current_inst = encoded_inst   
    data_write.resume()    
    
    
def print_check(key):
    
    global current_key
    
    if key != current_key:
        print(key)
    current_key = key


def write_data():
    f.write(ser.read(),'w',2)

    
init_serial()
ser.write('\n\nConnection established...'.encode())
data_write = write_thread()
data_write.start()

for key in key_list:
    keyboard.add_hotkey(key,print_check,args=[key],timeout=timeout)
    keyboard.add_hotkey(key,print_check,args=['stop'],timeout=timeout,trigger_on_release = True)
    keyboard.add_hotkey(key,write_check,args=[key.encode()],timeout=timeout)
    keyboard.add_hotkey(key,write_check,args=['1'.encode()],trigger_on_release = True)
