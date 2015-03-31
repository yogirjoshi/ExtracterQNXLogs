'''
Created on Jan 27, 2015

@author: y2joshi
'''
class TraceCSVFormatter:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def writeHeader(self):
        '''
        '''
        return ""
    def writeTrailer(self):
        '''
        '''
        return ""
    
    def writeState(self, dict):
        retVal=""    
        count=len(dict.keys())
        for key in dict:
            if key == 'ID':
                retVal=retVal + "ID=" + str(dict[key])
            elif key == 'timestamp':
                retVal=retVal + "timestamp=" + str(dict[key])     
            else:    
                retVal=retVal + key + "=" + str(dict[key]) 
            count = count - 1
            if count > 0:
                retVal=retVal + ","
        return retVal + "\n"
    
class TraceXMLFormatter:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def writeHeader(self):
        '''
        '''
        return "<Trace>\n"
    def writeTrailer(self):
        '''
        '''
        return "</Trace>\n"
    
    def writeState(self, dict):
        retVal=""
        retVal = retVal + "<State>\n"     
        for key in dict:
            if key == 'ID':
                retVal=retVal + "<ID>" + str(dict[key]) + "</ID>\n"
            elif key == 'timestamp':
                retVal=retVal + "<timestamp>" + str(dict[key]) + "</timestamp>\n"    
            else:    
                retVal=retVal + "<Key>" + key + "</Key>\n"
                retVal=retVal + "<Value>" + str(dict[key]) + "</Value>\n"
        retVal = retVal + "</State>\n"
        return retVal
             
class TraceCRVXMLFormatter:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def writeHeader(self):
        '''
        '''
        return "<log>\n"
    def writeTrailer(self):
        '''
        '''
        return "</log>\n"
    
    def writeState(self, dict):
        retVal=""
        retVal = retVal + "<event>\n"    
        retVal=retVal + "<name>" + str(dict['ID']) + "</name>\n"

        for key in dict:
            retVal = retVal + "<field>\n"      
            retVal=retVal + "<name>" + key + "</name>\n"
            retVal=retVal + "<value>" + str(dict[key]) + "</value>\n"
            retVal = retVal + "</field>\n"     
        retVal = retVal + "</event>\n"
        return retVal             