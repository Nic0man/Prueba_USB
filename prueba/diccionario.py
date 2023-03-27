monedas = {'euro':'€', 'dollar':'$', 'yen':'¥'}
divisa = input('Que divisa quiere utilizar? ')
if divisa in monedas:
    print(f'la divisa si existe en el sistema')
else:
    print(f'la divisa no existe en el sistema')

