def sum_lists(list1, list2):
    max_length = max(len(list1), len(list2))

    padded_list1 = list1 + [0] * (max_length - len(list1))
    padded_list2 = list2 + [0] * (max_length - len(list2))

    result_list = [padded_list1[i] + padded_list2[i] for i in range(max_length)]

    return result_list


list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(sum_lists(list_a, list_b))

list_c = [10, 20, 30, 40, 50]
list_d = [1, 2, 3]
print(sum_lists(list_c, list_d))
