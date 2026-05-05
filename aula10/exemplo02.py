# Este for para de executar quando ha um erro

#for i in range(5):
#    total_produzido = float(input('Valor total da venda: '))
#    funcionarios = int(input('Total de funcionarios: '))
#
#    media_por_funcionario = total_produzido / funcionarios
#    print(f'Media por funcionario: {media_por_funcionario:.2f}')  


# For com try: Nao para de executar, se lança um erro
for i in range(3):
    try:
        total_produzido = float(input('Valor total da venda: '))
        funcionarios = int(input('Total de funcionarios: '))

        media_por_funcionario = total_produzido / funcionarios
        print(f'Media por funcionario: {media_por_funcionario:.2f}')  

    except ValueError:
        print('Informe um numero')

    except ZeroDivisionError:
        print('Divisao por zero')
    else: 
    
