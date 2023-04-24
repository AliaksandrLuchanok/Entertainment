# Напишите функцию, которая переворачивает строку
def inverted_String ():
  use_string = input("Enter your string, please: ")
  inverted_list = list()
  for i in range(len(use_string)):
    inverted_list.append(use_string[-1-i])
  print(*inverted_list)
inverted_String ()