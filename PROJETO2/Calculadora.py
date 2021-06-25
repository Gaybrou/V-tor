# Perguntar para o usuario qual operaçao deseja fazer 
# Pedir os dois numeros da operaçao 
# Fazer a operaçao
# mostrar o resultado na tela 
from abc import ABC

while True:
 print("Qual operaçao você deseja fazer (- + / *):")
 operacao = input("Se nem uma digete (g) para sair:")
 if operacao == 'g':    
   break

 elif operacao == '+' or operacao == '-' or operacao == '/' or operacao == '*':
  A =  int(input('primeiro numero:'))
  B =  int(input('segundo numero:'))
 else:
     print('fim:')
   
 if operacao == '+':
   Total = A + B
   print(Total)
 
 elif operacao == '/':
   Total = A / B
   print(Total)

 elif operacao == '-':
   Total = A - B
   print(Total)

 elif operacao == '*':  
  Total = A * B
  print(Total)


 
 