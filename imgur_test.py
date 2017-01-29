import pyimgur

client_id = '11e147eb82b23bf'
client_secret = 'd5daa5da37cf34d663ea79cf0c385bb6cf2c56f7'

path = "session_2/0.png"

im = pyimgur.Imgur(client_id)

uploaded_image = im.upload_image(path, title='test_1')

print(uploaded_image.title)
print(uploaded_image.link)
print(uploaded_image.size)
print(uploaded_image.type)

