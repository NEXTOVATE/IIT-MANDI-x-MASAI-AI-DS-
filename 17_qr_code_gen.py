import qrcode

url = input("Enter the url")

img = qrcode.make(url)

img.save("qrcode.png")
print("qrcode created successfully")
