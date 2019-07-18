# import xlrd
#
# loc="Data_Set.xlsx"
# st=input("Enter an element/compound")
#
# def main():
mass=input("Input")

#    global sheets
#    test()
#    SampleMoles=input("Enter no of moles to convert or n if you dont know")
#    SampleMass=input("Enter the mass to convert or m if you dont know")
#    workbook=xlrd.open_workbook(loc)
#    sheets=workbook.sheet_by_index(0)
#    Find_Moles(SampleMoles,SampleMass)
#    Find_Mass(SampleMoles,SampleMass)
#
# def test():
#     print("testing")
#
# def Find_Moles(Moles,Mass):
#     global sheets
#     print(sheets.nrows)
#     for i in range(sheets.nrows):
#         if (st.casefold()==sheets.cell_value(i,1).casefold()):
#             Molar_Mass=sheets.cell_value(i,3)
#             Calc_Moles=int(Mass)/Molar_Mass
#             output=print("The number of moles is "+str(Calc_Moles)+" and the molar mass is "+str(Molar_Mass))
#             break
#      if((type(Moles) is int) && (type(Mass) is int)):
#         return output ("Overspecified system, please try again")
#     if(type(Moles) is int):
#         output=print("The number of moles is " +str(Moles)+ "and the molar mass is "+str(Molar_Mass))
#     return output
#
#
# def Find_Mass(Moles,Mass):
#     global sheets
#     if (Mass=="m"):
#       for i in sheets.nrows:
#             if (st.casefold()==sheets.cell_value(i,1).casefold()):
#                 Molar_Mass=sheets.cell_value(i,3)
#                 Calc_Mass=Moles*Molar_Mass
#                 output=print("The mass of the sample is "+Calc_Mass)
#                 break
#     elif(((type(Moles) is int) && (type(Mass) is int)):
#         return output ("Overspecified system, please try again"))
#     else:
# 	    output=print("The sample mass is  "+Mass)
#     return output
#
# if __name__ == "__main__":
# 	main()
#
