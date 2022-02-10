'''
author: Augusto Cesar
linkedin: https://www.linkedin.com/in/ysantz/
github: https://github.com/zSantz
Facebook: https://www.facebook.com/15151515647546bc/

create_day: 10/02/2022
'''
print('##################################')
print('##SISTEMA DE LISTA DE CONVIDADOS##')
print('##################################\n')

print('Bem vindo ao sistema de lista de convidados')
entrar = int(input('Para entrar no programa Digite 1[sim] / 2[não]: '))

nomes_convidados = []
cont2 = 1

while(entrar == 1):
    print('1 - Adicionar convidados\n2 - Remover convidados\n3 - Consultar convidados\n4 - Limpar lista\n5 - Sair ')
    menu = int(input('Digite uma opção: '))
    print('###################\n')
    if(menu == 1):
        cont = 0
        quantidade_convidados = int(input("Digite a quantidade de convidados que deseja adicionar: "))
        while(cont < quantidade_convidados):
            nomes_convidados.append(input('Digite o nome do convidado #'+ str(cont2) + ': '))
            cont += 1
            cont2 += 1
        cont = 0
        cont2 = 1
    elif(menu == 2):
            remove_convidados = input('Digite qual nome do convidado deseja remover: ')
            nomes_convidados.remove(remove_convidados)
    elif(menu == 3):
        print('###################')
        print('Lista de Convidados')
        print('###################')
        for i in nomes_convidados:
            print('-------------------')
            print(str(cont2) + ' - ' + i)
            cont2 += 1
        cont2 = 1
        print('###################\n')
    elif(menu == 4):
        print('###################\n')
        nomes_convidados.clear()
        print('Lista Excluida')
        print('###################\n')
    elif(menu == 5):
        break
print('Programa Finalizado :)')