import sys

def collatz(number):
    while number > 1: # enquanto não chegar a 1 vai rodar a função!!!
        print(number, end=', ') # Mostrar os resultados
        if number % 2 == 0: # even
            number = number//2 # define o valor pra retornar
        else:
            number = 3*number + 1
    print(1) # quando chegar a 1 vai mostrar 1 e terminar

try:
    while True:
        try:
            print('Please enter a integer number or press CTRL+C to exit')
            playerNumber = int(input())
            print('Your sequence: ', end='')
            collatz(playerNumber)
        except ValueError:
            print('Please enter a valid number')
            continue # loops back
except KeyboardInterrupt:
    sys.exit()

