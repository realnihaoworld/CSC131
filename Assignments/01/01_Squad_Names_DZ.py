#####################################################################
# author: Danison Zhang 
# date: 11/29/23
# description:
####################################################################

# A function to read the contents of a text file. It receives a string
# representing the name of the file, and returns a list containing all
# the names in the file. This function is also in charge of ensuring
# that the filename provided actually exists. If the file does not
# exist, the function prints an error message and prompts the user for a
# new file name.
def read_file(file_name):
    list = []
    with open(file_name) as f:
        for line in f:
            list.append(line)
    
    return list

# A function that receives two string arguments and returns a boolean
# that represents whether the first string begins with the second
# string.
def begin(name, search):
    pass
    
# A function that receives two string arguments and returns a boolean
# that represents whether the first string ends with the second string.
def end(name, search):
    pass
    
# A function that receives two string arguments and returns a boolean
# that represents whether the first string contains the second string.
def contain(name, search):
    return (search in name)
    
# A function that receives two arguments i.e. a list of names, and a
# substring. It then creates a short 3 element list that contains the
# number of times that the substring appears in the list. The first
# element is the number of names in which the substring appears at the 
# beginning. The second element in the number of names in which the 
# substring appears at the end. The third element in the number of
# names that contain the substring.

######################## MAIN #####################################
# prompt the user for the file name
while True:
    try:
        file_name = input("What file do you want to open? ")

        if file_name != "input.txt":
         raise NameError
        break
        
    except NameError:
        print("The file name you specified does not exist")
    
# store the names in the file in a list
name_list = read_file(file_name)

# print out the number of names in the list
print(f"The file has {len(name_list)} names in it")

# prompt the user for the substring they want to search for
search_string = input("What name (or substring) are you interested in searching for? ")

# calculate the search statistics


# print out the results of the search.
print("--------------------------------------------------")

print("--------------------------------------------------")