#!/usr/bin/python

# Goal : study the correlation between the reputation of a user and the tags he used in his posts
# (number of tags and list of unique tags)

import sys

oldKey = None
tags_list = [] # tags list for the current user
reputation = -1 # -1 means we did not find yet the reputation info of the current user

# output header line
print "user_id", "\t", "reputation", "\t", "nb_tags", "\t", "tag_list"

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # if non standard length, skip the line
        continue

    thisKey, type, thisValue = data_mapped

    # before moving to the next user (if the current user actually exist in the user file 
    # and has a non-null tags number in his posts) 
    if oldKey and oldKey != thisKey and reputation != -1 and len(tags_list) !=  0:
        # we print the user_id, his reputation, his number of unique tags and the sorted list of his tags
        print oldKey, "\t", reputation, "\t", len(set(tags_list)), "\t", sorted(list(set(tags_list)))
        del tags_list[:] # memory management
        oldKey = thisKey;
        reputation = -1

    oldKey = thisKey
    if type == "B":
        # for each line, we retrieve reputation if it is from the user file, 
        reputation = thisValue
    else:
        # or add the tag to the tags list if from the nodes file
        tags_list.append(thisValue)

# we manage the last user like the others
if oldKey != None and reputation != -1 and len(tags_list) != 0:
    print oldKey, "\t", reputation, "\t", len(set(tags_list)), "\t",  sorted(list(set(tags_list)))

