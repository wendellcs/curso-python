class Game:
    def __init__(self, name = '' , yearLaunch = 0, multiplayer = False , note = 0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note

    def __str__(self): 
        return f'Game: {self.name}\nLauching year: {self.yearLaunch}'


game1 = Game('Minecraft', 2008, True , 8.5)
game2 = Game('Counter-Striker:Global Offensive', 2013, True , 10)


print('########### Game data ###########')
print(game1)
print(game2)
