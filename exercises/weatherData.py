# -*- coding: UTF-8 -*-

"""

This code expected to do 2 basic data analysis using a given data set starting from 1853,the dataset given in named “Oxford_data_weather.txt”
First of all read data from txt and in second step this String data goes to the cleaning part to be in appropriate form csv file.
for next step creates nestedList which is needed form(in every line has 12 coloumn which is months of that year)
Analysis-1 Minimum temperature during the total data period
Analysis-2 Total sunshine hours during the total data period


:author: <Metehan Gelgi>
:copyright: ......
:license: ......
"""


import os
import pandas as pd
import re
import statistics
import numpy as np
import time




def CleanData(lines):
    """
    gets lines and cleans information part,previsional identifiers,cleans unnecessary whitespaces.
    :param lines: list(str)
    :return: String
    """
    for i in range(5):
        print(lines[0])
        del (lines[0])  # deletes information part

    del (lines[1])  # deletes units

    '''            ---- tries to deletes provisional parts but there is problem which I didn't understand
    for i in lines:
        x=re.search('Provisional',i)   
        if (x):
            lines.remove(i)
    '''

    lines.reverse()
    for i in range(6):  # deletes 2018 which is provisional parts.     ---try to recover provisional parts(note to myself)
        del (lines[0])
    lines.reverse()

    lines2=list()
    for i in lines:     #First deletes whitespaces at the start of lines, replaces other whites Spaces with comma
        i=i.lstrip()
        i = re.sub("\s+", ",", i.strip())
        lines2.append(i)

    StringData = "\n".join(lines2)  #joins lines
    StringData = StringData.replace('*', '')

    return StringData



def CreateNestedList():
    """
    this function reads data from csv file, then by using pandas.iloc()-- gets dataframe and creates nestedList
    :return: list(2 dimensional list)
    """
    csvData = pd.read_csv("Oxford_wdata.csv")
    w, h = 12,int(len(csvData)/12)#creates pre two dimension list
    nestedList = [[0 for x in range(w)] for y in range(h)]
    #nestedList = np.zeros((int(len(csvData)/12), 12))   ----when apply this code (instead of previous 2 lines)- error occurs
    ColCounter=0
    RowCounter=0
    for i in range(len(csvData)):#gets inforation of that line
        yyyy=csvData.iloc[i][0]
        mm=csvData.iloc[i][1]
        tmax=csvData.iloc[i][2]
        tmin=csvData.iloc[i][3]
        af=csvData.iloc[i][4]
        rain=csvData.iloc[i][5]
        sun=csvData.iloc[i][6]

        newDict={'yyyy':yyyy,'mm':mm,'tmax':tmax,'tmin':tmin,'af':af,'rain':rain,'sun':sun}# puts together as a dictionary
        nestedList[RowCounter][ColCounter]=newDict

        if ColCounter < 11:
            ColCounter+=1
        else:
            ColCounter=0
            RowCounter+=1

    return nestedList

def Analysis1(nestedList):
    """
    this function has 3 different part for Tmin data:
    1-gets all tmin data then prints it
    2-gets average for each month then determines which month is best(highest degree)
    3- do same thing with second step but calculates for each decades
    :param nestedList: list(2 dimensional)
    :return: None
    """
    print(20 * "-", 'Analysis1', 20 * "-","\n")

    Tmin,Width,Height=getNecessaryColumn(nestedList,'tmin') #limitation with needed data(Tmin)
    for i in range(Height):#prints all data
        print(Tmin[i][0:12])


    Average=getAverage(Tmin,Width,Height)# gets average of all datas month by month
    print("Averages are:")
    for avg in Average: # prints averages
        print("%.2f" % avg, end=" ")

    print("\n\n", "The best weather in that Month(with degree): ", Average.index(max(Average)) + 1, "(",
          "%.2f" % max(Average), "C)\n")

    MeanOfDecades(Tmin,Height,Width,startingYear=nestedList[0][0].get('yyyy')) #do same thing with second step but first divides into decades

def Analysis2(nestedList):
    """
    Before analysing for sun hours, I need data so i will remove which years do not have data about sun times(1853-1928)
    this function has 3 different part for Sun data:
    1-gets all sun data then prints it
    2-gets average for each month then determines which month is best(has more time to have sun)
    3- do same thing with second step but calculates for each decades
    :param nestedList: list(2 dimension)
    :return: None
    """
    print(20*"-",'Analysis2',20*"-","\n")

    sunList,Width,Height=getNecessaryColumn(nestedList,'sun') # limitation data related with sun hours(sun)
    index=0
    for i in range(Height): # cleaning previous of 1929 which do not have data for sunny hours
        if isinstance(sunList[i][0],float):
            index=i
            break
    sunList=sunList[index:]
    Height=Height-index

    for i in range(Height): # prints all data related with sun hours
        print(sunList[i][0:12])

    Average = getAverage(sunList, Width, Height) # gets average of all datas month by month
    print("Averages are:")
    for avg in Average:
        print("%.2f" % avg, end=" ")

    print("\n\n", "The best weather in that Month(with sunny Hours): ", Average.index(max(Average)) + 1, "(",
          "%.2f" % max(Average), " Hours)\n")

    MeanOfDecades(sunList, Height, Width,startingYear=1929)#do same thing with second step but first divides into decades ---- I couldn't get 1929 from combining nestedList and sunList

def getNecessaryColumn(nestedList,identifier):
    """
    this function gets nestedList and with identifier gets information from specified coloumn, then create float datas in nestedList.
    identifier is string which is tmin or sun (coloumn datas)
    :param nestedList:list(2 dimensional)
    :param identifier:str
    :return:list(2 dimensional),int,int
    """
    print('Jan.  Feb.  March April   May  June   July  August  Sept.  Oct.  Nov.  December')

    Height = len(nestedList)
    Width = len(nestedList[0])
    w, h = 12, len(nestedList)  # creates pre two dimension list
    reArrangedNestedList = [[0 for x in range(w)] for y in range(h)]
    #reArrangedNestedList = np.zeros((len(nestedList),12)) --------when apply this code (instead of previous 2 lines)- error occurs
    for i in range(Height):    # gets data from related coloumn(Tmin or sun)
        for j in range(Width):
            MinDegree = nestedList[i][j].get(identifier)
            if MinDegree == '---':
                # print(MinDegree)
                reArrangedNestedList[i][j] = '---'
                continue
            MinDegreeFloat = float(MinDegree)
            reArrangedNestedList[i][j] = MinDegreeFloat

    return reArrangedNestedList,Width,Height



def getAverage(property,Width,Height):
    """
    property is about: this data comes from Tmin or Sun?
    first of all gets help from getRidOfScoreForMonths to get rid of '---' datas
    then basicly calculates averages month by month
    :param property: list(2 dimensional)
    :param Width: int
    :param Height: int
    :return: list
    """
    Averages = []
    for i in range(Width):
        meanList = getRidOfScoreForMonths(property, Height, i)
        Averages.append(statistics.mean(meanList))
    return Averages


def getRidOfScoreForMonths(property,Height,i):
    """
    property is about: this data comes from Tmin or Sun?
    i: getAverage function sends data with 1 dimensional array month by month(with all years --- eg. Feb2009,Feb2010..)
    This code detects '---'(missing datas) and remove these datas from calculation of mean.
    :param property: list(2 dimensional)
    :param Height: int
    :param i: int
    :return:list
    """
    MeanList=list()
    for a in range(Height):
        if  isinstance(property[a][i], float):
            MeanList.append(property[a][i])

    return MeanList

def MeanOfDecades(property,Height,Width,startingYear):
    """
    this function calculates averages by dividing decades.(uses getAverage function)
    First part it detects how many year left for next decade by using starting year
    Secondly get averages for each decade
    Lastly calculates remaining decade(2010-2017 --- by 2018 discarded)
    :param property: list(2 dimensional)
    :param Height: int
    :param Width: int
    :param startingYear: int
    :return: None
    """
    #first decade
    remainingYear=startingYear%10
    YearForEndOfDecade=10-remainingYear

    TempProperty=property[0:YearForEndOfDecade].copy() #gets list which has all data for Tmin or sun hours for that decade
    firstDecadeAvg=getAverage(TempProperty,Width,YearForEndOfDecade) #gets averages for that decade month by month
    print(startingYear,"-",startingYear+YearForEndOfDecade-1, end=": ") #prints it
    for avg in firstDecadeAvg:
        print("%.2f" % avg, end=" ",)
    print("\n")

    #for next decades
    x=0
    year=startingYear+YearForEndOfDecade
    for a in range(10+YearForEndOfDecade,Height-YearForEndOfDecade,10):
        nextDecadeProperty=property[a-10:a].copy() #gets list which has all data for Tmin or sun hours for that decade
        nextAverages=getAverage(nextDecadeProperty,Width,10) #gets averages for that decade month by month
        print(year, "-", year + 9, end=": ") #prints it
        for avg in nextAverages:
            print("%.2f" % avg, end=" ")
        print("\n")
        year=year+10
        x=max(x,a)


    #for last 8 years
    LastTempProperty=property[x:].copy() #gets list which has all data for Tmin or sun hours for that decade
    LastAvg=getAverage(LastTempProperty,Width,8) #gets averages for that decade month by month
    print(year, "-", year + 7, end=": ") #prints it
    for avg in LastAvg:
        print("%.2f" % avg, end=" ")
    print("\n")


def main():
    """there is 5 main steps in functions:
    1-reading
    2-cleaning
    3-transform into NestedList
    4-Analysis1
    5-Analysis2
    """
    with open("weather_data_Oxford.txt", 'r+') as file:
        lines = file.readlines()

    StringData = CleanData(lines)

    with open("Oxford_wdata.csv", "w") as file2:
        file2.write(StringData)

    nestedList = CreateNestedList()
    t1=time.time()
    Analysis1(nestedList)
    t2=time.time()
    Analysis2(nestedList)
    t3=time.time()
    print("Time for first analysis:",t2-t1) #prints time needed for first analysis
    print("Time for second analysis:",t3-t2) #prints time needed for second analysis

if __name__ == '__main__':
    main()








