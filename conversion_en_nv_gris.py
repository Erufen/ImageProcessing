from PIL import Image

from _utils import compare

im = Image.open("chemin de l'image")

# isolation des couches de couleur de l'image
im1 = im.split()[0] # couche rouge
im2 = im.split()[1] # couche verte
im3 = im.split()[2] # couche bleu
im4 = im.convert("L") # conversion RGBA -> niveaux de gris

compare(im1, im2, im3, im4)
