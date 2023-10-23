"""This program is meant to work with an .ini file. It will output a .ini file with the 
configuration setting swapped with the setting itself."""

#I dont know how to describe this without it being incredibly wordy. See for yourself
def stringswap(line):
   
    #Create two substrings of a line with an = character functioning as a delimiter
    left_side_string = line[:line.find('=')]
    right_side_string = line[line.find('=') + 1 :]

    #Return the two substrings in swapped positions and concatenated
    return (right_side_string.strip() + " = " + left_side_string.strip())

#Validate user Input
while True:
    try:
        in_file = open(input("Please enter file name including the file extension: "))
    except:
        print("""File does not exist, or is not in the correct directory. 
Move the file into directory the script was executed and try again""")
    else:
        break

#Open output file to be written into
out_file = open('reversed.ini', 'w')

#Write into output file all lines, and swap those with an = character
for line in in_file:
    if line.find('=') != -1:
        out_file.write(stringswap(line) + "\n")
    else:
        out_file.write(line)

#Close up all files
out_file.close()
in_file.close()