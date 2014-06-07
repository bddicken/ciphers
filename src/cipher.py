import json
import fileinput
import datetime
import random
import sys
import string

#
# Cipher
#
# This is the super-class that all ciphers should inherit from.  This class doesnt
# have any actual encryption or decryption funtionality. This is left up to the 
# sub-classes.
#
class Cipher:
    
    def __init__(self):
        pass

    def __del__(self):
        pass

    def encrypt(self, text):
        print "encrypt!"

    def decrypt(self, text):
        print "decrypt!"

#
# Plain
#
# This cipher spits out exactly what it is given, for both encryption and 
# decryption.
#
class Plain(Cipher):
    def encrypt(self):
        for line in self.text:
            print line

    def decrypt(self):
        for line in self.text:
            print line

#
# BasicRotatingCipher
#
# Implements a basic rotating text cipher.
#
class BasicRotatingCipher(Cipher):
    primary = list(string.printable)
    cipher = list(string.printable)
    step = 3

    def rotate(self, lst, n):
        return lst[n:] + lst[:n]

    def encrypt(self, text):
        retString = ""
        for char in text:
            self.cipher = self.rotate(self.cipher, self.step)
            index = self.primary.index(char)
            retString += self.cipher[index]
        return retString

    def decrypt(self, text):
        retString = ""
        for char in text:
            self.cipher = self.rotate(self.cipher, self.step)
            index = self.cipher.index(char)
            retString += self.primary[index]
        return retString

#
# DoubleRotation
#
# This class simply applies the BasicRotatingCipher twice to the input.
#
class DoubleRotation(Cipher):
    
    def encrypt(self, text):
        c1 = BasicRotatingCipher()
        first = c1.encrypt(text)
        c2 = BasicRotatingCipher()
        second = c2.encrypt(first)
        return second
    
    def decrypt(self, text):
        c1 = BasicRotatingCipher()
        first = c1.decrypt(text)
        c2 = BasicRotatingCipher()
        second = c2.decrypt(first)
        return second

#
# CaesarSquare
#
# Uses Caesars square cipher.
#
class CaesarSquare(Cipher):
    
    def encrypt(self, text):
        print "implement CSq encrypt"
    
    def decrypt(self, text):
        print "implement CSq decrypt"

