#positivos e media
positivos = [float(input("digite os valores:")) for _6
 in range(6)] #colocar em for in range para a contagem
totalpositivos = 0 
somadospositivos = 0

for y in positivos:
    if y > 0:
        totalpositivos += 1
        somadospositivos += y

print('{} valores positivos'.format(totalpositivos))
print('{:.1f}'.format(somadospositivos / totalpositivos))