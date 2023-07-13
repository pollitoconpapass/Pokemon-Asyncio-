import asyncio
from random import randint
from typing import AsyncIterable
from req_http import http_get

# The highest Pokemon id
MAX_POKEMON = 898


async def get_random_pokemon_name() -> str: 
    pokemon_id = randint(1, MAX_POKEMON) #-> id generator
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}" #-> it will search the id of that pokemon
    pokemon = await http_get(pokemon_url) #-> waits until it finds it
    return str(pokemon["name"]) #-> return the pokemon name on a string


async def next_pokemon(total: int) -> AsyncIterable[str]:
    for _ in range(total):
        name = await get_random_pokemon_name() #-> it will operate depending on how much pok we want...
        yield name #-> returns each name asynchronously


async def main():
    # retrieve the next 20 pokemon names
    async for name in next_pokemon(20): 
        print(name)

    # asynchronous list comprehensions
    names = [name async for name in next_pokemon(20)]
    print(names)


asyncio.run(main())
