import os, time

print("Temporizador\n\n")

segundos = 0
minutos = 0

while True:
    os.system("cls")
    segundos = segundos + 1
    if segundos == 60:
        minutos = minutos + 1
        segundos = 0

    if segundos == 1 and minutos != 1:
        print((str(minutos) + " minutos || " + str(segundos) + " segundo"))
    elif minutos == 1 and segundos != 1:
        print((str(minutos) + " minuto || " + str(segundos) + " segundos"))
    elif minutos == 1 and segundos == 1:
        print((str(minutos) + " minuto || " + str(segundos) + " segundo"))
    else:
        print((str(minutos) + " minutos || " + str(segundos) + " segundos"))

    time.sleep(1)