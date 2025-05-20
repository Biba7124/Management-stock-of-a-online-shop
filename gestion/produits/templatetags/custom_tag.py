from django import template

register = template.Library()

# Récupère la valeur d’un dictionnaire avec une clé donnée
def get_value(dictionary, key):
    return dictionary.get(key)

# Ajoute une classe CSS à un champ de formulaire
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})

# Enregistre les filtres personnalisés
register.filter('getval', get_value)
register.filter('addclass', addclass)
