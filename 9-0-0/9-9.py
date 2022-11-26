# -*- encoding: utf-8 -*-
'''
@File    :   9-9.py
@Time    :   06/11/2022, 12:20:47
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''

CITY_PRINT_WIDTH:int = 14
DIST_PRINT_WIDTH:int = 5

def print_destinations(distances:dict, city:str) -> None:
    """
    Print destinations of a city

    :param dict distances:
    :param str city:
    """
    
    for dest in sorted(distances[city]):                     
        print(f'{city: <{CITY_PRINT_WIDTH}}' + 
              f'{dest: <{CITY_PRINT_WIDTH}}' + 
              f'{distances[city][dest]: >{DIST_PRINT_WIDTH}}')

def read_distance_file(filename:str) -> list:
    """
    Reads rows from file to list
    
    param : str, filename from user
    return: list, rows from read file (or empty list if none was read)
    """
    
    try:
        with open (filename, "r", encoding="utf-8") as read_file:
            rows:list = read_file.readlines()  
        read_file.close()
    except OSError:
        print(f"Error: '{filename}' can not be read.")
        return []
    
    return rows

def add_rows_to_dict(rows:list) -> dict:
    """
    Adds read rows to dict
    
    param : list, of rows read from file
    return: dict, distances[city:str][destination:str] = distance:int
    """
    
    distances:dict = {}

    for row in rows:               
        split_row = row.strip().split(";")
        if len(split_row) != 3:
             print("Error: Too many or too few entries in a row:")
             print(row)
             return {}
         
        city:str = split_row[0]
        dest:str = split_row[1]
        dist:int = int(split_row[2])
        
        if len(city) == 0 or len(dest) == 0:
            print("Error: Bad data in file.")
            return {}

        if city not in distances:
            distances[city] = {dest: dist}
        else:           
            distances[city].update({dest: dist})            
        
    return distances

def add_key_value_pair(distances:dict) -> None:
    """
    Adds connection to dict
    
    param : dict, of connections
    return: none
    """
    
    city:str = input("Enter departure city: ")
    dest:str = input("Enter destination city: ")
    try:
        temp:str = (input("Distance: "))
        dist:int = int(temp)
    except ValueError:
        print(f"Error: '{temp}' is not an integer.")
        return
    
    if city not in distances:
        distances[city] = {dest: dist}    
    else:           
        distances[city].update({dest: dist})   
        
    if dest not in distances:
        distances[dest] = {}
        
def remove_key_value_pair(distances:dict) -> None:
    """
    Removes connection from dict
    
    param : dict, of connections
    return: none
    """
    
    city:str = input("Enter departure city: ")
    if city not in distances:         
        print(f"Error: '{city}' is unknown.") 
        return
    
    dest:str = input("Enter destination city: ")
    if dest in distances[city]:
            distances[city].pop(dest)
    else:
        print(f"Error: missing road segment between '{city}' and '{dest}'.")
        
def print_neighbours(distances:dict) -> None:
    """
    Lists neighbours of a city
    
    param : dict, of connections
    return: none
    """
    
    city:str = input("Enter departure city: ")
    if city not in distances:         
        print(f"Error: '{city}' is unknown.") 
        return
             
    print_destinations(distances, city)
        
def fetch_neighbours(distances:dict, city:str) -> list:
    """
    Returns a list of all the cities that are directly connected to city.
    
    :param data: dict, distance information between the known cities.
    :param city: str, the name of the city whose neighbours we
           are interested in.
    :return: list[str], the neighbouring city names in a list.
    """
    
    neighbours:list = []
    
    if city in distances:
        for dest in distances[city]:
            neighbours.append(dest)
    
    return neighbours

def distance_to_neighbour(distances:dict, city:str, dest:str):
    """
    Returns the distance between two neighbouring cities.    
    
    :param data: dict, distance information between the known cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: int | None, The distance between <departure> and
           <destination>. None if there is no direct connection
           between the two cities.
    """
        
    if city in distances:
        if dest in distances[city]:
            return distances[city][dest]
    
    return None
        
def print_route(distances:dict) -> None:
    """
    Prints route from city to dest
    
    param : dict, of connections
    return: none
    """
    
    city:str = input("Enter departure city: ")
    if city not in distances:
        print(f"Error: '{city}' is unknown.")
        return
    dest:str = input("Enter destination city: ")    
   
    # uses premade algo to find route 
    route = find_route(distances, city, dest)
    
    # no route
    if len(route) == 0:           
        print(f"No route found between '{city}' and '{dest}'.")
    # 2 cities long route
    elif len(route) == 2:
        # same city and dest?
        if route[0] == route[1]:
            print(f"{route[0]}-{route[1]} (0 km)")
        # different cities
        else:
            print(f"{route[0]}-{route[1]} ({distances[route[0]][route[1]]} km)")
    # otherwise prints a long route
    else:
        route_str:str = ""
        route_len:int = 0
        route_stops:int = len(route)
        i:int = 0
        
        while i < route_stops:
            if i < route_stops-1:             
                route_len += distances[route[i]][route[i+1]]
            route_str += f"{route[i]}-"
            i += 1
        
        print(route_str.rstrip('-') + f" ({str(route_len)} km)")             

def menu(distances:dict) -> None:
    """
    Displays a python 3.6 compatible menu for user
    
    param : dict, of connections
    return: none
    """
    
    while True:
        cmd = input("Enter action> ")
        
        if cmd == "display":
            for city in sorted(distances):
                print_destinations(distances, city)  
        elif cmd == "add":
            add_key_value_pair(distances)
        elif cmd == "remove":
            remove_key_value_pair(distances)
        elif cmd == "neighbours":
            print_neighbours(distances)
        elif cmd == "route":
            print_route(distances)
        elif cmd == "":
            print("Done and done!")
            return None
        else:
            print(f"Error: unknown action '{cmd}'.")   
        """
        rip no python 3.10 :'(
        match cmd:
            case "display":
                display(distances)
            case "add":
                add_key_value_pair(distances)
            case "remove":
                remove_key_value_pair(distances)
            case "neighbours":
                list_neighbours(distances)
            case "route":
                get_route(distances)
            case "":
                print("Done and done!")
                return None
            case _:
                print(f"Error: unknown action '{cmd}'.")   
        """
        
def find_route(data, departure, destination):
    """
    This function tries to find a route between <departure>
    and <destination> cities. It assumes the existence of
    the two functions fetch_neighbours and distance_to_neighbour
    (see the assignment and the function templates below).
    They are used to get the relevant information from the data
    structure <data> for find_route to be able to do the search.

    The return value is a list of cities one must travel through
    to get from <departure> to <destination>. If for any
    reason the route does not exist, the return value is
    an empty list [].

    :param: dict, of connections
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: list[str], a list of cities the route travels through, or
           an empty list if the route can not be found. If the departure
           and the destination cities are the same, the function returns
           a two element list where the departure city is stores twice.
    """

    if departure not in data:
        return []

    elif departure == destination:
        return [departure, destination]

    greens = {departure}
    deltas = {departure: 0}
    came_from = {departure: None}

    while True:
        if destination in greens:
            break

        red_neighbours = []
        for city in greens:
            for neighbour in fetch_neighbours(data, city):
                if neighbour not in greens:
                    delta = deltas[city] + distance_to_neighbour(data, city, neighbour)
                    red_neighbours.append((city, neighbour, delta))

        if not red_neighbours:
            return []

        current_city, next_city, delta = min(red_neighbours, key=lambda x: x[2])

        greens.add(next_city)
        deltas[next_city] = delta
        came_from[next_city] = current_city

    route = []
    while True:
        route.append(destination)
        if destination == departure:
            break
        destination = came_from.get(destination)

    return list(reversed(route))

def main():
    filename = input("Enter input file name: ")
    rows = read_distance_file(filename)
    
    # exit prog if nothing was read
    if len(rows) == 0:
        return 0  
    
    # exit prog if data was invalid
    dist = add_rows_to_dict(rows)
    if len(dist) == 0:
        return 0
    
    menu(dist)
    
    """
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(dist)
    """

if __name__ == "__main__":
    main()
