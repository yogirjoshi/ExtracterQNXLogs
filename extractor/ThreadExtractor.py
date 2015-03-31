'''
Created on Jan 27, 2015

@author: y2joshi
'''
#!/usr/bin/python
import math
import sys, getopt
from Formatter import *
from EventFinder import *
import re
if __name__ == '__main__':
    inputFile=None
    outputFile=None
    patternString=None
    formattrace=None
    trFormatter = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:o:p:f:h", ["ifile=","ofile=","pattern=","format=","help"])
    except getopt.GetoptError:
        print 'ThreadExtractor.py -i <inputfile> -o <outputfile> -p <pattern> -f <CSV/XML>'
        sys.exit(2)     
    for opt,arg in opts:
        if opt == '-i':
            inputFile = arg
        elif opt == '-o':
            outputFile = arg
        elif opt == '-p':
            patternString = arg
        elif opt == '-f':
            formattrace = arg 
            if formattrace == "CSV":
                trFormatter = TraceCSVFormatter()
            elif formattrace == 'XML':    
                trFormatter = TraceXMLFormatter()
            elif formattrace == 'CRV':       
                trFormatter = TraceCRVXMLFormatter()
        elif opt == '-h':
            print 'ThreadExtractor.py -i <inputfile> -o <outputfile> -p <pattern> -f <CSV/XML>'
            sys.exit(2)    
    outputFd = open(outputFile,"w") 
    xmlDict=None
    outputFd.write(trFormatter.writeHeader())   
    thFinder = ThreadFinder()       
    eventList= thFinder.getEvents()
    eventCount=0
    ts=None
    with open(inputFile) as inputFd:
        for line in inputFd:
            xmlDict={}
            linePat = re.compile('pid:([0-9]+)[ ]+tid:([0-9]+)');
            matchx=linePat.search(line)
            if matchx:
#                 print line
                xmlDict['pid'] = matchx.group(1)
                xmlDict['tid'] = matchx.group(2)
                p = re.compile('t:([0-9a-z]+)');
                m = p.match(line)
                if m:
                    ts=m.group(1)
                else:
                    ts=0    
                for each_event in eventList:
                    if line.find(each_event) > 0:
                        xmlDict[each_event.lower()] = 1
                    else:
                        xmlDict[each_event.lower()] = 0
                xmlDict['ID'] = eventCount  
#                 xmlDict['timestamp'] = ts      
                outputFd.write(trFormatter.writeState(xmlDict))     
                eventCount=eventCount+1  
    outputFd.write(trFormatter.writeTrailer())             
                