import requests
import sys


def fetch_characters(movie_id):
    #Base URL for SWAPI films endpoint
    url = f"https://swapi-api.alx_tools.com/api/films/{movie_id}/"
    
    try:
        #fetch movie data
        response = requests.get(url)
        response.raise_for_status() # raises an error if the request failed
        
        # Parse JSON response
        data = response.json()
        
        #extract movie title and character list
        movie_title = data.get("title", "Unknown movie")
        characters = data.get("characters", [])
        
        #print movie title
        print(f"Characters in '{movie_title}':")
        
        #fetch each character's name in the same order
        for character_url in characters:
            char_response = requests.get(character_url)
            char_data = char_response.json()
            char_name = char_data.get("name", "Unknown Character")
            print(char_name)
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <Movie ID>")
    else:
        movie_id = sys.argv[1]
        fetch_characters(movie_id)
            