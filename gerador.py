import qrcode

for i in range(0, 5):
    qr = input('link para ser convertido: ')
    qrc = qrcode.QRCode(
        version=None,
        error_correction=qrcode.ERROR_CORRECT_H,
    )
    qrc.add_data(qr)
    img = qrc.make_image(fill_color='#3B8435',
                         back_color='#FFFFFF')
    type(img)
    img.save(f'{i}.png')
