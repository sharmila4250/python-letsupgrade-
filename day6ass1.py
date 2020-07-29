list1=[1,2,3,4,5,7,8]
list2=["a","b","c","d","e"]
res = {list1[i]: list2[i] for i in range(min(len(list1),len(list2)))} 
print("First list is"+str(list1))
print("Second list is"+str(list2))
print("Combined list is"+str(res))
  