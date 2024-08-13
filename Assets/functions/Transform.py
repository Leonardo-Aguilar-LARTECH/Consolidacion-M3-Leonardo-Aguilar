import os

magos = []
cientificos = []
otros = []


def agrupar(list):

    for i in list:
        if i == "Harry Houdini" or i == "David Blaine" or i == "Teller":
            magos.append(i)
        elif i == "Newton" or i == "Hawking" or i == "Einstein":
            cientificos.append(i)
        else:
            otros.append(i)


def hacer_grandiosos(magos):
    n = 0
    for i in magos:
        magos[n] = "el gran " + i
        n = n + 1


def imprimir_nombres(list):
    n = 0
    print("Listado de Nombres:")
    print()
    for i in list:
        print(list[n])
        n = n + 1
    print()
    print("#########################")
    print()
    hacer_grandiosos(magos)
    print("Los Magos son:")
    print()
    for i in magos:
        print(i)
    print()
    print("#########################")
    print()
    print("los cientificos son:")
    print()
    for i in cientificos:
        print(i)
    print()
    print("#########################")
    print()
    print("Los demas son:")
    print()
    for i in otros:
        print(i)

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
