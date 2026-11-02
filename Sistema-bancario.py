saldo= 0
limite= 500
extrato=""
numero_saques= 0
limite_saques=5
deposito=0
saque=0
print("Seja bem vindo ao sistema bancario, aqui voce podera cadastrar seus depositos, saques e extratos bancarios")

while True:
    opcao_escolhida=input("""
=============== Operações ===============
1- Deposito
2- Saque
3- Extrato
0- Sair
========================================= 
""")
    if opcao_escolhida == "1":
     valor = float(input("Digite o valor do deposito: \t"))
     if valor > 0:
       deposito += valor
       saldo+= valor
       print(f"Deposito efutuádo com sucesso! Saldo atual:{saldo}")
       extrato+= f"depositos: R${valor:.2f}\n"
       while True:
        novo_deposito=input("Deseja realizar um novo deposito? (s/n)")
        if novo_deposito.lower() == "s": 
         valor= float(input("digite o valor do deposito!\t"))
         if valor > 0:
          deposito += valor
          saldo+= valor
          print(f"Deposito efutuádo com sucesso! Saldo atual:{saldo}")
          extrato+= f"depositos: R${valor:.2f}\n"
         else:
           print("Não foi possível realizar o deposito., o valor digitado não deve ser negativo!")
        elif novo_deposito.lower() == "n":
         break    
        else:
         print("nao foi possivel reaconhecer a opção digitada, por favor digite uma das opções valdas (s/n)")    
     else:
      print("Não foi possível realizar o deposito., o valor digitado não deve ser negativo!")

    elif opcao_escolhida == "2":
      print("valor maximo de R$500 por saque")
      valor = float(input("Digite o valor do saque: \t"))
      if valor > 0 and valor <= limite and valor<= saldo and numero_saques < limite_saques:
       saque += valor 
       saldo -= valor
       numero_saques += 1
       print(f"saque efetuado com sucesso! saldo atual: {saldo}")
       extrato+= f"saques: R${valor:.2f}\n"
      elif numero_saques>= limite_saques:
        print("Você atingiu o limite de saques diários, tente novamente amanhã!")
      elif valor <= 0:
       print("Não foi possível realizar o saque., o valor digitado não deve ser negativo!")
      elif valor >limite:
       print("Não foi possível realizar o saque., valor acima do limite!")
      elif valor > saldo:
       print("Não foi possível realizar o saque., saldo insuficiente!")
      else:
       print("Não foi possível realizar o saque., por favor digite uma das opções validas")
       
      while True:
       novo_saque= input("deseja realizar um novo saque? (s/n)")
       if novo_saque.lower() == "s":
         valor=float(input("digite o valor do saque: "))
         if valor > 0 and valor <= limite and valor <= saldo and numero_saques < limite_saques:
          saque += valor 
          saldo -= valor
          numero_saques += 1
          print(f"saque efetuado com sucesso! saldo atual: {saldo}")
          extrato+= f"saques: R${valor:.2f}\n"
         elif numero_saques>= limite_saques:
          print("Você atingiu o limite de saques diários, tente novamente amanhã!")
         elif valor <= 0:
          print("Não foi possível realizar o saque., o valor digitado não deve ser negativo!")
         elif valor > limite:
          print("Não foi possível realizar o saque., valor acima do limite!")
         elif valor > saldo:
          print("Não foi possível realizar o saque., saldo insuficiente!")
         else:
          print("Não foi possível realizar o saque., por favor digite uma das opções validas")
         
       elif  novo_saque.lower() == "n":   
         break
       else:
        print("nao foi possivel reaconhecer a opção digitada, por favor digite uma das opções valdas (s/n)") 
        
    elif opcao_escolhida == "3":

     print("============== Extrato ==============")
     if extrato =="":
      print("não foram realizadas mocimentações!")
     else:
      print(extrato)

     print(f"\nSaldo atual: R$ {saldo:.2f}")
     

    elif opcao_escolhida == "0":
     print("ecerrando programa...")
     break