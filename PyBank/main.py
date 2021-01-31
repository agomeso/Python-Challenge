import csv
file_path = "./Resources/budget_data.csv"
total_mth = 0
total_pandl = 0.00
ave_pandl = 0.00
great_inc = {}
great_dec = {}

with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header

    for row in csvreader:
        total_mth = total_mth + 1

        # if (row[0].lower() == user_movie.lower()):
        #    print(f"{row[ 0 ]} is rated {row[rating]} with a rating of {row[5]}")

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits(date and amount) over the entire period
# The greatest decrease in losses(date and amount) over the entire period
print("Financial Analysis")
print("----------------------------")
print("Total Months: {total_mth}")
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
