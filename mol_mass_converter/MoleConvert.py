import xlrd
loc="C:\Users\ASUS\Downloads\PYTHON and shiit\Data_Set.xlsx";
st=input("Enter an element/compound");
SampleMoles=input("Enter number of moles or n if you dont know");
SampleMass=input("Enter the mass or m if you dont know");
workbook=xlrd.open_workbook(loc);
sheets=workbook.sheet_by_index(0);
Find_Moles(SampleMoles,SampleMass)
Find_Mass(SampleMoles,SampleMass)
def Find_Moles(Moles,Mass):
		for i in sheet.nrows:
			if(st.casefold()==sheets.cell_value(i,1).casefold()):
				Molar_Mass=sheets.cell_value(i,3);
				Calc_Moles=Mass/Molar_Mass;
				output=print("The number of moles is "+Calc_Moles+" and the molar mass is "+Molar_Mass);
				break
	if(type(Moles) is int):	
		output=print("The number of moles is " +Moles+ "and the molar mass is "+Molar_Mass);
   return output


def Find_Mass(Moles,Mass):
	if (Mass=="m"):
		for i in sheet.nrows:
			if(st.casefold()==sheets.cell_value(i,1).casefold()):
				Molar_Mass=sheets.cell_value(i,3);
				Calc_Mass=Moles*Molar_Mass;
				output=print"The mass of the sample is "+Calc_Mass);
				break
	else:
		output=print("The sample mass is  "+Mass);
  return output


