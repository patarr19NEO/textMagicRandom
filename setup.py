from setuptools import setup, find_packages

setup(
    name="textMagicRandom",
    version="1.3.0",
    author="patarr19",
    description="Генератор никнеймов, паролей и текстовых заглушек",  # Описание
    packages=find_packages(),  # Автоматически найдет все пакеты
    python_requires=">=3.6",   # Минимальная версия Python
)