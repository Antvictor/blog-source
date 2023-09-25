a = [1,2,"test",0.5]
print(a[-1])
a.append("hello")
print(a)
a.insert(2, "world")
print(a) 
del a[3]
print(a)
print(a.pop())
print(a.pop(2))
a.insert(2,"test")
a.append("test")
print(a) 
a.remove("test")
print(a) # [1, 2, 0.5, 'test']
a.remove("test")
print(a) # [1, 2, 0.5]

tuple = (1,2,"2",0.2)
print(tuple)
print(tuple[2])
# del tuple[2]
maps = {'name':"Ant", 'age':25, 2:3}
print(maps)
print(maps[2])
print(maps['name'])
# print(maps[3])
print(maps.keys())
print(maps.values())

print(maps.get(3, 3))


maps['new'] = 'hello'
print(maps) # 

maps[2] = 4
print(maps)

sets = {"1","sss",2,3,0.5}
print(sets)

sets.add("1")
print(sets)

sets.add(22)
print(sets)

sets.add("123")
print(sets)

sets.update("123")
print(sets)

maps1 = {"test":"sets"}
sets.update(maps1)
print(sets)

sets.remove("test")
print(sets) 
print(sets.pop())
sets.discard("test")
print(sets)
# sets.remove("test") # 报错
del sets
# print(sets)

