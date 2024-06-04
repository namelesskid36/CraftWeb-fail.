import os, shutil
#file handling -> open file, close file, read file
path = 'test.txt'
# my_files = open(path)
# print(my_files)
# print(my_files.read()) # to read the file
# print(my_files.writable()) # to check wheater tto write in file or not
# my_files.close()

#----------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------#

# my_another_file = open(path, 'r+')
# print(my_another_file)
# print(my_another_file.readable) #to check whether the file camn be readable or not ig..
# print(my_another_file.writable) #to check whether th file can be writable ot not ig..
# print(my_another_file.read()) #to read the files
# my_another_file.write('\n Ram \n') # to write on the files
# my_another_file.close()

#----------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------#

# my_another_file = open(path, 'w+') #
# print(my_another_file)
# print(my_another_file.readable()) #to check whether the file camn be readable or not ig..
# print(my_another_file.writable()) #to check whether th file can be writable ot not ig..
# my_another_file.write('Ram \n Arjesh')
# print(my_another_file.seek(1))
# print(my_another_file.read())
# print(my_another_file.seek(0))
# print(my_another_file.readlines())
# my_another_file.close()

#----------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------#

# my_another_file = open('next.txt', 'a+') #to create file ig..
# print(my_another_file)
# print(my_another_file.readable()) #to check whether the file camn be readable or not ig..
# print(my_another_file.writable()) #to check whether th file can be writable ot not ig..
# my_another_file.write('Hello \n World')
# print(my_another_file.seek(10))
# print(my_another_file.read())
# my_another_file.close()

#----------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------#
# shutil.copy('next.txt', "text1.txt") # to create a new and copy the texts from the files to the new one..

# os.remove('next.txt')   #to delete files..

# shutil.move('test.txt', 'next1.txt')