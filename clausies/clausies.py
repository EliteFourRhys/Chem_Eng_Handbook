import pandas as pd

def main():
    user_input()


def user_input():
    print("An example to find VP at given temp: H20 25 None")
    inpt = input("Please enter data in the form: Formula T1 T2 P1 P2 :")
    lst = inpt.split()
    return lst


if __name__ == "__main__":
    main()