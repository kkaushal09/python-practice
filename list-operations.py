import re

lst = ["city",123,123,123,0,0,0,6,6,6,98,97,97,97,"bangalore"]

pattern = r'^([a-zA-Z])+$'

def removestr(lst):
  print(lst)
  lst1 = []
  for i in lst:
    print(i)
    istr = str(i)
  #  pattern = re.compile("^([a-zA-Z])+$")
  # pattern.match(i)
  # st = re.i(.*[a-zA-z])
  
    if not re.match(pattern, istr):
      # print(i)
      lst1.append(i)
    # else:
    # print("Not string")
      # lst1.append(i)
      print(lst1)
    return lst1

lst_new = removestr(lst)
    
print(lst_new)
# print(lst1)
# s=set(lst1)
# print(s)
#for sort    
srt = []
for i in range(0,len(lst1)):
  x = lst1[i]
  y = lst1[i+1]
  print(x,y)
  if x > y:
    srt[i] = y
  else:
    srt[i] = x
    
#2nd largest and 2nd smallest number

# for i in lst1:
#   lar = lst1[i]
#   sec_lar = lst1[i] 
#   if lst1[i+1] > lst1[i]:
#     lar = lst1[i+1]
    
# second largest number
lst_len = len(lst1)
sec_lar = lst1[lst_len-1]
sec_small = lst1[1]
    
