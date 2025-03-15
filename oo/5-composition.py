# Base class or Superclass
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


class GameStudio:
    def __init__(self , name = ''):
        self.name = name
        self.games = []

    def add_game(self,game):
        self.games.append(game)
    
    def evaluate_studio_quality(self):
        total_notes = sum(game.note for game in self.games)
        num_games = len(self.games)

        if num_games == 0:
            print(f'This studio has not released any game yet.')
        else: 
            average_note = total_notes / num_games
            print(f'Average gaming rate: {self.name} - {average_note:.2f}')

game1 = Game('Minecraft', 2008, True , 8.5)
game2 = Game('Counter-Striker:Global Offensive', 2013, True , 10)
game3 = Game('The last of us 2', 2020, False , 9.9)

studio = GameStudio('Awesome Games')
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.evaluate_studio_quality()

for game in studio.games:
    game.technical_sheet()

# Composition - When a class contains or is made up of objects of other class.