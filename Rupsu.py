import random


class Item(object):
    def __str__(self):
        return self.__class__.__name__.lower()


# The idea is that we in attack, call the victim's relevant strategy for resolving our conflict
# they decide if we succeed or fail. Bit messy.

class Paper(Item):
    def attack(self, item):
        return item.evalPaper(self)

    def evalPaper(self, item):
        return Result.TIE

    def evalRock(self, item):
        # It's a loss for the *rock*
        return Result.LOSS

    def evalScissors(self, item):
        # A victory for the scissors
        return Result.VICTORY


class Rock(Item):
    def attack(self, item):
        return item.evalRock(self)

    def evalPaper(self, item):
        return Result.VICTORY

    def evalRock(self, item):
        return Result.TIE

    def evalScissors(self, item):
        return Result.LOSS


class Scissors(Item):
    def attack(self, item):
        return item.evalScissors(self)

    def evalPaper(self, item):
        return Result.LOSS

    def evalRock(self, item):
        return Result.VICTORY

    def evalScissors(self, item):
        return Result.TIE


# kinda an Enum __str__ is toString(), __eq__ is equals()
class Result:
    def __init__(self, value, name):
        self.vale = value
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.vale == other.value


Result.VICTORY = Result(0, "You win!")
Result.LOSS = Result(1, "Your opponent wins!")
Result.TIE = Result(2, "It's a tie!")


# the actual RPS game begins here

# First some helper methods
def string_to_item(arg):
    switch = {
        "paper": Paper(),
        "rock": Rock(),
        "scissors": Scissors(),
    }
    return switch.get(arg, Rock())  # dumb mode


def random_item():
    items = [Paper(), Rock(), Scissors()]
    return random.choice(items)

# set-up + game loop
rounds = input("How many rounds? ")
rounds = int(rounds)
print("Game started")
while rounds > 0:
    choice = input("Make your choice for round {}: ".format(rounds))
    choice = string_to_item(choice)
    opponent = random_item()
    result = choice.attack(opponent)
    print("You chose {}, your opponent chose {}. {}".format(choice, opponent, result))
    rounds -= 1
