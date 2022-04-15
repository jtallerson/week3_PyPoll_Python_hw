# Add our dependencies.
import csv
import os

#os.chdir('C:\\Users\Admin\OneDrive\Desktop\Bootcamp HW\week3_PyPoll_Python_hw\PyPoll Analysis')
#print(os.listdir())

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)


    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)

    # Print the file object.
    #print(election_data)


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    txt_file.write("Counties in the election\n-------------------------\nArapahoe\nDenver\nJefferson")







#1. The total number of votes cast.
#print(len(election_data.readlines()) - 1)
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote.

# Assign a variable for the file to load and the path.
