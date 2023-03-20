import csv
from pathlib import Path

# Get Path to the csv file
csv_path = Path(__file__).parent / "Resources/election_data.csv"


# open the csv file and extract the data
with open(csv_path, "r", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)

    # save header and move to the data
    header = next(csv_reader)

    vote_results_data = {}
    for row in csv_reader:
        # we don't need values from 'Voter ID' or 'County' columns
        candidate_name = row[2]
        if candidate_name in vote_results_data:
            # candidate is already in dict, add another vote to total
            vote_results_data[candidate_name] += 1
        else:
            # candidate has not been added to our dict yet
            vote_results_data[candidate_name] = 1

total_votes = sum(vote_results_data.values())

# create a multiline string for candidate results and find winner in the same loop
candidate_results = []
winner = ""
max_votes_for_candidate = max(vote_results_data.values())
for candidate_name, vote_for_candidate in vote_results_data.items():
    # create a string for each candidates results
    candidate_results.append(f"{candidate_name}: {vote_for_candidate/total_votes:.03%} ({vote_for_candidate:,})")
    
    # find the winner by comparing to max votes
    if vote_for_candidate == max_votes_for_candidate:
        winner = candidate_name
candidate_results_string = "\n".join(candidate_results)

output = f"""
Election Results
-------------------------
Total Votes: {total_votes:,}
-------------------------
{candidate_results_string}
-------------------------
Winner: {winner}
-------------------------
"""

print("")
print(output)
print("")

# save to PyPoll_analysis.txt
txt_path = Path(__file__).parent / "analysis/PyPoll_analysis.txt"
with open(txt_path, "w") as txt_file:
    txt_file.write(output)
