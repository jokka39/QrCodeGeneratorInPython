import qrcode
import qrcode.constants

def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(text)  # Add data (the URL or text you want to encode)
    qr.make(fit=True)  # Optimize the size of the QR code
    img = qr.make_image(fill_color="black", back_color="white")  # Generate image
    img.save(file_name)  # Save the image

text = "https://img-webcalypt.ru/storage/memes/27976/202412/y6BvfEsSx3SH0AJeS5xMjYuePcc3BI4pzXsYiIVJa4SVtDAWKpq86WkJWjY2hnwswR24SnK43gCjPaFXHn2n1LuXj1KjytepUe56PS6Axfx9z83O2eFlZtOMaAj0B2ch.jpeg"
file_name = "qr_code.png"

generate_qr_code(text, file_name)
print(f"QR code saved as {file_name}")