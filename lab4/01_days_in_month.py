#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# (if/elif/else)

months_day_count = {'1':  31,
                    '2':  28,
                    '3':  31,
                    '4':  30,
                    '5':  31,
                    '6':  30,
                    '7':  31,
                    '8':  31,
                    '9':  30,
                    '10': 31,
                    '11': 30,
                    '12': 31,
                    }


user_input = input("Введите, пожалуйста, номер месяца: ")
if user_input.isdigit():
    month = int(user_input)

    if 1 <= month <= 12:
        day_count = months_day_count[user_input]
        print('Вы ввели', month)
        print('Кол-во дней в месяце:', day_count)
    else:
        print('Месяца с таким номер не существует.')
else:
    print('Необходимо ввести число.')