class Game:
    total_games = 0 # Class variable to count the total number of games

    def __init__(self, name = '' , yearLaunch = 0, multiplayer = False , note = 0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note

        Game.total_games += 1 # Increment by one every time the class is instantiated.

        self.totalEvaluation = 0
        self.evaluators = 0

    def __str__(self): 
        return f'Game: {self.name}\nLauching year: {self.yearLaunch}'

    def technical_sheet(self):
        print('########### Game data ###########')
        print(f'\nGame: {self.name}')
        print(f'Launching year: {self.yearLaunch}')
        print(f'Multiplayer?: {self.multiplayer}')
        print(f'Note: {self.note}')

    def evaluate(self, note):
        self.totalEvaluation += note 
        self.evaluators += 1

    def average(self):
        print('-' * 40)
        print('Game Rating')
        print(f'Game: {self.name}')
        print(f'Rating: {self.totalEvaluation / self.evaluators}')
        print('-' * 40)
        

game1 = Game('Minecraft', 2008, True , 8.5)
game2 = Game('Counter-Striker:Global Offensive', 2013, True , 10)

# Showing the total of games created

print(f'{Game.total_games} game{"s were " if Game.total_games > 1 else " was "}created')