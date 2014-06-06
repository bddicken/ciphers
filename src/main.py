#!/usr/bin/python

from cipher import Cipher, Plain, BasicRotatingCipher
import sys
from argparser import args, PrintOptions

def main():

    alg = None    
    METHOD = Cipher
    cipherCommand = "METHOD = " + args.method

    try:
        exec cipherCommand
        method = METHOD()
        if args.task == 'encrypt':
            method.encrypt()
        elif args.task == 'decrypt':
            method.decrypt()
        else:
            print "invalid task"
            sys.exit(0)
    except:
        print "invalid method"
        sys.exit(0)

if __name__ == "__main__":
    main()
