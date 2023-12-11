"""
Author:     Caleb R.
Date:       12/11/2023
Purpose:    A program meant to help with a change of coordinates specifically from polar to rectangular or rectangular to polar.
"""
# Import any necessary libraries
import numpy as np
import sympy as smp
import math

# Initialize any values and create any methods
user_choice = 0
#Set up initial given values3
x_given = 0.0
y_given = 0.0
r_given = 0.0
theta_given = 0.0
expression = True
#Set up hange of coordinate equations
def to_polar (x_given,y_given):
    r_final = smp.sqrt(x_given**2 + y_given**2)
    theta_final = math.degrees(smp.atan(y_given/x_given))
    ans = print(f"\n(r, \u03B8) = ({r_final:.2f}, {theta_final:.2f}\u00B0)\n")
    return ans
def to_xy (r_given, theta_given):
    x_final = r_given * smp.cos(theta_given)
    y_final = r_given * smp.sin(theta_given)
    ans = print(f"\n(x, y) = ({x_final:.2f}, {y_final:.2f})\n")
    return ans
# Start a while loop with varying if, elif, and else statements
while user_choice != "3":
    #Give user option to choose something else
    user_choice = input("\nChoose one of the following options:\n\t1.) Make a change of coordinates from polar to rectangular\
                            \n\t2.) See additional resources\n\t3.) Quit the program\n")
    # 1ST OPTION: Change of Coordinates
    if user_choice == "1": #If the user wished t have help, use symbols to show the equation to the user
            p_o_s = input("\nWould you like to convert a POINT or a SYSTEM? ").upper()
            if p_o_s == "POINT" or p_o_s == "P": #For a point
                print("\nYou have chosen to perform a change-of-coordiantes on a point.")
                change_coordinates = input("\nAre you converting to RECTANGULAR or POLAR? ").upper()
                if change_coordinates.__eq__("R") or change_coordinates.__eq__("RECTANGULAR") or change_coordinates.__eq__("RECT"):
                    r_given = float(input("\nWhat is the radius given? "))
                    theta_given = float(input("What is the given \u03B8 (in degress counter-clockwise from the x-axis)? "))
                    theta_given_rad = math.radians(theta_given)
                    to_xy(r_given,theta_given_rad)
                elif change_coordinates.__eq__("P") or change_coordinates.__eq__("POLAR"):
                    x_given = float(input("\nWhat is the given x-value? "))
                    y_given = float(input("What is the given y-value? "))
                    to_polar(x_given,y_given)
                else:
                    print(f"\n{change_coordinates} is not within the bounds asked. Please try again.\n")

            elif p_o_s == "SYSTEM" or p_o_s == "S": #For a system
                print("\nYou have chosen to perform a change-of-coordiantes on a system.")
                change_coordinates = input("\nAre you converting to RECTANGULAR or POLAR? ").upper()
                if change_coordinates.__eq__("R") or change_coordinates.__eq__("RECTANGULAR") or change_coordinates.__eq__("RECT"):
                    x,y,r = smp.symbols("x,y,r")
                    a = "x\u00b2 + y\u00b2"
                    c = "r\u00b2"
                    print("\nHere is a step by step guide to convert to rectangular. First, write the original system the")
                    print("problem gave.")
                    next_step_2 = input("\nInsert Y to continue when you are ready. ").upper()
                    if next_step_2 == "Y":
                        print(f"\nNow, check to see if r is by itself on one side of the system. If it is, and there isn't")
                        print("an additional r on the other side of the system, multiple the system by r.")
                        print("If there r was on both sides of the system, then just continue the steps for now.")
                        next_step_3 = input("\nInsert Y to continue when you are ready. ").upper()
                        if next_step_3 == "Y":
                            print(f"\nIf you were able to multiple the system by r, realize that {c} = {a}")
                            print("Now, you can focus on the other side of the equation.")
                            print("Once again, if you didn't multiply r at first, just continue the steps.")
                            next_step_4 = input("\nInsert Y to continue when you are ready. ").upper()
                            if next_step_4 == "Y":
                                print("\nRealize that x = r * cos(\u03B8) and that y = r * sin(\u03B8). Convert these to x and y.")
                                next_step_5 = input("\nInsert Y to continue when you are ready. ").upper()
                                if next_step_5 == "Y":
                                    print("\nIf there are any additional trig functions involving \u03B8, realize that the trig")
                                    print("function is some variation of y/r, x/r, or y/x. ")
                                    next_step_6 = input("\nInsert Y to continue when you are ready. ").upper()
                                    if next_step_6 == "Y":
                                        print("Now, most of the system should be changed into rectnagular or Cartesian coordinates.")
                                        print(f"However, if there is still a r that is singular, realize r = \u00b1\u221A({a}).")
                                        print(f"It is important to include \u00b1 as r is both postive or negative when \u03B8 is not")
                                        print("mentioned in relation to r.")
                                        next_step_7 = input("\nInsert Y to continue when you are ready. ").upper()
                                        if next_step_7 == "Y":
                                            print("\nAfter, revise your work and make sure that no r or \u03B8 variables are left and that")
                                            print("everything has been converted in terms of x and y.")
                                            print("Nicely done, you're ready to move on to the next problem.\n")
                                        else:
                                            print("Sorry, incorrect input.")
                                    else:
                                        print("Sorry, incorrect input.")
                                else:
                                    print("Sorry, incorrect input.")
                            else:
                                print("Sorry, incorrect input.")
                        else:
                            print("Sorry, incorrect input.")
                    else:
                        print("Sorry, incorrect input.")
                elif change_coordinates.__eq__("P") or change_coordinates.__eq__("POLAR"):
                    x,y,r = smp.symbols("x,y,r")
                    a = "x\u00b2 + y\u00b2"
                    c = "r\u00b2"
                    print("\nHere is a step by step guide to convert to polar. First, write the original system the")
                    print("problem gave.")
                    next_step_2 = input("\nInsert Y to continue when you are ready. ").upper()
                    if next_step_2 == "Y":
                        print(f"\nNow, check for any {a} or \u221A({a}). If you have {a}, realize ")
                        print(f"{c} = {a}. Therefore, r = \u00b1\u221A({a}). Convert these if they are present.")
                        next_step_3 = input("\nInsert Y to continue when you are ready ").upper()
                        if next_step_3 == "Y":
                            print("\nNext, check for x/y or y/x. If you have one convert x/y to cot(\u03B8) or y/x to tan(\u03B8)")
                            print("These are based on the trig functions you learned earlier.")
                            next_step_4 = input("\nInsert Y to continue when you are ready. ").upper()
                            if next_step_4 == "Y":
                                print("\nLastly, realize that x = r * cos(\u03B8) and that y = r * sin(\u03B8). If you have isolated and")
                                print("singular x or y components change those first.")
                                next_step_5 = input("\nInsert Y to continue when yyou are ready. ").upper()
                                if next_step_5 == "Y":
                                    print("\nAfter, revise your work and make sure that no x or y variables are left and that")
                                    print("everything has been converted in terms of r and \u03B8.")
                                    print("Nicely done, you're ready to move on to the next problem.\n")
                                else:
                                    print("Sorry, incorrect input.")
                            else:
                                print("Sorry, incorrect input.")
                        else:
                            print("Sorry, incorrect input.")
                    else:
                        print("Sorry, incorrect input.")
                else:
                    print(f"\n{change_coordinates} is not within the bounds asked. Please try again.\n")
            else:
                print(f"\n{p_o_s} is not within the bounds asked. Please try again.\n")
    #4TH OPTION: Credits and additional material
    elif user_choice == "2":
        print("\nProblems:")
        print("\tThe test problems used were from Professor Ben Woodruff's 215 Problem Set")
        print("\tAdditinoal test problems used were from Professor Ben Woodruff's 215 Wekk 8 Quiz")
    #5TH OPTION: Quitting the program
    elif user_choice == "3":
        print("\nThank you for using this program. Please cme again! ^-^\n")
    #6TH OPTION: Escape for incorrect values
    else:
        print(f"\n{user_choice} is not an acceptable choice at this time. Please try again.\n")