import qrcode
from PIL import Image

print("Running QR script...")

# Your website URL
url = "https://praveenasekarcareer-stack.github.io/Digital-Card/"

# Create QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)

# Create image
img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')

# Load logo (use smaller image)
logo = Image.open("profile image.jpeg")

# Resize logo
qr_width, qr_height = img_qr.size
logo_size = int(qr_width * 0.15)
logo = logo.resize((logo_size, logo_size))

# Position center
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Paste WITHOUT mask (IMPORTANT)
img_qr.paste(logo, pos)

# Save as PNG
img_qr.save("final_qr.png")

print("QR code created successfully!")