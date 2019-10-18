#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program calculates if a year is a leap year


def main():
    # This function calculates if a year is a leap year

    # Input
    year_str = input("Please enter the year: ")

    # Process and Output
    try:
        year = int(year_str)
        if year % 4 == 0:
            if year % 100 != 0:
                print(year, "is definately a leap year!")
            elif year % 100 == 0 and year % 400 == 0:
                print(year, "is definately a leap year!")
            else:
                print(year, "is not a leap year :(")
        else:
            print(year, "is not a leap year :(")
    except Exception:
        print("Wrong input!!!")


if __name__ == "__main__":
    main()
