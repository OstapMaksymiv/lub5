def znaki(napis):
    dict1={}
    for i in napis:
        if i in dict1:
            dict1[i] += 1

        else:
            dict1[i]=1
    return dict1
print(znaki("samohzdfgdfod"))


def znaki(napis):
    dict1={}
    for i in napis:
        dict1[i]=dict1.get(i,0)+1
       # if i in dict1:
        #    dict1[i] += 1
        #
       # else:
       #     dict1[i]=1
    return dict1
dict2=znaki("samohzdsdasdfasdfgdfod")

for i in  sorted(dict2.keys()):
    print(i,dict2[i])
