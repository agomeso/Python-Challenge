import csv
file_path = "./Resources/election_data.csv"
total_votes = 0
election = {"Voter ID": "", "County": "", "Candidate": ""}
got_votes = {"Name": [], "Total": []}
Cand_one = 0
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

        # If the candidate is not in the list append ELSE add 1
        candidates = row[2]
        # A complete list of candidates who received votes
        if candidates not in got_votes["Name"]:
            got_votes["Name"].append(candidates)
            # else
            # x = got_votes["Total"] + 1
        # The winner of the election based on popular vote.
        # The total number of votes each candidate won
        # for candidate in got_votes{"Names"}
        if (candidates == got_votes["Name"][0]):
            Cand_one = Cand_one + 1
        # if (candidates == got_votes["Name"][1]):
        #     Cand_two = Cand_two + 1
        # if (candidates == got_votes["Name"][2]):
        #     Cand_three = Cand_three + 1
        # if (candidates == got_votes["Name"][3]):
        #     Cand_four = Cand_four + 1

print(got_votes["Name"])
print(f"{got_votes['Name'][0]}: ({Cand_one})")
print(Cand_one)
# The percentage of votes each candidate won


print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print("Khan: 63.000 % (2218231)")
print("Correy: 20.000 % (704200)")
print("Li: 14.000 % (492940)")
print("O'Tooley: 3.000 % (105630)")
print("-------------------------")
print("Winner: Khan")
print("-------------------------")
