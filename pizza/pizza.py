import sys
from tabulate import tabulate
import csv

# get filename from command line arguments
filename = sys.argv

# check for correct number of command line arguments
if len(filename) == 1:
    sys.exit("Too few command-line arguments")

if len(filename) > 2:
    sys.exit("Too many command-line arguments")

# check if the file is a CSV file
if len(filename) == 2 and filename[1].endswith(".csv"):
    try:
        with open(filename[1]) as file:
            lines = file.readlines()
    except:
        sys.exit("File does not exist")

# if the file is not a CSV file, exit the program
if not filename[1].endswith(".csv"):
    sys.exit("Not a CSV file")

# create an empty list to hold the data from the CSV file
output_list = []

# read the CSV file and add each row to the output list
with open(filename[1], "r") as file:
    lines = csv.reader(file)
    for i in lines:
        output_list.append(i)

# get the header from the first row of the output list
header = output_list[0]

# use tabulate to print the output list in a table format
print(tabulate(output_list[1:], headers=header, tablefmt="grid"))
