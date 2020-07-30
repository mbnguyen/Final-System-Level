#
#  Question1.py
#  System Level Assignments
#
#  Created by Minh Nguyen on 7/25/20.
#  Copyright © 2020 Minh Nguyen. All rights reserved.
#
import os

programName = "Question1.py"
print("Creating a 'FINALpython' folder")
os.system("mkdir FINALpython")

print("Creating a subdirectory of FINALpython called 'copies'")
os.system("mkdir FINALpython/copies")

print("Creating a subdirectory of FINALpython called 'encrypted'")
os.system("mkdir FINALpython/encrypted")

print("Creating a subdirectory of FINALpython called 'decrypted'")
os.system("mkdir FINALpython/decrypted")

print("Creating a copy of " + programName + " and places the copy into FINALpython")
os.system("cp " + programName + " FINALpython/")

print("\n*********************\n")
print("Showing the directory  FINALpython by running ls command:")
os.system("ls FINALpython/")

