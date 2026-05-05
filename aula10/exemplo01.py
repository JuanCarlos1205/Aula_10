# Calculo de produtividade
# ------------------------

print('***Calculo de Produtividade***')

try:
    total_produzido = float(input('Valor total da venda: '))
    funcionarios = int(input('Total de funcionarios: '))

    media_por_funcionario = total_produzido / funcionarios
    print(f'Media por funcionario: {media_por_funcionario:.2f}')  

except ValueError:
    print('Informe um numero')

except ZeroDivisionError:
    print('Divisao por zero')