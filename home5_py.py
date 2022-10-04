import random
def up_and_num(lp:list,n:list)->list:
    lp=list(map(lambda x:x.upper(),lp))
    for i in range(2,len(lp)+2):#иначе первый язык учавствует не по правилам
        n.append(i)
    return list(zip(n,lp))
def game(num_list):
    new_list=[]
    for j,i in num_list:
        val = 0
        for num in i:
            val+=ord(num)
            #print(num)
        if not val%j:
            new_list.append((j,i))
            #print(f'{j} {i} + {val}')
    return new_list

#Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension
#1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#'абвгдейка - это передача' = >" - это передача"
string_val=input('введите текст, будут удалены слова, содержащие идущие подряд "абв" -> ')
if 'абв' in string_val:
    world=string_val.split(' ')
    del_fragment='абв'
    for i in world:
        if del_fragment not in i:
            print(i, end=' ')
        print()
else:
    print(string_val)
#2- Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая 
#ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более 
#чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
#Предусмотрите последний ход, ибо там конфет остается меньше.
#a) Добавьте игру против бота
#b) Подумайте как наделить бота "интеллектом"
bool_exit=True
while bool_exit:
    try:
        
        print('игра с конфетами человек против человека\nЗадайте количество конфет\
 на столе ->',end=' ')
        candies=int(input())
        input('играют два человека, первый ход определяет жеребьевка.\n нажмите ввод,\
 для выбора первого игрока')
        print(f'игрок №{random.randint(1,2)} начинает игру, введите свое имя  -> ')
        name=input()
        name2=input('следующий игрок, представьтесь -> ')
        count=0
        while True:
            while not(count>0 and count<29): 
                print(f'{name} сколько конфет возмете?')
                count=int(input())
            candies-=count
            if candies<=0:
                print(f'{name2} winner!!!')
                break
            count=0
            while not(count>0 and count<29):
                print(f'{name2} сколько конфет возмете?')
                count=int(input())
            candies-=count
            if candies<=0:
                print(f'{name} winner!!!')
                break
            count=0


        print('начать игру заново? y\\n-> ')
        if input()!='y':
            break

    except ValueError:
        print('что то пошло не так...')
#3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1
# до длины первого.
#['python', 'c#']
#[1,2]
#Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера
# и языка, написанного большими буквами.
#[(1,'PYTHON'), (2,'C#')]
#Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в 
#делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на 
#сумму очков.
#[сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
#[(1,'PYTHON'), (102,'C#')]
#Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 
#Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
#Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
#Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным 
#списком
#https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&
print('списки языков программирования и числа')
lang_prog=['Планкалкюль', 'Ассемблер', 'AspectC++', 'AspectJ', 'AspectLua', 'CaesarJ',\
   'Compose', 'ObjectTeams', 'Basic', 'Cg', 'JOVIAL', 'Pascal', 'PL/M', 'QBASIC', 'REXX', \
   'Активный Оберон', 'Алгол 68', 'Алгол', 'Shell', 'Модула', 'Оберон', 'ПЛ/1',\
  'Упрощённый Алгол', 'Фокал', 'Фортран', 'PHP', 'GNU bc', 'Euphoria', 'Limbo', 'Lua',\
 'Maple', 'MATLAB', 'Occam', 'PureBasic', 'Scilab',\
'Активный Оберон', 'Алгол', 'Би', 'КОБОЛ', 'Модула-2', 'Модула-3', 'Оберон', 'Паскаль', \
'РАПИРА', 'Си', 'Golang', 'Mercury', 'Prolog', 'Curry', 'Action Script', 'C++/CLI', 'C#',\
'ColdFusion', 'D', 'Dart', 'Object Pascal', 'Dylan', 'Eiffel', 'Game Maker Language (GML)', \
'Groovy', 'Haxe', 'Io', 'Java', 'JavaScript', 'MC#', 'Object Pascal', 'Objective-C', 'Perl',\
'PHP', 'Pike', 'Python', 'Ruby', 'Self', 'Simula', 'Smalltalk', 'Swift', 'Vala',\
'Visual Basic', 'Visual DataFlex', 'Zonnon', 'Ada', 'Активный Оберон', 'Компонентный Паскаль', \
'Модула-3', 'Оберон-2', 'Cat', 'Clean', 'Dylan', 'Elm', 'Erlang', 'F#', 'Gentee', 'Haskell',\
'Hope', 'J', 'Mathematica', 'OCaml', 'Scheme', 'АПЛ', 'Лисп', 'Лого', 'РЕФАЛ', 'C++', \
'Kotlin', 'PHP', 'Curry', 'Delphi', 'Erlang', 'Mathematica', 'Mozart', 'Nemerle', 'Python', \
'Rust', 'Scala', 'Swift', 'Zonnon', 'Активный Оберон', 'Component Pascal', 'Модула-3', 'Julia',\
'Visual DataFlex', 'FBD', 'IL', 'Ladder Diagram', 'Sequential Function Chart', 'SPCLK', \
'ST или SCL', 'Forth', 'Joy', 'NetP', 'PostScript', 'Afnix', 'Alef', 'ChucK', 'Clojure', \
'Concurrent Pascal', 'Corn', 'C#', 'Curry', 'E', 'Eiffel', 'Erlang', 'Java']
lang_prog=set(lang_prog)
num=[]
result=up_and_num(lang_prog,num)
print(f'участвующие языки программирования - {result}')
result=game(result)
print(f'выигравшие языки: {result}')
#Дополнительно(по желанию):
#1 - Создайте программу для игры в ""Крестики-нолики"".
print('игра крестики/нолики')
#2 - Создать программу, считывающую два полинома из двух файлов и записывающая в третий файл их сумму.
print('считывание двух палиномов и запись в файл')