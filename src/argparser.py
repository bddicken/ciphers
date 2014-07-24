import argparse

OptionsParser = argparse.ArgumentParser()
OptionsParser.add_argument('--task', '-t', required=True, help="encrypt or decrypt")
OptionsParser.add_argument('--method', '-m', required=True, help="method of encryption to use. Can use `Plain`, `BasicRotatingCipher`, `DoubleRotation`, or `CaesarSquare`")
args = OptionsParser.parse_args()

def PrintOptions():
    print "Task:   " + args.task
    print "Method: " + args.method
