from cats import Client

client = Client(api_key="API KEY HERE")

images = client.search_image(breed_ids="beng") # list of cats.Image objects
image = images[0] # an instance of cats.Image
print(image.url)
# prints a random URL

breed = client.search_breed("sib") # short for siberien
print(breed.id) # breed is an instance of cats.Breed
# above prints "sibe"
