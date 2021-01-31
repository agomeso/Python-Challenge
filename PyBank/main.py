import csv
file_path = "./Resources/budget_data.csv"
total_mth = 0
total_pandl = 0.00
ave_pandl = 0.00
great_inc = {"date": "", "amount": 0}
great_dec = {"date": "", "amount": 0}
output_file = "./Analysis/output.txt"
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
        if (profit < great_dec["amount"]):
            great_dec["date"] = date
            great_dec["amount"] = profit

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_mth}")
print(f"Total: ${total_pandl}")
print(f"Average Change: ${total_pandl/total_mth}")
print(
    f"Greatest Increase in Profits: {great_inc['date']} $({great_inc['amount']})")
print(
    f"Greatest Decrease in Profits: {great_dec['date']} $({great_dec['amount']})")
print("----------------------------")
print("End of Financial Analysis")

with open(output_file, "w") as outputfile
outputfile.write("Financial Analysis\n")
outputfile.write("----------------------------\n")
outputfile.write(f"Total Months: {total_mth}\n")
outputfile.write(f"Total: ${total_pandl}\n")
outputfile.write(f"Average Change: ${total_pandl/total_mth}\n")
outputfile.write(
    f"Greatest Increase in Profits: {great_inc['date']} $({great_inc['amount']})\n")
outputfile.write(
    f"Greatest Decrease in Profits: {great_dec['date']} $({great_dec['amount']})"\n)
outputfile.write("----------------------------\n")
outputfile.write("End of Financial Analysis\n")
