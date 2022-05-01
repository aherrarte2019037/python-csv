def solicitar_datos ():
    name_serie=input ("¿Cuál es el nombre de la serie\n")
    cap_vistos=int(input("¿Cuántos capítulos has vistos?\n"))
    return [name_serie,cap_vistos]


datos = solicitar_datos()
name_serie=datos[0]
cap_vistos=datos[1]
print (name_serie)

accion =  menu_builder('¿En qué estado se encuentra la serie?',
            ['Quiero verla', 'La estoy viendo', 'Dejé de verla'],
           '',
            return_value= False, default_options=['Finalizada',])