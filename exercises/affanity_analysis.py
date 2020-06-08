

affanityData={"A":[],"B":[],"C":[],"D":[],"E":[]}
affanityKeys=["A","B","C","D","E"]
#################Check powerset function to find all combinations of these products.  AB-ABC-ABCD.....
lengthofData=0


def print_iterator(it):
    for x in it:
        print(x, end=' ')
    print('')  # for new line

def power_set(input):
    # returns a list of all subsets of the list a
    if (len(input) == 0):
        return [[]]
    else:
        main_subset = [ ]
        for small_subset in power_set(input[1:]):
            main_subset += [small_subset]
            main_subset += [[input[0]] + small_subset]
        return main_subset

def cleanPowerSet(powerset):
    letternewSet=[]
    for LetterSet in powerset():
        if LetterSet._sizeof_() >=1:
            letternewSet.append(LetterSet)
    return letternewSet

try:
    with open("W2_Affinity_dataset.txt","r") as dosya:
        lengthofData=len(dosya.readlines())
        dosya.seek(0)
        print("The data is.....")
        print("A B C D E")
        print(dosya.read())
        dosya.seek(0)
        line=dosya.readline()

        while line is not '':

            for i in range(0,10,2):
                if i==0:
                    preList=affanityData["A"]
                    preList.append(line[i])
                elif i==2:
                    preList = affanityData["B"]
                    preList.append(line[i])
                elif i==4:
                    preList = affanityData["C"]
                    preList.append(line[i])
                elif i==6:
                    preList = affanityData["D"]
                    preList.append(line[i])
                else:
                    preList = affanityData["E"]
                    preList.append(line[i])
            line = dosya.readline()

except(FileNotFoundError):
    print("I coulnd't find your file...")

print(affanityData)
print_iterator(affanityData.get('A')) #####
affanity=dict()



def calculateAffanity(affanityData,affanity):
    for i,j in affanityData.items():
        for x,y in affanityData.items():
            if x is not i:
                list1,list2=y,j
                #
                frqCounter=0
                frqList1=0
                frqList2=0
                for k in range(len(list1)):
                    if int(list1[k])==1:
                        if int(list2[k])==1:
                            frqCounter=frqCounter+1
                    if int(list1[k]) == 1:
                        frqList1 = frqList1 + 1
                    if int(list2[k]) == 1:
                        frqList2 = frqList2 + 1


                #
                support=frqCounter/lengthofData
                #
                confidence=frqCounter/frqList1
                #
                lift=confidence/frqList2

                affanity.update({x+i:[support,confidence,lift]})
    return (affanity)

print(power_set(affanityKeys))
setofpowers=power_set(affanityKeys)
#setofpowers=cleanPowerSet(setofpowers)
setofpowers.remove([])

def CalculateAffanityinNewWay(affanityData,affanity,setofpowers):
    for setLetters in setofpowers:
        if setLetters._sizeof_()==2:
            print()



affanity=calculateAffanity(affanityData,affanity)

for i,j in affanity.items():
    print(i,j)











