from email.policy import default
from operator import truediv
from readchar import readkey, key  
from os import system       


def menu_builder(header: str, options: list, footer: str, return_value = False, default_options = []):
    cursor_position = 0
    options += default_options

    while True:
        # Print Menu
        clean_screen()
        print(f"{header}\n")
        for index, option in enumerate(options):
            if index == cursor_position:
                print(f"\t>> {option}")
            else:
                print(f"\t   {option}")
        print(f"\n{footer}")

        # Modify cursor postion
        new_cursor_position = readkey()
        if new_cursor_position == key.UP:         # UP ARROW
            cursor_position -= 1
            cursor_position %= len(options)
        elif new_cursor_position == key.DOWN:     # DOWN ARROW
            cursor_position += 1
            cursor_position %= len(options)
        elif new_cursor_position == key.ENTER:   # ENTER KEY
            if return_value is True: return options[cursor_position]
            else: return cursor_position

  # Cleans terminal screen  
def clean_screen():
    system("cls")




def solicitar_datos ():
    name_serie=input ("¿Cuál es el nombre de la serie?\n")
    estado_serie =  menu_builder('¿En qué estado se encuentra la serie?',
            ['Quiero verla', 'En proceso', 'Dejé de verla'],
           '',
            return_value= True, default_options=['Finalizada',])
    duracion_serie=int(input("¿Cuántos minutos dura los capíulos de la serie?\n"))
    cap_vistos=int(input("¿Cuántos capítulos has vistos?\n"))
    plataforma_serie=menu_builder('¿En qué platadorma se encuentra la serie?',
            ['Netflix', 'HBO', 'Disney Plus'],
           '',
            return_value= True, default_options=['Primevideo','Crunchyoll'])
    return [name_serie,estado_serie,duracion_serie,cap_vistos,plataforma_serie]
    
"""""
datos = solicitar_datos()
name_serie=datos[0]
estado_serie=datos[1]
duracion_serie=datos[2]
cap_vistos=datos[3]
plataforma_serie=datos[4]
"""
#estado_serie =  menu_builder('¿En qué estado se encuentra la serie?',
#            ['Quiero verla', 'La estoy viendo', 'Dejé de verla'],
#           '',
#            return_value= True, default_options=['Finalizada',])

#print (name_serie,estado_serie,duracion_serie, cap_vistos,plataforma_serie)

lista=["a","c"]
menu_builder('¿En qué estado se encuentra la serie?',
            lista,
           '',
            return_value= True, default_options=['Finalizada',])