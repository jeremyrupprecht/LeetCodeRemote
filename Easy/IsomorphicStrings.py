import string

s = "foo"
t = "bar"

Dict1 = {}
Dict2 = {}

zipped = zip(s, t)

for a, b in zipped:

    # case 1, both letters are new, create a new mapping

    if (not a in Dict1) and (not b in Dict2):
        Dict1[a] = b
        Dict2[b] = a

    elif (Dict1.get(a) != b) or (Dict2.get(b) != a):
        print(False)
        


print("we done")

    # case 2, find a repeated letter, its dictionary mapping lines up

    # case 3, find a repeated letter, its not in the dicionary mapping does not line up
