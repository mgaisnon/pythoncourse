import random
from random import randint

secret = randint(0, 100)
number = int(input('entrer un chiffre entre entre 0 et 100 : '))
essai =0
while secret != number:

    if secret > number:
        print('C\'est plus')
    else:
        print('C\'est moins')
    number = int(input('entrer un chiffre entre entre 0 et 100 : '))
print('Bravo vous avez trouvé')
