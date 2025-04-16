def sum_lists(list1, list2):
    min_length = min(len(list1), len(list2))

    result_list = []

    for i in range(min_length):
        result_list.append(list1[i] + list2[i])

    return result_list


list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(sum_lists(list_a, list_b))

list_c = [10, 20, 30, 40]
list_d = [1, 2, 3]
print(sum_lists(list_c, list_d))
