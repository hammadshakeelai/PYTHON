def issorted(my_list):
    if my_list==[] or len(my_list)==1:
        return True
    for i in range(len(my_list)-1):
        if my_list[i]>my_list[i+1]:
            return False
    return True
def selection_sort(my_list):
    if issorted(my_list):
        return my_list
    for i in range(len(my_list)-1):
        if my_list[i]>my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    return selection_sort(my_list)
my_list = [4, 3, 2, 1,9,7,8,6,5]

print(selection_sort(my_list))  # Output: [1, 2, 3, 4]