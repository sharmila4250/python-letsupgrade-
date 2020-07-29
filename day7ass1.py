port1={21:"FTP", 22:"SSH",23:"telnet",80:"http"}
print ("Original dictionary is : ") 
print(port1)  

port2={} 

for k,v in port1.items(): 
    if v in port2: 
        port2[v].append(k) 
    else: 
        port2[v]=[k] 

print ("Dictionary after swapping is :  ")  
print("keys: values") 

for i in port2: 
   print(i, ":", port2[i]) 