#!/usr/bin/python

# Goal : find the top-10 tags, ordered by the number of threads the appear in (as we can often find
# several times the same tag in the same thread, here we will count them only once per thread)

import sys

old_key = None
old_abs_parent_id = None
N = 10 # the number of elements of the top-N
top_N_list = [(0,0) for i in range(0,N)] # the current top-10 list of couples (nb_of_occurences_in_threads,tags)
threads_total_count = 0 # the number of threads where we find the current tag

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # if non standard length, skip the line
        continue
    current_key_data = data[0].split("%")
    tag = current_key_data[0]
    current_abs_parent_id = current_key_data[1]
    tag_count = int(data[1])

    # before moving to the next tag
    if old_key and old_key != tag:

        # we add the current couple (nb_of_occurences_in_thread, tag) in the top-10, sort the list 
        # and keep the new top-10
        top_N_list.append((threads_total_count,old_key))
        new_top_N_list = sorted(top_N_list,key = lambda tag_pair : tag_pair[0])
        del top_N_list[:] #memory management
        top_N_list = new_top_N_list[1:N+1]
        threads_total_count = 0
        old_abs_parent_id = None 
    
    # for each first occurence of a thread_id for the current tag, we increment the thread counter
    old_key = tag
    if old_abs_parent_id == None or old_abs_parent_id != current_abs_parent_id:
        threads_total_count += tag_count
    old_abs_parent_id = current_abs_parent_id

# we manage the last tag like the others
if old_key != None:
        top_N_list.append((threads_total_count,old_key))
        new_top_N_list = sorted(top_N_list,key = lambda tag_pair : tag_pair[0])
        del top_N_list[:]
        top_N_list = new_top_N_list[1:N+1]

# we write the top-10 list, starting with the tag present in the biggest number of threads
for tag_pair in reversed(top_N_list):
    threads_total_count = tag_pair[0]
    tag = tag_pair[1]
    print tag,'\t',threads_total_count


