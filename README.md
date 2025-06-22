# textMagicRandom
мини-библиотека для генерации случайных данных, созданая лично для меня

Библиотека для генерации случайных данных с русским колоритом. Идеально подходит для:
- Тестирования приложений 🧪
- Создания игровых никнеймов 🎮
- Генерации надежный паролей 🔒
- Заполнения макетов текстом-заглушкой 📋

## Установка

Мне лень выкладывать на pypi, может потом вылажу

## Быстрый старт

```python
from textMagicRandom import generator

# Никнейм для игры
print(generator.generate_nicknames())  # Пример: "Безумный_Скелет_42"

# Надёжный пароль
print(generator.generate_password(10))  # Пример: "k3F$mX8!pL"

# Текст-заглушка
print(generator.text_stub(3))  # Пример: "Пубтджи яни лосось"
```

## Документация

### 📌 generate_nicknames()
Генерирует случайный никнейм в формате `Прилагательное_Существительное_Число`.

```python
generator.generate_nicknames() -> str
# Возвращает: "Седой_Дракон_15"
```

### 🔐 generate_password(count)
Создает сложный пароль указанной длины (минимум 8 символов).

```python
generator.generate_password(count: int) -> str
# Пример: generator.generate_password(12) → "qW1#pL9*&zXy"
```

**Исключения:**
- `ValueError` - если длина меньше 8

### 📜 text_stub(word_count)
Генерирует псевдо-текст из случайных слов(русский лорем ипсум)

```python
generator.text_stub(word_count: int) -> str
# Пример: generator.text_stub(2) → "Пубтджи яни лосось амнэ"
```

## Пример интеграции

```python
# Создаём тестового пользователя
test_user = {
    "nickname": generator.generate_nicknames(),
    "password": generator.generate_password(10),
    "bio": generator.text_stub(5)
}
```

## Развитие проекта

Хочешь добавить:
- Больше слов в словари?
- Новые функции генерации?
- Поддержку английского языка?

## Лицензия

а нету!
