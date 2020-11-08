from PIL import Image
# permet de réaliser un effet sépia
from PIL import ImageOps
# pour modifier le contraste
from PIL import ImageEnhance

# convertion en 'noir et blanc' obligatoire pour travailler avec ImageOps.colorize
im = Image.open("chemin de l'image").convert("L")

# (132, 84, 129) : violet (240, 176, 113) : orange
im = ImageOps.colorize(im, (132, 84, 129), (240, 176, 113))
# augmente le contraste
im = ImageEnhance.Contrast(im).enhance(3)
# désaturation de la couleur
im = ImageEnhance.Color(im).enhance(0.5)

im.show()
