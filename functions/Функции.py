# file1 = open('makers.txt', 'r')
# print(file1.read())

'''
r - read

r+ - read + write

w - write

w+ - read + write

a - append

a+ - append + read

x - write(если файла не существует)

b - binary

t - text

rt -> r 

rb -> rb
'''

# file1 = open('makers.txt', 'r')
# print(file1.read(10))
# file1.seek(0)
# print(file1.read(5))
# file1.seek(0)
# print(file1.read(6))
# seek()

# file1 = open('makers.txt', 'r')
# list_ = file1.readlines()
# list_ = [line.replace('\n','') for line in list_]
# print(list_)

# file2 = open('bootcamp.txt', 'w')
# file2.write("It's such a beutiful day today" + '\n')
# file2.write("Today is my birthday" + '\n')
# list_mottos = ["Just Do It.", "Think different.", "Because You're Worth It.",
#              "Got Milk?"]
# list_mottos = [motto + '\n' for motto in list_mottos]

# print(list_mottos)

# dict_ = {'name':'makers', 'hello':'world'}

# file2.writelines(list_mottos)

# file3 = open('files.txt', 'a')

# list_mottos = ["Just Do It.", "Think different.", 
# "Because You're Worth It.","Got Milk?"]
# list_mottos = [motto + '\n' for motto in list_mottos]

# file3.write('Mottos of big companies' + '\n')
# for motto in list_mottos:
#     file3.write(motto)

# file3.close()
# print(file3.closed)

# with open('files.txt', 'w+') as my_file:
#     print(my_file.read())
#     my_file.write('Additional string')
    
# print(my_file.closed)