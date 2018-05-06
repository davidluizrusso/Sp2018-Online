# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:40:29 2018

@author: seelc
"""


'''Locke class, uses __enter__ and __exit__ methods to manage state of the Locke'''
class Locke:
    
    def __init__(self, capacity):
        self.capacity = capacity
    
       
    def __enter__(self):
        print("stopping pumps")
        print("opening the doors")
        print("closing the doors")
        print("restarting the pumps")

    
    #If I was working with opening + reading files I would ensure that
    #I was closing the file here, however in this example that isnt the case    
    def __exit__(self):
        print("stopping pumps")
        print("opening the doors")
        print("closing the doors")
        print("restarting the pumps")

    #Compares the boats moved to the Locke capacity to determine if the
    #boats can pass through
    def move_boats_through(self, boats):
        
        if boats > self.capacity:
            raise Exception("Not enough capacity")
        else:
            print("Moved boats succesfully")

 
#Used below code to test that outputs matched sample outputs       
small_locke = Locke(5)
large_locke = Locke(10)
boats = 8

#small_locke.move_boats_through(boats)
small_locke.__enter__()
small_locke.__exit__()


large_locke.move_boats_through(boats)




