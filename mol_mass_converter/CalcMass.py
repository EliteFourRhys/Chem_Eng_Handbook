import re
import xlrd
num=[]
word=[]
loc=r"Data_Set2.xlsx"
s=input("Enter an element/compound's formula\nFo Example for Carbon Dioxide enter C1O2\nFor Sulphuric Acid enter H2S1O4 ")
workbook=xlrd.open_workbook(loc)
sheets=workbook.sheet_by_index(0)
num=[int(s) for s in re.findall(r'-?\d+\.?\d*',s)]
print(num)
i=0
j=0
Molar_Mass=0
for i in range(len(s)-1):
    t="" 
      
    if(s[i].isupper() & (not(s[i+1].islower()))):
        word.append(s[i])
        j=j+1
    elif(s[i].isupper() & s[i+1].islower()):
        t=t+s[i]+s[i+1]
        word.append(t)
        j=j+1
    else:
         continue
if(s[len(s)-1].isupper()):
    a=""
    word.append(s[len(s)-1])
print(word)

for i in range(len(word)):
       for j in range(sheets.nrows):
           if(word[i]==sheets.cell_value(j,2)):
              Molar_Mass=Molar_Mass+(sheets.cell_value(j,0)*num[i])
       
print("The Molar Mass of "+s+" is "+str(round(Molar_Mass,2))+" g/mol")