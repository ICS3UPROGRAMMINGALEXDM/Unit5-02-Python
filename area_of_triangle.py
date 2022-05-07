#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Calculates the area of a triangle

# calculates the area of the triangle with the inputted base and height
def calculate_area(base_int, height_int):
    area = (base_int * height_int) / 2
    print("The area of your triangle is {}cm^2".format(area))


def main():
    # get user input
    base = input("What is the base length of your triangle in cm: ")
    height = input("What is the height of your triangle in cm: ")
    try:
        # converts to floats
        height_int = float(height)
        base_int = float(base)
        # only calls the function if the variables are positive
        if (base_int > 0) and (height_int > 0):
            # calls the function with the arguments base_int and height_int
            calculate_area(base_int, height_int)
        else:
            print("numbers can not be negative")
    except ValueError:
        print("Numbers entered were invalid")


if __name__ == "__main__":
    main()
