from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

# Найти все цитаты и авторов
texts = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# Проверить, что количество цитат и авторов совпадает
if len(texts) != len(authors):
    raise ValueError("Количество цитат и авторов не совпадает!")

#С помощью функции range(len) определим общее количество цитат
for i in range(len(texts)):
#Присвоим номер каждой цитате так, чтобы нумерация шла с 1
    print(f"Цитата номер - {i + 1}")
#Выводим саму цитату, указывая её id
    print(texts [i].text)
#Выводим автора цитаты
    print(f"Автор цитаты - {authors[i].text}\n")

