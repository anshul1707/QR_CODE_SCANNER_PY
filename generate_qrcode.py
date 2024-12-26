import qrcode # to genrate qr code
# for decoding qr
from pyzbar.pyzbar import decode 
from PIL import Image
# genrating qr
myqr = qrcode.make("") # insert link jisko qr me convert krna hai "inside this"
myqr.save("qr code.png" , scale = 8)

#decoding qr
b = decode(Image.open("qr code.png"))
#printing decoded qrs data 
print("you will redirect to this link : ") 
print(b[0]. data.decode("ascii"))
