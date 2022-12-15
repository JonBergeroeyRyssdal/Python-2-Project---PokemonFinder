#Ask for user input
#create a dynamic URL based on step 1
#fetch the data from the url in step 2
#convert json to a dictionary
#print out pokeomn data

import requests 
import json

print("Welcome to Pokedex.")

search = True

while search:



    indexNumber = input("Give a pokemon index-number or an pokemon?: ").lower()
    print("\n")

    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{indexNumber}")

    if req.status_code == 200:
    
        pokemon = req.json()

        print(f"Name: {pokemon['name'].capitalize()}")
        print(f"Index number: {pokemon['order']}")
        print(f"Height: {pokemon['height']}")
        print(f"Weight: {pokemon['weight']}")
        print(f"Type: {pokemon['types'][0]['type']['name']}")

        print("\n")

    else: 

        print("Pokemon not found.")
        print("\n")


    moreSearch = True  

    while moreSearch:
            
        searchAgain = input("Do you want to look for another Pokemon? (y/n) ").lower().capitalize()

        if searchAgain in ["N", "NO"]:
            print("Thanks for using this Pokedex.")
            moreSearch = False
            search = False

        elif searchAgain in ["Y", "Yes"]:
            moreSearch = False
            search = True
            
        else:
            moreSearch = True 