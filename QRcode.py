import qrcode
from PIL import Image

Logo_link = "C:\\Users\\Mohan\\Downloads\\vnr.png"
logo = Image.open(Logo_link)
 
# taking base width
basewidth = 100
 
# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
 
# taking url or text
url=input('Enter the text or paste the link to convert it into a QR Code : \n')

# adding URL or text to QRcode
QRcode.add_data(url)
 
# generating QR code
QRcode.make()
 
# taking color name from user
QRcolor = 'Brown'
 
# adding color to QR code
QRimg = QRcode.make_image(fill_color=QRcolor, back_color="white").convert('RGB')
 
# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)
 
# save the QR code generated
QRimg.save("QR.png")
 
img = Image.open(r"QR.png") 
img.show() 

