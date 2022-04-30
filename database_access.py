import csv;
import data_validation;

def get_file_writer():
    with open('database,csv', 'w', newline='') as file:
        fieldnames = ['serie', 'estado', 'duracion_capitulo', 'capitulos_vistos', 'plataforma', 'tiempo_invertido'];
        writer = csv.DictWriter(file, fieldnames=fieldnames);
    
    return writer;        
    
def get_file_reader():
    with open('database,csv', newline='') as file:
        reader = csv.DictReader(file);
    
    return reader;


def add_movie(serie, estado, duracion_capitulo, capitulos_vistos, plataforma):
    try:
        duracion_capitulo = int(duracion_capitulo);
        capitulos_vistos = int(capitulos_vistos);
        string_validate = [serie, estado, plataforma];
        int_validate = [duracion_capitulo, capitulos_vistos];
        
        for string in string_validate:
            is_valid = data_validation.validate_string(string);
            if not is_valid: break;
        
        if not is_valid:
            print('Datos incorrectos, intenta otra vez');
            return;
        
        for integer in int_validate:
            is_valid = data_validation.validate_int(integer);
            if not is_valid: break;
        
        if not is_valid:
            print('Datos incorrectos, intenta otra vez');
            return;
    except:
        print('Datos incorrectos, intenta otra vez');
        return;
        
    file_writer = get_file_writer();