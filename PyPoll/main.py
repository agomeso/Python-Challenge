import csv
file_path = "./Resources/election_data.csv"
total_votes = 0
election = {"Voter ID": "", "County": "", "Candidate": ""}
got_votes = {}

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
        # print('Khan', got_votes['Khan'])

# The winner of the election based on popular vote.
winner = 0
for key, value in got_votes.items():
    if winner < value:
        winner = value
        elected = key
# print(elected)
# get rid of the ' on O'Tooley
o = str("O'Tooley")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(
    f"Khan: {str(round(got_votes['Khan']/total_votes*100,5))}% ({got_votes['Khan']})")
print(
    f"Correy: {round(float(got_votes['Correy']/total_votes*100),5)}% ({got_votes['Correy']})")
print(
    f"Li: {round(float(got_votes['Li']/total_votes*100),5)}% ({got_votes['Li']})")
print(
    f"O'Tooley: {round(float(got_votes[o]/total_votes*100),5)}% ({got_votes[o]})")
print("-------------------------")
print(f"Winner: {elected}")
print("-------------------------")
