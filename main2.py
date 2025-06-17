import qrcode
import qrcode.constants
from PIL import Image

def create_gradient(width, height, color1, color2):
    """Create a gradient image."""
    gradient = Image.new('RGB', (width, height))
    for y in range(height):
        r = int((color2[0] - color1[0]) * (y / height) + color1[0])
        g = int((color2[1] - color1[1]) * (y / height) + color1[1])
        b = int((color2[2] - color1[2]) * (y / height) + color1[2])
        for x in range(width):
            gradient.putpixel((x, y), (r, g, b))
    return gradient

def generate_qr_code_with_gradient(text, filename):
    # Create a QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Create a matrix of the QR code (True for black, False for white)
    qr_matrix = qr.get_matrix()
    width = len(qr_matrix)
    height = len(qr_matrix[0])

    # Create a gradient image
    gradient = create_gradient(width * 10, height * 10, (107, 213, 255), (82, 241, 255))  # Red to Blue

    # Create the QR code image
    img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')
    
    # Create a mask for the QR code
    mask = Image.new('L', img.size)
    for y in range(height):
        for x in range(width):
            if qr_matrix[x][y]:
                mask.paste(255, (x * 10, y * 10, (x + 1) * 10, (y + 1) * 10))

    # Composite the gradient and the QR code
    gradient.putalpha(mask)
    gradient.save(filename)
    print(f"QR code with gradient saved as {filename}")

# Usage
text = "https://github.com/jokka39"
filename = "qr_code_gradient.png"
generate_qr_code_with_gradient(text, filename)