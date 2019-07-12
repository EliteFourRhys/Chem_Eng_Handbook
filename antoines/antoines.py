import pandas as pd
import math
import os
import sys

def main():
    global succes
    succes = False
    # loop until you get succesful calculation for paramaters add in
    while succes == False:
      try:
         lst = user_input()
         data = constants(lst)
         if (lst[1] == 'None') or (lst[1] == 'none') or (lst[1] == 'NaN'):
             to_temp(data, lst[2])
         elif (lst[2] == 'None') or (lst[2] == 'none') or (lst[2] == 'NaN'):
             to_VP(data, lst[1])
         else:
             print('that didnt work, make sure you have caps and specify the unknown as none')
      except:
          print('that didnt work, make sure you have caps and specify the unknown as none')
          pass

def user_input():
    print("An example to find VP at given temp: H20 25 None")
    inpt = input("Please enter data in the form: Formula GivenTemp GivenVP :")
    lst = inpt.split()
    return lst

def constants(usr):

    # provide a pre screen function that matches names to id to improve quary use

    formula = (usr[0])

    # load csv into a pandas df
    df = pd.read_csv('Antoine_Coefficients.csv')

    # decided we will query by forumula and return all among forumula..seems most practical, need to change things
    # this will take a user provided querey and return the constants, whats nice about this is it can return all rows for multiple temp ranges
    #print(df[df['Formula'].str.match(str(formula))])
    data = df[df['Formula'].str.match(str(formula))]
    return data

def to_temp(data, vp):
    #just asssigning things from dataframe
    A, B, C = data.A, data.B, data.C
    counter = A.first_valid_index()
    #run through the antoines calculation for all the query hits, we will give multiple results labeled
    # this looks weird.. but just had to adjust the indexing of all the different slices i was making
    while counter < (len(data) + A.first_valid_index()):
        temp = ((B[counter]/(A[counter]-math.log(float(vp), 10))) - C[counter])
        output = 'Temp:{} C  VP:{} mmHg  Formula:{}  Names:{} {}   Temp Range:{} - {}'.format(temp, vp, data.Formula[counter], data.Name[counter], data.Formula[counter], data.TMIN[counter], data.TMAX[counter])
        print(output)
        counter += 1
    global succes
    succes = True

def to_VP(data, temp):
    A, B, C = data.A, data.B, data.C
    counter = A.first_valid_index()
    while counter < (len(data) + A.first_valid_index()):
        vp = 10**(A[counter] - (B[counter]/(float(temp) + C[counter])))
        output = 'Temp:{}  VP:{}  Formula:{}  Names:{} {}   Temp Range:{}-{}'.format(temp, vp, data.Formula[counter], data.Name[counter], data.Formula[counter], data.TMIN[counter], data.TMAX[counter])
        print(output)
        counter += 1 
    global succes
    succes = True

if __name__ == "__main__":
    main()