# nothing really changes for async except for the namespace

# usually, you would import Client from cats like this
from cats import Client

# for async support, import it from async_cats
from async_cats import Client

# now you can instantiate the class
client = Client("YOUR_API_KEY_HERE")

# now you should await all the methods in the client


async def coroutine():
    all_breeds = await client.get_breeds()
    # returns all the breeds available as a list of async_cats.Breed objects

    print(all_breeds[0].wikipedia_url)
    # prints the wikipedia URL of the first breed in the list

    beng = await client.search_breed("beng")  # short for bengal
    print(beng.wikipedia_url)
    # prints the wikipedia_url of the breed


# now we use asyncio to run the coroutine
import asyncio

asyncio.run(coroutine())
