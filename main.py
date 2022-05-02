#Menu principal 
from email.policy import default
from operator import truediv
from readchar import readkey, key  
from os import system               
import database_access 
import csv
import data_validation 
import statistics


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
    name_serie=input ("¿Cuál es el nombre de la serie? ")
    estado_serie =  menu_builder('¿En qué estado se encuentra la serie?',
            ['Quiero verla', 'En proceso', 'Dejé de verla'],
           '',
            return_value= True, default_options=['Finalizada',])
    duracion_serie=int(input("¿Cuántos minutos dura los capíulos de la serie? "))
    cap_vistos=int(input("\n¿Cuántos capítulos has visto? "))
    plataforma_serie=menu_builder('¿En qué platadorma se encuentra la serie?',
            ['Netflix', 'HBO', 'Disney Plus'],
           '',
            return_value= True, default_options=['Primevideo','Crunchyoll'])
    return [name_serie,estado_serie,duracion_serie,cap_vistos,plataforma_serie]

def accion_usuario(accion,):
    if accion == 0:
        database_access.add_series(name_serie,estado_serie,duracion_serie,cap_vistos,plataforma_serie)    
    
    elif accion == 1:
        database_access.get_all_series()
    
    elif accion == 2:
        print ("cap vistos")
    
    elif accion == 3:
        estadistica_a_ver =  menu_builder('¿Qué desea ver?',
        ['Serie con minutos más invertidos', 'Platadorma más utilizada',],
        '',
        return_value= False, default_options=['Series finalizas','Todas las series'])
        if estadistica_a_ver == 0:
            serie_mas_vista=statistics.get_most_watched_series()
            print (serie_mas_vista)
        elif estadistica_a_ver == 1:
            plataforma_mas_utilizada=statistics.get_most_watched_platform()
            print (plataforma_mas_utilizada)
        elif estadistica_a_ver == 2:
            series_finalizadas=statistics.get_finished_series()
            print (series_finalizadas)
        elif estadistica_a_ver == 3:
            #AQUÍ HACES LOS TUYO, ÁNGEL
    
    elif accion == 4:
            print ("Salió")
  
accion =  menu_builder('¿Qué deseas hacer?',
            ['Agregar serie', 'Modificar estado de serie', 'Modificar capítulos vistos'],
           '',
            return_value= False, default_options=['Estadísticas','Salir'])

if accion == 0:
    datos = solicitar_datos()
    name_serie=datos[0]
    estado_serie=datos[1]
    duracion_serie=datos[2]
    cap_vistos=datos[3]
    plataforma_serie=datos[4]
                
accion_usuario(accion)