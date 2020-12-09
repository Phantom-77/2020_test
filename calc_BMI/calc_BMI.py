# This is a sample app 'calculator body mass index' (BMI)

from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print(Style.BRIGHT + Back.BLUE + 'Это калькулятор индекса массы тела')
print(Back.RESET)
a = int(input('Введите свой рост (см):'))
b = int(input('Введите свой вес (кг):'))
c = b / (a / 100) ** 2
res = round(c, 1)

if res < 15.9:
    print('Ваш ИМТ= ' + str(res))
    print(Back.RED + 'Внимание! У Вас ярко выраженный дефицит массы!')
elif 16 <= res <= 18.5:
    print('Ваш ИМТ = ' + str(res))
    print(Back.YELLOW + 'У Вас дефицит массы тела')
elif 18.6 <= res <= 25:
    print('Ваш ИМТ = ' + str(res))
    print(Back.GREEN + 'У вас масса тела в норме')
elif 25.1 <= res <= 30:
    print('Ваш ИМТ = ' + str(res))
    print(Back.YELLOW + 'У вас предожирение')
elif 30.1 <= res <= 35:
    print('Ваш ИМТ = ' + str(res))
    print(Back.MAGENTA + 'У вас ожирение I степени!')
elif 35.1 <= res <= 40:
    print('Ваш ИМТ = ' + str(res))
    print(Back.RED + 'У вас ожирение II степени!')
else:
    print('Ваш ИМТ = ' + str(res))
    print(Back.RED + 'Внимание!!! У вас ожирение III степени!')

input()
