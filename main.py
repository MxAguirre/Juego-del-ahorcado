import random
import csv
import interfaz


def leer_palabra_secreta(csvfilename):
    archivo = open(csvfilename)
    lista_de_palabras = list(csv.DictReader(archivo))
    archivo.close()
    palabra_secreta = random.choice(lista_de_palabras) # Selecciono una palabra de la lista
    return palabra_secreta['palabras'] # Retorno la palabra selecciona al azar


def pedir_letra(letras_usadas):
    letra = ''
    longitud = 2
    letra_repetida = True
    alfabeto = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p'
                    , 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                # Para verificar que sea una letra del alfabeto
    en_alfabeto = False

    while letra == '' or longitud > 1 or letra_repetida == True or not en_alfabeto:
        letra = str(input('Ingrese una letra: ')).lower()
        longitud = len(letra)
        letra_repetida = letra in letras_usadas # Compruebo que no sea una letra repetida
        if letra in alfabeto: # Compruebo que este en el alfabeto
            en_alfabeto = True
    letras_usadas.append(letra) # Agrego la letra nueva a la lista de letras
    return letras_usadas # Retorno las lista de letras


def verificar_letra(letra, palabra_secreta):
    resultado = False
    if letra in palabra_secreta: # Verifico si la ultima letra que agregue esta en la palabra secreta
        resultado = True
    return resultado

def validar_palabra(letras_usadas, palabra_secreta):
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i - 1] in letras_usadas: 
            resultado = True
        else:
            resultado = False
            break
    return resultado
    
if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False
    

    # Leer la palabra secreta de un archivo csv.
    palabra_secreta = leer_palabra_secreta('palabras.csv')
    
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
    while intentos < max_cantidad_intentos and not es_ganador:
        # Pedir una nueva letra
        letra = pedir_letra(letras_usadas)[len(letras_usadas) - 1]
        
        # Verificar si la letra es parte de la palabra secreta        
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break

    if es_ganador:
        print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')