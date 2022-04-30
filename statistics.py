import database_access;

def get_most_watched_series():
    all_series = database_access.get_all_series();
    most_watched_series = max(all_series, key=lambda item:item['tiempo_invertido']);
    return most_watched_series;

def get_most_watched_platform():
    all_series = database_access.get_all_series();
    platforms_count = {};
    
    for series in all_series:
        key = series['plataforma'];
        platforms_count[key] = platforms_count.get(key, 0) + 1;
    
    most_watched_platform = max(platforms_count, key=platforms_count.get);
    most_watched_platform = {
        'plataforma': most_watched_platform,
        'cantidad_series': platforms_count[most_watched_platform],
    };

    return most_watched_platform;

def get_finished_series():
    all_series = database_access.get_all_series();
    finished = list(filter(lambda item: item['estado'] == 'Finalizada', all_series));

    return finished;