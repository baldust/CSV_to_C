
import pandas as pd
#%%
filename = "data/A11.csv"

data = pd.read_csv(filename)

str = "{\n"
for ii,i in enumerate(data):
    #print(ii,i)
    str += "\t.{} = ".format(i)+"{"
    for i,k in enumerate(data[i]):
        if i != 0:
            str+=","
        str+= "\n\t\t{}".format(k)
    str+="\n\t}"
    if ii != data.shape[1]-1:
        str+=","
    str+="\n"
str += "};"
print(str)

#%%

filename = "data/A3.csv"

data = pd.read_csv(filename)


str = "{\n"
for ii,i in enumerate(data):
    #print(ii,i)
    str += "\t.{} = ".format(i)+"{"
    for i,k in enumerate(data[i]):
        if i != 0:
            str+=","
        str+= "\n\t\t{}".format(k)
    str+="\n\t}"
    if ii != data.shape[1]-1:
        str+=","
    str+="\n"
str += "};"
print(str)



#%%
filename = "data/A2_2.csv"

data = pd.read_csv(filename)
Data = data.transpose()

str = "{\n\t.a = \n"
for ii,i in enumerate(Data):
    #print(ii,i)

    str += "\t".format(i)+"{"
    for i,k in enumerate(Data[i]):
        if i != 0:
            str+=","
        str+= "\t{:.13f}".format(k)
    str+="}"
    if ii != data.shape[1]-1:
        str+=","
    str+="\n"
str += "};"
print(str)

#%%
import numpy as np
filename = "data/A4_2.csv"
temp = pd.read_csv(filename)

a = np.zeros((14,14)) + 1
#names = list(temp['k'].values)#.extend(list(temp['l'].values))

names = [
    'methane',
    'ethane',
    'propane',
    'iButane',
    'nButane',
    'nPenthane',
    'nitrogen',
    'carbonDioxide',
    'waterVapor',
    'hydrogenSulfide',
    'hexane',
    'heptane',
    'oxygen',
    'iPenthane']

out = pd.DataFrame(a,index=names, columns=names)
for i,j,ak,al in zip(temp['k'],temp['l'],temp['akl'],temp['alk']):
    out[i][j] = ak
    out[j][i] = al




str = "{\n\t.a = \n"
for ii,i in enumerate(out):
    #print(ii,i)

    str += "\t".format(i)+"{"
    for i,k in enumerate(out[i]):
        if i != 0:
            str+=","
        str+= "\t{:.13f}".format(k)
    str+="}"
    if ii != data.shape[1]-1:
        str+=","
    str+="\n"
str += "};"
print(str)
#print(out)