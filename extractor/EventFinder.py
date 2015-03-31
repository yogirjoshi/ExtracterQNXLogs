'''
Created on Jan 27, 2015

@author: y2joshi
'''

class ThreadFinder:
    '''
    classdocs
    '''

    
    def __init__(self):
        '''
        Constructor
        '''
    def getEvents(self):
#         return ["THCREATE", "THREADY", "THRUNNING", "THREPLY"]     
        return ["THCREATE", "THRUNNING", "THREPLY", "THREADY", "THDESTROY", "THMUTEX", "THSEM"]     
        