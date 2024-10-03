import random


class Outcome:

    def __init__(self, name, odds):
        self.name = name  # Name of this outcome
        self.odds = odds  # Payout odds of this outcome

    def winAmount(self, amount):  # Payout from house
        return amount * self.odds

    def __eq__(self, other):  # Compares another outcome against this one to see if their names are the same
        return self.name == other.name

    def __ne__(self, other):  # Compares another outcome instance against this one to see if their names are different
        return not self.name == other.name

    def __hash__(self):  # Creates a hash value for the name of the outcome
        return hash(self.name)

    def __str__(self):
        return "{name:s} ({odds:d}:1)".format_map(vars(
            self))  # vars creates a dictionary that maps attribute names to their values. It is displayed as the name of the attribute and then the odds:1

    def __repr__(self):
        return "{class_:s}({name!r}, {odds!r})".format(class_=type(self).__name__, **vars(
            self))  # Shows the class name and its attribute values. The attributes are represented as their data types i.e a string is returned with speech marks around it


class Bin(frozenset):  # Extending the class as to get all the basic functions of frozenset
    pass


class Wheel:

    def __init__(self):
        self.all_outcomes = set()
        self.rng = random.randint(0, 37)

    def addBins(self, bins):
        self.bins = bins

    def next(self):
        return random.choice(self.bins)

    def getBin(self, binName):
        return self.bins[binName]

    def addOutcomes(self, outcomes):
        self.allOutcomes = outcomes

    def getOutcome(self, name):
        for i in self.allOutcomes:
            if i.name.lower() == name.lower():
                return i

    # def binIterator(self):
    # pass
    # return all of the bins


class BinBuilder:  # Creates the 36 number bins with their variety of outcomes

    def __init__(self):
        self.bins = [set() for i in range(38)]

        self.outcomes =          [Outcome('Straight Bet', 35),               # 0
                                  Outcome("Column 1-2 Split", 17),           # 1
                                  Outcome("Column 2-3 Split", 17),           # 2
                                  Outcome("Row up - down Split", 17),        # 3
                                  Outcome("Street Bet", 11),                 # 4
                                  Outcome("Column 1-2 Corner", 8),           # 5
                                  Outcome("Column 2-3 Corner", 8),           # 6
                                  Outcome("Line", 5),                        # 7
                                  Outcome("Dozen", 2),                       # 8
                                  Outcome("Column", 2),                      # 9
                                  Outcome("Low", 1),                         # 10
                                  Outcome("High", 1),                        # 11
                                  Outcome("Even", 1),                        # 12
                                  Outcome("Odd", 1),                         # 13
                                  Outcome("Red", 1),                         # 14
                                  Outcome("Black", 1),                       # 15
                                  Outcome("Five", 6)                         # 16
                                  ]

    def genStraightBets(self):
        for i in range(0, 38):  # Every number
            # Sets outcome straight bet
            self.bins[i].add(self.outcomes[0])

    def genSplitBets(self):
        for r in range(0, 12):  # rows

            n = 3 * r + 1  # First Column Number
            # Sets outcome column 1-2 split
            self.bins[n].add(self.outcomes[1])
            self.bins[n + 1].add(self.outcomes[1])

            n = 3 * r + 2  # Second Column Number
            # Sets outcome column 2-3 split
            self.bins[n].add(self.outcomes[2])
            self.bins[n + 1].add(self.outcomes[2])

        for i in range(1, 33):  # Every number except last 3

            # Sets outcome vertical split bet
            self.bins[i].add(self.outcomes[3])
            self.bins[i + 3].add(self.outcomes[3])

    def genStreetBets(self):
        for r in range(0, 12):  # rows

            n = 3 * r + 1  # First Number in Column
            # Sets outcome street bet
            self.bins[n].add(self.outcomes[4])
            self.bins[n + 1].add(self.outcomes[4])
            self.bins[n + 2].add(self.outcomes[4])

    def genCornerBets(self):
        for l in range(0, 11):  # Lines inbetween rows

            n = 3 * l + 1  # First Number in Column
            # Sets outcome column 1-2 corner
            self.bins[n].add(self.outcomes[5])
            self.bins[n + 1].add(self.outcomes[5])
            self.bins[n + 3].add(self.outcomes[5])
            self.bins[n + 4].add(self.outcomes[5])

            n = 3 * l + 2  # Second Number in Column
            # Sets outcome column 2-3 corner
            self.bins[n].add(self.outcomes[6])
            self.bins[n + 1].add(self.outcomes[6])
            self.bins[n + 3].add(self.outcomes[6])
            self.bins[n + 4].add(self.outcomes[6])

    def genLineBets(self):
        for l in range(0, 11):  # Lines inbetween rows

            n = 3 * l + 1  # First Number in Column
            # Sets outcome line
            self.bins[n].add(self.outcomes[7])
            self.bins[n + 1].add(self.outcomes[7])
            self.bins[n + 2].add(self.outcomes[7])
            self.bins[n + 3].add(self.outcomes[7])
            self.bins[n + 4].add(self.outcomes[7])
            self.bins[n + 5].add(self.outcomes[7])

    def genDozenBets(self):
        for d in range(0, 3):
            for i in range(1, 13):
                n = d * 12 + i
                self.bins[n].add(self.outcomes[8])

    def genColumnBets(self):
        for c in range(0, 3):
            for r in range(0, 12):
                n = r * 3 + c + 1
                self.bins[n].add(self.outcomes[9])

    def genEvenMoneyBets(self):
        RED = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}  # set of numbers that are red

        # Assigning bins
        for n in range(1, 37):
            if n < 19:
                self.bins[n].add(self.outcomes[10])
            else:
                self.bins[n].add(self.outcomes[11])
            if n % 2 == 0:
                self.bins[n].add(self.outcomes[12])
            else:
                self.bins[n].add(self.outcomes[13])
            if n in RED:
                self.bins[n].add(self.outcomes[14])
            else:
                self.bins[n].add(self.outcomes[15])

    def genFive(self):
        # Set & assign five bet
        self.bins[0].add(self.outcomes[16])
        self.bins[1].add(self.outcomes[16])
        self.bins[2].add(self.outcomes[16])
        self.bins[3].add(self.outcomes[16])
        self.bins[37].add(self.outcomes[16])

    def buildBins(self, wheel):

        # Generates all possible bets
        self.genStraightBets()
        self.genSplitBets()
        self.genStreetBets()
        self.genCornerBets()
        self.genLineBets()
        self.genDozenBets()
        self.genColumnBets()
        self.genEvenMoneyBets()
        self.genFive()

        wheel.addOutcomes(self.outcomes)

        # Creates bin objects in wheel object
        wheel.addBins(tuple(Bin(self.bins[i]) for i in range(38)))


class Bet:
    def __init__(self, amount, outcome):
        self.amountBet = amount
        self.outcome = outcome

    def winAmount(self):
        return self.amountBet + self.outcome.winAmount(self.amountBet)

    def loseAmount(self):
        return self.amountBet

    def __str__(self):
        return "{} bet on {}".format(self.amountBet, self.outcome.__str__())

    def __repr__(self):
        return "Bet({}, {})".format(self.amountBet, self.outcome)


class InvalidBet(Exception):
    pass


class Table:

    def __init__(self):
      self.bets = []

    def placeBet(self,bet):
      self.bets.append(bet)
      # raise InvalidBet

    def clearBets(self):
        self.bets = []

    def __iter__(self):
      return iter(self.bets)

    def __str__(self):
      return "{}".format(*self.bets)

    def __repr__(self):
      pass

    def isValid(self):
      if sum(self.bets) > self.maximum:
        raise InvalidBet


class Game:

    def __init__(self, wheel, table):
        self.wheel = wheel
        self.table = table

    def cycle(self, player):
        before = player.stake
        self.table.clearBets()
        player.placeBets()
        after = player.stake
        winningBin = self.wheel.next()
        winningOutcomes = list(winningBin)

        winCheck = False
        iterator = self.table.__iter__()
        for i in iterator:
          if i.outcome in winningOutcomes:
            player.win(i)
          else:
            # If the player has less than 10 left end the game
            if player.lose():
                player.stopPlaying()

class Player:

    def __init__(self, table, wheel):
        self.table = table
        self.active = True
        self.wheel = wheel

    def playing(self):
        return self.active

    def stopPlaying(self):
        self.active = False

    def placeBets(self):
        for i in self.bets:
            self.table.placeBet(i)
            self.stake -= i

    def win(self, bet):
        self.stake += bet.winAmount()

    def lose(self):
        return True if self.stake < 10 else False

    def setStake(self, stake):
        self.stake = stake

    def setRounds(self, rounds):
        self.roundsToGo = rounds

    def winners(self, outcomes):
        pass
        # The game will notify a player of each spin using this method. This will be invoked even if the player places no bets.


class Martingale(Player):

    def __init__(self, table, wheel):
        super().__init__(self, table, wheel)
        self.lossCount = 0
        self.betMultiple = 1

    def win(self, bet):
        super().win(self, bet)
        self.lossCount = 0
        self.betMultiple = 1

    def lose(self, bet):
        super().lose(self, bet)
        self.lossCount += 1
        self.betMultiple = self.betMultiple * 2


class SevenReds(Martingale):

    def __init__(self, table, wheel):
        super().__init__(self, table, wheel)
        self.redCount = 7

    # def placeBets(self):
    # if self.redCount == 0:
    # self.table.placeBet(self.betAmount * self.betMultiple, black)

    def winners(self, outcomes):

        redSeen = False
        for i in outcomes:
            if i[1] == 'red':
                self.redCount -= 1
                redSeen = True
                break

        if not (redSeen):
            self.redCount = 7


class PlayerRandom(Player):

    def __init__(self, table, wheel):
        super().__init__(table, wheel)
        self.rng = random.random
        self.bins = self.table.wheel.bins

    def placeBets(self):
        self.table.placeBet(self.randAmount, self.randOutcome)


class Player1326State(Player):

    def __init__(self, player, wheel):
        self.player = player

    def currentBet(self):
        pass
        # Constructs a new Bet from the player’s preferred Outcome. Each subclass has a different multiplier used when creating this Bet.

    def nextWon(self):
        pass

    def nextLost(self):
        pass


class Player1326NoWins(Player1326State):

    def currentBet(self):
        betMultiple = 1
        # self.player.outcome

    def nextWon(self):
        pass


class Player1326OneWin(Player1326State):

    def currentBet(self):
        betMultiple = 3

    def nextWon(self):
        pass


class Player1326TwoWins(Player1326State):

    def currentBet(self):
        betMultiple = 2

    def nextWon(self):
        pass


class Player1326ThreeWins(Player1326State):

    def currentBet(self):
        betMultiple = 6

    def nextWon(self):
        pass


class Player1326(Player):

    def __init__(self, table, wheel):
        super().__init__(table, wheel)
        # self.state =
        # self.outcome = self.table.wheel.outcomes

    def placeBets(self):
        # self.state.currentBet()
        pass

    def win(self, bet):
        super().win(self, bet)
        # self.state.nextWon()

    def lose(self, bet):
        pass
        # self.state.lose()


class PlayerCancellation(Player):

    def __init__(self, table, wheel):
        super().__init__(self, table, wheel)
        self.resetSequence()

    def resetSequence(self):
        self.sequence = list(range(1, 7))

    def placeBets(self):
        bet = self.sequence[0] + self.sequence[-1]
        # places Bet

    def win(self, bet):
        super().win(self, bet)
        self.sequence.remove[0]
        self.sequence.remove[-1]

    def lose(self, bet):
        super().lose(self, bet)
        self.sequence.append(self.sequence[0] + self.sequence[-1])


class PlayerFibonacci(Player):

    def __init__(self, table, wheel):
        super().__init__(self, table, wheel)
        self.recent = 1
        self.previous = 0

    def win(self, bet):
        super().win(self, bet)
        self.recent = 1
        self.previous = 0

    def lose(self, bet):
        super().lose(self, bet)
        self.next = self.recent + self.previous
        self.previous = self.recent
        self.recent = self.next


class Passenger57(Player):

    def __init__(self, table, wheel):
        super().__init__(table, wheel)
        self.amountBet = 10
        self.bet = Bet(self.amountBet,self.wheel.getOutcome("Black"))

    def placeBets(self):
        self.table.placeBet(self.bet)
        self.stake -= self.amountBet


class Simulator:
    # maxima = []
    # durations = []
    # for session in range(100):
    # stakeDetails = []
    # while player.playing:
    #   play one cycle of Game
    #   save current stake in stakeDetails
    # maxStakeDetails = max(stakeDetails)
    # lenStakeDetails = len(stakeDetails)
    # durations.append(lenStakeDetails)
    # find average and standard deviation of maxima list and durations list

    def __init__(self, game, player):
        self.samples = 50
        self.bettingUnits = 100
        self.initDuration = 250
        #self.initStake = self.bettingUnits * table.minimum
        self.durations = []
        self.maxima = []

        self.player = player
        self.player.setStake(1000)  # Starting Budget of the player
        self.player.setRounds(7)  # players duration of play

        self.game = game

    def session(self):
        stakeValues = []
        while self.player.playing():
            self.game.table.clearBets()
            self.game.cycle(self.player)
            stakeValues.append(self.player.stake)
            print(stakeValues)
        return stakeValues

    def gather(self):
        for i in range(self.samples):
            print(i,'doing this sample')
            # I need to reset the game here
            sessionList = self.session()
            print('session complete')
            print(sessionList)
            self.maxima.append(max(sessionList))
            self.durations.append(len(sessionList))
            print("list finished, for loop single loop")
        print("for loop done")
        print(self.maxima,"maxima")
        print(self.durations,"durations")


class IntegerStatistics(list):

    def __init__(self, iterable):
        super().__init__(iterable)
        self.sum = sum(self.list)
        self.length = len(self.list)

    def mean(self):
        return self.sum // self.length

    def stdev(self):
        mean = self.mean()
        return ((sum((x - mean) ** 2 for x in self) / (self.length - 1)) ** 1 / 2)

if __name__ == "__main__":
    builder = BinBuilder()
    theWheel = Wheel()
    builder.buildBins(theWheel)
    theTable = Table()
    theGame = Game(theWheel,theTable)
    thePlayer = Passenger57(theTable,theWheel)
    #thePlayer = Player1326(theTable,theWheel)
    sim = Simulator(theGame, thePlayer)
    #print(thePlayer)
    sim.gather()