#heritage ASCII

class Forme:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y


class Carre(Forme):
    def __init__(self, x: int, y: int, cote: int):
        super().__init__(x, y)
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
    Carre(x=5, y=3, cote=4)
]

for forme in formes:
    forme.dessiner(ecran)

for ligne in ecran:
    print(' '.join(ligne))
