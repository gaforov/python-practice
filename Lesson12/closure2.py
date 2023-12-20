def parent_function(person, coins):
    # coins = 3 # we move this variable to parent paranthesis

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print('\n' + person + ' has ' + str(coins) + ' coins left.')
        elif coins == 1:
            print('\n' + person + ' has ' + str(coins) + ' coin left.')
        else:
            print('\n' + person + ' is out of coins')

    return play_game

john = parent_function('John', 3)
mike = parent_function('Mike', 5)

john()
john()

mike()


