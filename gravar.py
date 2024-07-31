arquivo = open('teste.txt','w')
arquivo.write('teste')
arquivo.close()

leitura = open('teste.txt','r')
dados = leitura.read()
print(dados)
leitura.close()