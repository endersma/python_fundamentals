# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

# def biggie_size(arr):
#     new_arr = []
#     for num in range(0, len(arr), 1):
#         if arr[num] > 0:
#             new_arr.append('big')
#         else:
#             new_arr.append(num)
#     return new_arr

# print(biggie_size([-1,4,3,-5,2,7,-3,-8]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# def count_positives(pos_array):
#     sum_pos = 0
#     for val in pos_array:
#         if val > 0:
#             sum_pos += 1
#     pos_array[len(pos_array) - 1 ] = sum_pos
#     return pos_array

# print(count_positives([1,2,4,-1,3]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# def sum_total(user_arr):
#     total = 0
#     for num in user_arr:
#         total += num
#     return total

# print(sum_total([1,2,4,5]))

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

# def sum_avr(user_arr):
#     total = 0
#     avr = 0
#     for i in range(0, len(user_arr), 1 ):
#         total += user_arr[i]
#     avr = total/len(user_arr)
#     return avr

# print(sum_avr([1,2,4,5]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# def length(user_arr):
#     count = 0
#     for i in user_arr:
#         count = len(user_arr)
#     return count

# print(length([1,2,5,7,8,2,4]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# def minimum(user_arr):
    
#     if len(user_arr) == 0:
#         return False
#     min_val = user_arr[0]
#     for i in user_arr:    
#         if i < min_val:
#             min_val = i
#     return min_val

# print(minimum([5,2,5,7,8,2,4]))
# print(minimum([]))

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

# def maximum(user_arr):
    
#     if len(user_arr) == 0:
#         return False
#     max_val = user_arr[0]
#     for i in user_arr:    
#         if i > max_val:
#             max_val = i
#     return max_val

# print(maximum([5,2,5,7,8,2,4]))
# print(maximum([]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# def ultimate_analysis(user_arr):
#     ult_list = {
#         'sumTotal': None,
#         'average' : None,
#         'minimum' : None,
#         'maximum' : None,
#         'length' : 0
#     }
#     if len(user_arr) == 0:
#         return ult_list
#     else:
#         ult_list['minimum'] = user_arr[0]
#         ult_list['maximum'] = user_arr[0]
#         ult_list['sumTotal'] = 0
#     for i in user_arr:
#         if i < ult_list['minimum'] :
#             ult_list['minimum'] = i
#         elif i > ult_list['maximum']:
#             ult_list['maximum'] = i

#         ult_list['sumTotal'] += i
#         ult_list['length'] = len(user_arr)
#     ult_list['average'] = ult_list['sumTotal']/len(user_arr)
#     return ult_list

# print(ultimate_analysis([1,2,4,5]))
# print(ultimate_analysis([]))
# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

# def reverse_list(user_arr):
#     test_var = 0
#     pos_1 = 0
#     pos_end = 0
#     for i in user_arr:
#         pos_1 = user_arr[0]
#         pos_end = len

# This is tough. I give up
    