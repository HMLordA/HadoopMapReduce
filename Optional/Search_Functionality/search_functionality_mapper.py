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
import re
import csv

reader = csv.reader(sys.stdin,delimiter='\t')
re_delimiters = '\W+' # used for regex to split on non-alphanumeric characters

for line in reader:
    # if non standard length or header, skip the line
    if len(line) != 19:
        continue
    if line[0] == "id":
        continue

    body = line[4]
    title = line[1]
    node_type = line[5]

    # we find the correct thread_id, depending of the node_type 
    abs_parent_id = line[0]
    if node_type != "question":
        abs_parent_id = line[7]
    
    # we create list of words in body and title 
    words_in_body = re.split(re_delimiters,body)
    words_in_title = re.split(re_delimiters,title)

    # we print each not-numerical not-empty word, with its thread_id 
    for word in words_in_body:
        if not word.isdigit() and word != "" :
            print "{0}\t{1}".format(word.lower(),abs_parent_id)
    for word in words_in_title:
        if not word.isdigit() and word != "":
            print "{0}\t{1}".format(word.lower(),abs_parent_id)


