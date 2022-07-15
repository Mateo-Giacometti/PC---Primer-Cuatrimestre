def match_duration(hours, minutes, seconds):
    """
    Calcular la duracion del partido en segundos.
    
    Parameters
    ----------
    hours : int
        Almacena el valor de la horas del partido.
    minutes : int
        Almacena el valor de los minutos del partido.
    seconds : int
        Almacena el valor de los segundos del partido.
    -------
    duracion : int
        Pasa el valor de las horas y los minutos a segundos. Suma
        los parametros anteriormente descriptos.

    """
    duracion = (hours * 3600) + (minutes * 60) + seconds
    print('El partido duro', duracion, 'segundos')
match_duration(11, 6, 23)