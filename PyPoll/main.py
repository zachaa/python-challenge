import csv
import sys
from pathlib import Path

# check if CSV file exists through a relative path
csv_path = Path("./PyPoll/Resources/election_data.csv")
if not csv_path.exists():
    print(f"Path settings are different, this relative path works for me: {csv_path}")
    print("Exiting program early.")
    sys.exit()

# open the csv file and extract the data
with open(csv_path, "r") as csv_file:
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

# create a string for candidate results and find winner in the same loop
candidate_results = []
winner = ""
max_votes_for_candidate = max(vote_results_data.values())
for candidate_name, vote_for_candidate in vote_results_data.items():
    candidate_results.append(f"{candidate_name}: {vote_for_candidate/total_votes:.03%} ({vote_for_candidate})")
    if vote_for_candidate == max_votes_for_candidate:
        winner = candidate_name
candidate_results_string = "\n".join(candidate_results)

output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
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
txt_path = Path("./PyPoll/analysis/PyPoll_analysis.txt")
with open(txt_path, "w") as txt_file:
    txt_file.write(output)
