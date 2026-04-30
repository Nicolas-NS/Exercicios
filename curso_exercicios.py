# -1-crie-um-programa-que-escreva-uma-saudação-com-uma-mensagem-personalizada----------------------------------------------------------------------------------

# nome = str(input("qual seu nome? "))
# print(f"olá {nome}, bem vindo !!")

# -2-crie-um-programa-que-formate-a-data-de-nascimento-de-uma-pessoa----------------------------------------------------------------------------------

# dia = int(input("dia que você nasceu: "))
# mês = int(input("mês que você nasceu: "))
# ano = int(input("ano que você nasceu: "))

# print(f"{dia}/{mês}/{ano}")

# -3-crie-um-programa-que-printa-a-soma-de-dois-números----------------------------------------------------------------------------------

# numero1 = float(input("numero: "))
# numero2 = float(input("numero: "))

# print(numero1 + numero2)

# -4-crie-um-programa-que-diga-o-dobro-o-triblo-e-a-raiz-quadrada-de-um-número-------------------------------------------------------------------

# n = int(input("escreva um número qualquer: "))
# dobro = n*2
# triplo = n*3
# raiz = n**1/2

# print(f"o dobro do seu número é {dobro}, o triplo é {triplo} e a raiz é {raiz}")

# -5-crie-um-programa-que-tire-a-média-de-duas-notas-de-um-aluno--------------------------------------------------------------------------

# nota1 = float(input("escreva nota1: "))
# nota2 = float(input("escreva nota2: "))

# print("a media é", (nota1 + nota2)/2)

# -6-crie um programa que trasforme um valor de metros em centimetros e em milimetros-------------------------------------------------------

# metros = int(input('escreva seu valor em metros: '))

# centimetros = metros * 100
# milimetros = metros * 1000

# print(f'o valor em centimetros é {centimetros} o  valor em milimetros é {milimetros}')

# -7-crie um programa que leia um número qualquer e faça sua tabuada----------------------------------------------------------------------

# n1 = int(input('escreva um número qualque: '))

# print("a tabuada desse número:")

# print("-------------------")
# print(f"  1 x {n1} =",1*n1)
# print(f"  2 x {n1} =",2*n1)
# print(f"  3 x {n1} =",3*n1)
# print(f"  4 x {n1} =",4*n1)
# print(f"  5 x {n1} =",5*n1)
# print(f"  6 x {n1} =",6*n1)
# print(f"  7 x {n1} =",7*n1)
# print(f"  8 x {n1} =",8*n1)
# print(f"  9 x {n1} =",9*n1)
# print(f"  10 x {n1} =",10*n1)
# print("------------------")

# -8-crie um programa leia quanto dinheiros uma pessoa tem na sua carteira e quantos dolas ela pode compra----------------------------------------------------------------------
# obs: dolar = 3.27 R$
# r = int(input('valor na sua carteira: '))

# dolar = r/3.27
# dolar = round(dolar,2)

# print(f"você pode compra {dolar} dolares")

# -9-crie um programa que leia a largura e aultura de uma parede e calculer sua área e quanto de tinta necessária pra pintala----------------------------------------------------------------------
# obs: um litro de tinta pinta 2m²

# L = float(input('largura da parede: '))
# A = float(input('aultura da parede: '))
# área = A*L
# print(f'a área da parede é {área}')
# print('a quantidade de tinta necessária é',área /2 )

# -9-crie um programa que leia um preço de  um produto e der seu novo preço em 5% desconto----------------------------------------------------------------------

# p = int(input("preço do produto: "))
# p1 =  p * 0.05
# p = p - p1
# print('O novo preço do produto é', p)

# -9-crie um programa que leia um salario de  um fucionario e der seu novo salario com 15% de aumento----------------------------------------------------------------------

# s = int(input("salario atual: "))
# s1 =  s * 0.15
# s = s1 + s
# print('O novo salario com aumento de 15% é:', s)

# -10-crie um fução que caulcule uma equação do segudo grau---------------------------------------------------------------------------------- 

# import math

# def equação_segundograu (a,b,c):
#     delta = b**2 - 4 * a * c
#     raizd = math.sqrt (delta)
#     baskara_cima_positivo = -b - raizd
#     baskara_cima_negativa = -b + raizd
#     baskara_baixo = a*2
#     baskara1 = baskara_cima_positivo/baskara_baixo
#     baskara2 = baskara_cima_negativa/baskara_baixo
#     return baskara2, baskara1

# a = int(input("escerva o elemento A: "))
# b = int(input("escreva o elemento B: "))
# c = int(input("escreva o elemeto C: "))

# vain = equação_segundograu (a,b,c)
# print(vain)

# -11--Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar----------------------------------
# número = int(input("escreva um número qualquer: "))

# if número/2 == 0:
#     print("seu número é PAR")
# else:
#     print("seu número é IMPAR")

# -12-Desenvolva um programa que altere em tempo de execução a palavra Java pela palavra Python na frase Exercícios de Java------------------

# javapy = 'exercício de java'
# print(javapy)
# pyjava = javapy.replace("java", "python")
# print(pyjava)#1 Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar.
# número = int(input("escreva um número qualquer: "))

# if número/2 == 0:
#     print("seu número é PAR")
# else:
#     print("seu número é IMPAR")

# -13-Desenvolva um programa que altere em tempo de execução a palavra Java pela palavra Python na frase Exercícios de Java------------------

# javapy = 'exercício de java'
# print(javapy)
# pyjava = javapy.replace("java", "python")
# print(pyjava)

# -14-Desenvolva um programa que leia um número inteiro qualquer e que apresete o número informado, seguido do seu antecessor e do seu sucessor

# número = (input("escreva um número qualquer: "))
# #antecessor = número - 1
# #sucessor = número + 1
# print(f'seu numero é {número}, o antecessor dele é {antecessor} e o sucessor dele é {sucessor}.')------------------------------------------------------

# -15-faça um programa que calcule se com 3 retas é possivel forma um triangulo---------------------------------------------------------------------

# reta1 = float(input("reta 1: "))
# reta2 = float(input("reta 2: "))
# reta3 = float(input("reta 3: "))

# if reta1 + reta2 < reta3: print("não é possivel formar um triangulo")
# elif reta2 + reta3 < reta1: print("não é possivel forma um triangulo")
# elif reta1 + reta3 < reta2 : print("não é possivel forma um triangulo")
# else: print('é possivel forma um triangulo :)')

# -16-Escreva um programa para aprove o empréstimo bancá para a compra de um casa----------------------------------------------------------------------
# obs: O programa va parguntar o valor da casa, o salário do comprador a am quantos anos ele va pagar.
# Calcula o valor da prestação mensal. sabendo que ela não pode exceder 30% do salário ou então o empréstimo ser negado.

# valor_da_casa = float(input("escreva o valor da  casa: "))
# salario = float(input('escreva o seu salario mensal: '))
# anos = int(input('escreva em quantos anos você ira pagar a casa: '))

# prestação = round(valor_da_casa/(anos*12))
# if prestação > 0.30*salario :
#     print(f"O finaciamento não foi aprovado!, o valor das parcelas ({prestação}), é maior que 30% do seu salario ")
# else:
#     print(f'finaciamento foi aprovado!, com parcelas de {prestação} por {anos} anos.')

# -17-A-Confederação Nacional de Natação precisa da um programa que leia o ano de nascimento de um atleta e mostre sua categoria, da acordo com a idade:

# anoquenasceu = int(input("escreva o ano que você nasceu: "))
# idade = 2026 - anoquenasceu
# print(idade,'anos de idade')

# if idade <= 9:
#     print('atleta Mirim')
# elif idade <= 14:
#     print('atleta Infantil')
# elif idade <= 19:
#     print('atleta Junior')
# elif idade <= 19 :
#     print("atleta Senior")
# else:
#     print('atleta Master')

# -18-Faça-um-analisador-de-números-primos--------------------------------------------------------------------------------------------------------------------

# reset = '\033[0m'
# vermelho = "\033[31m"
# amarelo = "\033[33m"
# verde = "\033[32m"

# n = int(input(f"{reset}digite um número: "))
# a = 0
# for i in range(1,n+1):
#     if n%i == 0 :
#         print(f'{amarelo} {i} {reset}', end= " ")
#         a += 1
#     else:
#         print(f"{vermelho}{i}{reset}", end=" ")

# print(f"\no número {n} foi dividido {a} vezes")

# if a == 2:
#     print(f"{verde}ELE É UM NÚMERO PRIMO{reset}")
# else:
#     print(f"{vermelho}ELE Não É UM NÚMERO PRIMO{reset}")

# -19-Faça-uma-analise-de-nome------------------------------------------------------------------------------------------------------------

# nome = str(input("qual seu nome?: ")).strip()
# separa = nome.split()

# print('Seu nome Maiúsculo é:', nome.upper())
# print('Seu nome minúsculo é:', nome.lower()) 
# print(f'seu nome tem {len(nome) - (nome.count(' '))} letras.')
# print(f'seu primeiro é {separa[0]} nome tem {len(separa[0])} letras.') 

# -20-Faça-um-analisador-de-nome-de-cidade-e-diga-se-ela-começa-com-santo------------------------------------------------------------------------------------------------------------

# city = input('escreva o nome da sua cidade: ').strip().capitalize()
#  if city[0:5] == 'Santo':
#     print(f'O nome da sua cidade é {city} e começa com Santo.')
# else:
#     print(f'O nome da sua cidade é {city} e não começa com Santo.')

# -21-Faça-um-analisador-de-nome-que-diga-se-o-nome-tem-ou-não-'silva'---------------------------------------------------------------

# nome = input("digite seu nome: ").strip().lower()
# i = nome.find('silva')
# if i == -1:
#     print('seu nome não tem silva.')
# else:
#     q = nome.count('silva')
#     print(f'seu nome tem {q} silvas.')

# -22-Desenvolva-um-programa-que-leia-o-nome,-idade-e-sexo-de-4-pessoas.-No-final-do-programa,-mostre:-a-média-de-idade-do-grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

# i = ' '
# while i != 'm' and i != 'f' :
#     i = input("digite seu gênero[m/f]: ").lower().strip()
#     if i != 'm' and i != 'f': 
#         print('por favor digite um gênero valido[m/f]')

# if  i == 'm':
#     i = 'masculino'
# else:
#     i = 'feminino'
# print(f'seu gênero é {i}')

#-23-Faça-um-programa-que-leia-dois-números-e-abra-um=menu-pra-você-escolher-as-opções--------------------------------------------------

# n1 = int(input("digite um números: "))
# n2 = int(input("digite um segundo número: "))

# while True :
    
#     print('''[1]Soma
# [2]mutiplicar
# [3]maior
# [4]novos números
# [5]acabar programa ''')
#     fazer = int(input(">>> oq você quer fazer com esses números: "))
#     if fazer == 1:
#         print("=-=-=-=-=-=-=-=-=-=-=-=-=-")
#         print(f'a soma de {n1}+{n2}={n1+n2}')
#     elif fazer == 2:
#         print("=-=-=-=-=-=-=-=-=-=-=-=-=-")
#         print(f' a mutiplicação de {n1}*{n2}={n1*n2}')
#     elif fazer == 3:
#         if n1 > n2:
#             print("=-=-=-=-=-=-=-=-=-=-=-=-=-")
#             print(f' o maior número é {n1}')
#         else:
#             print("=-=-=-=-=-=-=-=-=-=-=-=-=-")
#             print(f"o maior número é {n2}")
#     elif fazer == 5:
#         print("=-=-=-=-=-=-=-=-=-=-=-=-=-")
#         print("fim do programa")
#         break
#     elif fazer == 4: 
#         print("escolha novos números")
#         n1 = int(input("digite um números: "))
#         n2 = int(input("digite um segundo número: "))
#         print("=-=-=-=-=-=-=-=-=-=-=-=-=-")
#     else:
#         print('digite uma opção válida!!!')
#         print("=-=-=-=-=-=-=-=-=-=-=-=-=-")



# -24-um-programa-que-mostra-a-tabuada-de-qualquer-número-natural---------------------------------------------------------------


# b = 1
# a = int(input('quer ver a tauada de qual número: '))
# print("=-=-"*5)
# while True:
    
#     if a > 0:
        
#         print(f"{a} x {b} = {a * b}")
#         b += 1
#         if b == 10:
#             b -= 9
#             print("=-=-"*5)
#             a = int(input('quer ver a tauada de qual número: '))
#             print("-=-=-"*5)
#     else: break
        
# print("número invalido!")

# -25-programa-que-joga-ímpar-ou-Par--------------------------------------------------------------------------------------------------------------------------------------------


# import random 


# print("=-="*10)
# print("BORA JOGAR ÍMPAR OU PAR!!")

# cont = 0

# while True:
#    print("=-="*10)
#    número_jogador = int(input('Digite um número: '))
#    escolha = input("PAR ou IMPAR [P/I]: ").upper().strip()
#    print('---' * 10)

#    número_pc = random.randint(0,10)

#    total = número_pc + número_jogador 
#    if total % 2 == 0: 
#       resuldado = "PAR"
#    else:
#       resuldado = 'Impar'

#    print(f"Você escolheu {número_jogador} e o computador {número_pc}. Total deu {total} é {resuldado}")
#    print('---' * 10)

#    if escolha[0] == resuldado[0]:
#       print('você ganhou!!!')
#       print("Vamos jogar novamente...")
#       cont += 1
#    else:
#       break

# print(f'Game over. Você venceu {cont} rodadas.')

#-26-um-sistema-de-cadastro-e-analíse-de-dados----------------------------------------------------------------------------------------------------------------------------------

# mais_18 = 0
# masculino = 0
# mulheres_menos_20 = 0
# p = 0 
# while True:
#     print('''-----------------------
#   CADASTRE UMA PESSOA
# -----------------------''')
#     p += 1 #contagem de pessoas

#     idadepessoa = int(input("idade: "))
    

#     Sexo = 'i' #reinicia a variável se não, buga
#     while Sexo[0] not in ('F', 'M'):  #validação apenas quando digita a opção certa
#         Sexo = input("Sexo[M/F]: ").upper().strip()

#     # analísa os dados
#     if Sexo[0] == "M": 
#             masculino += 1
#     if idadepessoa < 18 and Sexo[0] == 'F':
#             mulheres_menos_20 += 1
    

#     print('-----------------------')
#     q = '' #reinicia a variável se não, buga
#     while q not in ('N', 'S'): 
#         q = input("Quer continuar? [S/N]: ").upper().strip()
    
#     # analíse dos dados
#     if idadepessoa >= 18:
#         mais_18 += 1
#     if q[0] == 'N': 
#         break

# # resultado
# print(f'''\n    ====FIM-DO-PROGRAMA====''')
# print(f"Total de pessoas: {p}")
# print(f"Total de pessoas +18: {mais_18}")
# print(f"Total de homens: {masculino}")
# print(f"Total de Mulheres com menos 20: {mulheres_menos_20}")



#-26-um-programa-que-cadastre-produtos-e-analíse-os-dados------------------------------------------------------------------------------

# t = float('inf')
# pro1000 = 0
# total = 0
# while True:
#     print('''-----------------------
#   LOJA  DO BOLSONARO
# -----------------------''')
    
#     produto = input("Nome do Produto: ")
#     Valor = float(input('Valor do Produto: R$'))
    
#     # salva o nome do produto mais baratos
#     if t > Valor :
#         t = Valor
#         menor = produto
        
    
#     # conta o valor total das compras
#     total += Valor
#     if Valor >= 1000: 
#         pro1000 += 1 

#     # quer continuar?
#     print('-----------------------')
#     m = 'i' #reinicia a variável se não, buga
#     while m not in ('N', 'S'): 
#         m = input("Quer continuar? [S/N]: ").upper().strip()
    
#     if m[0] == 'N': 
#          break

# # resultado
# print(f'''\n    ====FIM-DO-PROGRAMA====''')
# print(f"Total de gasto: {total:.2f}")
# print(f"Protudo custam mais 1000R$ : {pro1000}")
# print(f"Protudo mais Barato: {menor}, R${t:.2f}")


#-27-um-programa-que-é-um-caixa-eletrônico-ler-um-valor-e-devolve-em-cedulas------------------------------------------------------------------------------

# print('''-----------------------
#   CAIXA ELETRÔNICO
# -----------------------''')

# valor = int(input("Qual valor você quer sacar: R$"))

# while True:
#     notas50 = valor // 50
#     resto = valor % 50
#     print(f"Total de {notas50} Notas de R$50")
#     if resto != 0 :
#         nota20 = resto // 20
#         resto = resto % 20
#         print(f"Total de {nota20} Notas de R$20")
#         if resto != 0 :
#             notas10 = resto // 10
#             resto = resto % 10
#             print(f"Total de {notas10} Notas de R$10")
#             if resto != 0 :
#                 notas1 = resto // 1
#                 print(f"Total de {notas1} Notas de R$1")
    
#     break

#-27-um-programa-que-ler-um-número-e-verefica-numa-tupla-e-devolve-um-número-por-extenço------------------------------------------------------------------------------

 
# numeros_por_extenso = (
#      "um", "dois", "três", "quatro", "cinco",
#     "seis", "sete", "oito", "nove", "dez",
#     "onze", "doze", "treze", "quatorze", "quinze",
#     "dezesseis", "dezessete", "dezoito", "dezenove", "vinte", "zero"
# )

# n = int(input(' digite um número de (0 a 20): '))
# while n < 0 or n > 20:
#     n = int(input("não valído, digite novamente: "))

# numerodigitado = numeros_por_extenso[n-1]
# print(f"Você digitou o número: {numerodigitado}")

#-28-um-programa-que-pega-5-números-aleátorios-e-adiciona-numa-tupla-e-análisa------------------------------------------------------------------------------

# from random import randint

# a = randint(1,10)
# b = randint(1,10)
# c = randint(1,10)
# d = randint(1,10)
# e = randint(1,10)

# tupla = a,b,c,d,e
# maior = 0
# menor = 11
# for i in tupla:
#     if i > maior :
#         maior = i
#     if i < menor:
#         menor = i

# print(f'os números aleatorios são {tupla}')
# print(f'o maior número dessa tupla é {maior}')
# print(f"o menor número dessa tupla é {menor}")
        
# valor1 = int(input("digite um número de (1,10): "))
# valor2= int(input("digite um número de (1,10): "))
# valor3 = int(input("digite um número de (1,10): "))
# valor4 = int(input("digite um número de (1,10): "))

# tupla = valor1,valor2,valor3,valor4
# tupla2 = 0
# nove = 0
# posição = tupla.index(3)
# for i in tupla:
#     if i == 9:
#         nove += 1
#     if i % 2 == 0:
#         tupla2 += (i,)
# print(f'O valor 9 aparece {nove} vezes')
# print(f"O número 3 aparece na {posição}* posição")
# print(f'{tupla2}')

#-29-um-programa-que-adiciona-números-a-uma-lista-e-não-permite-repeti-itens-e-retonar-os-itens-em-ordem-cresente------------------------------------------------------------------------------

# valor = []

# while True :
#     continuar = 'reset'
#     adicionador = (int(input('Typer one Number: ')))
#     if adicionador not in valor:
#         valor.append(adicionador)
#         print("Valor foi adicionado...")
#     else: 
#         print('esse valor ja existe na lista...')

#     while continuar not in ('N','S'):
#         continuar = input("Você quer continuar [S/N]: ").strip().upper()

#     if continuar[0] == 'S':
#         continue
#     elif  continuar[0] == 'N':
#         break

#     continuar = 'reset'

# valor.sort()
# print(f'os valores que você escreveu foram {valor}')

#-30-um-programa-que-adiciona-números-a-uma-lista-e-separa-em-duas-outras:lista-par,-lista-ímpar------------------------------------------------------------------------------
 
# valor = []
# par = []
# impar = []

# while True :
#     continuar = 'reset'
#     adicionador = (int(input('Typer one Number: ')))
#     valor.append(adicionador)


#     while continuar not in ('N','S'):
#         continuar = input("Você quer continuar [S/N]: ").strip().upper()

#     if continuar[0] == 'S':
#         continue
#     elif  continuar[0] == 'N':
#         break

#     continuar = 'reset'

# for v in valor:
#     if v % 2 == 0:
#         par.append(v)
#     else :
#         impar.append(v)

# print("os valores digitados da lista foram:",valor)
# print("os valores Pares são:",par)
# print("os valores ímmpares são:",impar)

#-31-um-programa-que-adiciona-peso-e-nome-a-uma-lista-depois-analísa-os-dados------------------------------------------------------------------------------

# dados = []
# total = []
# donomenor = []
# donomaior = []
# pessoas = 0
# maiorpeso = 0
# menorpeso = float('inf')

# while True :
#     continuar = 'reset'
#     adicionador1 = (str(input('Escreva seu Nome: ')))
#     dados.append(adicionador1)
#     adicionador2 = (int(input('Escreva seu Peso: ')))
#     dados.append(adicionador2)

#     total.append(dados[:])
#     dados.clear()
#     pessoas += 1

#     while continuar not in ('N','S'):
#         continuar = input("Você quer continuar [S/N]: ").strip().upper()

#     if continuar[0] == 'S':
#         continue
#     elif  continuar[0] == 'N':
#         break
    
#     continuar = 'reset'

#-32-um-programa-que-leia-peso-e-nome-das-pessoas-depois-análise------------------------------------------------------------------------------

# for i in total:
#     print(i[1],i[0])
#     if i[1] > maiorpeso : 
#         maiorpeso = i[1]
#     if i[1] < menorpeso :
#         menorpeso = i[1]
    
# for i in total:
#     if i[1] == maiorpeso:
#         donomaior.append(i[0])
#     if i[1] == menorpeso:
#         donomenor.append(i[0])

# print(f'total  de {pessoas} entrevistadas.')
# print(f"Maior pesso foi {maiorpeso}, de {donomaior}")
# print(f"Maior pesso foi {menorpeso}, de  {donomenor}")

#-33-um-programa-que-adiciona-números-a-uma-lista-com-duas-lista-par-e-impar------------------------------------------------------------------------------

# números = [[], []]  

# for cont in range(7):
#     n = int(input('Escreva um número: '))
    
#     if n % 2 == 0:
#         números[1].append(n)  
#     else:
#         números[0].append(n)  

# números[0].sort()
# números[1].sort()

# print(f'Os números ímpares são: {números[0]}')
# print(f'Os números pares são: {números[1]}')

# matriz = [[0,0,0],[0,0,0],[0,0,0]]

# for l in range (0,3):
#     for c in range(0,3):
#         matriz [l] [c]= int(input(f"escreva um número na posição ({l},{c}): "))


# for l in range(0,3):
#     for c in range(0,3):
#         print(f'[{matriz [l] [c]:^5}]', end='')
#     print()


#-34-um-programa-que-adiciona-númenos-a-uma-Matríz------------------------------------------------------------------------------

# print("CRIAÇÃO DE UMA MATRÍZ!")
# print('''[] [] []
# [] [] []
# [] [] []''')

# matriz = [[1,2,3],[4,5,6],[7,8,9]]

# for l in range (0,3):
#     for c in range(0,3):
#         matriz [l] [c]= int(input(f"escreva um número na posição ({l},{c}): "))

# print("SUA MATRIÍZ:")
# print("-=-=-=-"*3)
# for l in range(0,3):
#     for c in range(0,3):
#         print(f'[{matriz [l] [c]:^5}]', end='')
#     print()
# print("-=-=-=-"*3)

# totalp = 0
# for l in range(3):
#     for c in range(3):
#         if matriz[l][c] % 2 == 0:
#             totalp += matriz[l][c]

# soma = 0
# for l in range(3):
#    soma += matriz [l] [2]

# maior = matriz[1][0]
# for c in range(3):
#     if matriz[1] [c] > maior:
#         maior = matriz[1] [c]

# print("Soma total dos números pares:", totalp)
# print(f'soma de todo os itens da coluna 3:{soma}')
# print('o maior item da lina 2:',maior)

#-35-um-programa-que-crie-jogos-de-MegaSena------------------------------------------------------------------------------

# import random
# from time import sleep
# print('=-=-='*3)
# print('   MEGA SENA')
# print('=-=-='*3)

# t = []
# n = int(input("digite a quantidade de jogos: "))
# for cont in range(1,n+1):
#     palpit = random.sample(range(0,61), k=6)
#     print(f'o jogo {cont}:{palpit}')
#     t.append(palpit[:])
#     sleep(1)
    
# print(f'os jogos são {t}')

#-36-um-programa-que-adiciona-nomes-e-notas-e-adiciona-a-uma-lista-composta-e-mostre-as-médias------------------------------------------------------------------------------

# lista_alunos = []

# while True:
#     nome = (input("NOME: "))
#     nota1 = float(input("NOTA1: "))
#     nota2 = float(input("NOTA2: "))
#     aluno = [nome,nota1,nota2]
    
#     lista_alunos.append(aluno)
    
#     continuar = 'corintias'
#     while continuar[0] not in ['s','n']:
#         continuar = input("Quer Continuar [s/n]: ").strip().lower()

#     if continuar[0] == 'n':
#         break
# print("")

# print('BOLETIM: ')
# print("N*.| Nomes         |Médias")
# print('-------'*4)
# for cont in range(0,len(lista_alunos)):
#     print(cont,'|', end='')
#     print(lista_alunos[cont] [0], end='-=-=-=-') 
#     print((lista_alunos[cont] [1] + lista_alunos[cont] [2]) / 2)
# print('-------'*4)
# print("")

# while True:

#     quem = int(input("Você quer mostrar a nota de qual aluno? (999 para interromper): "))
#     if quem == 999:
#         break

#     print("as notas foram: ",lista_alunos [quem] [1],lista_alunos [quem] [2])

# print("fim do programa!")

#-37-avaliacao-de-alunos-e-sistema-de-ranking-com-dados---------------------------------------------------------------------------------------------------

# aluno = {}
# aluno['nome'] = str(input("Nome: "))
# aluno['Média'] = float(input("Média: "))

# if aluno['Média'] >= 7:
#     aluno['Situação'] = 'Aprovado'
# else:
#     aluno['Situação'] = 'Reprovado'
# print('-=-=-='*3)
# for k,v in aluno.items():
#     print(f"{k} é {v}")
# print('-=-=-='*3)

# #Sorteio Dados
# from random import randint
# from time import sleep
# from operator import itemgetter

# resultados = {}
# resultados['jogador1'] = randint(1, 6)
# resultados['jogador2'] = randint(1, 6)
# resultados['jogador3'] = randint(1, 6)
# resultados['jogador4'] = randint(1, 6)

# for k,v in resultados.items():
#     print(f"{k} tirou {v}")
#     sleep(1)

# Ranking = dict()

# Ranking = dict(sorted(resultados.items(), key=itemgetter(1), reverse=True))

# n = 1
# print('-=-=-'*3)
# print('    RANKING')
# print('-=-=-'*3)
# for k,v in Ranking.items():
#     print(f'{n}* Lugar: {k} com {v}')
#     n += 1
#     sleep(1)
# print('-=-=-'*3)

#-38-sistema-de-cadastro-com-idade-trabalho-e-aposentadoria--------------------------------------------------------------------------------------

# from datetime import datetime
# anoatual = datetime.now().year
# dados = {}

# dados['nome'] = input("Nome: ")
# dados['idade'] = anoatual - int(input("Ano de Nascimento: ")) 
# Carteira = int(input("Número da Carteira de Trablho: "))

# if Carteira != 0:
#     dados['Carteira de Trabalho'] = Carteira
#     dados['Ano de Contradação']  = int(input("Ano da Contradaçâo: "))
#     dados['Salário']  = float(input("Seu Salário: "))
#     anosdetrabalho = anoatual - dados['Ano de Contradação']
#     if anosdetrabalho < 35:
#         dados['Aposentadoria'] = (35 - anosdetrabalho) + dados['idade']
#     else:
#         dados['Aposentadoria'] = 'Já esta aposentado'
# else:
#     dados['Carteira de Trabalho'] = 'Não em'

# print('-=-=-'*3)
# print('     DADOS')
# print('-=-=-'*3)
# print(dados)
# for k,v in dados.items():
#     print(f'{k} é {v}')

#-39-cadastro-de-jogador-com-estatisticas-de-gols-por-partida--------------------------------------------------------------------------------------------------

# dados = {}

# dados['nome'] = input("Nome do jogador: ")
# n_partidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))

# dados['gols'] = []

# for cont in range(0, n_partidas):
#     gols = int(input(f"Quantos gols na partida {cont+1}: "))
#     dados['gols'].append(gols)

# dados['total'] = sum(dados['gols'])

# print('-=-=-'*3)
# print(dados)
# print('-=-=-'*3)

# for k,v in dados.items():
#     print(f"{k} é {v}.")

# print('-=-=-'*5)
# print(f"O jogador {dados['nome']} Jogou {n_partidas} Partidas.")
# for i,gols in enumerate(dados['gols']):
#     print(f'Na partida {i}*, marcou {gols} gols')

# print(f'Total foi {dados["total"]} gols')

#-cadastro-e-analise-de-pessoas-com-media-e_filtro_de_idade-------------------------------------------------------------------------------------------------
 
# dados = dict()
# lista = list()

# while True:
#     dados['Nome'] = input("Nome: ")
    
#     while True: 
#         Sexo = input("Sexo: [M/F] ").strip().upper()
#         if Sexo[0] in ('M','F'):
#             break
#     dados['Sexo'] = Sexo

#     dados['Idade'] = int(input("Idade: "))
#     lista.append(dados.copy())

#     continuar = '0'
#     while continuar[0] not in ('N','S'):
#         continuar = input("Deseja Continuar? [S/N] ").strip().upper()

#     if continuar[0] == 'N':
#         break

# media = sum(i['Idade'] for i in lista) / len(lista)

# # Cria uma Lista do nome das mulheres cadastradas.
# mulheres = [i['Nome'] for i in lista if i['Sexo'] == 'F']

# print('-=-=-=-'*10)
# print(f'- Foram a cadastradas {len(lista)} Pessoas ')
# print(f'- A média das Idades é {media} Anos')
# print(f'- As mulheres cadastradas foram: {mulheres}')

# print(f'\n- Lista de pessoas acima da média de idade: \n')

# # Mostra quantas pessoas estão acima do média de idade.
# for i in lista:
#     if i['Idade'] > media: 
#         print(i,'\n')
        
#funções de textos:
from time import sleep
def titulo(a):
    tam = len(a) + 2
    print("-"*tam)
    print("",a)
    print("-"*tam)

def linha(a):
    print("-"*a)

#-41-contador-personalizado-com-validacao-de-passo-e-animacao-de_saida---------------------------------------------------------------------------------------

# def contador(i, f, p):
#     """
#     A função contador faz uma contagem de acordo com um passo e um número inicial até um número final.
#     i = número Inicinal
#     f = número final
#     p = passo, contagem do número
    
#     """

#     if p == 0:
#         print('Passo não pode ser 0!')
#         return
    
#     print(f'Contagem de {i} até {f} de {p} em {p}:')
    
#     if i < f and p < 0:
#         p = -p
#     if i > f and p > 0:
#         p = -p

#     if p > 0:
#         while i <= f:
#             print(i, end=' ', flush=True)
#             sleep(0.2)
#             i += p
#     else:
#         while i >= f:
#             print(i, end=' ', flush=True)
#             sleep(0.2)
#             i += p

#     print('FIM!')

# contador(1,10,1)
# contador(10,1,-1)
# contador(10,1,1)
# contador(10,1,0)
# help(contador)

#Programa de autenticação de senha.

# def validação(senha):
#     if len(senha) < 8:
#         return False

#     tem_numero = tem_maiuscula = tem_minuscula = False

#     for caracter in senha:
#         if caracter.isupper():
#             tem_maiuscula = True
#         if caracter.islower():
#             tem_minuscula = True
#         if caracter.isdigit():
#             tem_numero = True

#     return tem_maiuscula and tem_minuscula and tem_numero


# while True:
#     senha = input("Crie sua senha: ")
#     if validação(senha):
#         print("Senha criada com sucesso!")
#         break
#     print("Senha inválida, tente de novo.")

# print("Obrigado")



#função voto

# def voto(ano_nascimento):
#     import datetime

#     ano_atual = datetime.datetime.now().year
#     idade = ano_atual - ano_nascimento

#     if idade < 16: return (f"Idade igual a {idade}, NÃO PODE  VOTAR!!")

#     elif 16 <= idade < 18 or idade > 65 : return (f"Idade igual a {idade}, VOTO OPCIONAL!!")

#     else : return (f"Idade igual a {idade}, VOTO OBRIGAtóRIO!!")

# titulo("Função Análiser de voto")

# ano_nascimento = int(input("Escreva o ano que você nasceu: "))
# print(voto(ano_nascimento))

# linha(20)

def fatorial(n, show=False):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
        print(resultado)
    return resultado

print(fatorial(5))




# ========================================================================================================================================

