
my_list = [i for i in range(1,40+1)]
# print(my_list)

def random_list(my_list):
    import random
    mylist = my_list[:]
    randomlist = []
    for _ in range(len(my_list)):
        i = random.choice(mylist)
        randomlist.append(i)
        mylist.remove(i)
    # print(randomlist)
    # print(mylist)
    # print(my_list)
    return randomlist

mylist = random_list(my_list)
def issorted(mylist):
    if mylist==[] or len(mylist)==1:
        return True
    for i in range(len(mylist)-1):
        if mylist[i]>mylist[i+1]:
            return False
    return True

def first_list_is_empty(list1,mid, list2):
    if list2[0]>mid:
        return [mid] + list2
    return list2 + [mid]

def quick_sort(my_list):
    
    if my_list==[] or len(my_list)==1:
        return my_list
    elif len(my_list)==2:
        if my_list[0] > my_list[1]:
            return [my_list[1], my_list[0]]
        else:
            return my_list
    elif issorted(my_list):
        return my_list
    else:
        mid = my_list[len(my_list)//2]
        list1 = []
        list2 = []
        for i in my_list:
            if i==mid:
                continue
            elif i<mid:
                list1.append(i)
            else:
                list2.append(i)
        if list1==[]:
            return first_list_is_empty(list1, mid, list2)
        elif list2==[]:
            return first_list_is_empty(list2,mid,list1)
        elif list1[0]>list2[0]:
            answer = quick_sort(list2) + [mid] + quick_sort(list1)
        answer = quick_sort(list1) + [mid] + quick_sort(list2)
        if issorted(answer):
            return answer
        return quick_sort(answer)
    
sorted_list = quick_sort(mylist)
print(sorted_list)
print(my_list)
flag=False
for i in range(len(my_list)):
    if sorted_list[i]!=my_list[i]:
        print("Error: Lists not sorted correctly")
        flag=True
        break
if not flag:
    print("Lists sorted correctly")