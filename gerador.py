import qrcode

cont = int(input('quantos qrcodes serão gerados: '))
cor = input('digite a cor que deseja para o preenchimento: ')
pCor = "'"+cor+"'"
for i in range(0, cont):
    qr = input('link para ser convertido: ')
    qrc = qrcode.QRCode(
        version=None,
        error_correction=qrcode.ERROR_CORRECT_H
    )
    qrc.add_data(qr)
    img = qrc.make_image(fill_color=cor,
                         back_color='#FFFFFF')
    type(img)
    img.save(f'{i}.png')
