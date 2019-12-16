# https://codechalleng.es/bites/176/

WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    piece1 = WHITE + BLACK
    piece2 = BLACK + WHITE
    size = int(size / 2)
    for x in range(size):
        print(size * piece1)
        print(size * piece2)




if __name__ == '__main__':
    create_chessboard()