s = 1000

try: 
    v = float(input('Informe o valor que deja retirar: '))
except ValueError:
       print('Informe um numero!')

except KeyboardInterrupt:
        print('Operaçao cancelada pelo usuario')
else:
    if v > s:
        print('Saque exedido do saldo.')
    
    elif v <= 2:
        print('Saque precisa ser maior que R$ 2,00')
        
    else:
        sf -= v
        print('\nSaque realizado com sucesso')
        print(f'O saldo depois do retiro e: {sf:.2f}')
finally:
    print('Operacao realizada')

print('\nPrograma encerrado')
