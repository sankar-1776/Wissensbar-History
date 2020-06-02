# This python program is to calulate the area of a circle given its radius.


# In the following five lines we are importing modules to do certain stuff with.
from tkinter import *
import math
import os # os = Operating System commands (Commands without a capital 'C'.).
import sys
import datetime # datetime, like the name suggests, is the module that w use to work with dates and times.
os.system("cls")

print("Copyright © Sankar Harikrishnan 2020.")
print("")
print("")
print("")
print("Hello! How are you? I hope you are well! The date is as shown below in the format YYYY-MM-DD: ") # Like it is said in this line, the date appears in the format of YYYY-MM-DD.
print(datetime.date.today()) 
print("")
print("This is a program that will calculate the area of a circle! Try it out now!")
print("")
print("This is a program to calculate the area of a circle given it's radius. The user inputs the radius and then the computer calculates the value and given an output. The user also has some features that she or he can use in order to make the answer more suitable and accpetable for them. Please use and enjoy!")
print("")
name_a = str(input("Please enter the name you would like us to call you: "))
print("Hello " + name_a + "! How are you? I hope you are doing well... Do not fear when I ask for your name again. That is only for knowing your entire name.")
print("")

print("You will have to enter an email address before you can proceed any further.")
# The following code will collect and store an email address from the user's end.
def email_collector():
    filename = "emails.txt"
    file = open(filename, 'a')
    email = str(input("Please enter your email address: "))
    if "@" and ".com" in email: # This statement checks if the email address that the user has provided ends with a '.com' or not. We only accept a '.com' thereof.
        if email in filename:
            print("")
            print("Success!" + name_a + ". You have managed to enter and hopefully verify an email address.")
            print("")
            print("The email address that you have submitted is shown below: ")
            print(email)
            pass
        else:
            filename = "emails.txt"
            file = open(filename, 'a')
            name = str(input("Please enter your name: "))
            file.write(email)
            file.write(" - " + name + "\n")
            file.close()
    elif "@" and ".org" in email:
        if email in filename:
            print("")
            print("Success!" + name_a + ". You have managed to enter and hopefully verify an email address.")
            print("")
            print("The email address that you have submitted is shown below: ")
            print(email)
            pass
        else:
            filename = "emails.txt"
            file = open(filename, 'a')
            name = str(input("Please enter your name: "))
            file.write(email)
            file.write(" - " + name + "\n")
            file.close()
    elif "@" and ".gov" in email:
        if email in filename:
            print("")
            print("Success!" + name_a + ". You have managed to enter and hopefully verify an email address.")
            print("")
            print("The email address that you have submitted is shown below: ")
            print(email)
            pass
        else:
            filename = "emails.txt"
            file = open(filename, 'a')
            name = str(input("Please enter your name: "))
            file.write(email)
            file.write(" - " + name + "\n")
            file.close()
    elif "@" and ".io" in email:
        if email in filename:
            print("")
            print("Success!" + name_a + ". You have managed to enter and hopefully verify an email address.")
            print("")
            print("The email address that you have submitted is shown below: ")
            print(email)
            pass
        else:
            filename = "emails.txt"
            file = open(filename, 'a')
            name = str(input("Please enter your name: "))
            file.write(email)
            file.write(" - " + name + "\n")
            file.close()
    elif "@" and ".cc" in email:
        if email in filename:
            print("")
            print("Success!" + name_a + ". You have managed to enter and hopefully verify an email address.")
            print("")
            print("The email address that you have submitted is shown below: ")
            print(email)
            pass
        else:
            filename = "emails.txt"
            file = open(filename, 'a')
            name = str(input("Please enter your name: "))
            file.write(email)
            file.write(" - " + name + "\n")
            file.close()
    elif "@" and ".net" in email:
        if email in filename:
            print("")
            print("Success!" + name_a + ". You have managed to enter and hopefully verify an email address.")
            print("")
            print("The email address that you have submitted is shown below: ")
            print(email)
            pass
        else:
            filename = "emails.txt"
            file = open(filename, 'a')
            name = str(input("Please enter your name: "))
            file.write(email)
            file.write(" - " + name + "\n")
            file.close()
    elif "@" and ".ne" in email:
        if email in filename:
            print("")
            print("Success!" + name_a + ". You have managed to enter and hopefully verify an email address.")
            print("")
            print("The email address that you have submitted is shown below: ")
            print(email)
            pass
        else:
            filename = "emails.txt"
            file = open(filename, 'a')
            name = str(input("Please enter your name: "))
            file.write(email)
            file.write(" - " + name + "\n")
            file.close()
    elif "@" and ".in" in email:
        if email in filename:
            print("")
            print("Success!" + name_a + ". You have managed to enter and hopefully verify an email address.")
            print("")
            print("The email address that you have submitted is shown below: ")
            print(email)
            pass
        else:
            filename = "emails.txt"
            file = open(filename, 'a')
            name = str(input("Please enter your name: "))
            file.write(email)
            file.write(" - " + name + "\n")
            file.close()
    else:
        print("")
        print("Error! We cannot verify this email address. Please use another email address.")
        print("")
        print("In case you have entered your email address in upper-case letters, please enter them in the lower-case for an acknowledgement.")
        email_collector()

        
email_collector()


# I will now calculate the area of the circle as per the user input.
def circle_area_calc():
    try:
        pi = 3.141592635
        print("")
        try:
            global r
            r = float(input("Please enter the value of the radius of this circle: "))
        except ValueError:
            print("Please do not enter non-decimals here.")
            circle_area_calc()
        ar_ = r**2*pi
        print("")
        def flow_checkpoint1():
            trunc_check = str(input("Our answer can have lots of decimal places. Would you like to shorten it? (y/n). The standard shortening is to three decimal places. Use 'm' for More Information such as what else you can do from here: "))
            print("")
            if trunc_check == "y":
                print("The area of this circle is as shown below: ")
                print("{0:.3f}".format (ar_))
                print("")
                pass
            elif trunc_check == "n":
                print("The area of this circle is as shown below: ")
                print(ar_)
                print("")
                pass
            elif trunc_check == "t":
                print("Your answer is as shown below: ")
                print(math.trunc(ar_))
                print("")
            elif trunc_check == "m": # In case someone wants to use a command to get a return of a value other than a three decimal placed one or with a greater number of decimal points, s/he can use 'm' for more information.
                print("")
                print("-------------------------------------------------------------------------------------------------------------------------")
                print("MORE INFORMATION: ")
                print("")
                print("This is an information module. It can be used to find out information about some other things you can do to the decimal points.")
                print("")
                print("1. Use 'f' to floor, i.e., remove the decimal points and go to the lowest closest integer to that decimal number.")
                print("2. Use 'c' to ceil, i.e., remove the decimal points and go to the highest closest integer to that decimal number.")
                print("3. Also, you can enter 'q' to quit.")
                print("-------------------------------------------------------------------------------------------------------------------------")
                print("")
                flow_checkpoint1()
            elif trunc_check == "f":
                print("Your answer is as shown below: ")
                print(math.floor(ar_))
                print("")
            elif trunc_check == "c":
                print("Your answer is as shown below: ")
                print(math.ceil(ar_))
                print("")
            elif trunc_check == "q":
                quit_check = str(input("If you quit, then you will have to restart the machine. Are you sure that you want to quit? If yes, then enter 'y' and hit enter, if not, then hit 'n' and then enter: "))
                if quit_check == "y":
                    sys.exit()
                elif quit_check == "n":
                    pass
                else:
                    print("")
                    print("Error! This is not a valid character for any function this particular step can do. Please check your input and try again.")
            else:
                print("")
                print("Error! We do not recognize this action. Please only type in 'y' or 'n'. For more information type in 'm'.")
                flow_checkpoint1()
                    
                    
        flow_checkpoint1()

            
    except ValueError and TypeError and ZeroDivisionError:
        print("")
        print("Error! Please do not enter values that cannot be used or worked upon by systems and their respective functions. Try again.")
        circle_area_calc()
            
                
circle_area_calc()    


# The following function will be used to check if the user wants to calculate the areas of further circles and then loop him/her back to circle_area_calc().
def consequent_calculator():
    while True:
        check1 = str(input("Type in 'y' to calculate another circle's area or 'q' to quit:  "))
        if "y" in check1:
            print("")
            circle_area_calc()
        elif "q" in check1:
            quit_check = str(input("If you quit, then you will have to restart the machine. Are you sure that you want to quit? If yes, then enter 'y' and hit enter, if not, then hit 'n' and then enter: "))
            if quit_check == "y":
                sys.exit() # This states that if the user input's 'n', then the program will self kill
            elif "n" in check1:
                print("")
                pass
            else:
                print("Sorry! This is not an accepted command. Please check and try again.")
                print("")
                consequent_calculator()
        elif "y" and "n" not in check1:
            print("")
            print("Error! Either 'y' or 'n'has to be entered.")
            consequent_calculator()
        else:
            print("")
            print("Error! Please do not enter any values other than 'y' or 'n'.")
            consequent_calculator()


consequent_calculator() # This will run the function to repeatedly to check if the user wants to calculate the area of further circles (consequent_calculator).

            
    
# This is the end of this particular program!

