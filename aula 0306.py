def main():
 idade = -1

 while idade < 0:
  idade = int(input("Digite a sua idade: "))
  if idade < 0:
   print("Idade inexistente, digite novamente: \n")

#idade = int(input("Digite a sua idade: "))
 if idade < 0: 
    print("idade inexistente")
 elif idade < 5:
  print("Você está na creche")
 elif idade >= 5 and idade <= 10:
  print("Você está no fundamental (1° ao 5° ano)")
 elif idade >= 11 and idade < 16:
  print("Você está no fundamental 2 (6° ao 9° ano)")
 elif idade >15 and idade <= 18:
  print("Você está no ensino médio (1° ao 3° ano)")
 else:
  print("Você está fora da escola")
  return 0
main()