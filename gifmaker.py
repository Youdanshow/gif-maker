import sys
from PIL import Image

# Liste pour stocker les images
images = []

# Boucle pour ouvrir les images passées en arguments
for arg in sys.argv[2:]:
    image = Image.open(arg)
    images.append(image)

if images:
    # extension .gif
    images[0].save( sys.argv[1], save_all=True, append_images=images[1:], duration=500, loop=0)
else:
    print("Aucune image fournie.")
