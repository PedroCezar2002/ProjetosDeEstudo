import time
class Temporizador:
    print(f'Temporizador')
    
    #Informações de tempo que serão dadas pelo usuário e que depois serão convertidas para numeros inteiros
    horasString = input(f'Digite as horas: ')                   
    horasInt = int(horasString)
    minutosString = input(f'Digite os minutos: ')
    minutosInt = int(minutosString)
    segundosString = input(f'Digite os segundos: ')
    segundosInt = int(segundosString)
    
    #Metodo que converte o tempo total em segundos e envia o resultado para uma variável
    tempoTotalEmSegundos = ((horasInt*60*60) + (minutosInt*60) + segundosInt)

    #Laço que mostrará ao usuário o tempo restante e o mesmo irá diminuir o tempo em 1 a cada segundo
    while (tempoTotalEmSegundos>0):
        print("Tempo restante: {}".format(tempoTotalEmSegundos))
        tempoTotalEmSegundos -= 1
        time.sleep(1)
    
    #Mensagem que indicará ao usuário que o tempo se esgotou assim que o processo finalizar
    print(f"Fim do Temporizador")