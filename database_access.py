import csv;
import data_validation;

#Nombres de las columnas
fieldnames = ['serie', 'estado', 'duracion_capitulo', 'capitulos_vistos', 'plataforma', 'tiempo_invertido'];

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
#Devuelve False si la película no se añadió (dato incorrecto)
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

#Actualizar dato de película según indíce, field puede ser 'estado' o 'capitulos_vistos'
#Devuelve True si la película se edito o False si un dato es incorrecto
def update_movie(index, field, value):
    try:
        is_valid = False;
        
        if (field == 'estado'):
            is_valid = data_validation.validate_string(value);
            
        if (field == 'capitulos_vistos'):
            value = int(value);
            is_valid = data_validation.validate_int(value);
        
        if not is_valid: return False;
        
        movies = get_movies();
        if len(movies) == 0: return True;
        
        movie = movies[index];
        movie[field] = value;
        movies[index] = movie;
        
        file = open('database.csv', 'w', newline='', encoding='utf-8');
        file_writer = csv.DictWriter(file, fieldnames=fieldnames);
        
        file_writer.writeheader();
        file_writer.writerows(movies);
        file.close();
        
        return True;
        
    except:
        return False;

#Ejemplos
#print(get_movies());
#add_movie('Mindhunter', movie_states[0], 20, 0, movie_platforms[0]);
#update_movie(1, fieldnames[1], movie_states[2]);