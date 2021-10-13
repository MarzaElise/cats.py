from cats import Client

client = Client(api_key="API KEY HERE")

all_breeds = client.get_breeds()
# returns all the breeds available as a list of cats.Breed objects

print(all_breeds[0].wikipedia_url)
# prints the wikipedia URL of the first breed in the list

beng = client.search_breed("beng")  # short for bengal
# beng is an instance of cat.Breed
print(beng.wikipedia_url)
