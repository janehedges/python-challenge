import os
import csv

# Define the path to the CSV file
file_path = 'election_data.csv'  # Update the path to your CSV file

# Initialize variables
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Open the CSV file and read its contents
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skip the header row
    
    for row in csvreader:
        # Extract the candidate from the row
        candidate = row[2]
        
        # Increment the total votes count
        total_votes += 1
        
        # Track the total number of votes each candidate received
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

# Determine the winner based on popular vote
for candidate, votes in candidates.items():
    if votes > winner["votes"]:
        winner["name"] = candidate
        winner["votes"] = votes

# Prepare the analysis results
analysis = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""
for candidate, votes in candidates.items():
    analysis += f"{candidate}: {percentages[candidate]:.3f}% ({votes})\n"

analysis += f"-------------------------\nWinner: {winner['name']}\n-------------------------"

# Print the analysis to the terminal
print(analysis)

# Export the analysis to a text file
output_file = 'election_analysis.txt'
with open(output_file, 'w') as file:
    file.write(analysis)

