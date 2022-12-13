def dodawanie(a,b):
   return a+b

def odejmowanie(a,b):
    return a - b

def mnozenie(a,b):
    return a * b

def dzielenie(a,b):
    if b ==0:
        return
    else:
        return a / b
kalkulator={'+':dodawanie,'-':odejmowanie,'*':mnozenie,'/':dzielenie}
u1=float(input("wprowadz liczbe A"))
u2=float(input("wprowadz liczbe B"))
u3=input("Podaj dzialania")
print(kalkulator[u3](u1,u2))