myList = ['Prshnt' , "Om" , "Albash" , "Rites" , "Sujal", 77 , 50.28]
# print(myList)
# print(type(myList))
# print(myList[1])
# print (myList[-1])
# print(myList[2:5])
# print(myList[:4])
# print(myList[1:])
# print(myList[1:3:5])
# print(myList[:])
# print(myList[::-1])

# myList.append('Harish')
# myList.append('Laxman')
# print(myList)
# myList.insert(1,"Sanket")
# print(myList)
#
# myList.remove('Sanket')
# print(myList)

# newList = myList.copy()
# print(myList)
# print(newList)



# MULTIDIMENSIONAL LIST
# mylist = [['Om' , 'Ali'] , ['99.70'] , [4275676 , 'YYY']]
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])


# list1 = ['Om' , 'Ali']
# print(list1*2)
#
# list2 = [50,49,99]
# print(list1 + list2)
#
# del list2[2]
# print(list2)
#
# del list2
# # print(list2)    #Error

# list1.clear()
# print(list1)

# --------------------------------------------------------------------------------------------------------------------

# name = "Om"
# print(name)
# myname = list(name) #TYPECASTING
# print(myname)


#-------------------------------------------------------------------------------------------------------------------


# #Sorting Example
# mylist = [22,4,5,676,9]
# mylist.sort()
# print(mylist)
# mylist.sort(reverse = True)
# print(mylist)

#----------------------------------------------------------------------------------------------------------------

# #Address
# math = 50
# print(id(math))
# phy = 50
# print(id(phy))      # Python has Memory <Management System


#-----------------------------------------------------------------------------------------------------------------------


#Alising means assigning one variable reference to another var

# mylist = [22,4,5667,7,8,76,5]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))





# 2 types of spcl oprtr in py : Membership oprtr and spcl oprtr
# memb oprtr = 1.in , 2.not in

# name = 'Om'
# print('Z' in name)
# print('Z' not in name)


# for i in range(1,11):
#     print([i*2] , [i*3] , [i*4] , [i*5] ,  [i*6])
# print("-----------------------------------------------------------------------------------------")
# for i in range(1, 11):
#     print([i*9])




#Prog to find pos neg or zero no.

# no = int(input("Enter any no,"))
# if no>0:
#     print("Positive")
# if no<0:
#     print("Negetive")
# if no == 0:
#     print("Zero")




# # Prog for working day and Weekend
#
# y = input("Enter Day")
# if y== ('Sat' and 'sun'):
#     print("Weekend")
# else:
#     print ("WeekDay")

#
#
# # WAAP to accept 3 ppr marks and calculate total
#
#
# math = int(input("Enter marks"))
# phy = int(input("Enter marks"))
# bio = int(input("Enter marks"))
#
# total = math+phy+bio
# percent = int(total/3)
#
# if(percent>60):
#     print("Eligible")
# else:
#     print("NotEligible")




# WAP to accept 5 df value in 5 df var and check max value and print by using simple if statement


# a = int(input("1st no"))
# b = int(input("1st no"))
# c = int(input("1st no"))
# d = int(input("1st no"))
# e = int(input("1st no"))
#
# if (a>b and a>c and a>d and a>e):
#     print ("a")
# if (b>a and b>c and b>d and b>e):
#     print ("b")
# if (c>a and c>b and c>d and c>e):
#     print ("c")
# if (d>a and d>c and d>b and d>e):
#     print ("d")
# else:
#     print("e")







