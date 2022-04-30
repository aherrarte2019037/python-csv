import csv;
import data_validation;

#Variables que contienen las plataformas y los estados de una película
movie_platforms = ['Netflix', 'HBO', 'Disney Plus', 'Primevideo', 'Crunchyoll'];
movie_states = ['Quiero verla', 'En proceso', 'Dejé de verla', 'Finalizada'];
   
#Obtener lista de películas
def get_movies():
    file = open('database.csv', newline='', encoding='utf-8');
    file_reader = csv.DictReader(file);
    movies = [];
    
    for row in file_reader: movies.append(row);
    
    file.close();
    return movies;

#Devuelve True si la película se añadió
#Devuelve False si la película no se añadió
def add_movie(serie, estado, duracion_capitulo, capitulos_vistos, plataforma):
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
        fieldnames = ['serie', 'estado', 'duracion_capitulo', 'capitulos_vistos', 'plataforma', 'tiempo_invertido'];
        file_writer = csv.DictWriter(file, fieldnames=fieldnames);
        file_writer.writerow({
            'serie': serie.title(),
            'estado': estado.capitalize(),
            'duracion_capitulo': duracion_capitulo,
            'capitulos_vistos': capitulos_vistos,
            'plataforma': plataforma.title(),
            'tiempo_invertido': 0,
        });
        file.close();

        return True;
        
    except:
        return False;