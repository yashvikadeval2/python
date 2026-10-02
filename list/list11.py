#list 
# l = [1, 2, 3, 4, 5]
# list = []
# for i in l:
#     list.append(i*i)

# print(list)

#map function
# l=[1,2,3,4,5]
# def get(list):
#     return list**2
# value=map(get,l)
# for i in value:
#     print(i)

#lambda function using
# l=[1,2,3,4,5]
# value=map(lambda list:list**2,l)
# print(value)
# for i in value:
#     print(i)  

#
# l=['gautam','vivek','shailesh']
# l1=map(lambda list:list.capitalize(),l)
# print(list(l1))


# list = [1, 2, 3, 4, 5]
# list1 = [i**2 for i in list]
# print(list1)

# nums = [10, 3, 192, 55, 20, 77 , 91]
# def divisible(i):
#     return True if i%5==0 else False
# v = filter(divisible, nums)
# print(list(v))

# ages = [5, 12, 17, 18, 24, 32]

# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True

# adults = filter(myFunc, ages)

# for x in adults:
#   print(x)

# def mygenerator():
#   print('First item')
#   yield 10
#   print('Second item')
#   yield 20
#   print('Last item')
#   yield 30
# gen = mygenerator()
# for i in gen:
#   print(i)

# def get_sequence_upto(x):
#   for i in range(x):
#     yield i
# a=get_sequence_upto(10)
# for i in a:
#   print(i)

# a1 = {12,13,14}
# a2 = [21,22]
# a1.update(a2)
# print(a1)

n=int(input("enter n:"))

for i in range(n):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        print(i)