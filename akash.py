def send(obj):
	return obj['size']

def send2(obj):
	return obj['name']

my_list = [{'name': "foo", 'size': 5}, {'name': "bar", 'size': 3}, {'name': "baz", 'size': 7},{'name': "aaz", 'size': 7}]
my_list.sort(key=lambda x:[x['size'],x['name']])
#my_list.sort(key=send2)
print(my_list)

lst=["akash","Tanwaini","sdf"]
x="##".join(lst)
print(x)
x=x.replace("##","  --  ")
x=" sdf  "
print(len(x))
x=x.strip()
print(len(x))
print(x)




