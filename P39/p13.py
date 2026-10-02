#13. Find keys with maximum value.


l = {"A": 50,"B": 80,"C": 70,"D": 90,"E": 60}

max = 0
m_key = ""

for key in l:
    if l[key] > max:
        max = l[key]
        m_key = key

print("Key with maximum value:", m_key)
print("Maximum value:", max)