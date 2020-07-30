#
#  Question7.py
#  Final
#
#  Created by Minh Nguyen on 7/29/20.
#  Copyright © 2020 Minh Nguyen. All rights reserved.
#
from os import walk

def main():
    directory = "../encrypted"
    path = "."
    programName = "Question7.py"
    encryptOrDecrypt = 0 # 0 for encrypt, 1 for decrypt
    print("\nReading this directory...")

    for (dirpath, dirnames, filenames) in walk(path):
        for file in filenames:
            if file == "." or file == ".." or file == programName:
                continue

            pathFile = path + "/" + file
            if encryptOrDecrypt == 0:
                print("Encrypting " + pathFile)
            else:
                print("Decrypting " + pathFile)
            input = open(pathFile, "rb")
            pathFile = directory + "/" + file
            output = open(pathFile, "wb")
            outputContent = ""
            try:
                byte = input.read(1)
                key = 150
                shift = key % 26
                num = key % 10
                if encryptOrDecrypt == 1:
                    shift = 26 - shift
                    num = 10 - num

                while byte:
                    if ord(byte) >= ord('A') and ord(byte) <= ord('Z'):
                        outputContent += str(chr((ord(byte) + shift - ord('A')) % 26 + ord('A')))
                        if key - 1 > 0:
                            key = (key - 1) % 256
                        else:
                            key = 255
                    elif ord(byte) >= ord('a') and ord(byte) <= ord('z'):
                        outputContent += str(chr((ord(byte) + shift - ord('a')) % 26 + ord('a')))
                        if key - 1 > 0:
                            key = (key - 1) % 256
                        else:
                            key = 255
                    elif ord(byte) >= ord('0') and ord(byte) <= ord('9'):
                        outputContent += str(chr((ord(byte) + num - ord('0')) % 10 + ord('0')))
                        if key - 1 > 0:
                            key = (key - 1) % 256
                        else:
                            key = 255
                    else:
                        outputContent += str(chr(ord(byte)))
                    byte = input.read(1)
                print("Copy to " + pathFile)
                output.write(outputContent.encode('utf-8'))
            except IOError:
                print("Cannot open the file(s). Please try again.")
            finally:
                input.close()
                output.close()

main()

