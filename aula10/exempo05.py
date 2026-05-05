print('***Calculo de Produtividade***')

try:
    total_produzido = float(input('Valor total da venda: '))
    funcionarios = int(input('Total de funcionarios: '))

    media_por_funcionario = total_produzido / funcionarios 

except Exception as e:
    print(f'Ops! erro nos valores de entrada!: {e}')

except KeyboardInterrupt:
    print('Operaçao cancelada pelo usuario')

# Se nao de erro executa o else
else:
    print(f'Media por funcionario: {media_por_funcionario:.2f}')
    
# Executa sempre com erro ou nao, o bloco finally sempre ira executar
finally: 
    print('Programa encerrado')
