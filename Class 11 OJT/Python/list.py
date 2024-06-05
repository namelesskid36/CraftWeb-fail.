list=["Hello","World","Whats","UP"]
print(list)
print(type(list))
print(list[0])
print(list[1])
print(list[2])
print(len(list))

laptops= ['dell', 'hp', 'lenovo', 'mac']
print(laptops[0])
print(laptops.index('hp'))

laptops.append('sony')
print(laptops)

laptops.insert(2, 'microsoft')
print(laptops)

laptops.remove('microsoft')
print(laptops)
removed =laptops.pop(4)

print(removed)
print(laptops)

laptops.insert(2, 'microsoft')
laptops.append('microsoft')
print(laptops)


count = laptops.count('microsoft')
print(count)

laptops.sort()
print(laptops)

laptops.sort(reverse=True)
print(laptops)

laptops.reverse()
print(laptops)

copy_laptops = laptops.copy()
print (copy_laptops)

laptops.copy()
print(laptops)

laptops.clear()
print(laptops)

