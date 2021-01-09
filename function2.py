# !/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: Dec 2020
# This program calculates the area of tringle


print(" calculate the area of a tringle ")

def calculate_area_of_tringle():


    # Uncomment below to take inputs from the user
    length_string = input('Enter the base length(cm): ')
    height_string = input('Enter the height(cm): ')

# calculate the semi-perimeter
    try:
        length = int(length_string)
        height = int(height_string)
        area =  0.5 * length * height
        print('The area of the triangle is %0.2f cm2' %area)

    except Exception:
        print("This is not a number")

def main():

    # call functions
    calculate_area_of_tringle()


if __name__ == "__main__":
    main()
