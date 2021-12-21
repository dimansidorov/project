import requests  # импортируем библиотеку requests
import datetime  # импортируем библиотеку datetime для работы с датами


def currency_rates(valute):  # обьявляем функцию, принимающую в себя авргумент валюты
    """ Функция принимает введеную пользователем код валюты и выводит актуальную на сегодняшний день курс и номинал"""
    valute = valute.upper()  # чтобы пользователь мог ввести код валюты с маленькой буквы
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if valute not in response:  # если валюты нет - возвращаем None
        return None

    # далее через срезы берем нужные данные: сколько рублей за эту валюту, дату, номинал
    rub = response[response.find('<Value>', response.find(valute)) + 7:response.find('</Value>', response.find(valute))]
    some_date = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    nom = response[
          response.find('<Nominal>', response.find(valute)) + 9:response.find('</Nominal>', response.find(valute))]
    name_valute = response[
                  response.find('<Name>', response.find(valute)) + 6:response.find('</Name>', response.find(valute))]
    day, month, year = some_date[0], some_date[1], some_date[2]
    return f'Курс составляет {rub} рублей за {nom} {name_valute} сегодня: {datetime.datetime.strptime(f"{day}/{month}/{year}", "%d/%m/%Y").date()}'

if __name__ == '__main__':
    print(currency_rates('eur'))
    print(currency_rates('hkd'))
