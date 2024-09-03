# Running code https://onecompiler.com/python/42r4nteke
import re

lst = ["city",123,123,123,0,0,0,6,6,6,98,97,97,97,"bangalore"]

pattern = r'^([a-zA-Z])+$'

def isstr(str):
  if re.match(pattern, str):
    return True
  return False
  
def removestr(lst):
  lst_num = []
  for i in lst:
    str_i = str(i)
    check_str = isstr(str_i)
    if not check_str:
      lst_num.append(i)
  return lst_num

def lst_sort(lst):
  lst_len = len(lst)
  for i in range(0, lst_len):
    # print(f"I:{i}")
    for j in range(i+1, lst_len):
      # print(f"J:{j}")
      # print(lst[i], lst[j])
      if lst[i] > lst[j]:
        print(f"Swapping {lst[i]} and {lst[j]}")
        # temp = lst[i]
        # lst[i] = lst[j]
        # lst[j] = temp
        lst[i], lst[j] = lst[j],lst[i]
  return lst
  
def n_element(lst,*args):
  len_lst = len(lst)
  # print(args)
  # print(len_lst)
  for arg in args:
    if arg >= 0:
      print(f"Element at pos {arg} is {lst[arg]}")
    if arg < 0:
      x = abs(arg)
      print(f"Element at pos {arg} is {lst[len_lst-x]}")      

  
lst_new = removestr(lst)
print(f"List without string: {lst_new}")

lst_new = set(lst_new)
lst_new = list(lst_new)
# print(f"Sorted list:{lst_new}")
sort_lst = lst_sort(lst_new)
print(f"Sorted list:{sort_lst}")


x = n_element(sort_lst,1,3,-3)
