import math
def toBinary(a):
    l,m=[],[]
    for i in a:
        l.append(ord(i))
    for i in l:
        m.append(int(bin(i)[2:]))
    return m
text_tst=input("Introduceti textul: ")
print(toBinary(text_tst))
