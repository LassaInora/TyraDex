<div align="center">

[![Logo Pokémon](https://raw.githubusercontent.com/LassaInora/Tyradex/refs/heads/images/logo.png)](https://tyradex.app/)
# Tyradex for Python
[![LassaInora - Tyradex](https://img.shields.io/static/v1?label=LassaInora&message=Tyradex&color=yellow&logo=github)](https://github.com/LassaInora/Tyradex "Go to GitHub repo")
[![GitHub tag](https://img.shields.io/github/tag/LassaInora/Tyradex?include_prereleases=&sort=semver&color=orange)](https://github.com/LassaInora/Tyradex/releases/)
[![stars - Tyradex](https://img.shields.io/github/stars/LassaInora/Tyradex?style=social)](https://github.com/LassaInora/Tyradex)
[![forks - Tyradex](https://img.shields.io/github/forks/LassaInora/Tyradex?style=social)](https://github.com/LassaInora/Tyradex)

[![PyPI version](https://badge.fury.io/py/Tyradex.svg)](https://badge.fury.io/py/Tyradex)
[![Supported Versions](https://img.shields.io/pypi/pyversions/Tyradex.svg)](https://pypi.org/project/Tyradex)

___

[![Click for README - English](https://img.shields.io/badge/Click_for_README-English-red)](README.md)

---

</div>

# Entrée en la matière

Ce script Python interagit avec l'[API Tyradex](https://tyradex.app/) pour récupérer des informations détaillées sur les
Pokémon, leur génération et leurs types. Il est conçu pour faciliter l'accès à des informations pour chaque Pokémon ou
type telles que l'ID Pokédex, la génération, la catégorie, les statistiques, etc...  
Le script est organisé en classes représentant différents aspects des données Pokémon et inclut des fonctions permettant
d'obtenir les informations de façon claire et optimisée.

# Comment l'utiliser
## Installation
- Unix/ macOS : `python3 -m pip install --upgrade Tyradex`
- Windows : `py -m pip install --upgrade Tyradex`
-

## Interface Librairie

La librairie Tyradex pour Python propose une interface simple et intuitive pour une utilisation dans vos différents
projets.  
→ [Comment utiliser la librairie ?](https://github.com/LassaInora/Tyradex/wiki/Labrary-Interface)

## Interface en ligne de commande

Cette librairie possède également une interface en ligne de commande renvoyer les données json brut de l'API en
conservant l'avantage du cache de l'adaptation Python.  
→ [Comment utiliser la CLI ?](https://github.com/LassaInora/Tyradex/wiki/Command-Line-Interface)

# Dépendance

Cette librairie utilise les dépendances

* [requests](https://requests.readthedocs.io/en/latest/) créé par [Kenneth Reitz](https://github.com/kennethreitz)
* [pratik](https://github.com/LassaInora/Pratik) créé par [LassaInora](https://github.com/LassaInora)

# Référence de l'API

* Le script interagit avec l'API Tyradex hébergée sur https://tyradex.app/api/v1/.
* Consultez la [documentation de l'API](https://tyradex.app/docs) pour plus de détails sur les points d'extrémité
  disponibles et la structure des données.

# Contributeurs

### API créée par

* [Yarkis01](https://github.com/Yarkis01)
* [Ashzuu](https://github.com/Ashzuu)

### Adaptation Python par

* [LassaInora](https://github.com/LassaInora)

# Licence

Ce projet est sous licence [MIT License](https://github.com/LassaInora/Tyradex/blob/main/LICENSE).