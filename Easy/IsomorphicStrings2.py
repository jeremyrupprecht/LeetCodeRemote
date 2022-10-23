import string

s = "badc"
t = "baba"

zipped = zip(s, t)

for a, b in zipped:
    s = s.replace(a, b)
    
print(s)

if (s == t):
    print(True)
else:
    print(False)
