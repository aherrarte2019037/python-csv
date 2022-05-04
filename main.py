#Menu principal 
from ast import Break, While
from email.policy import default
from operator import truediv
from readchar import readkey, key  
from os import system               
import database_access 
import csv
import data_validation 
import statistics
menu=True

#ALGORITMO ARCHIVOS Y PERSISTENCIA 
#Fecha De Creación 03/05/2022
#DISEÑO
#Angel Andres Herrarte Lorenzana
#Irving Fabricio Morales Acosta
#PROPÓSITO
#El propósito de este algoritmo es leer y escribir series en un archivo csv.
#Se podrá editar los capítulos vistos y el estado de la serie
#Se mostrarán todas las series y las que tienen el estado de Finalizada
#También se podra mostrar la plataforma más utilizada por el usuario

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
  
def clean_screen():
    system("cls")

def solicitar_datos ():
    clean_screen();
    name_serie=input("¿Cuál es el nombre de la serie? ")
    estado_serie =menu_builder('¿En qué estado se encuentra la serie?',
            ['Quiero verla', 'En proceso', 'Dejé de verla'],
           '',
            return_value= True, default_options=['Finalizada',])
    clean_screen();
    duracion_serie=int(input("¿Cuántos minutos dura los capítulos de la serie? "))
    clean_screen();
    cap_vistos=int(input("¿Cuántos capítulos has visto? "))
    plataforma_serie=menu_builder('¿En qué platadorma se encuentra la serie?',
            ['Netflix', 'HBO', 'Disney Plus'],
           '',
            return_value= True, default_options=['Primevideo','Crunchyroll'])
    return [name_serie,estado_serie,duracion_serie,cap_vistos,plataforma_serie]

def accion_usuario(accion):
    if accion == 0:
        datos = solicitar_datos()
        name_serie=datos[0]
        estado_serie=datos[1]
        duracion_serie=datos[2]
        cap_vistos=datos[3]
        plataforma_serie=datos[4]
        database_access.add_series(name_serie,estado_serie,duracion_serie,cap_vistos,plataforma_serie)    
    
    elif accion == 1:
        clean_screen();
        series=database_access.get_all_series();
        series = list(map(lambda x: '{} - {}'.format(x['serie'], x['estado']) , series));
        
        if len(series) == 0:
            print('No has agregado series :(\nComienza agregando tus series favoritas!');
            return;
        
        series_index = menu_builder('Escoge una serie',
            series,
            '',
        );
        new_state = menu_builder('¿A qué estado quieres actualizar la serie?',
            ['Quiero verla', 'En proceso', 'Dejé de verla'],
           '',
            return_value= True, default_options=['Finalizada']
        );
        database_access.update_series(series_index, 'estado', new_state);
    
    elif accion == 2:
        clean_screen();
        series=database_access.get_all_series();
        series = list(map(lambda x: '{} - {} Capítulos vistos'.format(x['serie'], x['capitulos_vistos']) , series));
        series_index = menu_builder('Escoge una serie',
            series,
            '',
        );
        new_caps=int(input('¿Cuántos capítulos has visto ahora?\n'))
        database_access.update_series(series_index, 'capitulos_vistos', new_caps);
   
    elif accion == 3:
        estadistica_a_ver =  menu_builder('------ESTADÍSTICAS------',
        ['Serie con minutos más invertidos', 'Plataforma más utilizada',],
        '',
        return_value= False, default_options=['Series finalizadas','Todas las series'])
        if estadistica_a_ver == 0:
            serie_mas_vista=statistics.get_most_watched_series()
            print (serie_mas_vista)
            input('Presionar ENTER para continuar...');
        
        elif estadistica_a_ver == 1:
            plataforma_mas_utilizada=statistics.get_most_watched_platform()
            print (plataforma_mas_utilizada)
            input('Presionar ENTER para continuar...');
        
        elif estadistica_a_ver == 2:
            clean_screen();
            series_finalizadas=statistics.get_finished_series()
            
            if len(series_finalizadas) == 0:
                print('No has finalizado series :(\n');
                input('Presionar ENTER para continuar...');
                return;
            
            print('-------SERIES FINALIZADAS-------\n');
            for serie in series_finalizadas:
                nombre = serie['serie'].title();
                print(f'• {nombre}');
                print('\n');
            
            input('Presionar ENTER para continuar...');
        
        elif estadistica_a_ver == 3:
            clean_screen();
            series=database_access.get_all_series();
            if len(series) == 0:
                print('No has agregado series :(\nComienza agregando tus series favoritas!');
                return;

            
            print('-------LISTA DE SERIES-------\n');
            for serie in series:
                nombre = serie['serie'].title();
                estado = serie['estado'].capitalize();
                duracion_cap = str(serie['duracion_capitulo']) + ' Minutos';
                cap_vistos = serie['capitulos_vistos'];
                plataforma = serie['plataforma'].title();
                tiempo = str(serie['tiempo_invertido']) + ' Minutos';
                                
                print(f'{nombre}');
                print(f'Estado: {estado}');
                print(f'Duración por capítulo: {duracion_cap}');
                print(f'Capítulos vistos: {cap_vistos}');
                print(f'Plataforma: {plataforma}');
                print(f'Tiempo total: {tiempo}');
                print('\n');

            input('Presionar ENTER para continuar...');
            for x in range(250):
                print('\n');
                            
    elif accion == 4:
        print ("Hasta pronto :)")
        exit();
 
while menu==True:
    clean_screen();
    accion =  menu_builder('------MENÚ------',
                ['Agregar serie', 'Modificar estado de serie', 'Modificar capítulos vistos'],
            '',
                return_value= False, default_options=['Estadísticas','Salir'])
                
    accion_usuario(accion)
