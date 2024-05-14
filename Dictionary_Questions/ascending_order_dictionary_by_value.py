num=int(input("Enter a number of items in the dictionary: "))
d={}
for i in range(num):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    d[key]=value
sorted_d=sorted(d.items(),key=lambda x:x[1])
print(sorted_d)
# d2=d1.copy is a command used to make a refrence where we have taken a snapshot of the situation and changes in d1 will not affect d2
# whereas d2=d1, in this changes in d1 will affect d2 
