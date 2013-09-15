def median(unsorted_list):
    sorted_list = sorted(unsorted_list)
    if len(sorted_list) % 2 == 0:
        median = sorted_list[(len(sorted_list)-1)/2]*.5 + sorted_list[len(sorted_list)/2]*.5
    else:
        median = sorted_list[len(sorted_list)/2]
    return median



print median([1,2,4,8])


