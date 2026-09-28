import os

def conversor_coordernada(linhacoluna):
    letra = linhacoluna[0].upper()
    numero = linhacoluna[1:]

    letra = ord(letra) - ord('A')
    numero = int(numero)

    return numero -1, letra

def coordenada_valida(linhacoluna):
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if (len(linhacoluna) >= 2
        and linhacoluna.upper()[0] in letras
        and linhacoluna[1:].isdigit()
        and int(linhacoluna[1:]) in numeros):
        return True
    else:
        return False

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def coordenada_str(linha, coluna):
    return chr(coluna + ord('A')) + str(linha + 1)