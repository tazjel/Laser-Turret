#!/usr/bin/env python
# coding: utf8
from gluon import *
import serial

class SerialDev():
    def __init__(self, device,baud):
        self.device = device
        self.baud = baud
        self.ser = serial.Serial(self.device,baud)
        self.ser.timeout = 0.01
        if (self.ser.isOpen()): 
            self.last_received = self.ser.readline()
        else: self.last_received = None
        
    def sendCmd(self,command):
        if (self.ser.isOpen()):
            self.ser.write(command)#+'\r')
            return self.ser.readline()
        else: return None
