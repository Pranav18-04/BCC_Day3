#  # WAP to accept percentage and if per>90 assign grade A > if grtr than 80 assign grade B 60 grade C and last pertage <60 -> fail
#
#
# a = int(input("1st no"))
#
#
# if a>90:
#     print("Grade A")
# elif a>80 and a<90:
#     print("Grade B")
# elif a > 60 and a < 80:
#     print("Grade C")
# else:
#     print("Fail")


#--------------------------------------------------------------------------------------------------------------------

#Dictionary

# mydict = {
#     "name" : "Om",
#     "proffesional" : "dvloper",
#     "empid" : 1001
# }
# print(mydict)
# print(type(mydict))




mydict = {
    101: "om",
    102: "Ali",
    "103": "mohit",
    "104":"sujal",
    101:"ashish",
    "104":"ashish"

}
print(mydict)       #Upfate krra hai


a = mydict[102]
# print(a)


mydict[102] = "peter"
# print(mydict[102])


# for x in mydict:
#     print(x)

# for x in mydict.values():
#     print(x)




# for x,y in mydict.items():
#     print(x,y)


# mydict["mono"] = 3257875476
# print(mydict)
#
#
#
#
# mydict.pop(101)
# print(mydict)



# name = "PrashantJha"
# print(name[0])
# print(name[1])
# print(name[-1])
# # print(name[15])       Error
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])


# s = "kfsdjrhjfb id best for practicing ld figvh"
# print(s.find("for")) # gives starting index no.
# print(s.find("python")) # default -1
# print(s.find("best"))



# j = "prsnt" , "peter" , "john"
# m = '&'.join(j)
# print(m)



# s = "Python is Highlvl programming language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())



#.format() function

# print("SubMarks")
# phy = 50
# chem = 60
# math = 80
#
# print("phy = {} chem = {} math = {}".format(phy,chem,math))
# print("phy = {0} chem = {1} math = {2}".format(phy,chem,math))
# print("phy = {x} chem = {y} math = {z}".format(x=phy,y=chem,z=math))
# total = phy+chem+math
# print(f"{total}")
# print("Rollno=" , "7".zfill(4))




# print('prashantjha777'.isalnum())  # True  alphanumeric
# print('prashantjha'.isalpha())     # True    alpha
# print('777f'.isdigit())
# print('sfgdsdsd'.islower())
# print(''.islower())
# print('PRASHANT'.isupper())
# print('My Name Is Prashant'.istitle())
# print(''.istitle())
# print(' '.isspace())
# print('Hello'.startswith("He"))
# print('Hello'.endswith("lo"))

# a = 50
# b = 30
# c = 20
# d = 10
#
# print((a+b)*c/d)
# print((a-b)*c/d)
# print(a+(b*c)/d)


# x = ['A','B','C']
# y = ['A','B','C']
# z = [1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)


# name = "prashant"
# vovels = 0
# consonent = 0
# data = ['a','e','i','o','u']
# for i in name:
#     for i in data
#         vovels+=1
#     else :
#         consonent+=1
# print(vovels)
# print(consonent)