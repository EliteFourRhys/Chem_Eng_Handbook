import pandas as pd
import math

def main():
    succes = False
    # loop until you get succesful calculation for paramaters add in
    lst = user_input()
    data = constants(lst)
    if (lst[2] == 'None') or (lst[2] == 'none') or (lst[2] == 'NaN'):
        to_temp(data, lst[3])
    else:
        to_VP(data, lst[2])


def user_input():
    print('just need a few things')
    print("An example to find VP at given temp: H20 Water 25 None")
    inpt = input("Please enter data in the form: Formula Name GivenTemp GivenVP :")
    lst = inpt.split()
    return lst

def constants(usr):
    print('stuff')

    # provide a pre screen function that matches names to id to improve quary use
    name = 'Water'
    ident = 'some_example_id'

    # load csv into a pandas df
    df = pd.read_csv('Antoine_Coefficients.csv')

    # this will take a user provided querey and return the constants, whats nice about this is it can return all rows for multiple temp ranges
    print(df[df['Name'].str.match(str(name))])
    data = df[df['Name'].str.match(str(name))]
    return data

def to_temp(data, vp):
    print('calculating')
    print(vp)
    #just asssigning things from dataframe
    A, B, C = data.A, data.B, data.C
    tmin, tmax = data['TMIN'], data['TMAX']
    counter = 0
    results = [] 
    #run through the antoines calculation for all the query hits, we will give multiple results labeled
    while counter < len(data):
        temp = ((B[counter]/(A[counter]-math.log(float(vp), 10))) - C[counter])
        counter += 1 
        results.append(temp)   
    print(results)

def to_VP(data, temp):
    print('calculating')
    print(temp)
    A, B, C = data.A, data.B, data.C
    tmin, tmax = data['TMIN'], data['TMAX']
    counter = 0
    results = [] 
    while counter < len(data):
        vp = 10**(A[counter] - (B[counter]/(float(temp) + C[counter])))
        counter += 1 
        results.append(vp)

if __name__ == "__main__":
    main()