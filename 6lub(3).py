def Zad3(*args):
    for Zad3 in args:
       print(Zad3)
Zad3(3,"Mafin",7,[12,123],12.34)


def max(num1,*args):
    m=num1
    for i in args[1:]:
        if m<i:
            m=i
    return m
print(max(1,0,0,-1))




