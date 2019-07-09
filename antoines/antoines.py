import pandas as pd

def main():
    succes = False
    # loop until you get succesful calculation for paramaters
    lst = user_input()
    data = constants(lst)

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

    # iterating rows to slow, try to avoid using these lines
    # for rows in df.iterrows():

    # this will take a user provided querey and return the constants, whats nice about this is it can return all rows for multiple temp ranges
    print(df[df['Name'].str.match(str(name))])
    data = df[df['Name'].str.match(str(name))]
    return data

def calculation():
    print('calculating....')

if __name__ == "__main__":
    main()