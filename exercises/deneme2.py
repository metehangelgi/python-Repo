import re

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if (x):
  print("YES! We have a match!",x)
else:
  print("No match")




import re

str = "The rain in Spain"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())




w, h = 8, 5;
Matrix = [[0 for x in range(w)] for y in range(h)]


Matrix[0][0] = 1
#Matrix[6][0] = 3 # error! range...
Matrix[0][6]= 3 # valid
Matrix[4][7]=10
print(Matrix[4][7])
#Matrix[5][8]=10
#print(Matrix[5][8])

mete,ahmet=12,13
print('%12f',mete)



for i in range(10):
  for j in range(20):
    print(i*j)
    if i==2:
      break


mete=[1,2,3,4,5,6,'---']


mete.remove('---')
print(mete)




ahmet=[[1,2,3],[4,5,6],[7,8,9] ]

print(ahmet[0:2])



aaaa=1234

print(len(aaaa))


1,2,3,4,5,6