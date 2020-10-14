#!python3
# Volume Calculator
# Feel free to rename your variables

import math

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Fiona
    # Modified:
    print("=====Volume Calculator=====")
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author: Fiona
    # Modified:
    print("Enter the shape and related values to determine volume.")
    print("Then you will get the volume of the shape.")

    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    
    if shape == sphere:
        prompts = ["Enter the radius: "]
    if shape == cuboid:
        prompts = ["Enter the height: ", "Enter the length: ", "Enter the width: "]
    if shape == cone:
        prompts = ["Enter the height: ", "Enter the radius: "]
    if shape == cylinder:
        prompts = ["Enter the radius: ", "Enter the height: "]
    if shape == pyramid:
        prompts = ["Enter the length: ", "Enter the width: ","Enter the height: "]
    return prompts

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements
    
    return measurements

def VSphere():
    volume
    return volume

def VCuboid():
    volume
    return volume

def VCone():
    volume
    return volume

def VCylinder():
    volume
    return volume

def VPyramid():
    volume
    return volume

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    # Author: Fiona
    # Modified: 
    title()
    instructions()
    getInputs(getParams(input("Enter the name of the shape: ")))
    


main()