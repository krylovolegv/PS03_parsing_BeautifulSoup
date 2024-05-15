from bs4 import BeautifulSoup
import requests
from googletrans import Translator

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово. text.strip удаляет все пробелы из результата
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        # Чтобы программа возвращала словарь
        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    # Функция, которая сообщит об ошибке, но не остановит программу
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def translate_to_russian(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='ru')
    return translated.text

# Создаём функцию, которая будет делать саму игру
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Получаем слово и его определение
        word_dict = get_english_words()
        if word_dict is None:
            continue

        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Переводим слово и его определение на русский язык
        word_russian = translate_to_russian(word)
        word_definition_russian = translate_to_russian(word_definition)

        # Начинаем игру
        print(f"Значение слова - {word_definition_russian}")
        user = input("Что это за слово? (Введите слово на русском) ")
        if user.lower() == word_russian.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word_russian}")

        # Создаём возможность закончить игру
        play_again = input("Хотите сыграть еще раз? да/нет ")
        if play_again.lower() != "да":
            print("Спасибо за игру!")
            break

word_game()
