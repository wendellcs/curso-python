class Game:
    name = ''
    yearLaunch = 0
    multiplayer = False
    note = 0


# Objetos

game1 = Game()
game1.name = 'Minecraft'
game1.yearLaunch = 2008
game1.multiplayer = True 
game1.note = 9.7

print('########### Game data ###########')
print(f'Game: {game1.name}\nLauching year: {game1.yearLaunch}')

game2 = Game()

game2.name = 'Counter-Strike:Global Offensive'
game2.yearLaunch = 2013
game2.multiplayer = True 
game2.note = 10

print(f'\nGame: {game2.name}\nLauching year: {game2.yearLaunch}')