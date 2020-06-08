'''
-----------------------------------------------------------------------------------------------------------
|  This Code is about Population. We simulated ratio of male and female with respect to different policies...|
|  Written By Metehan Gelgi                                                                                  |
|  17.07.2019                                                                                                |
----------------------------------------------------------------------------------------------------------
'''

import random
import numpy as np
import time



def helpRatioMaleFemale():
    'this function used for predict next baby --- initial ratio is taken from the user. Return male and female ratio'
    #@param: None
    #output: float,float
    f = 0
    m = 0

    for i in range(10000):  # to get 2 decimals at least in men-women ratios
        # this is not about fixed number(10.000) I am just trying to predict ratio of male-female ratios for next generation(I could use 100 or anything, but I wanted to get more valuable ratio of males and females)

        a = random.choice(['m', 'f'])
        if a == 'f':
            f += 1
        if a == 'm':
            m += 1

    rationOfMale = m / (f + m)
    rationOfFemale = f / (f + m)
    return rationOfMale,rationOfFemale


def FirstBaby(ParentMale,ParentFemale,fertility):
    'gets #male and #female by fertility rate and calculates babies genders for that generation'
    #@param:int,int,float
    #output:int,int,int,int

    if ParentMale>=ParentFemale:
        couple=ParentFemale
    else:
        couple=ParentMale

    parents=couple*fertility

    rationOfMale,rationOfFemale= helpRatioMaleFemale()

    NumberMale=parents*rationOfMale
    NumberFemale=parents*rationOfFemale

    return np.round(NumberMale),np.round(NumberFemale),np.round(couple),np.round(parents)




def UntilSon(ParentMale,ParentFemale,fertility):
    'gets #male and #female by fertility rate and calculates babies genders for that generation',
    'differen between firstson func and this function is: this function have kind of recursive function in itself to determines new babies until son will be born.'
    # @param:int,int,float
    # output:int,int,int,int
    Daughtercounter=0
    sumgirls=0
    sumboys=0
    NumberMale=0
    NumberFemale=0


    if ParentMale>=ParentFemale:
        couple=ParentFemale
    else:
        couple=ParentMale

    parents=couple*fertility
    initialParents = parents
    while parents is not 0:

        rationOfMale, rationOfFemale = helpRatioMaleFemale() #predicts male-female ratio of that generation

        sumboys+=parents*rationOfMale
        sumgirls+=parents*rationOfFemale


        #fertility will not change in same parents
        parents=parents*rationOfFemale #at each step who has girl will have another new child
        Daughtercounter+=1

        if Daughtercounter==9:
            break

    return np.round(sumboys),np.round(sumgirls),np.round(couple),np.round(initialParents) # to get rid of decimal people.


"""
------------------------------------------TEST PART---------------------------------------------
"""
'This part is the coomon for both functions. Gets inputs and prepeare for functions'

people=int(input("how many people do you want in your data set(#10000 as pdf)>>>>"))
MaleFemaleRatio=float(input("Please Enter the Male/Female ratio(MFR) (0.51 if you want->(51 male 49 female))>>>>"))
rationOfFemale=1-MaleFemaleRatio
rationOfMale=MaleFemaleRatio

#rationOfMale,rationOfFemale= helpRatioMaleFemale()-- we don't need anymore because we are taking ratio from user...

fertilityRate=float(input("Please enter the fertility rate (the % of parents that can have a baby)(0.89 as pdf)>>>>"))

NumberFemale=rationOfFemale*people
NumberMale=rationOfMale*people

NumberFemaleS2=NumberFemale  # this will bee going to be used in UntilSon function- to use same dataSet
NumberMaleS2=NumberMale # this will bee going to be used in UntilSon function- to use same dataSet
generation=int(input("how many generation do you want? (#10 as pdf)>>>>"))

print("------------------------------------------For FirstSon Function------------------------------")


q1 = time.time()   #gets time for first function starts
wholesMales=list()
wholesFemales=list()

# to print at the end all males,females
wholesFemales.append(NumberFemale)
wholesMales.append(NumberMale)

couple=0
parents=0


for i in range(generation):
    GenerationMales,GenerationFemales,couple,parents=FirstBaby(NumberMale,NumberFemale,fertilityRate)
    wholesMales.append(GenerationMales)
    wholesFemales.append(GenerationFemales)
    print(i+1, "th generation: ")
    print("No.of MALES: ",NumberMale)
    print("No.of FEMALES: ", NumberFemale)
    print("No.of couples: ",couple)
    print("No.of Parents: ",parents)
    print("No.of babies Total: ",GenerationMales+GenerationFemales)
    print("No.of baby girls: ",GenerationFemales)
    print("No.of Baby sons: ",GenerationMales)
    print("baby son ratio: ",(GenerationMales/(GenerationFemales+GenerationMales))*100)
    print("baby girl ratio: ",(GenerationFemales/(GenerationFemales+GenerationMales))*100)
    NumberFemale = GenerationFemales #this generation's males and females are parents for next generations
    NumberMale = GenerationMales
    print("-" * 40)




q2 = time.time()  # gets time when firstSon function part end,takes time which second function starts




print("----------------------------------------For UntilSon Function-----------------------------")

wholesMalesS2=list()
wholesFemalesS2=list()

# to print at the end all males,females
wholesFemalesS2.append(NumberFemaleS2)
wholesMalesS2.append(NumberMaleS2)

for i in range(generation):
    GenerationMales,GenerationFemales,couple,parents=UntilSon(NumberMaleS2,NumberFemaleS2,fertilityRate)
    wholesMalesS2.append(GenerationMales)
    wholesFemalesS2.append(GenerationFemales)

    print(i+1, "th generation: ")
    print("No.of MALES: ", NumberMaleS2)
    print("No.of FEMALES: ", NumberFemaleS2)
    print("No.of couples: ", couple)
    print("No.of Parents: ", parents)
    print("No.of babies Total: ", GenerationMales + GenerationFemales)
    print("No.of baby girls: ", GenerationFemales)
    print("No.of Baby sons: ", GenerationMales)
    print("baby son ratio: ", (GenerationMales / (GenerationFemales + GenerationMales)) * 100)
    print("baby girl ratio: ", (GenerationFemales / (GenerationFemales + GenerationMales)) * 100)
    NumberFemaleS2=GenerationFemales    #this generation's males and females are parents for next generations
    NumberMaleS2=GenerationMales
    print("-" * 40)


print('-'*20,"Report for 1st function",'-'*20)
print('\n',wholesMales)
print(wholesFemales)
print("whole Females: ",sum(wholesFemales))
print("whole Males: ",sum(wholesMales))
print("Female Ratio is",(sum(wholesFemales)/(sum(wholesFemales)+sum(wholesMales)))*100)
print("Male Ratio is",(sum(wholesMales)/(sum(wholesFemales)+sum(wholesMales)))*100)


print('-'*20,"Report for 2nd function",'-'*20)
print('\n',wholesMalesS2)
print(wholesFemalesS2)
print("whole Females: ",sum(wholesFemalesS2))
print("whole Males: ",sum(wholesMalesS2))
print("Female Ratio is",(sum(wholesFemalesS2)/(sum(wholesFemalesS2)+sum(wholesMalesS2)))*100)
print("Male Ratio is",(sum(wholesMalesS2)/(sum(wholesFemalesS2)+sum(wholesMalesS2)))*100)




q3 = time.time()



print("-"*50)
print("time for function 1 ends: ",q2-q1)
print("time for function 2 ends: ",q3-q2)


"time different for first and second function is so significant problem in that case because there is 5-10 more times need for 2nd fuction" \
"Second function actually acts like recursive algorithm so it needs more time and more space in memory"


'''
I expected to high amount of difference between scenario 1 and scenario 2, but there is not big difference between them. 
Yes this policy changes ratio but there is similar results. I am not sure why, but I tried 4-5 runs but male ratio is decreasing for 2nd funtion
Actually 10.000-1.000.000 initial population does not affect ratio of male and female significantly, because everytime I can get different ratios(sometimes 10.000 has high male ratio in same function sometimes vise versa.)
1,000,000 initial population can give us more valuable and truly outcome because there is more data so we can interpret easily. also by this way we can minimize contradiction, and can get generalized information.
'''


