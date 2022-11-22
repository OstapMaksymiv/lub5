sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}
for key,values in sample_dict.items():
    print(f'{key:<10}:{values:>10}')
print()
for key in sample_dict.keys():
    print(key,sample_dict[key])
print()
dict={}
lista=["age","salary","name",]
for key in lista:
    if key in sample_dict:
        dict[key]=sample_dict[key]
print(dict)
dict={}
for i in lista:
    del sample_dict[i]
print(sample_dict)
if "Jones" in sample_dict.values():
    print("jest")
else:
    print("no")
sample_dict.update({"city"})
print(sample_dict)