nome = input("informe o nome do usuário: ")
peso = float(input("informe o peso em kg: ").replace(",", ".")) 
#o replace serve para que o usuario coloque ,.
altura= float(input("informe a altura em metros: ").replace(",", ".")) 

imc = peso/(altura**)

#imprimindo

print(f" O IMC de {nome} é {imc:,.2f}.")

#diagnostico
if imc < 16.9:
    print (f"{nome} Abaixo do peso.") 
elif imc < 18.5:
    print (f"{nome} Peso normal.")
elif  imc < 25:
    print (f"{nome} Sobrepeso.")
else:
    print (f"{nome} obesidade.")
    