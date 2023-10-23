"""Program will output a file (using data chosen by the user)
that swaps the configuration setting with the setting itself"""

#Prompt user for filepath

#Main function of the program(see line1)
def stringswap(line):
    left_side_string = line[:line.find('=')]
    right_side_string = line[line.find('=') + 1 :]
    
    #return the swapped string
    return (right_side_string.strip() + " = " + left_side_string.strip())

test_line = "name = joe"
print(stringswap(test_line))