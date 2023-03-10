# Работа с файлами

# Каретка = Указатель - Курсор

# open(<путь до файла>)

# file = open('/home/alibek/dekstop/data_types/files.py')  #Абсолютный путьь -вручную прописываем путь подробно

# file = open('files.py') #Относительный путь

# ~ working -> desktop/py.26/files/files.py

#py.26 -> files/files.py

# file = open('files.py')

# data = (file.read())

# print(type())

# file.close()

# Режимы работы с файлами

# 1. r/r+ (read)
# 2. w/w+ (wriite)
# 3. a/a+ (append)

# b,x


# file = open('text.txt', 'r')

# print(file.read())

# file.close()

# file = open('text.txt', 'r')

# data = file.readlines()
# print(data)
# print(len(data[0]))
# file.close()

# file = open('text.txt', 'r')

# print(file.readline())

# print(file.readline())

# file.close()

# file = open('text.txt', 'r')
# print(file.readline())
# print('!!!!')
# print(file.read())
# file.close()


# контекстный менеджер

# with open('text.txt', 'r') as file:
#     data = file.read()
#     print(data)
#     print(file, 'inside')
# print(file, 'outside')

# with open('text.txt', 'r') as f:
#     print(f.tell())
#     data = f.read(20)
#     print(f.tell())
#     print(data)
#     print(f.read())
#     print(f.tell())

# file.tell() -> возвращает индекс где находиться указатель(курсор)

# file.seak(index) -> перемещает курсор на этот индекс который вы передали

# with open('text.txt', 'r') as file:
    # print(file.readline())
    # file.seek(0)
    # print(file.readline())
    # file.seek(0)
    # a = file.read()
    # print(file.readline())
    # print(file.readlines(-1))

# print(a)

# with open('test.txt', 'w') as file:
#     # file.write('Pervaya strochka!\n')
#     # file.write('\nHe is bastard of Ned Stark!\n')
#     # file.write('This is lesson about files')
#     # file.seek(0)
#     data = (['Pervaya strochka!\n', 'He is bastard of Ned Stark\n', 'This is lesson about files!'])
#     file.writelines(data)

# with open('test.txt', 'a+') as file:
#     file.write('\nJohn Snow is a North King!')
#     file.write('\nYpi know nothing John Snow!')
#     file.seek(0)   
#     print(file.read())


'-----------------------------------------------------------------------------------------------------'


