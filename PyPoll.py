#1.The data we need to retrieve
#1.1 Import modules 
import csv
import os

#1.2 (Assign a variable to load a file from a path)creates filename var referecning path to csv file 
file_to_load = os.path.join("Resources", "election_results.csv")

#1.4 (Assign a variable to save the file to a path)create an analysis .txt file 
file_to_save = os.path.join("analysis", "election_analysis.txt")

# CREATE TOTAL_VOTES VAR & new list
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load, "r") as election_data:

     # To do: read and analyze the data here.
     file_reader = csv.reader(election_data)

      # Print the header row.
     headers = next(file_reader)

     # Print each row in the CSV file.
     for row in file_reader:
        #print(row)
     
#2. The total number of votes cast
          total_votes +=1
     #print (total_votes)
#3. A complete list of candidates who recieved votes 
# Print the candidate name from each row
          candidate_name = row[2]
  # If the candidate does not match any existing candidate...
          if candidate_name not in candidate_options:
      # Add it to the list of candidates.
               candidate_options.append(candidate_name)
               candidate_votes[candidate_name] = 0
     # Add a vote to that candidate's count
          candidate_votes[candidate_name] += 1

 # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
     # Print the final vote count to the terminal.
     election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
     print(election_results, end="")
    # Save the final vote count to the text file.
     txt_file.write(election_results)
          # Determine the percentage of votes for each candidate by looping through the counts.
          # 1. Iterate through the candidate list.
     for candidate_name in candidate_votes:
          # Retrieve vote count of a candidate.
          votes = candidate_votes[candidate_name]
          # Calculate the percentage of votes.
          vote_percentage = float(votes) / float(total_votes) * 100

          #  To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
          candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
          print(candidate_results)
          #  Save the candidate results to our text file.
          txt_file.write(candidate_results)
          # Determine winning vote count and candidate
          # Determine if the votes is greater than the winning count.
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               # If true then set winning_count = votes and winning_percent = vote_percentage.
               winning_count = votes
               winning_percentage = vote_percentage
               # And, set the winning_candidate equal to the candidate's name.
               winning_candidate = candidate_name

          #  To do: print out the winning candidate, vote count and percentage to terminal.
     winning_candidate_summary = (
     f"-------------------------\n"
     f"Winner: {winning_candidate}\n"
     f"Winning Vote Count: {winning_count:,}\n"
     f"Winning Percentage: {winning_percentage:.1f}%\n"
     f"-------------------------\n")
print(winning_candidate_summary)
# Save the winning candidate's results to the text file.
txt_file.write(winning_candidate_summary)

     #4. The percentage of votes each candidate won 
     #5. The total number of votes each candidate won 
     #6. The winner of the election based on popular vote

