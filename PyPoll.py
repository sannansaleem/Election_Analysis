#1.The data we need to retrieve
#1.1 Import modules 
import csv 
import os
from tkinter.tix import COLUMN 

#1.2 (Assign a variable to load a file from a path)creates filename var referecning path to csv file 
file_to_load = os.path.join("Resources", "election_results.csv")



#1.4 (Assign a variable to save the file to a path)create an analysis .txt file 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load, "r") as election_data:

     # To do: read and analyze the data here.
     file_reader = csv.reader(election_data)
      # Print the header row.
     headers = next(file_reader)
     print(headers)


    



#2. The total number of votes cast
#3. A complete list of candidates who recieved votes 
#4. The percentage of votes each candidate won 
#5. The total number of votes each candidate won 
#6. The winner of the election based on popular vote

