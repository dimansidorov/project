import re

def email_parse(email):
    pattern = re.compile(r'^(?P<username>\w+)@(?P<domain>\w+\.\w+)$')
    result = pattern.match(email)
    print(result)
    if result:
        return result.groups()
    else:
        raise ValueError(f'Введен некорректный адрес электронной почты: {email}')

user_email = input('Введите адрес электронной почты: ')
print(email_parse(user_email))