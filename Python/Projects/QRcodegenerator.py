# install all the libraries needed
# create a function that collects a text and converts it to a QRcode
# save QR code as an imaga
# run the function
# reference link https://pypi.org/project/qrcode/

import qrcode
def qrcode_generator():
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    userinput = input("enter url:")
    print(userinput)
    qr.add_data(userinput)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    type(img)  # qrcode.image.pil.PilImage
    img.save("linkedinprofile2.png")

    

qrcode_generator()
