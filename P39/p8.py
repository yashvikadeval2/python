# Count words in a sentence.

n=input("Enter a string: ")

count = 1

for i in n:
    if i==" ":
        count=count+1

print("count words =",count)