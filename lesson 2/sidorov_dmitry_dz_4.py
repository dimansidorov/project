wrong_staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']


for member in wrong_staff:
    member.split()[-1].title()
    print(f'Привет, {member.split()[-1].title()}')