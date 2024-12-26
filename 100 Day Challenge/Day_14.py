nums = input('Enter all the Numbers from which you want Find the Highest Number from.\n---:')
num_list = nums.split()
# print(num_list)
highest_num=int(num_list[0])
for num in num_list :
    if int(num) > highest_num :
        highest_num = int(num)
print(f'The Highest Number is : {highest_num}')

########################################################3
#aveage height
student_heights = input("Enter All The Heights: ")
std_height_list = student_heights.split()
average_height = 0
for height in std_height_list:
    average_height += int(height)
average_height /= len(std_height_list)
print(f' The Average Height is {round(average_height)}')