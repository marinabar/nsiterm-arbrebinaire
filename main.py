class Arbre:
  vide=None
  def __init__(self, valeur):
    self.__compte=0
    self.__valeur = valeur
    self.__gauche = Arbre.vide
    self.__droit = Arbre.vide
    
  def __str__(self):
    return f'({self.__valeur},{self.__gauche},{self.__droit})'
    
  def get_valeur(self):
    return self.__valeur
  def get_gauche(self):
    return self.__gauche
  def get_droit(self):
    return self.__droit

  def insert_gauche(self, valeur):
    self.__gauche = Arbre(valeur)
  def insert_droit(self, valeur):
    self.__droit = Arbre(valeur)

  def hauteur(self):
    if (self.__gauche and not self.__droit):
      return self.__gauche.hauteur() +1
    if (not self.__gauche and self.__droit):
      return self.__droit.hauteur() + 1
    if self.__gauche and self.__droit:
      return self.__gauche.hauteur()+self.__droit.hauteur() + 1
    else:
      return 0

  def taille(self):
    if self == None:
      return 0
    if (self.__gauche and not self.__droit):
      self.__compte+= self.__gauche.taille() +1
      print(self.__compte)
    if (not self.__gauche and self.__droit):
      self.__compte+= self.__droit.taille() +1
    if self.__gauche and self.__droit:
      self.__compte+= self.__droit.taille() +1 + self.__gauche.taille()
    else:
      return self.__compte


  def parcours_larg(self):
    file = [self]
    largeur = []
    while file:
      if file[0]:
        largeur.append(file[0].get_valeur())
        file.append(file[0].get_gauche())
        file.append(file[0].get_droit())
      file.pop(0)
    return largeur


  def parcours_prefixe(self):
    if self == None: return []
    else:
      return [self.get_valeur()]+ Arbre.parcours_prefixe(self.get_gauche())+ Arbre.parcours_prefixe(self.get_droit())

  def parcours_infixe(self):
    if self == None:return []
    else:
      return Arbre.parcours_infixe(self.get_gauche())+ [self.get_valeur()]+Arbre.parcours_infixe(self.get_droit())

  def parcours_postfixe(self):
    if self == None:return []
    else:
      return Arbre.parcours_postfixe(self.get_gauche()) +Arbre.parcours_postfixe(self.get_droit())+ [self.get_valeur()]


  def est_abr(self):
    val = self.parcours_infixe()
    for i in range(len(val)-1):
      if val[i+1]<val[i]:
        return False
    return True

  
def recherche(abr, valeur):
  if abr==None:
    return False
  else:
    valeurx=abr.get_valeur()
    if valeur < valeurx:
      return recherche(abr.get_gauche(), valeur)
    elif valeur > valeurx:
      return recherche(abr.get_droit(), valeur)
    else:
      print(valeurx)
      return True

def maxval(abr):
  if abr == None:
    return False
  if abr.get_droit()== None:
    print(abr.get_valeur())
    return 0
  else:
    maxval(abr.get_droit())
    return("")

def minval(abr):
  if abr == None:
    print("this tree is empty")
    return False
  if abr.get_gauche()== None:
    print(abr.get_valeur())
    return 0
  else:
    minval(abr.get_gauche())
    return  ''

def hauteur(abr):
  if (abr.get_gauche() and not abr.get_droit()):
    return abr.get_gauche().hauteur() +1
  if (not abr.get_gauche() and abr.get_droit()):
    return abr.get_droit().hauteur() + 1
  if abr.get_gauche() and abr.get_droit():
    return abr.get_gauche().hauteur()+abr.get_droit().hauteur() + 1
  else:
    return 0
  
# définir arbre
racine = Arbre("A")
racine.insert_gauche("B")
nB=racine.get_gauche()
nB.insert_gauche("D")
nB.insert_droit("E")
nE=nB.get_droit()
nE.insert_gauche("G")
racine.insert_droit("C")
nC = racine.get_droit()
nG=nE.get_gauche()


racine1 = Arbre(50)
racine1.insert_droit(76)
racine1.insert_gauche(17)
n2 = racine1.get_droit()
n1 = racine1.get_gauche()
n1.insert_droit(23)
n1.insert_gauche(9)
n11 = n1.get_gauche()
n12 = n1.get_droit()
n11.insert_droit(14)
n12.insert_gauche(19)
n112 = n11.get_droit()
n112.insert_gauche(12)
n1121 = n112.get_gauche()
n121=n12.get_gauche()

n2.insert_gauche(54)
n21= n2.get_gauche()
n21.insert_droit(72)
n212 = n21.get_droit()
n212.insert_gauche(67)
n2121=n212.get_gauche()


# test des méthodes
'''print(racine)
print(nB.get_gauche())
print(racine.parcours_larg())
print(racine.parcours_infixe())'''

print(hauteur(racine1))