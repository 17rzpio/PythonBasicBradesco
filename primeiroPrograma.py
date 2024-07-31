pi = 3.14
raio = int(input(" digite o raio: "))
area = pi * raio ** 2
print (" a area eh: ",area)

salario = 1500
tipo = type (salario)
print(salario)
print(tipo)

salario = 1500
codigo = 10.6
nome = "rodrigo"
estado = salario > codigo
tipo = type (salario)
print("codigo",codigo,"tipo", type(codigo),"nome",nome,"tipo",type(nome),"salario",salario,"tipo",type(salario),"estado",estado,"tipo",type(estado))

salario = 15004
codigo = 10.64
nome = "rodrigop"
estado = salario < codigo
print("codigo"+str(codigo)+"tipo"+ str(type(codigo))+"nome"+nome+"tipo"+str(type(nome))+"salario"+str(salario)+"tipo"+str(type(salario))+"estado"+str(estado)+"tipo"+str(type(estado)))
print("nome %s"%nome)

salario = int(input("digite salario"))
print("salario eh %d"%salario)