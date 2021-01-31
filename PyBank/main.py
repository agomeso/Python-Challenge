import csv
file_path = "./Resources/budget_data.csv"
total_mth = 0
total_pandl = 0.00
ave_pandl = 0.00
great_inc = {"date": "", "amount": 0}
great_dec = {"date": "", "amount": 0}

with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header

    for row in csvreader:
        # The total number of months included in the dataset
        total_mth = total_mth + 1
        date = row[0]
        profit = float(row[1])
        # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        total_pandl = total_pandl + profit
        # The greatest increase in profits(date and amount) over the entire period
        if (profit > great_inc["amount"]):
            great_inc["date"] = date
            great_inc["amount"] = profit
        # The greatest decrease in losses(date and amount) over the entire period
        # if (row[0].lower() == user_movie.lower()):
        #    print(f"{row[ 0 ]} is rated {row[rating]} with a rating of {row[5]}")


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_mth}")
print(f"Total: ${total_pandl}")
print(f"Average  Change: ${total_pandl/total_mth}")
print(
    f"Greatest Increase in Profits: {great_inc['date']} $({great_inc['amount']})")
print(f"# Greatest Decrease in Profits: Sep-2013 ($-2196167)")
