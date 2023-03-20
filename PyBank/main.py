import csv
from pathlib import Path

# Get Path to the csv file
csv_path = Path(__file__).parent / "Resources/budget_data.csv"


# open the csv file and extract the data
with open(csv_path, "r", encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)

    # save header and move to the data
    header = next(csv_reader)
    date_data = []
    p_l_data = []
    change_in_p_l = []

    for i, row in enumerate(csv_reader):
        # calculate the change in "Profit/Losses" for each month
        #  - this must come before appending to p_l_data because we look at the last added value
        #  - this also can not run on the first row, as there is not value before the first P/L
        if i != 0:
            change_in_p_l.append(int(row[1]) - p_l_data[-1])
        # add the data to our lists
        date_data.append(row[0])
        p_l_data.append(int(row[1]))

# calculate values for Financial Analysis
total_months = len(date_data)
net_total_amount = sum(p_l_data)
average_change = sum(change_in_p_l)/len(change_in_p_l)
greatest_increase = max(change_in_p_l)
greatest_decrease = min(change_in_p_l)

# find the indexes in the `change_in_p_l` list where the greatest changes are located
index_of_max = change_in_p_l.index(greatest_increase)
index_of_min = change_in_p_l.index(greatest_decrease)

# use the indexes from above to get the month of the increase
# use + 1 because the first month has no data and is not part of the `change_in_p_l` list
greatest_increase_date = date_data[index_of_max + 1]
greatest_decrease_date = date_data[index_of_min + 1]

output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total_amount:,}
Average Change: ${average_change:,.2f}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:,})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:,})
"""

print("")
print(output)
print("")

# save to PyBank_analysis.txt
txt_path = Path(__file__).parent / "analysis/PyBank_analysis.txt"
with open(txt_path, "w") as txt_file:
    txt_file.write(output)
