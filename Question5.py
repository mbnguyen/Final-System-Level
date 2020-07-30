#
#  Question5.py
#  Final
#
#  Created by Minh Nguyen on 7/29/20.
#  Copyright © 2020 Minh Nguyen. All rights reserved.
#
import os

def main():
    temp = "temp.txt"
    copyFolder = ["FINALpython/copies", "FINALc/copies"]
    path = "~/FINAL/"
    print("Saving the list of files that need to be copied to a temporary file called " + temp)
    os.system("awk '/^[-]/ {print $9}' FINALinstruction > " + temp)

    input = open(temp, "r")
    try:
        print("\n***********************************\n")
        print("I'm reading the file " + temp + "\n")
        for line in input:
            for folder in copyFolder:
                line = line.rstrip()
                print("Copy '" + line + "' to folder '" + folder + "'")
                file = path + line
                folder = path + folder
                os.system("cp " + file + " " + folder)
    except IOError:
        print("Cannot open the file(s). Please try again.")
    finally:
        input.close()

    print("\n***********************************\n")
    print("Delete the temporary file " + temp)
    os.system("rm " + temp)

main()

