# for i in range(1,5):#i=3
#     if i == 3:
#         break
#         #try (continue)
#     print(i)


# for i in range(1,6):
#     if i == 3:
#         continue
#     print(i , (6-i))
#
#
# for i,j in zip(range(1,6) , range(5,0,-1)):
#     if i == 3 and j==3:
#         continue
#     print(i," " ,j)


# syntax:
#
# initialization
# whileCondition:
#   statement
#   inc/dec


# i=1
# while i<=5:
#     print(i)
#     i=i+1



# username=''
# password=''
# while(username !="admin" and password !="hello"):
#     username = input("Enter username :")
#     password = input("Enter passsword :")







# n = int(input("enter number:"))
# sum=0
# i=1
# while i<=n:
#     sum = sum + i
#     i = i+1
# print("The sum of first 10 numbers is:",sum)


# name = prashant
# o/p = prashnt

# newname = " "
# name = "prashant"
# for i in name :
#     if i not in newname:
#          newname += i
# print(name)
# print(newname)







#string reversal

# name ="Omkar"
# reverse = " "
# for int  name:
#     reverse+=(5-i)


mycart = [10, 20, 200, 300, 800, 60, 700]

for i in mycart:
    if i > 400:
        print("This my purchased cart item")
        continue
    print(i)



# name = "omkar"
# pal = " "

# for i in name:
#     pal = i + pal
# print(pal)
# if pal == name:
#     print("palindrome")
# else:
#     print("not palindrome")



# name = input("Enter name")

# if name ==name[::-1]:
#   print("palindrome")
# else :
#   print("not palindrome")




# # ANAGRAM QUESTION
# x = "listen"
# y = "silent"
# for i in x:
#     if i not in y:
#         print("not anagram")
        
#     else:
#         print("anagram")



# mylist = {"name":"om" , "age":30}
# print(mylist)
# mylist["name"] = "omkar"
# print(mylist)
# mylist['city'] = "Pune"
# print(mylist)

# mylist.get("name")
# value = "omkar"
# if value in mylist:
#     print("yes")
# else:
#     print("no")


# for i in range(1,4):
#   for j in range(1,4):
#     print(i,end=" ")
#   print()

n = int (input("Enter number"))
for i in range(1,n+1):
    for j in range(1,n+1):
      print(chr(64+i),end=" ")
    print()

print("---------------------------------------------------------------------------------")
n = int (input("Enter number"))
for i in range(1,n+1):
    for j in range(1,n+1):
      print(n+1-i,end=" ")
    print()


n = int (input("Enter number of rows"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
      print("*",end=" ")
    print()