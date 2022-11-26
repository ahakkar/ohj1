# -*- encoding: utf-8 -*-
'''
@File    :   9-5.py
@Time    :   24/10/2022, 18:07:34
@Author  :   Antti Hakkarainen
@Student :   K79735
@Contact :   antti.i.hakkarainen@tuni.fi
@Course  :   COMP.CS.100 Ohjelmointi 1.
@Desc    :   TEMP
'''
def add_data_to_dict(data) -> dict:
    """
    param : TODO
    return: none
    """
    
    movies:dict = {}
    movies["genres"] = set()
    
    for row in data:
        row:str = row.strip()
        items:list = row.split(";")
        
        name:str = items[0]
        current_genres:list = items[1].split(',')        
        
        # add movie & its genres
        if name not in movies:
            movies[name] = set(current_genres)          
                
        # add genres
        for genre in current_genres:
            movies["genres"].add(genre)        
        
    return movies

def list_movie_info(movies: dict, user_input: str):
    """
    param : TODO
    return: none
    """
    found: list = []

    for movie, genres in movies.items():
        if user_input in genres:
            if movie != "genres": found.append(movie)
    
    found = sorted(found)
    if len(found) > 0:
        for val in found:
            print(val)
    
def menu(movies:dict) -> None:
    """
    param : TODO
    return: none
    """
    
    # prints all available genres
    genres:str = ""
    for val in sorted(movies["genres"]):
        genres += f"{val}, "
    print(f"Available genres are: {genres[0:-2]}")
    
    while True:
        user_input = input("> ")
        if user_input == "exit":
            return
        list_movie_info(movies, user_input)

def main():
    # read txt file to list
    filename = input("Enter the name of the file: ")
    try:
        with open (filename, "r") as read_file:
            data:list = read_file.readlines()  
        read_file.close()
    except OSError:
        print("bad file name!")
        return
    
    # process read data from list to dict
    movies = add_data_to_dict(data)
    menu(movies)       
        
if __name__ == "__main__":
    main()