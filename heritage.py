#heritage ASCII

class Forme:
    def __init__(self, x, y):
        self.x = x
        self.y = y






class Carre:
    def __init__(self, x, y, cote):
        self.x = x
        self.y = y
        self.cote = cote

    def dessiner(self, ecran):
        for i in range(self.y, self.y + self.cote):
            for j in range(self.x, self.x + self.cote):
                ecran[i][j] = '*'



#variables
LARGEUR = 50
HAUTEUR = 20

#code
ecran = [ ['.' for _ in range(LARGEUR)] for _ in range(HAUTEUR) ]
carre = Carre(x=1, y=2, cote=3)
carre.dessiner(ecran)
for ligne in ecran:
    print(' '.join(ligne))

