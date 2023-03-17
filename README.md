# Challenge 3 - Python

This repo contains two python scripts, in the PyBank and PyPoll directories, to generate reports found in the analysis directories.

## PyBank
The PyBank script reads the `budget_data.csv` file and calculates the change in profit/losses per month. When finished, it outputs a report to the terminal and [PyBank_analysis.txt](PyBank/analysis/PyBank_analysis.txt) giving the following data:
 
 - Total Months
 - Net Profit/Losses
 - Average Change in Profit/Losses
 - Date and Amount of the Greatest Increase in profits
 - Date and Amount of the Greatest decrease in profits

## PyPoll
The PyPoll script reads the `election_data.csv` file and calculates the total votes for each candidate in the election. When finished, it outputs a report to the terminal and [PyPoll_analysis.txt](PyPoll/analysis/PyPoll_analysis.txt) giving the following data:

 - Total votes cast
 - A list of all candidates, their percentage of votes, and their total number of votes
 - The winner of the election

### Note
I use pathlib to make sure the csv and txt files were found and placed in the proper directory instead of using os.path("../"). This way I could be sure the file location was relative to the main.py file rather than depending on the directory where the script was run from.

Code example:
```
from pathlib import Path
csv_path = Path(__file__).parent / "Resources/election_data.csv"
```