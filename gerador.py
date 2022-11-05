import qrcode

cont = int(input('quantidade de qrcode: '))
cor = input('cor do preenchimento: ')
corB = input('cor do fundo: ')
for i in range(cont):
    qr = input('link para ser convertido: ')
    qrc = qrcode.QRCode(
        None,
        qrcode.ERROR_CORRECT_H,
        border=2.5
    )
    qrc.add_data(qr)
    img = qrc.make_image(fill_color=cor,
                         back_color=corB)
    type(img)
    img.save(f'qrcodes/{i}.png')
