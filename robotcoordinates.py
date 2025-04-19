def image_to_robot_coordinates(image_x, image_y, image_width, image_height, robot_workspace):
    """
    Convert image coordinates to robot coordinates
    Przekształcić koordynaty zdjęcia na koordynaty robota
    
    Args:
        image_x, image_y: Środek obrazu obliczony w main.py
        image_width, image_height: Roździelczość obrazu, aby określać mniej więcej pozycje
        robot_workspace: TCP robota (jego granice) (x_min, x_max, y_min, y_max, z_min, z_max)
    
    Returns:
        x, y odczytywalne dla cobota.
    """
    # Zaokrąglić odleglość na zdjęciu
    norm_x = image_x / image_width
    norm_y = image_y / image_height

    # Dostosować do limitów robota
    robot_x = robot_workspace['x_min'] + norm_x * (robot_workspace['x_max'] - robot_workspace['x_min'])
    
    # Zmiana Y dla robota (Zazwyczaj Y w ramionach robota są liczone od dołu do góry, gdzie pixele są liczone odwrotnie)
    robot_y = robot_workspace['y_max'] - norm_y * (robot_workspace['y_max'] - robot_workspace['y_min'])
    
    return robot_x, robot_y
