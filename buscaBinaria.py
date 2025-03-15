# Ex 1

lista = [5,2,9,1,7,6]

#Ordena a lista
lista.sort()
print(lista)

#Ex 2

#Ordena de forma decrescente
lista.sort(reverse=True)
print(lista)

#Ex 3

lista = [5,2,9,1,7,6]

#Também orndena de forma crescente
lista_ordenada = sorted(lista)
print(lista_ordenada)

#Ex 4

lista = [5,2,9,1,7,6]

#Também orndena de forma crescente
lista_ordenada1 = sorted(lista, reverse=True)
print(lista_ordenada1)

#Ex 5

lista_frutas = [('maça', 3), ('banana',1),
                ('laranja',4),('uva',2)]

#Ordena pelos números pois no índice 1 esta números
lista_ordenada2 = sorted(lista_frutas, key=lambda x:x[1])
print(lista_ordenada2)

#Com o índice 0 ele irá ordernar em ordem alfabética pois é string
lista_ordenada3 = sorted(lista_frutas, key=lambda x:x[0])
print(lista_ordenada3)

#Ex 6

lista_frutas = [('maça', 3), ('banana',1),
                ('laranja',4),('uva',2)]

lista_ordenada4 = sorted(lista_frutas, key=lambda z: (z[1], z[0]))
print(lista_ordenada4)

#Estrutura de busca binária usando while

def busca_binaria(lista,alvo):

    l,h = 0, len(lista) - 1
    iteracao = 0

    while l <= h:
        m = (l + h) // 2
        print(f"Iteração{iteracao}: l={l}, h={h}, m={m}")

        if lista[m] == alvo:
            return m
        elif lista[m] < alvo:
            l = m + 1
        else:
            h = m - 1

    return - 1

lista = [11,15,20,27,28,50,56]
alvo = 28

resultado = busca_binaria(lista,alvo)
print(resultado)

#Estrutura de busca binária usando for

def busca_binaria(lista,alvo):

    l, h = 0, len(lista) -1

    for i in range(len(lista)):
        m = (l + h) // 2
        print(f"Iteração {i + l}: l={l}, h={h}, m={m}")

        if lista[m] == alvo:
            return m
        elif lista[m] < alvo:
            l = m + 1
        else:
            h = m - 1
    return - 1

lista = [11,15,20,27,28,50,56]
alvo = 50
resultado = busca_binaria(lista, alvo)
print(resultado)
