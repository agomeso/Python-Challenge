import csv
file_path = "./Resources/election_data.csv"
total_votes = 0
election = {"Voter ID": "", "County": "", "Candidate": ""}
got_votes = {}
output_file = "./Analysis/output.txt"

with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    for row in csvreader:
        # The total number of votes cast
        total_votes = total_votes + 1
        candidates = row[2]
        lis = candidates.split()
        # print(lis)
        for c in lis:
           # print(c)
            if c in got_votes:
                got_votes[c] = got_votes[c] + 1
            else:
                got_votes[c] = 1
    # A complete list of candidates who received votes
        # print(got_votes)

# print all the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
# The winner of the election based on popular vote.
winner = 0
for key, value in got_votes.items():
    pct = round(value/total_votes*100, 3)
    print(f"{key}: {pct} % ({value})")
    if winner < value:
        winner = value
        elected = key
print("-------------------------")
print(f"Winner: {elected}")
print("-------------------------")

# output
with open(output_file, "w") as outputFile:
    outputFile.write("Election Results\n")
    outputFile.write("----------------------------\n")
    outputFile.write(f"Total Votes: {total_votes}\n")
    outputFile.write("----------------------------\n")
    for key, value in got_votes.items():
        pct = round(value/total_votes*100, 3)
        outputFile.write(f"{key}: {pct} % ({value})\n")
    outputFile.write("----------------------------\n")
    outputFile.write(f"Winner: {elected}\n")
    outputFile.write("----------------------------\n")
