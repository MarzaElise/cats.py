# 1. instantiate client

from cats import Client

client = Client("YOUR_API_KEY_HERE")

images = client.get_all_images() # see the docstrings for more info on this
# images is a list of Image objects

first_image = images[0]
# now this is one cats.Image object

print(first_image.url) # URL of the image

filtered = client.search_image(breed_ids=BREED_ID) # id of the breed you want to receive

print(filtered[0]) # first image of all images that matched the filter
