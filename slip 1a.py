mylist=[]
n=int(input("Enter the number of items in list"))
#To accept the users list
for x in range(0,n):
    ele=int(input())
    mylist.append(ele)
print("original list: ",mylist)

#to remove duplicates
dup=[*set(mylist)]
print("Duplicates removed: ",dup)

