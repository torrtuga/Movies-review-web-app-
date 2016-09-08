import math
import string
import sys
myFile = open("sentiment.txt","r+")
line = myFile.readlines()

pos = 0.0
neg = 0.0
posa=[]
nega=[]
for i in range(len(line)):
    x = line[i]
    array = x.split()
    try:
        if(array[0]=="neg"):
            nega.append(neg + float(array[1])*100)
            posa.append(pos + float(array[3])*100)
        else:
            nega.append(neg + float(array[3])*100) 
            posa.append(pos + float(array[1])*100) 
    except :
        neg += 0.0
        pos += 0.0

x=sum(posa)/len(posa)
y=sum(nega)/len(nega)
#print(sum(posa)/len(posa))
#print(sum(nega)/len(nega))
#f = open('C:/Users/Raj/Desktop/movies/movieapp/actualrate.txt','w')
print(str(x)+','+str(y))
#f.write('\n')
sys.stdout.flush()


