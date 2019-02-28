#. challenge

imelda = 'More Mayhem', 'Imelda May', 2011, (
    (1, 'Pulling the Rug'), (2, 'Psycho'), (3, 'Mayhem'), (4, 'Kentish Town Waltz')    
)

album, band, year, tracks = imelda
print(f'{band} - {album}, released {year}')
for track in tracks:
    num, name = track
    print(f'\t{num}. {name}')
