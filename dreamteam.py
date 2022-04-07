#1
# def delete_vowels (c):
#     if len(c)<10: return 'too small'
#     vowels = ('a', 'e', 'i', 'o', 'u')
#     for x in c.lower():
#         if x in vowels:
#             c = c.replace(x, "")
#     return c 
# print(delete_vowels(input('text: ')))

#2
# accounts = [
#     [[1,5,5],[7,4,5],[1,3,5],[2,1,5],[7,3,9],[8,3,5],[1,5,0],[7,3,2],[9,3,5]],
#     [[1,5,3],[2,7,3],[6,3,5],[1,5,9],[7,3,3],[3,5,4],[1,5,6],[7,3,6],[3,5,8]],
#     [[1,5,3],[7,3,0],[3,5,4],[1,5,6],[7,3,2],[3,5,4],[1,5,9],[7,3,2],[3,5,0]],
#     [[1,5,1],[7,3,2],[3,5,3],[1,5,4],[7,3,5],[3,5,6],[1,5,7],[7,3,8],[3,5,9]],
# ]
# max = accounts[0][0]
# def max_list(l):
#     max_l = l[0]
#     for i in l:
#         if sum(i)>sum(max_l):
#             max_l = i
#     return max_l

# max_lists_between_4 = list(map(max_list,accounts))

# max_list_between_all = max_list(max_lists_between_4)

# print(max_lists_between_4)

# print(max_list_between_all)

#3
# list_1 = ['a', 'bc', 'de']
# list_2  = ['ab', 'c', 'de']
# list_3 =['ad','li']
# list_4 = ['a','dil']

# def check_2_list(l1,l2):
#     words1 = "".join(l1)
#     words2 = "".join(l2)
#     return 'Равны' if words1 == words2 else 'Не равны'
# print(check_2_list(list_1,list_2))


#4

# from IPython.display import display
# display('Теперь я тут PRINT()')


#5

# uniques = {3, 13, 15, 27, 1, 4, 8, 23, 19, 12, 9, 2, 17}
# def remove_evens(uniques):
#     l ={i for i in uniques if i%2!=0}
    
    
#     return sorted(l)

# print(remove_evens(uniques))


#6


# a = ((2>3),(5>3),(2==2),(3==4))
# print(a[0],a[1],a[2],a[3])

#7
def get_pairs(iterable):
    final = []
    for i in range(0, len(iterable), 2):
        final.append((iterable[i], iterable[i + 1]))
    return final

pairs = {}
keys_values = ('one', 1, 2, 'two', 3, 'three', 'four', 4, 'five', 5, 6, 'six', 7, 'seven', 'eight', 8, 'nine',9, 10, 'ten', 11, '11', 12 ,'13')

for (e1, e2) in get_pairs(keys_values):
    if type(e1) is str:
        pairs[e1] = e2
    else:
        pairs[e2] = e1

print(pairs)


    



#8
# from random import choice
# def check_numbers(s):
#     if s.count(',')>0 and s.count(' ')>0:return False
#     elif s.count(',')>0 and len(s.split(','))<3:return False 
#     elif s.count(' ')>0 and len(s.split())<3: return False
#     elif s.count(' ')==0 and s.count(',')==0: return False
#     else:
#         if s.count(',')>0: return s.split(',')
#         else:
#             return s.split()
    
# answer = ''
# from random import shuffle
# while True:
#     limit = int(input('limit: '))
#     if limit<7:
#         print('too small')
#     elif limit>30:
#         print('too big')
#     else:
#         numbers = input('numbers: ')
#         if check_numbers(numbers)==False:
#             print('try again')
#         else:
#             l = check_numbers(numbers)
#             for i in range(limit):
#                 answer+=choice(l)
#             print(answer)
#             break

#9
# s = input('Введите текст с верхном регистре и в нижнем регистре: ')
# alph = list(filter(str.isalpha, s))
# print(sum(map(str.isupper, alph)) / len(alph))
# print(sum(map(str.islower, alph)) / len(alph))

#10

# x = int(input('weight: '))
# def after_15(w):
#     y = 0.165
#     count = 1
#     for i in range(15):
#         final = (w+count) *y
#         print(f'{count}: ',final)
#         count+=1
# after_15(x)




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
