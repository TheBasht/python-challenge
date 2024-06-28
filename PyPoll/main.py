import os
import csv

# Task is to create a Python script that analyzes the votes and calculates each of the following values:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

def export_results(output_file, results):
    with open(output_file, "w") as open_file:
        for result in results:
            open_file.write(result + "\n")
            print(result)

# Initialize variables
script_dir_path = os.path.dirname(__file__)
csv_path = os.path.join(script_dir_path, "Resources", "election_data.csv")
output_path = os.path.join(script_dir_path, "Analysis", "financial_analysis.txt")
headers = []
total_votes = 0
candidates_votes = {}

# Read the CSV file
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Store and skip the header row
    headers = next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Increment the total vote count
        total_votes += 1

        # Get the candidate name from the row
        candidate = row[2]

        # If the candidate is not already in the list, add them
        if candidate not in candidates_votes:
            candidates_votes[candidate] = 0

        # If the candidate is already in the list, count the vote
        if candidate in candidates_votes:
            candidates_votes[candidate] += 1

# Make a list with the results as strings to print using list comprehension
results = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------",
    *[f"{candidate}: {candidates_votes[candidate] / total_votes * 100:.3f}% ({candidates_votes[candidate]})" for candidate in candidates_votes],
    "-------------------------",
    f"Winner: {max(candidates_votes, key=candidates_votes.get)}",
    "-------------------------"
]

# Call the function to export the analysis results
export_results(output_path, results)

# Print the path to the output file
print(f"Analysis results exported to: {output_path}")
