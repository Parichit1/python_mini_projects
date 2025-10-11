import qrcode

data = input("Please enter the url for the QR code you want: ").strip()
filename = input(
    "Please enter the name you want the QR code to be saved as: ").strip() + ".png"

qr = qrcode.QRCode(border=5, box_size=10)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR cod has been saved as {filename} .")
