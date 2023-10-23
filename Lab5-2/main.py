"""Program will output a file (using data chosen by the user)
that swaps the configuration setting with the setting itself"""

#Main function of the program(see line1)
def stringswap(line):
    left_side_string = line[:line.find('=')]
    right_side_string = line[line.find('=') + 1 :]
    
    #return the swapped string
    return (right_side_string.strip() + " = " + left_side_string.strip())

#Prompt user for filepath

#Open input file to be read, open output file to be written into
in_file = open('sample.ini')
out_file = open('reversed.ini', 'w')

#Write into output file all lines, and swap those with an = character
for line in in_file:
    if line.find('=') != -1:
        out_file.write(stringswap(line) + "\n")
    else:
        out_file.write(line)