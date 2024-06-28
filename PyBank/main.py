import csv
import os

# Task is to create a Python script that analyzes the records to calculate each of the following values:
# The total number of months included in the dataset.
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

def export_results(output_file, results):
    with open(output_file, "w") as open_file:
        for result in results:
            open_file.write(result + "\n")
            print(result)

# Initialize variables
script_dir_path = os.path.dirname(__file__)
csv_path = os.path.join(script_dir_path, "Resources", "budget_data.csv")
output_path = os.path.join(script_dir_path, "Analysis", "financial_analysis.txt")
headers = []
total_months = 0
total = 0
previous_profit_loss = 0
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]

# Read the CSV file
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Store and skip the header row
    headers = next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Increment the total number of months
        total_months += 1

        # Add the profit/loss to the net total
        total += int(row[1])

        # Calculate the change in profit/loss from the previous month
        change = int(row[1]) - previous_profit_loss

        # Add the change to the list of changes
        changes.append(change)

        # Update the previous profit/loss for the next iteration
        previous_profit_loss = int(row[1])

        # Check if the change is the greatest increase or decrease
        if change > greatest_increase[1]:
            greatest_increase = [row[0], change]
        if change < greatest_decrease[1]:
            greatest_decrease = [row[0], change]

# Calculate the average change
average_change = sum(changes) / len(changes)

# Make a list with the results as strings to print.
results = [
    "Financial Analysis",
    "----------------------------",
    f"Total Months: {total_months}",
    f"Total: ${total}",
    f"Average Change: ${average_change:.2f}",
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})",
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
]

# Call the function to export the analysis results
export_results(output_path, results)

# Print the path to the output file
print(f"Analysis results exported to: {output_path}")
