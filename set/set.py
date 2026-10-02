# s={1,2,3,4,5}
# print(s)

# s = {"apple", "banana", "cherry"}
# for x in s:
#   print(x)

#add
# s = {"apple", "banana", "cherry"}
# s.add("orange")
# print(s)

#remove
# s = {"apple", "banana", "cherry"}
# s.remove("apple")
# print(s)

#loop
# s = {"apple", "banana", "cherry"}
# for i in s:
#     print(i)

#union
# s={1,2,3}
# s1={4,5,6}
# s2=s.union(s1)
# print(s2)

#update
# s1={1,2,3}
# s2={4,5,6}
# s1.update(s2)
# print(s1)

#intersection
# s = {1,2,3}
# s1 = {1,2,5,4}
# s2 = s1.intersection(s)
# print(s2)

#differance
# s={1,2,3}
# s1={2,4,1}
# s2=s.difference(s1)
# print(s2)

#symmetric_difference
# s={1,2,3}
# s1={2,4,1}
# s2=s.symmetric_difference(s1)
# print(s2)

#frozenset
# x = frozenset({"apple", "banana", "cherry"})
# print(x)
# print(type(x))

#discard
# s={1,2,3}
# s.discard(2)
# print(s)

#pop
# s={1,2,3,4,5}
# s.pop()
# print(s)

#clear
# s={1,2,3}
# s.clear()
# print(s)

#del
# s={1,2,3}
# del s
# print(s)

#isdisjoint
# s=frozenset({1,2,3})
# s1=frozenset({4,5,6})
# print(s.isdisjoint(s1))

#issubset
# s=frozenset{1, 2}
# s1=frozenset{1, 2, 3, 4}
# print(s.issubset(s1))       
# print(s<=s1)      

#issuperset
# s=frozenset({1,2,3})
# s1=frozenset({1,2})
# print(s.issuperset(s1))
# print(s>=s1)
# print(s>s1)

#difference_update
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.difference_update(y)
# print(x)

#intersection_update
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)