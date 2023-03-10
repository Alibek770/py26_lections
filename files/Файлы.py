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

file1 = open('makers.txt', 'r')
data = file1.read()
print(data)