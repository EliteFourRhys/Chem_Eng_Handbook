import pandas as pd

def main():
    constants()

def search_text():
    print('one second')

def get_setup():
    print('just need some things....')

def constants():
    print('stuff')
    name = 'some_example_name'
    df = pd.read_csv('Antoine_Coefficients.csv')
    print(df)
    for rows in df.iterrows():
        print(rows)
        
    print(df.query('ID == 2'))

def calculation():
    print('calculating....')

if __name__ == "__main__":
    main()