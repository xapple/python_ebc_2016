###### Exercise 1 ############################
#There are many ways to solve this

s = "ajskndna"
num_vowels=0
for char in s:
    if char in "aeiou":
        num_vowels = num_vowels+1
print num_vowels,"vowels"

#if one needs to account for upper string character you can
#look in a lower case version of the string and print a warning if there is a number, as a function

s = "ajskndn13A"

def num_vowels(string):
    num_vowels=0
    for char in string.lower(): # we look in s.lower()
        if char in "aeiou":
            num_vowels = num_vowels+1
        if char.isdigit(): raise Warning("there is a number in the string")
    print num_vowels,"vowels"

num_vowels("a")



####### Exercise 2 ###########################
# There are many ways to solve this problem! Here is one:

num = 2
while num < 11:
    print(num)
    num += 2
print("Goodbye!")

# Here is another:
num = 2
while num <= 10:
    print(num)
    num += 2
print("Goodbye!")

# And another:
num = 0
while True:
    num += 2
    print(num)
    if num >= 10:
        print("Goodbye!")
        break

# And one more:
num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1
print("Goodbye!")

# There are always many, many different ways to solve a programming
# problem. Here are just four examples and surely there are quite
# a few more.

######## Exercise 3 ###########################
# There are many ways to solve this problem! Here is one:
for count in range(11):
    if count != 0 and count % 2 == 0:
        print(count)
print("Goodbye!")

# Here is another:
for count in range(2, 12, 2):
    print(count)
print("Goodbye!")


###### Exercise 4 ##########

# The answers come with running the exercise


####### Exercise 5 ################################
# There are many ways to solve this problem! Here is one:
s = 'azcbobobegghakl'
sub = 'bob'
total = 0
for i in range(len(s)-2):
    if s[i:i+3] == sub:
        total += 1
print 'number of times bob occurs is: ', total

####### Exercise 6 ################################
# There are many ways to solve this problem! Here is one:
s = 'azcbobobegghakl'
longest_str = ''
current_str = ''
for char in s:
    if (current_str == ''):
        current_str = char
    elif (current_str[-1] <= char):
        current_str += char
    elif (current_str[-1] > char):
        if (len(longest_str) < len(current_str)):
            longest_str = current_str
            current_str = char
        else:
            current_str = char
if (len(current_str) > len(longest_str)):
    longest_str = current_str
print 'Longest substring in alphabetical order is: ',longest_str

####### Exercise 7 #################################
# An example for how two write a function for exercise 6:

s = 'azcbobobegghakl'

def longest_alphabetical_substring(string):
    longest_str = ''
    current_str = ''
    for char in s:
        if (current_str == ''):
            current_str = char
        elif (current_str[-1] <= char):
            current_str += char
        elif (current_str[-1] > char):
            if (len(longest_str) < len(current_str)):
                longest_str = current_str
                current_str = char
            else:
                current_str = char
    if (len(current_str) > len(longest_str)):
        longest_str = current_str
    return(longest_str)

longest_alphabetical_substring("azcbobobegghakl")



###### Facultative 1

# we are looking for the smallest number
def gcd_iter(a, b):
    if a == 0 or b == 0:
        return max(a, b) # if one of them is zero then the answer is the other number
    i = min (a, b) # i is the minimum of the two
    while i>0: # while i > 0
        if a%i == 0 and b%i == 0:
            return(i) # it is the biggest denominator
        i = i-1

# recursive way
a = 12
b = 4

b = 12
a = 4

b = 36
a = 5

def gcd_rec(a, b):
    z = abs(a-b)
    if (a-b)==0:
        return b
    else:
        return gcd_rec(z,min(a, b))

print gcd_rec(a, b)




