import xlrd
loc=r"Data_Set.xlsx"
st=input("Enter an element/compound")
SampleMoles=input("Enter number of moles or n if you dont know")
SampleMass=input("Enter the mass or m if you dont know")
workbook=xlrd.open_workbook(loc)
sheets=workbook.sheet_by_index(0)
for i in range(sheets.nrows):
  if(st.casefold()==sheets.cell_value(i,1).casefold()):
    Molar_Mass=sheets.cell_value(i,3)
    break
print("The molar mass of "+st+" is "+str(Molar_Mass))
if((SampleMoles.isdigit() and SampleMass.isdigit()) or (SampleMoles.isalpha() and SampleMass.isalpha())):
	print("Invalid Input...Try again!")
	exit()
def Find_Moles(Moles,Mass):
	if(Moles=="n"):
		output=print("The number of moles is"+str(int(Mass)/Molar_Mass))
	else:
		output=print("straight up off yourself")
	return output
if(SampleMoles.isdigit()):
  	print("The number of moles is "+str(SampleMoles))
else:
 Find_Moles(SampleMoles,SampleMass)

def Find_Mass(Moles,Mass):
 if(Mass=="m"):
  output=print("The mass of the sample is "+str(int(Moles)*Molar_Mass))
 else:
  output=print("straight up off yourself")
 return output
if(SampleMass.isdigit()):
	print("The mass of the sample is "+str(SampleMass))
else:
	Find_Mass(SampleMoles,SampleMass)



