import qrcode

# Give your data
data = "https://instagram.com"

# output file name
filename = "insta.png"

# genrate Qr code
img = qrcode.make(data)

# save image to a file
img.save(filename)
