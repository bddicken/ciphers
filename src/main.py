#!/usr/bin/python

from cipher import Cipher, Plain, BasicRotatingCipher, DoubleRotation
import sys
from argparser import args, PrintOptions

def main():

    alg = None    
    METHOD = Cipher
    cipherCommand = "METHOD = " + args.method
    
    inputString = ""
    lines = sys.stdin.readlines()
    for line in lines:
        inputString += line
    inputString = inputString[:-1]

    try:
        exec cipherCommand
        method = METHOD()
        if args.task == 'encrypt':
            print method.encrypt(inputString)
        elif args.task == 'decrypt':
            print method.decrypt(inputString)
        else:
            print "invalid task"
            sys.exit(0)
    except:
        print "invalid method"
        sys.exit(0)

if __name__ == "__main__":
    main()
