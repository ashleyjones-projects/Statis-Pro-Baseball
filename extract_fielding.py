# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 11:48:23 2017

@author: w9641432
"""


def extract_fielding(sheet1,sheet2,name,np):
    
    
    namesF=[]
    infPosit=[]
    infstats=[]
    for rowOfCellObjects in sheet1['A134864':'A136815']: # Data from 2014-2016,cell number 
            for cellObj in rowOfCellObjects:
                namesF.append(cellObj.value)
    for rowOfCellObjects in sheet1['F134864':'F136815']: # Data from 2014-2016,cell number 
            for cellObj in rowOfCellObjects:
                infPosit.append(cellObj.value)
    for rowOfCellObjects in sheet1['G134864':'R136815']: # Data from 2014-2016,cell number 
            for cellObj in rowOfCellObjects:
                infstats.append(cellObj.value)
                

    namesOF=[]
    pos_OF =[]
    games_OF=[]
    for rowOfCellObjects in sheet2['A30620':'A31292']: # Data from 2014-2016,cell number 
            for cellObj in rowOfCellObjects:
                namesOF.append(cellObj.value)
    for rowOfCellObjects in sheet2['F30620':'F31292']: # Data from 2014-2016,cell number 
            for cellObj in rowOfCellObjects:
                pos_OF.append(cellObj.value)
    for rowOfCellObjects in sheet2['G30620':'G31292']: # Data from 2014-2016,cell number 
            for cellObj in rowOfCellObjects:
                games_OF.append(cellObj.value)

    Positions=[]
    gamesplayed=[]
    Po = []
    Ass=[]
    Err=[]
    C_sb=[]
    C_cs=[]
    E=[]  
    T=[]
    #import numpy as np
    stats = np.reshape(infstats,(len(namesF),12))
    for i in range(0,len(namesF)):          
        if name in namesF[i]:
            Positions.append(infPosit[i]);
            gamesplayed.append(stats[i][0])
            Po.append(stats[i][3])
            Ass.append(stats[i][4])
            Err.append(stats[i][5])
            if 'C' in Positions:         
                C_sb.append(stats[i][9])
                C_cs.append(stats[i][10])
            else:
                dummy=1;

            
            OF_games =[]
            OF_posit =[]
            
            if 'OF' in Positions:
                
                k=Positions.index('OF')
                OF_Assists=[]
                OF_Assists.append(Ass[k])
                OF_Assists=np.int32(OF_Assists)
                OF_Assists = (162/gamesplayed[k])*OF_Assists
                if OF_Assists>=15:
                    T=['T5','5']
                elif OF_Assists>=10 and OF_Assists<15:
                    T=['T4','4']
                elif OF_Assists>=5 and OF_Assists<10:
                    T=['T3','3']
                    
                elif OF_Assists<5:
                    T=['T2','2']
                else:dummy=1
                
                for j in range(0,len(namesOF)):
                    if name in namesOF[j]:
                     OF_games.append(games_OF[j])
                     OF_posit.append(pos_OF[j])
                     
                     
            
          
    Erravg=(np.sum(([Po]+[Ass]),axis=0))/(np.sum(([Po]+[Ass]+[Err]),axis=0))
    
    if 'C' in Positions:
        C_avg_sb=C_sb[0]
        C_avg_cs=C_cs[0]
#        if len(C_sb)>1:
#            C_avg_sb =[int(sum(l))/len(l) for l in zip(*C_sb)]
#            C_avg_sb=np.int32(C_avg_sb) 
#            C_avg_cs =[int(sum(l))/len(l) for l in zip(*C_cs)]
#            C_avg_cs=np.int32(C_avg_cs);
#        else:
#            print(C_sb,C_cs)       
#            C_avg_sb=np.int32(C_sb)
#            C_avg_cs=np.int32(C_cs)
    else:
        dummy=1
    
                                    
    # Caluclate fielding errors
            
                                           
    # Ratings (if no errors, rate as E0)
    #         1B     2B,SS,C,P      3B         OF
    #E1   .995-.999  .985-.999  .986-.999  .990-.999
    #E2   .990-.994  .975-.984  .976-.985  .980-.989
    #E3   .985-.989  .965-.974  .966-.975  .970-.979
    #E4   .980-.984  .955-.964  .956-.965  .960-.969
    #E5   .975-.979  .945-.954  .946-.955  .950-.959
    #E6   .970-.974  .935-.944  .936-.945  .940-.949
    #E7   .965-.969  .925-.934  .926-.935  .930-.939
    #E8   .960-.964  .915-.924  .916-.925  .920-.929
    #E9   .955-.959  .905-.914  .906-.915  .910-.919
    #E10  .000-.954  .000-.904  .000-.905  .000-.909 
    

    
    for k in range(0,len(Positions)):
        
        if '1B' in Positions[k]:
            
            if Erravg[k]>=0.995:
               E.append(['1'])
            elif Erravg[k]>= 0.990 and Erravg[k]<0.995:
               E.append(['2'])
            elif Erravg[k]>= 0.985 and Erravg[k]<0.990:
               E.append(['3'])
            elif Erravg[k]>= 0.980 and Erravg[k]<0.985:
               E.append(['4'])
            elif Erravg[k]>= 0.975 and Erravg[k]<0.980:
               E.append(['5'])
            elif Erravg[k]>= 0.970 and Erravg[k]<0.975:
               E.append(['6'])
            elif Erravg[k]>= 0.965 and Erravg[k]<0.970:
               E.append(['7'])
            elif Erravg[k]>= 0.960 and Erravg[k]<0.965:
               E.append(['8'])
            elif Erravg[k]>= 0.955 and Erravg[k]<0.960:
               E.append(['9'])
            elif Erravg[k]<0.955:
               E.append(['10'])
            else:dummy=1
                   
        elif '2B' or 'SS' or 'C' or 'P' in Positions[k]:
            
            if 'C' in Positions[k] :
                
                if (C_avg_sb+C_avg_cs)>0:
            
                    C_rating= C_avg_sb/(C_avg_sb+C_avg_cs)
                                
                    if C_rating>=0.70:
                        T=['TC','3']
                    elif C_rating>=0.60 and C_rating<0.70:
                        T=['TB','2']
                    elif C_rating<0.60:
                        T=['TA','1']
                    else:dummy=1
                    
                else:
                    T=['TC','3']
                
            else:
                dummy=1
                
                
            
            if Erravg[k]>=0.985:
               E.append(['1'])
            elif Erravg[k]>= 0.975 and Erravg[k]<0.985:
               E.append(['2'])
            elif Erravg[k]>= 0.965 and Erravg[k]<0.975:
               E.append(['3'])
            elif Erravg[k]>= 0.955 and Erravg[k]<0.965:
               E.append(['4'])
            elif Erravg[k]>= 0.945 and Erravg[k]<0.955:
               E.append(['5'])
            elif Erravg[k]>= 0.935 and Erravg[k]<0.945:
               E.append(['6'])
            elif Erravg[k]>= 0.925 and Erravg[k]<0.935:
               E.append(['7'])
            elif Erravg[k]>= 0.915 and Erravg[k]<0.925:
               E.append(['8'])
            elif Erravg[k]>= 0.905 and Erravg[k]<0.915:
               E.append(['9'])
            elif Erravg[k]<0.905:
               E.append(['10'])
            else:dummy=1
               
        elif '3B' in Positions[k]:
            
            if Erravg[k]>=0.986:
               E.append(['1'])
            elif Erravg[k]>= 0.976 and Erravg[k]<0.986:
               E.append(['2'])
            elif Erravg[k]>= 0.966 and Erravg[k]<0.976:
               E.append(['3'])
            elif Erravg[k]>= 0.956 and Erravg[k]<0.966:
               E.append(['4'])
            elif Erravg[k]>= 0.946 and Erravg[k]<0.956:
               E.append(['5'])
            elif Erravg[k]>= 0.936 and Erravg[k]<0.946:
               E.append(['6'])
            elif Erravg[k]>= 0.926 and Erravg[k]<0.936:
               E.append(['7'])
            elif Erravg[k]>= 0.916 and Erravg[k]<0.926:
               E.append(['8'])
            elif Erravg[k]>= 0.906 and Erravg[k]<0.916:
               E.append(['9'])
            elif Erravg[k]<0.906:
               E.append(['10'])
            else:dummy=1
               
        elif 'OF' in Positions[k]:
                        
            if Erravg[k]>=0.990:
               E.append(['1'])
            elif Erravg[k]>= 0.980 and Erravg[k]<0.990:
               E.append(['2'])
            elif Erravg[k]>= 0.970 and Erravg[k]<0.980:
               E.append(['3'])
            elif Erravg[k]>= 0.960 and Erravg[k]<0.970:
               E.append(['4'])
            elif Erravg[k]>= 0.950 and Erravg[k]<0.960:
               E.append(['5'])
            elif Erravg[k]>= 0.940 and Erravg[k]<0.950:
               E.append(['6'])
            elif Erravg[k]>= 0.930 and Erravg[k]<0.940:
               E.append(['7'])
            elif Erravg[k]>= 0.920 and Erravg[k]<0.930:
               E.append(['8'])
            elif Erravg[k]>= 0.910 and Erravg[k]<0.920:
               E.append(['9'])
            elif Erravg[k]<0.910:
               E.append(['10'])
            

    # NOW CONTATENTAE ALL DATA FRO GIVEN PLAYER AND PASS OUT
    
    Fielding = [name,Positions,gamesplayed,E,T]
    return Fielding   