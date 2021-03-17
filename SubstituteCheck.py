#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import json
import re

# load and parse the file
#xmlTree = ET.parse('b.xml')

xmlString = open("b.xml").read();
xmlTree = ET.fromstring(xmlString)
xmlString1 = xmlString


tags = json.load( open( "tag_table.json" ) )
tagsCharMusic = json.load( open( "tag_table_char_music.json" ) )
tagsMusicNumber = json.load( open( "tag_table_music_number.json" ) )
symbols = json.load( open( "symbol_table.json" ) )
symbols2 = {}


#Remove extra space characters
space = re.compile('[\r\n\t\f\v ]+')
xmlString1=space.sub(' ', xmlString1)


#Remove extra spaces between closing tag and next
space = re.compile('> ')
xmlString1=space.sub('>', xmlString1)

#Remove extra spaces before opening tag
space = re.compile(' <')
xmlString1=space.sub('<', xmlString1)


#Remove extra spaces before >
space = re.compile(' >')
xmlString1=space.sub('>', xmlString1)


variableText=""
variable=""
'''
206 is tag end
215 is space between words

for key in tagsCharMusic:
    xmlString1 = xmlString1.replace("<"+key+">", "<"+str(tagsCharMusic[key])+">");
    xmlString1 = xmlString1.replace("</"+key+">", "</"+str(tagsCharMusic[key])+">");
for key in tagsCharMusic:
    space = re.compile('<'+re.escape(key)+'>')
    xmlString1=space.sub('<'+str(tagsCharMusic[key])+">", xmlString1)
    space = re.compile('</'+re.escape(key)+'>')
    xmlString1=space.sub("</"+str(tagsCharMusic[key])+">", xmlString1)
'''
#print(xmlString1)
#print("")
#print("")


for key in tagsCharMusic:
    space = re.compile('<'+re.escape(key)+'>')
    xmlString1=space.sub(str(chr(215))+str(tagsCharMusic[key])+str(chr(215)), xmlString1)
    space = re.compile('</'+re.escape(key)+">")
    xmlString1=space.sub(str(chr(215))+str(chr(206))+str(chr(215)), xmlString1)


#print(xmlString1)
#print("")
#print("")

for key in symbols:
    symbols2[int(key)]=symbols[key]

symbols=symbols2
xmlString1=xmlString1.translate(symbols)


#print(xmlString1)
#print("")
#print("")

xmlString1=xmlString1.replace(str(chr(206)), " 0")


#print(xmlString1)
#print("")
#print("")

xmlString1=xmlString1.replace(str(chr(215)), " ")



#print(xmlString1)
#print("")
#print("")

for key in tagsMusicNumber:
    space = re.compile(key)
    xmlString1=space.sub(str(tagsMusicNumber[key]), xmlString1)

#print(xmlString1)
xmlString2 = re.sub(' +',' ',xmlString1)
print(xmlString2)
'''
for elem in xmlTree.iter():
    if elem.text!=None:
        text=elem.text.strip()
        if(text==""):
            continue
        variableText=variableText+text+'‡'


for key in symbols:
    symbols2[int(key)]=symbols[key]

symbols=symbols2
xmlString1=xmlString1.translate(symbols)

variableText1=variableText.translate(symbols)
#print(variableText1)

originalTextList=variableText.split('‡')
numeralTextList=variableText1.split('‡')

length = len(originalTextList)

'''
'''
for i in range(length):
    space = re.compile(">"+re.escape(originalTextList[i])+" 0 ")
    xmlString1=space.sub(" "+numeralTextList[i]+" 0 ", xmlString1);
#    xmlString1 = xmlString1.replace(">"+originalTextList[i]+"<", " "+numeralTextList[i]+"<");
space = re.compile('>'+re.escape(text)+' 0 ')
        xmlString1=space.sub(" "+variable+" 0 ", xmlString1)
        space = re.compile('>'+re.escape(text)+'<')
        xmlString1=space.sub(" "+variable+"<", xmlString1)
space = re.compile('[^0-9 ]')
xmlString1=space.sub("", xmlString1)
'''
'''
#print(variableText1)
print(xmlString1)
'''
