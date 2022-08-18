names = [' Bruce Wayne ' , 'Clark kent'  , 'Walley wet' ]
initials = []
for name in  names :
    parts = name.split()
    initials.append(parts[0][0]+parts[-1][0])
print(initials)

#2



names = [' Bruce Wayne ' , 'Clark kent'  , 'Walley wet' ]
initials = [name.split()[0][0]+ name.split()[-1][0] for name in names]
print(initials)

