#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import json
import re

# load and parse the file
#xmlTree = ET.parse('b.xml')
xmlString = open("b.xml").read();
xmlTree = ET.fromstring(xmlString)
#print(xmlString)


#Remove extra space characters
space = re.compile('[\r\n\t\f\v ]+')
xmlString=space.sub(' ', xmlString)
print("")
#print(xmlString.find('\r'))


#Remove extra spaces between closing tag and next
space = re.compile('> ')
xmlString=space.sub('>', xmlString)

#Remove extra spaces before opening tag
space = re.compile(' <')
xmlString=space.sub('<', xmlString)


#Remove extra spaces before >
space = re.compile(' >')
xmlString=space.sub('>', xmlString)


#Create Tag Table
tags = {}
a=1

for elem in xmlTree.iter():
    w=elem.tag
    v=elem.attrib
    if w not in tags.keys():
        tags[w] = 1
    else:
        tags[w] = tags[w]+1 
    if len(v)!= 0:
        for key in v:
            if key in tags.keys():
                tags[key] = tags[key]+1 
                continue
            tags[key]=1 
             
sortedTags=sorted(tags.items(), key=lambda x: (-x[1], x[0]))             

a=1
for t in sortedTags:
    tags[t[0]] = a 
    a=a+1 

json.dump( tags, open( "tag_table.json", 'w' ) ) #write disctionary to JSON
data = json.load( open( "tag_table.json" ) ) #Read Dictionary from JSON


tags2={}
tags3={}

i=0
for key in tags:
    tags2[key]=str(chr(119040+i))
    tags3[str(chr(119040+i))]="0"+str(tags[key])
    i=i+1
json.dump( tags2, open( "tag_table_char_music.json", 'w' ) ) #write disctionary to JSON
json.dump( tags3, open( "tag_table_music_number.json", 'w' ) ) #write disctionary to JSON
    
print(tags3)
print(tags2)
print(data)
print ("Size of the Tag Table", len(tags))


#Create Symbol Table
symbols = {}
symbols2 = {}

a=1
with open('b.xml') as f:
  while True:
    c = f.read(1)
    if not c:
      break
    if ord(c) in symbols.keys():
        continue
    if a>9:
        symbols2[c] = str(a)
        symbols[ord(c)] = str(a)
    else:
        symbols2[c] = "0"+str(a)
        symbols[ord(c)] = "0"+str(a)
    a=a+1


json.dump( symbols, open( "symbol_table.json", 'w' ) ) #write disctionary to JSON
json.dump( symbols2, open( "symbol_table_original.json", 'w' ) ) #write disctionary to JSON
data = json.load( open( "symbol_table.json" ) ) #Read Dictionary from JSON
print("")
print (data)
print("")
print ("Size of the Symbol Table", len(symbols))
print(sortedTags)
