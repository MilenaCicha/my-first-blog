# print('Hello Django Girls!')
# if 3 > 2:
#     print('To dziala!')
#
# if 5 > 2:
#     print('5 jest jednak wieksze od 2')
# else:
#     print('5 nie jest wieksze od 2')

#
# def hi(name):
#  if name == 'Ola':
#     print('Hej Ola')
#  elif name == 'Sonja':
#     print('Hej Sonja')
#  else:
#     print('Hej anonimie')

# def hi(imie):
#     print('Hej ' + imie + '!')
# hi('Monika')
#
# dziewczyny = ['Rachel', 'Monica', 'Phoebe']
# for imie in dziewczyny:
#     hi(imie)
#     print('Kolejna dziewczyna')
#
# def random(name):
#     print(name)
#
#
# random('Ola')
def get_object_or_404(Post, pk):
    if Post:
        return pk
    else:
        return 404

def wrong(abc, de=78, fgh=' Monika'):
    print(abc, de, fgh)
    print(abc)

wrong('Kasia', fgh='Magda')

# post = get_object_or_404(Post, pk=pk)

