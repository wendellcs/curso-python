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


# Specialized Class - A class which extends the functionality of a more general class.
class SinglePlayerGame(Game):
    def __init__(self, name = '', yearLaunch = '', note = 0, storyline = ''):
        super().__init__(name, yearLaunch, multiplayer = False, note = note)
        self.storyline = storyline

    def technical_sheet(self):
        super().technical_sheet()
        print(f'Story: {self.storyline}\n')

mult_game = Game('Fortnite', 2017, True, 7.3)
mult_game.technical_sheet()

sing_game = SinglePlayerGame('The Last of Us pt-2', 2020, 9.8, 'In The Last of Us, Joel, a hardened survivor, is tasked with smuggling Ellie, a teenage girl immune to a deadly fungal infection, across a post-apocalyptic U.S. Their journey is filled with danger and loss, but they form a deep bond. Upon learning Ellie must die to create a cure, Joel saves her, dooming humanity and lying to her about it.\n')
sing_game.technical_sheet()