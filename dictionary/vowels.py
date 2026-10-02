word="programming"
vowels=('a','e','i','o','u','A','E','I','O','U')
t=tuple(word)
print(t)

for i in t:
    if i not in vowels:
        print(i)