import json
import fileinput
import datetime
import random
import sys
import string

class Cipher:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def encrypt(self):
        print "encrypt!"

    def decrypt(self):
        print "decrypt!"

class Plain(Cipher):
    def encrypt(self):
        for line in sys.stdin:
            print line

    def decrypt(self):
        for line in sys.stdin:
            print line

class BasicRotatingCipher(Cipher):
    primary = list(string.printable)
    cipher = list(string.printable)
    step = 3

    def rotate(self, lst, n):
        return lst[n:] + lst[:n]

    def encrypt(self):

        for line in sys.stdin:
            for char in line:
                self.cipher = self.rotate(self.cipher, self.step)
                index = self.primary.index(char)
                sys.stdout.write(self.cipher[index])

    def decrypt(self):
        inputString = ""
        for line in sys.stdin:
            inputString += line
        for char in inputString:
            self.cipher = self.rotate(self.cipher, self.step)
            index = self.cipher.index(char)
            sys.stdout.write(self.primary[index])

