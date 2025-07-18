# GIF Maker

Ce dépôt contient un script Python simple permettant de créer des fichiers GIF à partir d'une série d'images.

## Prérequis
- Python 3
- [Pillow](https://pypi.org/project/Pillow/) (`pip install Pillow`)

## Utilisation
Assurez-vous que toutes les images ont la même dimension.

Exécutez le script en passant en premier argument le nom du GIF de sortie puis les images à combiner :

```bash
python gifmaker.py animation.gif image1.png image2.png [...]
```

## Exemple

```bash
python gifmaker.py sortie.gif capybara.jpg capybara2.jpg
```

Les images `capybara.jpg` et `capybara2.jpg` sont fournies comme exemple dans le dépôt.
