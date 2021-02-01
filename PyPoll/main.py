import csv
file_path = "./Resources/election_data.csv"
total_votes = 0
election = {"Voter ID": "", "County": "", "Candidate": ""}
got_votes = {"Name": [], "Total": []}
Khan = 0
Correy = 0
Li = 0
OTooley = 0
Winner = 0
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

        # If the candidate is not in the list append and add 1 ELSE add 1
        candidates = row[2]
        # A complete list of candidates who received votes
        if candidates not in got_votes["Name"]:
            got_votes["Name"].append(candidates)
        # The total number of votes each candidate won
        if (candidates == "Khan"):
            Khan = Khan + 1
        if (candidates == "Correy"):
            Correy = Correy + 1
        if (candidates == "Li"):
            Li = Li + 1
        if (candidates == "O'Tooley"):
            OTooley = OTooley + 1
        # The winner of the election based on popular vote.

# print(got_votes["Name"])

# # The percentage of votes each candidate won
# print(f"{got_votes['Name'][1]}")

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(
    f"{got_votes['Name'][0]}: {round(float(Khan/total_votes*100),5)}% ({Khan})")
print(
    f"{got_votes['Name'][1]}: {round(float(Correy/total_votes*100),5)}% ({Correy})")
print(f"{got_votes['Name'][2]}: {round(float(Li/total_votes*100),5)}% ({Li})")
print(
    f"{got_votes['Name'][3]}: {round(float(OTooley/total_votes*100),5)}% ({OTooley})")
print("-------------------------")
print("Winner: Khan")
print("-------------------------")
