from PIL import Image

im = Image.open("chemin de l'image")

##### pour garder le ratio de l'image

# facteur de réduction de la taille de notre image
facteur = 2.76

# t : taille
t = im.size
# [0] : valeur en x (largeur) ; [1] : valeur en y (hauteur)
t_reduit = (round(t[0] / facteur), round(t[1] / facteur))

im.resize(t_reduit).show()
