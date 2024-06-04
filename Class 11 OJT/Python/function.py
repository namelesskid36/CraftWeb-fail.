# # # # def helloworld():
# # # #     print("hello,world")
    
# # # #     helloworld()
# # # #     def hello(name, course_name):  #parameter
# # # #         print("Hello", name, "welcome to Python Traning")
# # # #         print(course_name)

# # # #         def hello(name, course_name):  
# # # #             print("Hello", name, "welcome to Python Traning")
# # # #         print(course_name)
# # # #     print ("i live in")
# # # #     print("i am studing at")

# # # #     hello(course_name='Python with django', name='ram')
# # # # def hello(name, course_name):  
# # # #         print("Hello", name, "welcome to Python Traning")
# # # #         print(course_name)

# # # #         hello(name='Ram')


# # #         #arbitrary arguments - *args

# # # # def sum(*args):
# # # #     total = 0
# # # #     for n in args:
# # # #         print(n)
# # # #         total+=n

# # # #     return total
# # # # resutlt = sum(2,3,4,5,6)
# # # # print(resutlt)



# # # # #kwargs

# # # def sum (**kwargs):
# # #     print("hello", kwargs['name'],"Wellcome to web devlopement traning")
# # #     print(kwargs['course_name'])

# # #    sum(name='Ram', course_name='Python with date science', another_course='python with date science')





# # l = float(input('Enter a lenght :'))
# # w = float(input('Enter a width :'))

# # def area():
# #     h=float(input("Enter a height :"))
# #     global area_of_object
# #     area_of_object =l*w
# #     return area_of_object

# # def volume():
# #     h = float(input('Enter a height : '))
# #     v = area_of_object*h
# #     return v

# # result = area()
# # result_volume = volume()
# # print(result)
# # print(result_volume)




# #lambda function

# # x= lambda a: a%2==0
# # even = x(int(input("Enter a even num: ")))
# # print(even)

# # y = lambda a,b: a+b
# # addition = y(10,15)
# # print(addition)



# #recurive function
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)

# result = factorial(3)