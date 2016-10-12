#!/usr/bin/env python


##Parameters
input_handle = "input.txt"


def file_stats (filename):
	'''Print thenumber of lines and the average number of
	characters per line in the file filename
	'''
	number_lines = 0
	number_characters = 0
	with open(filename) as f:
		for line in f:
			number_lines +=1
			number_characters += len(line.strip())
	print ("number of lines", number_lines, "number of characters", number_characters)

def append_to_file(filename,linetoappend):
	''' Add the linetoappend as a line at
	the end of the file filename
	'''
	inputhandle = open(filename,"a")
	inputhandle.write(linetoappend)
	inputhandle.close()


#Main program

file_stats(input_handle) # check the number of lines
append_to_file(input_handle,"ludo	0765432568\n") # Add a line
file_stats(input_handle) # Check that we added the line






