import os
import csv

# Define the file path
file_path = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
changes = []
dates = []

# Read the CSV file
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row

    # Initialize variables for tracking changes
    previous_profit_losses = None

    for row in csv_reader:
        # Extract date and profit/losses
        date = row[0]
        profit_losses = int(row[1])

        # Calculate total number of months and net total
        total_months += 1
        net_total += profit_losses

        # Calculate changes in profit/losses
        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)
            dates.append(date)

        # Update previous profit/losses for next iteration
        previous_profit_losses = profit_losses

# Calculate average change
average_change = sum(changes) / len(changes) if len(changes) > 0 else 0

# Find greatest increase and decrease in profits
greatest_increase = max(changes) if len(changes) > 0 else 0
greatest_decrease = min(changes) if len(changes) > 0 else 0

# Find the corresponding dates for greatest increase and decrease
greatest_increase_date = dates[changes.index(greatest_increase)] if len(changes) > 0 else ""
greatest_decrease_date = dates[changes.index(greatest_decrease)] if len(changes) > 0 else ""

# Format the output according to the specified analysis
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Print the analysis results
print(output)

# Save the results to a text file
output_file = 'budget_data.txt'
with open(output_file, 'w') as file:
    file.write(output)