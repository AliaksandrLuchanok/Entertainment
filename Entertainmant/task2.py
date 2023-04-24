'''
Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
Надо вернуть их пересечение [1, 2, 2, 3] (порядок неважен)
'''
def intersection_Lists (list1,list2):
  max_len = len(list1) + len(list2)
  intersection_list = list()
  list1 = sorted(list1)
  list2 = sorted(list2)
  flag1 = 0
  flag2 = 0
  for i in range(max_len-1):
    if list1[i + flag1] == list2[i + flag2]:
      intersection_list.append(list1[i + flag1])
    elif list1[i + flag1] > list2[i + flag2]:
      flag1 -= 1
    elif list1[i + flag1] < list2[i + flag2]:
      flag2 -=1
    if i + flag1 + 1 == len(list1) or i + flag2 + 1 == len(list2):
      return intersection_list
 

# Пользовательский ввод:
# use_size1 = int(input("Enter size of use_list1, please: "))
# use_list1 = [int(input(f'Input your {i} number use_list1: ')) for i in range(use_size1)] 
# use_size2 = int(input("Enter size of use_list2, please: "))
# use_list2 = [int(input(f'Input your {i} number use_list2: ')) for i in range(use_size2)] 
# print(*intersection_Lists (use_list1, use_list2))
print(*intersection_Lists ([1, 2, 3, 2, 0], [5, 1, 2, 7, 3, 2]))