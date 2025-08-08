import random

class Generator:
    def __init__(self):
        #you can change the base how do you want. these bases for reference only
        self.nouns = ["Мальчик","Христьянин","Крестьянин","Раб","Дэвочка","Скелет","Человек","Корабль","Единорог"]
        self.adjectives = ["Красивый", "Мудрый","Черный","Седой","Бородатый","Раздражающий","Веселый", "Розовый"]
        self.stub_words = ["камоня", "лосось", "икоро", "ямони", "куманё", "зожемэ", "пласехо", "амнэ", "лорево", "лорима",
                      "тунтун", "кахурэ", "атрэбы", "ылесо", "почакэ"]
        self.names_male = ["Владимир","Андрей","Дмитрий","Николай","Олег","Витя","Даниил","Святозар"]
        self.last_names_male = ["Путин","Цветков","Платков","Медведев","Петухов","Барыгин","Шевченко","Турчинов"]
        self.names_female = ["Олеся","Юлия","Анна","Анастасия","Натали","Татьяна","Виолетта","Варя"]
        self.last_names_female = ["Иванова","Тимошенко","Петрова","Глебова","Юрченко","Миролюбова","Книжова","Кац"]


    def generate_nicknames(self):
        number = random.randint(40,45)
        result = f"{random.choice(self.adjectives)}_{random.choice(self.nouns)}_{number}"
        if result == "Розовый_Единорог_42" or result == "Черный_Раб_42":
            return f"{result}\nВот вы везунчик!! Купите лотерейны билет!!"
        elif result == "Розовый_Единорог_41" or result == "Черный_Раб_41":
            return f"{result}\nОго! Так близко! Но не идеал!"
        else:
            return result

    def generate_password(self, count):
        if count < 8:
            raise ValueError("count должен быть не меньше 8 символов!")
        else:
            symbols = "QWERTYqwerty123570%^*#&?"
            return "".join(random.choice(symbols) for i in range(count))

    def text_stub(self, count: int) -> str: #Пубтджи
        count -= 2
        # лист со словами
        result = []

        for i in range(count): #count - сколько слов будет в result
            result.append(random.choice(self.stub_words)) # мы count раз добавляем в лист result рандомное слово из списка stub_words
        return "Пубтджи яни " + " ".join(result)  # выводим в строку то, что было в листе result

# v1.0.1

    def code(self, text: str) -> str:
        dict_of_letters = {
            'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
            'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
            'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
            'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
            'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B',
            'Z': 'A',
            'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
            'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
            'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
            'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
            'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b',
            'z': 'a',
        }

        code_text = []
        for char in text:
            if char in dict_of_letters:
                code_char = dict_of_letters[char]
                code_text.append(code_char)
            else:
                code_char = char
                code_text.append(code_char)

        return "".join(code_text)

    def fake_name(self, gender: str) -> str:
        if gender == "male":
            data = f"{random.choice(self.names_male)} {random.choice(self.last_names_male)}"
            if data == "Владимир Путин" or data == "Дмитрий Медведев":
                return f"{data}\nОГО! ВЫ ВЫБИЛИ РЕДКОЕ ФИ!!"
            else:
                return data
        elif gender == "female":
            data = f"{random.choice(self.names_female)} {random.choice(self.last_names_female)}"
            if data == "Юлия Тимошенко":
                return f"{data}\nОГО! ВЫ ВЫБИЛИ РЕДКОЕ ФИ!!"
            else:
                return data

    def search_letter(self, message: str, letter: str) -> int:
        how_many_times_have_seen_letter = 0

        for char in message:
            if char == letter:
                how_many_times_have_seen_letter += 1

        return f"Буква {letter} была увидена в слове {message} {how_many_times_have_seen_letter} раз!"
