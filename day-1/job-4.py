# list : pour cree un array et séparer chaque item d'une ,
# map : afficher un nombre x de data
# chr : chaque lettre de ton clavier à un code unicode, chr prend ce code et le traduit en lettre, nombre, symbole...
# range(97, 123) : on veut afficher toutes les lettres entre A et Z

alphabet = list(map(chr, range(97, 123)))

print(alphabet)