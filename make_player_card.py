# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 10:42:18 2017

@author: w9641432
"""

#def make_player_card(batter_list):
    
#from docx import Document
#from docx.shared import Mm
#
#document = Document()
#    
#section = document.sections[0]
#section.page_height = Mm(29)
#section.page_width = Mm(21)
#document.add_heading(bios[0],0)
#    
#document.save('Test.docx')

f = open(batter_list[0]+'.txt','w')
f.write('              '+batter_list[2]+"\n")
f.write('              '+batter_list[3]+"\n")
for i in range(0,len(batter_list[7])):
    f.write(batter_list[7][i]+'-'+str(batter_list[8][i])+'(E'+str(batter_list[9][i][0])+')'+ '  ')
f.write("\n")
f.write('---------'+"\n")
f.write('OBR:'+batter_list[11][1]+'         ') 
f.write('SP:'+batter_list[12][1]+'         ')
if any(batter_list[10]): 
    f.write('Arm:'+batter_list[10]+"\n") 
else:
    f.write('Arm:'+"\n")
f.write('CD:'+str(batter_list[13])+'         ') 
f.write('SAC:'+(batter_list[14][1])+'       ')
f.write('H&R:'+str(batter_list[15])+"\n")
f.write('---------'+"\n")

# INFIELD SINGLES
if any(batter_list[16]) :
    if len(batter_list[17])>1:
        f.write('1BF:' + str(batter_list[16][0]) + '-' + str(batter_list[16][-1]) + "\n")
    else:
        f.write('1BF:'+str(batter_list[16][0])+ "\n")
else:
    f.write('1BF:' + "\n")

# SINGLES    
if any(batter_list[17]):
    if len(batter_list[17])>1:
        f.write('1B7:' + str(batter_list[17][0]) + '-' + str(batter_list[17][-1]) + "\n")
    else:
        f.write('1B7:'+str(batter_list[17][0])+ "\n")
else:
    f.write('1B7:'+"\n")
 
if any(batter_list[18]):
    if len(batter_list[18])>1:
        f.write('1B8:' + str(batter_list[18][0]) + '-' + str(batter_list[18][-1]) + "\n")
    else:
        f.write('1B8:'+str(batter_list[18][0])+ "\n")
else:
    f.write('1B8:'+"\n")
 
if any(batter_list[19]):
    if len(batter_list[19])>1:
        f.write('1B9:' + str(batter_list[19][0]) + '-' + str(batter_list[19][-1]) + "\n")
    else:
        f.write('1B9:'+str(batter_list[19][0])+ "\n")
else:
    f.write('1B9:'+"\n")  
    
# DOUBLES   
if any(batter_list[20]):
    if len(batter_list[20])>1:
        f.write('2B7:' + str(batter_list[20][0]) + '-' + str(batter_list[20][-1]) + "\n")
    else:
        f.write('2B7:'+str(batter_list[20][0])+ "\n")
else:
    f.write('2B7:'+"\n")    

if any(batter_list[21]):
    if len(batter_list[21])>1:
        f.write('2B8:' + str(batter_list[21][0]) + '-' + str(batter_list[21][-1]) + "\n")
    else:
        f.write('2B8:'+str(batter_list[21][0])+ "\n")
else:
    f.write('2B8:'+"\n")
    
if any(batter_list[22]):
    if len(batter_list[22])>1:
        f.write('2B9:' + str(batter_list[22][0]) + '-' + str(batter_list[22][-1]) + "\n")
    else:
        f.write('2B9:'+str(batter_list[22][0])+ "\n")
else:
    f.write('2B9:'+"\n")

# TRIPLES

if any(batter_list[23]):
    if len(batter_list[23])>1:
        f.write('3B8:' + str(batter_list[23][0]) + '-' + str(batter_list[23][-1]) + "\n")
    else:
        f.write('3B8:'+str(batter_list[23][0])+ "\n")
else:
    f.write('3B8:'+"\n") 
    
# HOMERUNS

if any(batter_list[24]):
    if len(batter_list[24])>1:
        f.write(' HR:' + str(batter_list[24][0]) + '-' + str(batter_list[24][-1]) + "\n")
    else:
        f.write(' HR:'+str(batter_list[24][0])+ "\n")
else:
    f.write(' HR:'+"\n")

# STRIKEOUTS

if any(batter_list[25]):
    if len(batter_list[25])>1:
        f.write('  K:' + str(batter_list[25][0]) + '-' + str(batter_list[25][-1]) + "\n")
    else:
        f.write('  K:'+str(batter_list[25][0])+ "\n")
else:
    f.write('  K:'+"\n")

# WALKS

if any(batter_list[26]):
    if len(batter_list[26])>1:
        f.write('  W:' + str(batter_list[26][0]) + '-' + str(batter_list[26][-1]) + "\n")
    else:
        f.write('  W:'+str(batter_list[26][0])+ "\n")
else:
    f.write('  W:'+"\n") 

# HIT BY PITCH

if any(batter_list[27]):
    if len(batter_list[27])>1:
        f.write('HBP:' + str(batter_list[27][0]) + '-' + str(batter_list[27][-1]) + "\n")
    else:
        f.write('HBP:'+str(batter_list[27][0])+ "\n")
else:
    f.write('HBP:'+"\n")    
    
# OUTS

if any(batter_list[28]):
    if len(batter_list[28])>1:
        f.write('Out:' + str(batter_list[28][0]) + '-' + str(batter_list[28][-1]) + "\n")
    else:
        f.write('Out:'+str(batter_list[28][0])+ "\n")
else:
    f.write('Out:'+"\n") 
    
    
# CHART

f.write('Cht:' + batter_list[37] + "\n")
    
f.write('---------'+"\n")

# BD 2-B

if any(batter_list[33]):
    if len(batter_list[33])>1:
        f.write('BD-2B:' + str(batter_list[33][0]) + '-' + str(batter_list[33][-1]) + "\n")
    else:
        f.write('BD-2B:'+str(batter_list[33][0])+ "\n")
else:
    f.write('BD-2B:'+"\n")  
    
# BD 3-B

if any(batter_list[34]):
    if len(batter_list[34])>1:
        f.write('BD-3B:' + str(batter_list[34][0]) + '-' + str(batter_list[34][-1]) + "\n")
    else:
        f.write('BD-3B:'+str(batter_list[34][0])+ "\n")
else:
    f.write('BD-3B:'+"\n")

# BD HR

if any(batter_list[35]):
    if len(batter_list[35])>1:
        f.write('BD-HR:' + str(batter_list[35][0]) + '-' + str(batter_list[35][-1]) + "\n")
    else:
        f.write('BD-HR:'+str(batter_list[35][0])+ "\n")
else:
    f.write('BD-HR:'+"\n")        