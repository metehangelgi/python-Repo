

count=0

with open("denemeee.txt","r") as file:
    while file.readline() is not '':
        file.readline()
        count+=1



print(count)