from PIL import Image
from glob import glob
import os

# on récupère toutes les images
images = glob("*.jpg")

# facteur de réduction de l'image
facteurs = [2, 3, 5, 10]

# boucle sur les images
for image in images:
    im = Image.open(image)

    # boucle sur la liste des facteurs
    for facteur in facteurs:
        x, y = im.size
        x_facteur, y_facteur = round(x/facteur), round(y/facteur)
        im_resize = im.resize((x_facteur, y_facteur))
        filname, ext = os.path.splitext(image)
        new_filname = f"vignettes/{filname}-{x_facteur}x{y_facteur}_{ext}" # vignettes = nom du dossier dans lequel on place nos images
        im_resize.save(new_filname)
