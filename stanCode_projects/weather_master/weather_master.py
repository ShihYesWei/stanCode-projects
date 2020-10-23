"""
File: weather_master.py
Author: Alan Chen
-----------------------
This program allows users to enter indefinite numbers of temperatures data and leave the input mode by entering exit
number (default as -100).
The program will tell you the average, highest, lowest temperatures and cold days among these data.
"""

EXIT = -100


def main():
    """
    This program allows users to input temperatures and will compute the average, highest, lowest temperatures
    and cold days after entering exit number.
    The default exit number is -100.
    """
    print("stanCode \"Weather Master 4.0\"! ")
    x = int(input("Next Temperature: (or " + str(EXIT) + " to quit)? "))
    c = 0
    # numbers of "c"old days, +1 if the temp entered < 16.
    s = 0
    # "s"um of input temperatures, add every temp entered.
    n = 0
    # "n"umbers of temperatures, +1 when temp entered.
    h = x
    # "h"ighest temperature, if the entered temp > highest temp so far, then assign as highest temp
    l = x
    # "l"owest temperature, if the entered temp < highest temp so far, then assign as highest temp
    if x == EXIT:
        print("No temperatures were entered.")
    else:
        if x < 16:
            c += 1
        s += x
        n += 1
        while x != EXIT:
            x = int(input("Next Temperature: (or " + str(EXIT) + " to quit)? "))
            if x != EXIT:
                if x > h:
                    h = x
                if x < l:
                    l = x
                if x < 16:
                    c += 1
                s += x
                n += 1
        print("Highest temperature = " + str(h))
        print("Lowest temperature = " + str(l))
        print("Average = " + str(s / n))
        print(str(c) + " cold day(s)")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
