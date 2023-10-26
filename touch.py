#Botones touch para el robo_control
from machine import TouchPad, Pin
from time import sleep_ms

b_frente=TouchPad(Pin(32))
b_reversa=TouchPad(Pin(14))
b_derecha=TouchPad(Pin(27))
b_izquierda=TouchPad(Pin(33))
b_bocina=TouchPad(Pin(4))

while True:
    #touch=t.read()
    valores=[
        b_frente.read(),
        b_reversa.read(),
        b_derecha.read(),
        b_izquierda.read(),
        b_bocina.read(),
        ]
    nombres=[
        'frente',
        'reversa',
        'derecha',
        'izquierda',
        'bocina',
        ]
    for i,w in enumerate(valores):
        if w<100:
            print(nombres[i])
    sleep_ms(100)
