#!/usr/bin/env python

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("input_file", help="This is the path of the input FASTA file.", type=str)
parser.add_argument("output_file", help="The result of the analysis will be placed here.", type=str)

parser.add_argument("-t", "--threshold", help="The scoring threshold", type=int, default=10)
parser.add_argument("-f", "--fast", help="increase the speed of the program", action="store_true")


args = parser.parse_args()
print args.input_file
print args.output_file
print args.threshold
print args.fast
print "Success !!"
