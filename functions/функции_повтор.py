"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

"""
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
"""
"""
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

"""
# def func(list_:list):
#     res = ''.join(list(map(str,list_)))
#     res = int(res) + 1
#     res = str(res)
#     print(res,type(res))
#     res1 = list(res)
#     res1 = list(int,res)

#     return res1

# print(func(1,2,3))
# print(func([9]))
# print(func[5,4,9,9])


""""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.  

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used: 

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""
"""
Input: s = "III"
Output: 3
Explanation: III = 3.

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

# def romanToInt(s: str) -> int:
#     dict_ = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     s = list(s)
#     newlist=[]
#     for i in s:
#         num = dict_[i]
#         newlist.append(num)
#     list1 = newlist[::-1]
    
#[5, 1, 100, 10, 1000, 100, 1000]
#     i = 0
#     last = list1[0]
#     for x in list1:
#         if x < last:  
#             i -= x
#         else:
#             i += x
#         last = x
#     return i
    
# print(romanToInt("III"))
# print(romanToInt("LVIII"))
# print(romanToInt("MCMXCIV"))
# print(romanToInt("MMXCV"))


"""
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string."""
"""
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
"""

"""
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
"""
"""
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
"""

# def compareToAraise(word1,word2):
#     from functools import reduce
#     oper = reduce(lambda x,y: x+y, word1)
#     oper1 = reduce(lambda x,y: x+y, word2)
#     if oper == oper1:
#         print('True')
#     else:
#         print('False')

# compareToAraise(['a','cb'], ['ab','c'])


"""
Создайте функцию sum_range(start, end), которая суммирует все целые числа от значения start до величины end включительно. 
Если пользователь задаст первое число больше чем второе, просто поменяйте их местами.
"""



# def sum_range(start, end):
#     if start > end:
#         list_ = list(range(end,start+1))
#         sum_ = sum(list_)
#         return sum_
#     else:
#         list_ = list(range(start,end+1))
#         sum_ = sum(list_)
#         return sum_
        

# print(sum_range(6,1))

""""На входе имеем список строк разной длины. 
Необходимо написать функцию all_eq(lst), которая вернет новый список из строк одинаковой длины. 
Длину итоговой строки определяем исходя из самой большой из них. 
Если конкретная строка короче самой длинной, дополнить ее нижними подчеркиваниями с правого края до требуемого 
количества символов.
Расположение элементов начального списка не менять.

Input: ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']
Output: ['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa']"""

# lst = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa']

# def all_eq(lst):
#     max_ = len(max(lst))
#     list_ = []
#     for i in lst:
#         if len(i) != len(max_):
#             n = max - len(i)
#             under = '_'* n
#             konkan = i + under
#             list_.append(konkan)

#     list.append(max(lst))
#     return list_



# print(all_eq,lst)

#task
# s = "Hello World"

# def length_of_last_word(s):
#     words = s.split()
#     if len(words) == 0:
#         return 0
#     return len(words[-1])

# print(length_of_last_word('Hello World'))

"""
Дано предложение "Это короткое предложение", оно может быть перетасовано как "предложение3 короткое2 Это1" или 
"короткое2 предложение3 Это1".
Учитывая перетасованные предложения, содержащие не более 9 слов, восстановите и верните исходное предложение, 
удалив цифры в конце слов.

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
"""
    
# text_ = s = "is2 sentence4 This1 a3"
# def func(text):
#     list_ = text.split()
#     list_.sort(key = lambda x: x[-1])
#     new_str = ""
#     for i in list_:
#         new_str = new_str + i[:-1] + ' '
#     return(new_str).strip()

    
    
# print(func(text_))


#VIDEO

# substract()

# variable = substract()
# print(variable)

# def substract():
#     num1 = 20
#     num2 = 5
#     print(num1 + num2)
#     return num1 - num2

# list_ = [1,2,3,4,5,6,7,8,9,10,11,12,13,14, substract()]
# print(list_)

# def function():
#     print("I'm calling substract function")
#     print(substract())
#     variable = substract()
#     return variable

# print(function())

# def create_profile(name, age, image = 'default.jpg'):
#     return name, age, image

# print(create_profile(name = 'Raychel', age = 30, image = 'flower.png'))

def func(required, *args, **kwargs):
    print(required)

    if args:
        print(args)

    if kwargs:
        print(kwargs)

func('Makers', 'bootcamp', 'python', name = 'Raychel', age = 89)

