#!/usr/bin/python

# Goal : create an improved reverted index on the discussion forum data:
# - include words from both body and title of a message
# - give the thread_id of a post instead of the post_id (ease the index as same words can be used several
# times in a single thread, and as we are more interested by the context where the word will appear instead
# of its exact location)
# - delete doublons in the thread_id list associated with a word (we do not need to know a word appears
# several times in a thread)
# - associate the number of threads where it appears to a word (useful when words appears in 10s or 100s of threads,
# to have an idea of its frequency)
# - sort the thread_id list by numerical value instead of string value, to ease the read
# - delete the numerical keys of the index (we are interested by real words)

import sys

oldKey = None
nodes_list = [] # list of the thread_ids for the current word

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # if non standard length, skip the line
        continue

    thisKey, thisValue = data_mapped

    # before moving to the next word
    if oldKey and oldKey != thisKey:
        # print the sorted list of unique thread_ids (unicity done by using a set instead of a list)
        print oldKey, "\t", len(set(nodes_list)),"\t", sorted(list(set(nodes_list)))
        del nodes_list[:] #memory management
        oldKey = thisKey;

    oldKey = thisKey
    # for each word, we add the current thread_id (as an int) to the thread_id list
    nodes_list.append(int(thisValue))

# we manage the last word like the others
if oldKey != None:
    print oldKey, "\t", len(set(nodes_list)),"\t", sorted(list(set(nodes_list)))
    del nodes_list[:]

