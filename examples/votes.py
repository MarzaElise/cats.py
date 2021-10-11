from cats import Client

client = Client(api_key="API KEY HERE")
# 1 = upvote 0 = downvote
res = client.vote_image(image_id="id of the image", sub_id="sub id here", value=1)
# you can use id NwMUoJYmT for testing
print(res)
# above prints something like
# Response(id=333931, message='SUCCESS', level=None, status=None)

response = client.delete_vote(vote_id="vote id")
# vote id is received by Client.vote_image
print(res)
