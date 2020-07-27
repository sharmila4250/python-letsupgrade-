list1 = [1, 5, 6, 9, 11] 
list2 = [3, 4, 7, 8, 10] 

print ("The original list 1 is : " + str(list1)) 
print ("The original list 2 is : " + str(list2)) 

a= len(list1) 
b= len(list2) 
res = [] 

i=0; j=0;

while i < a and j < b: 
    if list1[i] < list2[j]: 
      res.append(list1[i]) 
      i=i+1
    
    else: 
      res.append(list2[j]) 
      j=j+1

res = res + list1[i:] + list2[j:] 
print("Merged list is ;"+str(res))