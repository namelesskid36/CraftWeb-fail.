a = {1,2,3,4,5}
a.add(6)
a.add("Nepal")
print(a)
b = {6,7,8,9,10}
a.update(b)
print(a)
a.remove(5)
print(a)
b=a.copy()
print(b)
b.clear()
print(b)


A={'a','b','c','d','e'}
B={'f','b','c','d','e'}
print(A.difference(B))
print(A.intersection(B))
print(A.isdisjoint(B))

removed_element = a.pop()
print(removed_element)
y= {'a','b','c','d'}
removed_element_y =y.pop()
print(removed_element_y)
print(A.symmetric_difference(B))
print(A.union(B))