#!user/bin/env python3

# Created by: RJ Fromm
# Created on: September 2019
# This program determines if year is a leap year


def main():

    year = int(input("Please enter a year : "))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("It is a leap year")
            else:
                print("It is not a leap year")
        else:
            print("It may be a leap year")
    else:
        print("It is not a leap year")


if __name__ == "__main__":
    main()
