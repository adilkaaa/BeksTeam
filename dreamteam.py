#1
# def delete_vowels (c):
#
#     vowels = ('a', 'e', 'i', 'o', 'u')
#     for x in c.lower():
#         if x in vowels:
#             c = c.replace(x, "")
#
#     return c
# print(delete_vowels(input('text: ')))

#2

#3

# list_1 = ['a', 'bc', 'de']
# list_2  = ['ab', 'c', 'de']
# list_3 =['ad','li']
# list_4 = ['a','dil']

# def check_2list(l1,l2):
#     words1 = "".join(l1)
#     words2 = "".join(l2)
#     return 'Подходит' if words1 == words2 else 'Не подходит'
# print(check_2list(list_1,list_2))
#4

#5



# uniques = {3, 13, 15, 27, 1, 4, 8, 23, 19, 12, 9, 2, 17}
# def ub(uniques):
#     l = []
#     for i in uniques:
#         if i % 2 != 0:
#             l.append(i)
#     l.sort(reverse=True)
#     return l
# print(ub(uniques))
#6
# a = ((2>3),(5>3),(2==2),(3==4))
# print(a[0],a[1],a[2],a[3])

#7

#8

#9
# s = input('Введите текст с верхном регистре и в нижнем регистре: ')
# alph = list(filter(str.isalpha, s))
# print(sum(map(str.isupper, alph)) / len(alph))
# print(sum(map(str.islower, alph)) / len(alph))

#10
# x = int(input('ves: '))
# def after_15(w):
#     y = 0.165
#     final = (w+15) *y
#     return final
# print(after_15(x))




#11
# text=str(input("Введите текст через пробел: ")).split()
# text.sort(key=len)
# print(text)

#12
# def farenheit_to_c(f):
#     c =  (f - 32) * (5/9)
#     return f'Градус фаренгейта на цельсию, {c}'

# def cel_to_farenheit(cel):
#     far = cel * 9/5 + 32
#     return f'Градус цельсии на фаренгейт,{far}'

# print(cel_to_farenheit(int(input('celsium: '))))
# print(farenheit_to_c(int(input('farenheit: '))))
