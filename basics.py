#data types
a = 1
b = 1.0
c = "hello"
d = "world"

print("integer :",type(a))
print("float :",type(b))

#list comprehension
list_a = []
list_a.append(a)
list_a.append(b)

[print(type(list_a[i])) for i in range(len(list_a))]

[print(i+a) for i in range(len(list_a))]

[print(c+" "+d) for i in range(len(list_a))]

