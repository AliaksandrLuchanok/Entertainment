'''
Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
Надо вернуть их пересечение [1, 2, 2, 3] (порядок неважен)
'''
use_string = input("Enter your string, please: ")
inverted_list = list()
for i in range(len(use_string)):
  inverted_list.append(use_string[-1-i])
print(*inverted_list)