import time

from text_magic_random import *

def searchin_rare():
    while True:
        nickname = generator.generate_nicknames()
        if "Черный_Раб_42" in nickname or "Розовый_Единорог_42" in nickname:
            time.sleep(0.1)
            print(nickname)
            print("ОН НАШЕЛСЯ!")
            break
        else:
            time.sleep(0.1)
            print(nickname)

def testing_featers():
    # Никнейм для игры
    print(generator.generate_nicknames()) # Пример: "Безумный_Скелет_42"

    # Надёжный пароль
    print(generator.generate_password(10)) # Пример: "k3F$mX8!pL"

    # Текст-заглушка
    print(generator.text_stub(3)) # Пример: "Пубтджи яни лосось"

    # скока л
    print(generator.search_letter("Параллелепипед", "л"))

    # кодирование
    print(generator.code("hello")) # превратится в svool

if __name__ == '__main__':
    choice = input("Найти редкие - 1\nТестирование функций - 2")
    if choice == "1":
        searchin_rare()
    elif choice == "2":
        testing_featers()
    else:
        print("Инвалид")
