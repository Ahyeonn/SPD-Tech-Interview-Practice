'''
Given two arrays a and b of numbers and a target value t, 
find a number from each array whose sum is closest to t.
Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  
⇒  [13, 6] or [4, 17] or [5, 14]
'''

def find_closest_sum_of_t(arr_1, arr_2, t):
    lst = []
    count = 0
    idx_of_arr_1 = 0
    idx_of_arr_2 = 0

    while count != len(arr_1):
        lst.append([arr_1[idx_of_arr_1], arr_2[idx_of_arr_2]])
        idx_of_arr_2 += 1
        if idx_of_arr_2 == len(arr_2):
            idx_of_arr_2 = 0
            count += 1
            idx_of_arr_1 += 1
    
    diff = 10000
    indexing = 0
    answer_lst = None
    while indexing != len(lst):
        idx = (lst[indexing][idx_of_arr_2]) + (lst[indexing][idx_of_arr_2 +1]) 
        abs_diff = abs(t-idx)
        if diff > abs_diff:
            diff = abs_diff
            answer_lst = [lst[indexing][idx_of_arr_2], lst[indexing][idx_of_arr_2 +1]]
            if diff == 0:
                return answer_lst
        indexing += 1
    return answer_lst

# print(find_closest_sum_of_t([9, 13, 1, 8, 12, 5, 2], [3, 17, 4, 14, 6], 20))
print(find_closest_sum_of_t([3, 13, 14, 2], [3, 17], 20))