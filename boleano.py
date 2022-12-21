x = int(input('Valor de x: ')) #qualquer coisa 
num = x = 1 
vet = []
while num != 0: #enquanto a entrada não for 0 vai continuar o laço.
 num = int(input("Valor: ")) #valores de entrada vão ser testados no if.
 if num != 3 and num != 0: #se os valores de entrada forem diferentes de 3 e de 0 , o valor será adicionado na lista.
  vet.append(num) #vai adicionar o NUM (valores de entrada) no final da lista. (append = adicionar o item no final da lista)
 elif num != 0: #se num(entrada) for == 3 , o ultimo valor da lista vai ser excluido , e esse valor vai ser armazenado na variavel X.
  x = vet.pop() #x vai adquirir o ultimo item da lista e vai deletá-lo.
print("{} e o vetor {}".format(x, vet))

