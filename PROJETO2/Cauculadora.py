# Perguntar para o usuario qual operaçao deseja fazer 
# Pedir os dois numeros da operaçao 
# Fazer a operaçao
# mo
# mostrar o resultado na tela 
print("- + / *:")
operacao = input("which operation do you want to do:")
A =  int(input('fist number:'))
B =  int(input('Second number:'))

if operacao == '+':
   Total = A + B
   print(Total)
 
elif operacao == '/':
   Total = A / B
   print(Total)

elif opercao == '-':
   Total = A - B
   print(Total)

elif operacao == '*':  
  Total = A * B
  print(Total)

else:
    print('operaçao invalida')
 