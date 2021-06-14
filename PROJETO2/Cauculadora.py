# Perguntar para o usuario qual operaçao deseja fazer 
# Pedir os dois numeros da operaçao 
# Fazer a operaçao
# mostrar o resultado na tela 
while True:
 print("- + / *:")
 #print("caso nao desejar fazer nem uma operacao digite \'Sair\':") 
 operacao = input("Qual operaçao deseja fazer? se nem uma digite \'sair\':")
 if operacao == 'sair':    
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

 
 