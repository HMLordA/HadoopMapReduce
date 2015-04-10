#!/usr/bin/python

# Goal : study the correlation between the reputation of a user and the tags he used in his posts
# (number of tags and list of unique tags)

import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')

for line in reader:
    # if non-standard length or header line, skip the line 
    if len(line) != 19 and len(line) != 5:
        continue
    if line[0] == "id" or line[0] == "user_ptr_id":
        continue

    # we will join tags from a node data file with reputation from a user data file
    # using the user_id as the key and an indicator 
    # for the file ("A" for nodes file, "B" for users file) 
    if len(line) == 19:
        # line of the nodes file
        author_id = line[3]
        tag_list = line[2].split(" ")
        # we print a line for each tag
        for tag in tag_list:
            if tag != "":
                print "{0}\t{1}\t{2}".format(author_id,"A",tag)
    else:
        # line of the users file
        author_id = line[0]
        reputation = line[1]
        # we print a line for the reputation
        print "{0}\t{1}\t{2}".format(author_id,"B",reputation)

