import pandas as pd



mete=pd.read_csv(r"proje.csv")
print(mete.head())
mete.close()




with open(r'proje.csv','r') as data:
    oku=data.read()
    data.tell("Alfa")
    print(oku)


