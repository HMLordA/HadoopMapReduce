#!/usr/bin/python

# Goal : find the top-10 tags, ordered by the number of threads the appear in (as we can often find
# several times the same tag in the same thread, here we will count them only once per thread)

import sys
import csv

reader = csv.reader(sys.stdin,delimiter='\t')

for line in reader:
    # if non standard length or header line, skip the line
    if len(line) != 19:
        continue
    if line[0] == "id":
        continue

    node_type = line[5]
    # we retrieve the correct thread_id, depending of the node_type
    abs_parent_id = line[0]
    if node_type != "question":
        abs_parent_id = line[7]

    tags = line[2]
    tag_list = tags.split(" ")
    for tag in tag_list:
        if tag != "":
            # print a line per tag, with its thread_id
            # we do not consider the empty tags
            # '%' will be the separator for the two subparts of the key
            # (we group the 2 infos in one key, otherwise it is not sure the same tags with the
            # same thread_ids will be group together by the shuffle-and-sort phase)  
            print "{0}%{1}\t{2}".format(tag,abs_parent_id,"1")

