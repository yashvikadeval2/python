# Count frequency of each character

# s=input("Enter a string: ")

# for i in s:
#     cnt=0
#     for j in s:
#         if i==j:
#             cnt=cnt+1
#     print(i,"=",cnt)

s=input("Enter a string: ")
x=""
for i in s:
    if i not in x:
        cnt=0
        for j in s:
            if i==j:
                cnt=cnt+1
        print(i,"=",cnt)
        x=x+i

