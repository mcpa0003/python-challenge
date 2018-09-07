import os
import csv

csvpath = os.path.join("election_data.csv")

with open(csvpath, newline="")as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(csv_header)

    vote_count = 0
    KhanCount = 0
    LiCount = []
    
    

    candidate = ["Khan", "Li"]

    for row in csvreader:
        
        vote_count = vote_count + 1
        if row[2] == str("Li"):
            print("hi")


        
      



    
print(vote_count)
print(KhanCount)
print(LiCount)
    
print("hello")