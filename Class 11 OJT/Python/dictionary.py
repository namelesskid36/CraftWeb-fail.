capital ={
    "Nepal":"Kathmandu",
    "India":"New Delhi",
    "China":"Beijing"
}
print(capital)
print(len(capital))
print(type(capital))

print(capital.keys())
print(capital.values())

print(capital['Nepal'])
capital["Japan"] = "Tokyo"
print(capital)

capital['Bhutan'] = 'Thimpu'
print(capital)

pop_element = capital.pop("Bhutan")
print(pop_element)
print(capital)

a={1,2,3,4}
b= (1,2,3,4)

marks = {
    "Math":80,
    "Science":80,
    "Nepali":80
}
print(marks)
capital.update(marks)
print(capital)
copy_capital = capital.copy()
print("This is a copy capital :", copy_capital)

copy_capital.clear()
print(copy_capital)

print(marks.items())

test={'key1':{'nestkey':{'subnestkey':'hello'}}}
print(test["key1"]['nestkey']['subnestkey'])
print(test["key1"]['nestkey'])
print(test["key1"])
print(test.values())

student = {}
print(type(student))
student["Name"]="Ram shrestha"
print(student)

student['age'] =17
student['address'] ='Kathmandu'
student['education'] ='SEE'
print(student)
student['hobby']=['Football','Volleyball','Basketball']
print(student)

print(student['hobby'][-1])