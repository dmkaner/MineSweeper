# YOUR NAME: Dylan kane
# YOUR PSU EMAIL ADDRESS:dqk5384@psu.edu
# DESCRIPTION OF ALGORITHM (APPROACH): convert code to conform to a class
# END OF HEADER INFORMATION
# -----------------------------------------------
import random

# -----------------------------------------------
# -----------------------------------------------
# DEFINE YOUR FUNCTIONS IN THIS SECTION
# -----------------------------------------------
# ALL FUNCTIONS MUST GO IN THIS CLASS:
class Minesweeper:
    
    
    def __init__(self, size):
        self.board = [] 

        for i in range(size):
            foo = []
            for e in range(size):
                foo.append(self.marker(size))
            self.board.append(foo)

    def marker(sef, dimension):
        if (random.randrange(1000) % dimension) == 0:
            return '*'
        else:
            return ' '

    def displayBoard(self, hide):
        char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
        print('      ', end='')
        for i in range(len(self.board)):
            print(char[i], end=' | ')
        print()

        for i in range(len(self.board) * 2 + 1):
            counter = 0
            if i % 2 == 0:
                print('----|', end='')
                for e in range(len(self.board)):
                    print('---|', end='')
                print()
            else:
                if int((i - 1) / 2) > 9:
                    print(' ' + str(int((i - 1) / 2)), end=' | ')
                else:
                    print('  ' + str(int((i - 1) / 2)), end=' | ')
                for e in range(len(self.board)):
                    if hide:
                        if self.board[int((i - 1) / 2)][e] == '*':
                            print(' ', end=' | ')
                        else:
                            print(self.board[int((i - 1) / 2)][e], end=' | ')
                    else:
                        print(self.board[int((i - 1) / 2)][e], end=' | ')
                print()
                counter += 1

    def makeMove(self, move):
        char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

        letter, y = move.split(',')
        x = 0
        y = int(y)
        for i in range(len(char)):
            if letter == char[i]:
                x = i
        if y >= len(self.board) or x >= len(self.board):
            print('Move "' + move + '" is out of range')
            return True

        if self.board[y][x] == '*':
            print('*****************************')
            print('******** B O O M ! **********')
            print('*****************************')
            board = []
            return False
        self.board[y][x] = self.checkSurroundings(y, x)
        return True

    def checkSurroundings(self, y, x):
        counter = 0
        try:
            if self.board[y + 1][x] == '*':
                counter += 1
        except:
            pass

        try:
            if self.board[y - 1][x] == '*' and y != 0:
                counter += 1
        except:
            pass

        try:
            if self.board[y][x + 1] == '*':
                counter += 1
        except:
            pass

        try:
            if self.board[y][x - 1] == '*' and x != 0:
                counter += 1
        except:
            pass

        try:
            if self.board[y + 1][x + 1] == '*':
                counter += 1
        except:
            pass

        try:
            if self.board[y - 1][x - 1] == '*' and x != 0 and y != 0:
                counter += 1
        except:
            pass

        try:
            if self.board[y + 1][x - 1] == '*' and x != 0:
                counter += 1
        except:
            pass

        try:
            if self.board[y - 1][x + 1] == '*' and y != 0:
                counter += 1
        except:
            pass

        return counter

    def winner(self):
        for i in self.board:
            for e in i:
                if e == ' ':
                    return False

        print("***********************************")
        print("********** W I N N E R ! **********")
        print("***********************************")
        board = []
        return True


# END OF CLASS
# ------------------------------------------------
# END OF FUNCTION DEFINITIONS
# ------------------------------------------------
# DO NOT MODIFY WHAT IS BELOW
def main():
    random.seed(0)  # Make sure the answers match the I/O tests
    size = 99999  # anything to get it started
    while size > 0:
        size = int(input("What size board do you want (3-15, enter 0 to stop)? "))
        print(size)
        if (size > 2) and (size < 16):
            game = Minesweeper(size)
            game.displayBoard(hide=True)
            move = "not empty"
            while move != "":
                move = input("Enter coordinate (e.g. \"A,15\") or empty string to stop: ")
                print(move)
                if len(move) > 0:
                    if game.makeMove(move):
                        if game.winner():
                            game.displayBoard(hide=False)
                            break
                        else:
                            game.displayBoard(hide=True)
                    else:
                        game.displayBoard(hide=False)
                        break
            for x in range(10):
                print()
            print("*****************************")
            print("******** NEW GAME! **********")
            print("*****************************")
        elif (size < 0) or (size in [1, 2]) or (size > 15):
            print("Please pay attention!")
            size = 999999


if __name__ == "__main__":
    main()


