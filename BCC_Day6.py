# # Q.10. What will be the output of the following code snippet?

# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20

# print(sum)


##2
# def f(i , values = []) :
#   values.append(i)
#   print(values)
# f(1)
# f(2)
# f(3)



##3
# def func(value , values) :
#   var = 1
#   values[0] = 44
# t = 3
# v = [1,2,3]
# func(t,v)
# print(t,v[0])



##4
# dict = {'c':97 , 'a':96 , 'b':98}
# for _ in sorted(dict) :
#   print (dict[_])


##5
# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))

# A. 1
# B. 2
# C. 3
# D. 4




##6
num = [1,2,3,4]
prod = 1
for i in (num) :
  prod = prod * num[i-1] /num[i]
print(prod)
