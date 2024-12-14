import chess
import chess.svg
import matplotlib.pyplot as plt
import cairosvg
import io


def setup_realtime_board_view():
    """
    Sets up a real-time matplotlib figure for the chessboard.
    Returns the figure and axes for updating later.
    """
    fig, ax = plt.subplots()
    ax.axis('off')  # Turn off axis for clean display
    plt.ion()  # Turn on interactive mode
    return fig, ax


def update_realtime_board(ax, fen):
    """
    Updates the real-time chessboard display.

    Args:
        ax: The matplotlib axes to draw on.
        fen: FEN string representing the chessboard state.
    """
    board = chess.Board(fen)
    svg = chess.svg.board(board)
    png = cairosvg.svg2png(bytestring=svg)

    image_stream = io.BytesIO(png)
    img = plt.imread(image_stream, format='png')

    ax.clear()  # Clear previous board
    ax.axis('off')  # Keep axis off
    ax.imshow(img)
    plt.pause(0.1)  # Pause for a brief moment to update the display


def play_realtime_game(fen_list):
    """
    Simulates a game by showing the chessboard in real-time for a series of FENs.

    Args:
        fen_list: A list of FEN strings representing the moves in a game.
    """
    fig, ax = setup_realtime_board_view()

    for fen in fen_list:
        update_realtime_board(ax, fen)
        plt.pause(1)  # Pause to simulate delay for the next move


def main():
    """
    Main function to demonstrate the real-time chessboard updates.
    """
    # Example FEN list to simulate a game
    fen_list = [
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",  # Initial position
        "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1",  # After e2-e4
        "rnbqkbnr/pppppp1p/8/6p1/4P3/8/PPPP1PPP/RNBQKBNR w KQkq g6 0 2"  # After g7-g5
    ]

    play_realtime_game(fen_list)


# To allow importing into other files without auto-executing the script
if __name__ == "__main__":
    main()
