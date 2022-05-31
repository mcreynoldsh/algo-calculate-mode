from ast import arg


def calculate_mode(arg_list):
    count= 0 
    largest_count= 0
    curr_largest=[]
    unique_list = []
    for x in arg_list:
        if unique_list.count(x) == 0:
            unique_list.append(x)

    for n in unique_list:
        if arg_list.count(n) > largest_count:
            largest_count=arg_list.count(n)
            curr_largest.clear()
            curr_largest.append(n)
        elif arg_list.count(n) == largest_count:
            curr_largest.append(n)    
    
    return curr_largest


