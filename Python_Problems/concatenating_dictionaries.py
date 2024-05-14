n=int(input("Enter the number of items in the dictionary to concantenate: "))
print("For first dictionary:")
d1={}
d2={}
for i in range(n):
    key=input("Enter the key")
    value=input("Enter the value")
    d1[key]=value
for i in range(n):
    key=input("Enter the key")
    value=input("Enter the value")
    d2[key]=value
d3={}
concatenated_dict = {}
for key, value in d1.items():
    concatenated_dict[key] = value
for key, value in d2.items():
    concatenated_dict[key] = value
print (concatenated_dict)