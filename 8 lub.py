def find(list1,wartosc1):
    list2=[]
    for i in range(len(list1)):
        if list1[i]==wartosc1:
            list2.append(i)
    return(list2)

print(find([1,3,56,6],10))

