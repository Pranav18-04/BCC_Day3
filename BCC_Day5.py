# def add():
#   n1 = int(input("Enter n1:"))
#   n2 = int(input("Enter n2:"))
#   print("Add =",n1+n2)
#   sum = n1+n2
#   mul = n1*n2
#   sub = n1-n2
#   div = n1/n2
#   return sum,mul,sub,div #IT IS OPTIONAL , NOT MENDATORY
# result = add()
# print(result)

#IN PYTHON WE CAN PASS 4 TYPES OF ARGUMENTS
    # POSITIONAL ARGU , KEYWORD ARGU , DEFAULT ARGU , VARIABLE LENGTH ARGU(VARIABLE NO OF ARGU)


#  POSITIONAL ARGU : 
# def personalInfo (fname , lname):
#   print("FirstName = " , fname)
#   print("LastName = " , lname)
# personalInfo("Om" , "Ali")


#KEYWORD ARGU
# def personalInfo (fname , lname):
#   print("FirstName = " , fname)
#   print("LastName = " , lname)
# fname = "om"
# lname = "Ali"
# personalInfo(fname , lname)


# #DEFAULT ARGU
# def cityName(city):
#   print(city)
# cityName("Karachi")
# cityName("Nagpur")
# # cityName() #Error ayega



# #VARIABLE LENGTH ARGU
# def studentName(*name):
#   print(name) 
# studentName("Om" , "Ali" , "Kunal" , "Rites" , "Sujal") #TOUPLE TYPE HAI



myList = [5,6,43,3,5,6,78]
#search element 7
n = len(myList)
def searchele(target):
  for i in range(len(myList)):
    if target == myList[i]:
      return i
  return -1
result=searchele(8)
if result == -1:
  print("Element not found")
else:
  print("Element found at index" , result)
print (result)





