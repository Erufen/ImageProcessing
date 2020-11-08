from PIL import Image

def compare(*args):
    largeur, hauteur = zip(*(i.size for i in args))

    largeur_totale = sum(largeur)
    hauteur_maximale = max(hauteur)

    image_composite = Image.new("RGB", (largeur_totale, hauteur_maximale)) 

    offset_x = 0
    for im in args:
        image_composite.paste(im, (offset_x, 0))
        offset_x += im.size[0]

    image_composite.show()

im1 = Image.open("chemin de l'image")
im2 = Image.open("chemin de l'image")
im3 = Image.open("chemin de l'image")
im4 = Image.open("chemin de l'image")
compare(im1, im2, im3, im4)
