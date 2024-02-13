#heritage ASCII

class Forme:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        
        
class Triangle(Forme):
    def __init__(self, x: int, y: int, base: int):
        Forme.__init__(self, x, y)
        self._base = base
    
    
    def dessiner(self, ecran):
        hauteur = self._base
        for i in range(self._y, self._y + hauteur):
            espaces = self._y + hauteur - i -1
            etoiles = self._base - espaces
            ligne_triangle = '.' * espaces + '* ' * etoiles
            ecran[i][self._x:self._x + self._base * 2 - 1] = ligne_triangle


class Carre(Forme):
    def __init__(self, x: int, y: int, cote: int):
        Forme.__init__(self, x, y)
        self._cote = cote

    def dessiner(self, ecran):
        for i in range(self._y, self._y + self._cote):
            for j in range(self._x, self._x + self._cote):
                ecran[i][j] = '*'


# Variables
LARGEUR = 50
HAUTEUR = 20

# Code
ecran = [['.' for _ in range(LARGEUR)] for _ in range(HAUTEUR)]
formes = [
    Carre(x=1, y=2, cote=3),
    Carre(x=5, y=3, cote=4),
    Triangle(x=15, y=10, base=4)
]

for forme in formes:
    forme.dessiner(ecran)

for ligne in ecran:
    print(' '.join(ligne))
