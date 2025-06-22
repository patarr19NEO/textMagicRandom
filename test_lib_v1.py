#how to use lib

from text_magic_random import *

#генерация ника
nickname = generator.generate_nicknames()
print(nickname)

#генерацию текста-заглушки
stub_text = generator.text_stub(10)
print(stub_text)

#генерация пароля
password = generator.generate_password(16)
print(password)