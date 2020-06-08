# Affinity analysis for data given by instructor, July 15th
import sys
if len(sys.argv) != 4:
    support_limit = 0
    confidence_limit = 0
    lift_limit = 0
    print("You have not indicated support, confidence and lift limits.")
    print("All correlations with parameters above zero will be shown as significant")
else:
    support_limit = float(sys.argv[1])
    confidence_limit = float(sys.argv[2])
    lift_limit = float(sys.argv[3])

source = open("W2_Affinity_dataset.txt")
temp = []
database = []

#Database initialization
for line in source:
    for i in line:
        if ord(i) == 48 or ord(i) == 49:
            temp.append(i)
    database.append(temp)
    temp = []

print(database)
# Support calculation function, accepts a list to be checked, ex: [1,2] is for B AND C
def support_calc(values):
    counter = 0
    for i in database:
        for j in values:
            inner_counter = 1
            if i[j] != "1":
                inner_counter = 0
                break
        if inner_counter == 1:
            counter += 1
    return counter / len(database)


#Confidence calculation, both parameters take on lists
def confidence_calc(left_hand, right_hand):
    combined_hand = set(left_hand+right_hand)
    if support_calc(left_hand) != 0:
        return support_calc(list(combined_hand)) / support_calc(left_hand)
    else:
        return 0

#Lift calculation, both parameters take on lists
def lift_calc(left_hand, right_hand):
    if support_calc(right_hand) != 0:
        return confidence_calc(left_hand, right_hand) / support_calc(right_hand)
    else:
        return 0

#Powerset formation to check every possible combination
def powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

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



relation_chart = list(powerset([0,1,2,3,4]))
relation_chart.remove([])
print(relation_chart)
#relation_chart = [[0],[1],[2],[3],[4]]
max_c = 0  #Used for figuring out the best correlation, not necessary


for i in relation_chart:
    for j in relation_chart:
        k = set(i+j)
        if len(k) != len(i)+len(j):     #Solves duplicates and similes
            continue
        a = support_calc(list(k))
        b = confidence_calc(i,j)
        c = lift_calc(i,j)
        if a > support_limit and b > confidence_limit and c > lift_limit:
            print(i,r"-->", j, "is significant")
            print("The support, conf, lift are: ", a,b,c)
        if max_c < c:
            max_c = c
            max_relation = str(i)+"--->"+str(j)+" with a lift of " + str(max_c)

print("The correlation with maximum lift within the given parameters is as follows")
print(max_relation)
