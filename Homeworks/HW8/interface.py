def get_option()->int:
    check = False
    while not check:
        option = input('Выберите вариант для работы со справочником и нажмите ввод:\n'
                        + '1 - Для записи нового абонента.\n'
                        + '2 - Для экспорта в файл, и просмотра телефонной книги.\n')
        if option in ('1', '2'):
            check = True
        else:
            print('Некорректный вариант ввода. Попробйуте снова.')
    return int(option)

def get_export_choose_option():
    check = False
    while not check:
        option = input('Выберите действие:\n'
                        + '1 - Экспорт книги в HTML формат\n'
                        + '2 - Вывести книгу на экран\n')
        if option in ('1', '2'):
            check = True
        else:
            print('Некорректный вариант ввода. Попробйуте снова.')
    return int(option)