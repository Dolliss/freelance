from statistics import mean
import pandas as pd
from tabulate import tabulate

def estimation(arr):
    mina = min(arr)
    maxa = max(arr)
    arr.remove(mina)
    arr.remove(maxa)
    return round(mean(arr), 2)

def normal_df(df):
    df['Средняя'] = df['Оценка'].apply(estimation)
    df2 = df.groupby(['Общество']).max()
    df2.sort_values(['Средняя'], inplace = True)
    df2.reset_index(inplace = True)
    return df2

#функция для создания новой таблицы
def create_table():
    #пустой массив
    df = []
    #название колонок
    col = ['Фамилия', 'Общество', 'Оценка']
    #проверялка)
    cheek = True
    while cheek:
        print('Введите через пробел:')
        print('Фамилия Общество Оценки(8 шт.)')
        s = input() 
        #разделяем строку через пробелы "1 2 фыв 31 1" -> ["1","2", "фыв","31", "1"]
        s = s.split()
        # если нас не устраивает длина ( должна быть 4)
        if len(s) != 10:
            print('Ошибка ввода')
        else:
            #пробуем привести счет матча к числовому виду, иначе выдаем ошибку
            try:
                new_row = []
                for i in range(2, len(s)):
                    new_row.append(int(s[i]))
                new_row2 = [s[0], s[1], new_row]
                df.append(new_row2)
            except:
                print('Ошибка ввода')
        # если вводим 1 - то добавляем новую строчку в табличку, а иначе нет
        input_cheek = input('1 - чтобы добавить еще строчку, иначе - выход')
        try:
            input_cheek = int(input_cheek)
            #если ввели не 1 и наша табличка не пустая, то выходим
            if input_cheek != 1 and df != []:
                cheek = False
            else:
                print('Заполните таблицу')
        except:
            #если табличка не пустая то выходим 
            if df == []:
                print('Заполните таблицу')
            else:
                cheek = False
                #возвращаем сформированную таблицу
    return pd.DataFrame(df, columns = col)
#меню выбора 1
input_menu1 = [(1, 'Чтение csv файла'),
              (2, 'Создание нового файла'),
             ('Иначе', 'Выход')]

#меню выбора 2
input_menu2 = [(1, 'Продолжить'),
               (2, 'Сохранить файл'),
             ('Иначе', 'Выход')]

#название столбцов
col = ['Фамилия', 'Общество', 'Оценка']

#работает пока не выберем выход
while True:
    #вывод меню и чтение вводимого параметра
    print(tabulate(input_menu1))
    cheek = input()
    
    #проверка - число ли введеный параметр
    try:
        cheek = int(cheek)
    #если не число - выход
    except:
        print('Bye!')
        break
        
    # если равно 1
    if cheek==1:
        #выбираем путь до файла
        path = input('Укажите путь: ')
        try:
            #пробуем открыть файл
            df = pd.read_csv(path)
            #откидываем первый столбец, тут бесполезные индыксы и применяем изменения
            df.drop(columns=['Unnamed: 0'], inplace = True)
            print('Ваша таблица:')
            #вывод открывшийся таблички
            print(tabulate(df, headers='keys', tablefmt='psql'))
            #если наименование заголовков таблицы не подходят, то говорим, что не подходит)
            if list(df) != col:
                print('Некорректные данные')
                continue
            #при чтении наш массив понимается как строка, удаляем скобки, разделяем по запятым и переводим в int
            df['Оценка'] = df['Оценка'].apply(lambda x: [int(i) for i in x[1:-1].split(',')])
        # если не открывается файл - некорректный путь
        except:
            print('Некорректный путь')
            continue
            
    #выбрали 2 - создаем свою табличку функцией
    elif cheek==2:
        df = create_table()
        #сохраняем таблицу 
        print('Введите имя файла + .csv для сохранения')
        path2 = input()
        try:
            df.to_csv(path2)
            print(f'Файл {path2} сохранен')
        except:
            print('Некорректное имя файла или таблица')
        
    # иначе - выход 
    else:
        print('Bye!')
        break
        
    # функция работы с табличкой и вывод результата
    df_finall = normal_df(df)
    print('Результат')
    print(tabulate(df_finall, headers='keys', tablefmt='psql'))
    print(tabulate(input_menu2))
    cheek2 = input()
    
    try:
        cheek2 = int(cheek2)
    except:
        print('Bye!')
        break
    if cheek2 == 1:
        continue
    elif cheek2 == 2:
        print('Введите имя файла + .csv для сохранения')
        path2 = input()
        try:
            df.to_csv(path2)
            print(f'Файл {path2} сохранен')
        except:
            print('Некорректное имя файла или таблица')
    else:
        print('Bye!')
        break
    

    
