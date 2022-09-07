from classe_forca import Forca

print('-' * 30)
print(f'{"Jogo da Forca": ^30}' )
print('-' *30 )

palavra = str(input('Digite uma palavra: ')).lower()
vidas =  int(input('Digite o número de vidas:'))
forca = Forca(palavra, vidas)
forca.jogar()