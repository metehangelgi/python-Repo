
import random


line=str()
lines=str()
for x in range(100):
    for a in range(5):
        line= line+" "+str(random.randint(0,1))

    lines=lines+line+"\n"
    line=str()


print(lines)

try:
    with open("own_affanity_dataset.txt","r+") as dosya:

        dosya.write(lines)
except(FileNotFoundError):
    print("sorry for no file such as ")