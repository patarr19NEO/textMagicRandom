import random

class Generator:
    def __init__(self):
        #you can change the base how do you want. these bases for reference only
        self.nouns = ["Мальчик","Христьянин","Крестьянин","Раб","Дэвочка","Скелет","Человек","Корабль","Единорог"]
        self.adjectives = ["Красивый", "Мудрый","Черный","Седой","Бородатый","Раздражающий","Веселый", "Розовый"]
        self.stub_words = ["камоня", "лосось", "икоро", "ямони", "куманё", "зожемэ", "пласехо", "амнэ", "лорево", "лорима",
                      "тунтун", "кахурэ", "атрэбы", "ылесо", "почакэ"]

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
