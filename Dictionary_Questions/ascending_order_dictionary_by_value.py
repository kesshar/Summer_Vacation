num=int(input("Enter a number of items in the dictionary: "))
d={}
for i in range(num):
    key=input("Enter the key: ")
    value=input("Enter the value: ")
    d[key]=value
sorted_d=sorted(d.items(),key=lambda x:x[1])
print(sorted_d)