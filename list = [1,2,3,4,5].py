a = ["satu","dua","tiga","empat", "lima"]
print(a)
for x in a:


list = [1,1,3,3,4,]
print(list.count(3))

print("\n")

list = [1,2,3,4,5,]
print(list.index(5))
print(len(list))

member = 3 in list
print(member)

memeber =3 not in list
print(member)

print(max(list))
print(mix(list))

v = [1,2,3,4,5]
v+=[6]
print(v)
v.insert(2,10)
print(v)
v.append(11)
print(v)

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = list1 + list2
print(list3)
a = list2 + list1
print(a)
list1.extend(list2)
print(list1)

list.extend("slow")
print(list)

x,y,z = [1,2,3]
print(y)
print(z)

list = [1,2,[3,4,5]]
print(list)
list[1] = 0
print(list)

list[2][1] = 6
print(list)

n=["12"]
a=n*5
print(a)

data = ["saya", "makan","'nasi"]
print(data)
join_list = " ".join(data)
print(join_list)

b =tuple(data)
print(b)

list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
print(list1 == list2)

list1.remove(3)
print(list1)

h = [1,2,3,4,5]
c= h.pop()
print(c)
print(h)

a = h.pop(2)
print(a)
print(h)

list = [1,4,3,5,2]
print(list)
print(sorted(list))
print(sorted(list, reverse=True))

list = [1,4,3,5,2]
a = b
print(a)
print(b)
print(id(b))
print(id(a))

b.clear()
print (b)
print (a)

  