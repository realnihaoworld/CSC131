#####################################################################
# author: Danison Zhang 
# date: 12/11/23
# description:  
#####################################################################

# A function to read the contents of a text file. It receives a string
# representing the name of the file, and returns a list containing all
# the lines in the file. This function is also in charge of ensuring
# that the filename provided actually exists. If the file does not
# exist, the function prints an error message and prompts the user for a
# new file name.
def read_file(file_name):
    list = []
    with open(file_name) as f:
        for line in f:
            list.append(int(line.strip("\n")))
    
    #list.sort()
    return list

# A function that prompts the user for a piece of information and
# returns that result to the calling statement. It receives a string
# describing the information that is required and uses that string to
# create the question that the user is asked.
def get_data(string):
    value = int(input(f"What population do you want as the {string}: "))
    return value

# A function that receives four pieces of information i.e. the minimum,
# maximum, and step sizes of the population table to be created, as well
# as the list that contains all the population values to be parsed. It
# then creates and returns a list containing as many elements as necessary 
# to store a result for each required population range. Each element in 
# that resulting list contains the number of cities in the original
# population list that have values in that range.
def frequency(minimum, maximum, step, city_list):
    list_size = maximum // step
    frequency_list = [0] * list_size
    
    lower = minimum
    upper = step
    for x in range(0, list_size):
        for value in city_list:
            if lower <= value < upper:
                frequency_list[x] += 1
        lower += step
        upper += step
    
    return frequency_list
    

####################### MAIN ####################################
# ask the user for the file name
while True:
    try:
        file_name = input("What is the name of the file with the population information? ")

        if file_name != "input.txt":
            raise NameError
        break
        
    except NameError:
        print("The file name you specified does not exist.")
        
# read the file and store the results in a list.
results_list = read_file(file_name)

# print out the information showing the number of cities in the original
# file.
print(f"This file has {len(results_list)} cities in it")
# Prompt the user for the minimum, maximum and interval populations.
min_value = get_data("minimum")
max_value = get_data("maximum")
interval = get_data("interval")

# create a list containing the frequencies of those population ranges.
frequency_list = frequency(min_value, max_value, interval, results_list)
print(frequency_list)
# print the table showing the population ranges and their frequency in
# the original file.
print("-" * 40)
print("Population\t\tFrequency")

lower = min_value
upper = interval
for x in range(0, len(frequency_list)):
    print(f"{lower}-{upper}\t\t{frequency_list[x]}")
    lower += interval
    upper += interval
print("-" * 40)