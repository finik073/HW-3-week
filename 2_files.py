#1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0  C:\Users\breusova\LP\week3
#2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
#3. Подсчитайте количество слов в тексте
#4. Замените точки в тексте на восклицательные знаки
#5. Сохраните результат в файл referat2.txt

def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        referat = f.read()
        print('\n')
        print(f'Длина строки составляет {len(referat)}.\n')
        print(f'Количество слов в тексте равно {len(referat.split())}.\n')
        task4 = referat.replace('.', '!')
        with open('referat2.txt', 'w', encoding='utf-8') as new_f:
            task5 = new_f.write(task4)
        with open('referat2.txt', 'r', encoding='utf-8') as control:
            print(f'Проверим что записалось в новый файл:\n{control.read()}\n')
    print('конец программы\n')

if __name__ == "__main__":
    main()
