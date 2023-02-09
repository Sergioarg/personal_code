# import modules
import qrcode
from PIL import Image

# taking image which user wants
# in the QR code center
Logo_link = 'https://media-exp1.licdn.com/dms/image/C510BAQGMs8pjfGLUTA/company-logo_200_200/0/1530903491297?e=2147483647&v=beta&t=rF56SW5wzjNsHUqv9SBLG2JxgwRupDAbjdQVb8juyh0'

logo = Image.open(Logo_link)

# taking base width
basewidth = 200

# adjust image size
wpercent = (basewidth / float(logo.size[0]))

hsize = int((float(logo.size[1]) * float(wpercent)))

logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# taking url or text
url = 'https://media1.giphy.com/media/qyjexFwQwJp9yUvMxq/giphy.gif?cid=ecf05e471isjac4w96cs4acjnevq22vd4a8qsu5amc13jmr4&rid=giphy.gif&ct=g'

# adding URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

# taking color name from user

# adding color to QR code
QRimg = QRcode.make_image(fill_color='black', back_color="white").convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)

QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save('xyzies.png')

print('QR code generated!')
