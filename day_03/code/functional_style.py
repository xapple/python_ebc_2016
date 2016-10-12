### Structure your code

# Import modules here if needed

input_path = "input.txt"

def file_stats(filename):
    number_lines = 0
    number_characters = 0
    with open(filename) as handle:
        for line in handle:
            number_lines +=1
            number_characters += len(line.strip())
    print "number of lines", number_lines, "number of characters", number_characters

def append_to_file(filename, linetoappend):
    inputfile = open(filename, "a")
    inputfile.write(linetoappend)
    inputfile.close()


# Main program #
file_stats(input_path)
append_to_file(input_path, "ludo    0765432568\n")
file_stats(input_path)






































































# import module
import re,os


# parameters

input_file = "input.txt"


# define function

def file_stats (filename):
    ''' Print the number of line as well as the number of characters
    in the file filename
    '''
    number_lines = 0
    number_characters = 0
    with open(filename) as f:
        for line in f:
            number_lines +=1
            number_characters += len(line.strip())
    print ("number of lines", number_lines, "number of characters", number_characters)

def append_to_file(filename,linetoappend):
    ''' Append the linetoappend at the end of filename.
    The function automatically add a line ending character \n
    '''
    inputfile = open(filename,"a")
    inputfile.write(linetoappend)
    inputfile.close()


#main program
inputfile = open(filename,"a")# check the input file
inputfile.write("kjnsajnakn"+"\n")#add a line
inputfile.close()#check the file


