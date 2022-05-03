import csv;
import data_validation;

#Nombres de las columnas
fieldnames = ['serie', 'estado', 'duracion_capitulo', 'capitulos_vistos', 'plataforma', 'tiempo_invertido'];

#Variables que contienen las plataformas y los estados de una serie
series_platforms = ['Netflix', 'HBO', 'Disney Plus', 'Primevideo', 'Crunchyoll'];
series_states = ['Quiero verla', 'En proceso', 'Dejé de verla', 'Finalizada'];
   
#Obtener lista de series
def get_all_series():
    file = open('database.csv', newline='', encoding='utf-8');
    file_reader = csv.DictReader(file, fieldnames=fieldnames);
    all_series = [];
    
    for row in file_reader:
        row['tiempo_invertido'] = int(row['tiempo_invertido']);
        row['duracion_capitulo'] = int(row['duracion_capitulo']);
        row['capitulos_vistos'] = int(row['capitulos_vistos']);
        all_series.append(row);
    
    file.close();
    return all_series;

get_all_series()
#print(all_series)

#Devuelve True si la serie se añadió
#Devuelve False si la serie no se añadió (dato incorrecto)
def add_series(serie, estado, duracion_capitulo, capitulos_vistos, plataforma):
    try:
        duracion_capitulo = int(duracion_capitulo);
        capitulos_vistos = int(capitulos_vistos);
        plataforma = plataforma.upper() if plataforma.casefold() == 'hbo' else plataforma.title()
        
        string_validate = [serie, estado, plataforma];
        int_validate = [duracion_capitulo, capitulos_vistos];
        
        for string in string_validate:
            is_valid = data_validation.validate_string(string);
            if not is_valid: break;
        
        if not is_valid:
            return False;
        
        for integer in int_validate:
            is_valid = data_validation.validate_int(integer);
            if not is_valid: break;
        
        if not is_valid:
            return False;
        
        file = open('database.csv', 'a', newline='', encoding='utf-8');
        file_writer = csv.DictWriter(file, fieldnames=fieldnames);
        file_writer.writerow({
            'serie': serie.title(),
            'estado': estado.capitalize(),
            'duracion_capitulo': duracion_capitulo,
            'capitulos_vistos': capitulos_vistos,
            'plataforma': plataforma.title(),
            'tiempo_invertido': capitulos_vistos * duracion_capitulo,
        });
        file.close();

        return True;
        
    except:
        return False;

#Actualizar dato de serie según indíce, field puede ser 'estado' o 'capitulos_vistos'
#Devuelve True si la serie se edito o False si un dato es incorrecto
def update_series(index, field, value):
    try:
        is_valid = False;
        
        if (field == 'estado'):
            is_valid = data_validation.validate_string(value);
            
        if (field == 'capitulos_vistos'):
            value = int(value);
            is_valid = data_validation.validate_int(value);
        
        if not is_valid: return False;
        
        all_series = get_all_series();
        if len(all_series) == 0: return True;
        
        series = all_series[index];
        series[field] = value;
        series['tiempo_invertido'] = series['capitulos_vistos'] * series['duracion_capitulo'];
        
        all_series[index] = series;
        
        file = open('database.csv', 'w', newline='', encoding='utf-8');
        file_writer = csv.DictWriter(file, fieldnames=fieldnames);
        
        file_writer.writeheader();
        file_writer.writerows(all_series);
        file.close();
        
        return True;
        
    except:
        return False;
#Ejemplos
#print(get_all_series());
#add_series('Mindhunter', series_states[0], 20, 0, series_platforms[0]);
#update_series(0, fieldnames[3], 1);