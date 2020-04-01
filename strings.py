name = "John,Doe,is,good"

res = name.lower()
res = name.upper()
res = name.split(',',1)
first_name = res[0]
last_name = res[1]

print(name)
print(res)
print(first_name)
print(last_name)

arr = ('a','e','i','o','u')
arr = ['a','e','i','o','u']
arr = {'a','e','i','o','u'}

hell= "".join(arr)
print(hell)