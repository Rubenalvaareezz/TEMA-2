from datetime import date
def calcula_edad(fecha):
    fecha_actual = date.today()
    cumple_este_año = date(fecha_actual.year, fecha.month, fecha.day)
    edad = fecha_actual.year - fecha.year
    if fecha_actual < cumple_este_año:
        edad -= 1 #edad = edad - 1

    #Ahora falta calcular los dias oara el próximo cumpleaños
    #¿Cual es la fecha del próximo cumpleaños?

    proximo_cumpleaños = cumple_este_año
    if cumple_este_año < fecha_actual:
        proximo_cumpleaños = date(fecha_actual.year + 1 , fecha.month, fecha.day)
        dias_proximo_cumpleaños = (proximo_cumpleaños-fecha_actual).days
    return edad, dias_proximo_cumpleaños

if __name__ == "__main__":
    dia = int(input("Dime tu fecha de nacimiento:"))
    mes = int(input("Dime tu fecha de nacimiento:"))
    año = int(input("Dime tu fecha de nacimiento:"))
    fecha=date(año,mes,dia)
    edad, dias = calcula_edad(fecha)
    print(f"Tienes {edad} años y faltan {dias} días para tu próximo cumpleaños.")
    
    