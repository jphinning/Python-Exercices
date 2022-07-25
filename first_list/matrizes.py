from mymatfunctions import *
from mymatutils import *

def multiplicacao_matrizes():
    m, n = ler_dimensao("Matriz A") # desempacotou a tupla, respectivamente em uma dupla atribuição
    o, p = ler_dimensao("Matriz B")
    if n == o: # verificar se pode multiplicar
        # criação das matrizes
        ma = cria_mat(m, n)
        ler_matriz("Matriz A", ma)
        mb = cria_mat(o, p)
        ler_matriz("Matriz B", mb)

        mres = multiplica_matriz(ma, mb)
        imprime_mat("Matriz A", ma)
        imprime_mat("Matriz B", mb)
        imprime_mat("Matriz R = A * B", mres)
    else:
        print(f"Coluna de A {n} é diferente da linha de B {o}. Não posso multiplicar!")

# vem a main da "aplicação"
# menu
opcao = 1
while opcao != 0:
    print("Menu de opcoes:")
    print("  0 - sair")
    print("  1 - multiplicar matrizes")
    print("  2 - multiplicar matriz por escalar")
    print("  3 - Maior, menor e soma dos elementos da matriz")
    print("  4 - determinante matriz 3x3 (Regra de Sarrus)")
    print("  5 - determinante matriz 4x4 (Teorema de Laplace)")
    print("  6 - transposta de matriz")
    opcao = int(input("  Qual sua opcao: "))
    if opcao == 0:
        break
    elif opcao == 1:
        multiplicacao_matrizes()
        # CHAMAR O EQUIVALENTE DO NUMPY E MOSTRAR OS RESULTADOS PARA COMPARAR
    elif opcao == 2:
        print ("Escolheu dois")
        # segue com as diversar opções solicitas
        # os algoritmos, sem interação com usuário, devem virar funções no módulo mymatfunctions
        # eventuais funções reutilizáveis com alguma interação deverm ser incluídos em mymatutils
        # o corpo da função escolhida deve vir neste script
        # (ver como foi distribuída a multiplicação de matrizes)
    elif opcao == 3:
        