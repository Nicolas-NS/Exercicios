#-1-crie um programa que escreva uma saudação com uma mensagem personalizada----------------------------------------------------------------------------------
# nome = input("qual seu nome? ")
# print(f"olá {nome}, bem vindo !!")

#-2-crie um programa que formate a data de nascimento de uma pessoa----------------------------------------------------------------------------------

# dia = input("dia que você nasceu: ")
# mês = input("mês que você nasceu: ")
# ano = input("ano que você nasceu: ")

# print(f"{dia}/{mês}/{ano}")

#-3-crie um programa que printa a soma de dois números----------------------------------------------------------------------------------

# numero1 = int(input("numero: "))
# numero2 = int(input("numero: "))

# print(numero1 + numero2)

#-4-crie um programa que diga o dobro o triblo e a raiz quadrada de um número-------------------------------------------------------------------

# n = int(input("escreva um número qualquer: "))
# dobro = n*2
# triplo = n*3
# raiz = n**1/2

# print(f"o dobro do seu número é {dobro}, o triplo é {triplo} e a raiz é {raiz}")

#-5-crie um programa que tire a média de duas notas de um aluno--------------------------------------------------------------------------

# nota1 = float(input("escreva nota1: "))
# nota2 = float(input("escreva nota2: "))

# print("a media é", (nota1 + nota2)/2)

#-6-crie um programa que trasforme um valor de metros em centimetros e em milimetros-------------------------------------------------------

# metros = int(input('escreva seu valor em metros: '))

# centimetros = metros * 100
# milimetros = metros * 1000

# print(f'o valor em centimetros é {centimetros} o  valor em milimetros é {milimetros}')

#-7-crie um programa que leia um número qualquer e faça sua tabuada----------------------------------------------------------------------

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

#-8-crie um programa leia quanto dinheiros uma pessoa tem na sua carteira e quantos dolas ela pode compra----------------------------------------------------------------------
#obs: dolar = 3.27 R$
# r = int(input('valor na sua carteira: '))

# dolar = r/3.27
# dolar = round(dolar,2)

# print(f"você pode compra {dolar} dolares")

#-9-crie um programa que leia a largura e aultura de uma parede e calculer sua área e quanto de tinta necessária pra pintala----------------------------------------------------------------------
#obs: um litro de tinta pinta 2m²

# L = float(input('largura da parede: '))
# A = float(input('aultura da parede: '))
# área = A*L
# print(f'a área da parede é {área}')
# print('a quantidade de tinta necessária é',área /2 )

#-9-crie um programa que leia um preço de  um protudo e der seu novo preço em 5% desconto----------------------------------------------------------------------

# p = int(input("preço do protudo: "))
# p1 =  p * 0.05
# p = p - p1
# print('O novo preço do protudo é', p)

#-9-crie um programa que leia um salario de  um fucionario e der seu novo salario com 15% de aumento----------------------------------------------------------------------

# s = int(input("salario atual: "))
# s1 =  s * 0.15
# s = s1 + s
# print('O novo salario com aumento de 15% é:', s)

#-10-crie um fução que caulcule uma equação do segudo grau---------------------------------------------------------------------------------- 

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

#-11--Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar----------------------------------
# número = int(input("escreva um número qualquer: "))

# if número/2 == 0:
#     print("seu número é PAR")
# else:
#     print("seu número é IMPAR")

#-12-Desenvolva um programa que altere em tempo de execução a palavra Java pela palavra Python na frase Exercícios de Java------------------

# javapy = 'exercício de java'
# print(javapy)
# pyjava = javapy.replace("java", "python")
# print(pyjava)#1 Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar.
# número = int(input("escreva um número qualquer: "))

# if número/2 == 0:
#     print("seu número é PAR")
# else:
#     print("seu número é IMPAR")

#-13-Desenvolva um programa que altere em tempo de execução a palavra Java pela palavra Python na frase Exercícios de Java------------------

# javapy = 'exercício de java'
# print(javapy)
# pyjava = javapy.replace("java", "python")
# print(pyjava)

#-14-Desenvolva um programa que leia um número inteiro qualquer e que apresete o número informado, seguido do seu antecessor e do seu sucessor

# número = (input("escreva um número qualquer: "))
# #antecessor = número - 1
# #sucessor = número + 1
#print(f'seu numero é {número}, o antecessor dele é {antecessor} e o sucessor dele é {sucessor}.')------------------------------------------------------

#-15-faça um programa que calcule se com 3 retas é possivel forma um triangulo---------------------------------------------------------------------

# reta1 = float(input("reta 1: "))
# reta2 = float(input("reta 2: "))
# reta3 = float(input("reta 3: "))

# if reta1 + reta2 < reta3: print("não é possivel formar um triangulo")
# elif reta2 + reta3 < reta1: print("não é possivel forma um triangulo")
# elif reta1 + reta3 < reta2 : print("não é possivel forma um triangulo")
# else: print('é possivel forma um triangulo :)')

#-16-Escreva um programa para aprove o empréstimo bancá para a compra de um casa----------------------------------------------------------------------
#obs: O programa va parguntar o valor da casa, o salário do comprador a am quantos anos ele va pagar.
#Calcula o valor da prestação mensal. sabendo que ela não pode exceder 30% do salário ou então o empréstimo ser negado.

# valor_da_casa = float(input("escreva o valor da  casa: "))
# salario = float(input('escreva o seu salario mensal: '))
# anos = int(input('escreva em quantos anos você ira pagar a casa: '))

# prestação = round(valor_da_casa/(anos*12))
# if prestação > 0.30*salario :
#     print(f"O finaciamento não foi aprovado!, o valor das parcelas ({prestação}), é maior que 30% do seu salario ")
# else:
#     print(f'finaciamento foi aprovado!, com parcelas de {prestação} por {anos} anos.')

#-17-A-Confederação Nacional de Natação precisa da um programa que leia o ano de nascimento de um atleta e mostre sua categoria, da acordo com a idade:

# anoquenasceu = int(input("escreva o ano que você nasceu: "))
# idade = 2024 - anoquenasceu
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

#-18-Faça-um-analisador-de-números-primos--------------------------------------------------------------------------------------------------------------------

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

#-19-Faça-uma-analise-de-nome------------------------------------------------------------------------------------------------------------

# nome = str(input("qual seu nome?: ")).strip()
# separa = nome.split()

# print('Seu nome Maiúsculo é:', nome.upper())
# print('Seu nome minúsculo é:', nome.lower()) 
# print(f'seu nome tem {len(nome) - (nome.count(' '))} letras.')
# print(f'seu primeiro é {separa[0]} nome tem {len(separa[0])} letras.') 

#-20-Faça-um-analisador-de-nome-de-cidade-e-diga-se-ela-começa-com-santo------------------------------------------------------------------------------------------------------------

# city = input('escreva o nome da sua cidade: ').strip().capitalize()
#  if city[0:5] == 'Santo':
#     print(f'O nome da sua cidade é {city} e começa com Santo.')
# else:
#     print(f'O nome da sua cidade é {city} e não começa com Santo.')

#-21-Faça-um-analisador-de-nome-que-diga-se-o-nome-tem-ou-não-'silva'---------------------------------------------------------------

# nome = input("digite seu nome: ").strip().lower()
# i = nome.find('silva')
# if i == -1:
#     print('seu nome não tem silva.')
# else:
#     q = nome.count('silva')
#     print(f'seu nome tem {q} silvas.')

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

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

#-21-Faça-um-programa-que-leia-dois-números-e-abra-um=menu-pra-você-escolher-as-opções--------------------------------------------------

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
#         print(f' a mutiplicação de {n1}+{n2}={n1*n2}')
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
#         print("escola novos números")
#         n1 = int(input("digite um números: "))
#         n2 = int(input("digite um segundo número: "))
#         print("=-=-=-=-=-=-=-=-=-=-=-=-=-")
#     else:
#         print('digite uma opção válida!!!')
#         print("=-=-=-=-=-=-=-=-=-=-=-=-=-")
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

import random 


print("=-="*10)
print("BORA JOGAR ÍMPAR OU PAR!!")

cont = 0

while True:
   print("=-="*10)
   número_jogador = int(input('Digite um número: '))
   escolha = input("PAR ou IMPAR [P/I]: ").upper().strip()
   print('---' * 10)

   número_pc = random.randint(0,10)

   total = número_pc + número_jogador 
   if total % 2 == 0: 
      resuldado = "PAR"
   else:
      resuldado = 'Impar'

   print(f"Você escolheu {número_jogador} e o computador {número_pc}. Total deu {total} é {resuldado}")
   print('---' * 10)

   if escolha[0] == resuldado[0]:
      print('você ganhou!!!')
      print("Vamos jogar novamente...")
      cont += 1
   else:
      break

print(f'Game over. Você venceu {cont} rodadas.')



#=========================================================================================================================================


