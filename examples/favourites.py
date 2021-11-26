# 1. instantiate the Client class

from cats import Client

client = Client("YOUR_API_KEY_HERE")

image_id = ... # image id you want to save as favourite
sub_id = ... # something unique

response = client.save_favourite(image_id, sub_id)
__id = response.id # a unique id to identify this specific favourtie

fav = client.get_favourite(favourite_id=__id) # a cats.Favourite object

image = fav.image # a cats.FavourtieImage object containing data about the image

print(image.url)

res = client.delete_favourite(favourite_id=__id) # to delete a favourtie that belongs to your account

print(res.message) # message returned by the API
