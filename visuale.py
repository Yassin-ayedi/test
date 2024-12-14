import tkinter as tk
import chess
import chess.svg
import matplotlib.pyplot as plt
import cairosvg
import io

# Global variables
current_index = 0
fen_list = [
    chess.STARTING_FEN,  # Starting position
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",  # Position after castling rights
    "r1bqkbnr/pppppppp/2n5/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 1 1",  # Black to move
]
canvas = None

# Function to display the board
def show_board():
    global canvas, current_index
    fen = fen_list[current_index]
    board = chess.Board(fen)

    # Generate the SVG representation of the board
    svg = chess.svg.board(board)

    # Convert SVG to PNG
    png = cairosvg.svg2png(bytestring=svg)

    # Convert PNG to an image for tkinter display
    image_stream = io.BytesIO(png)
    img = plt.imread(image_stream, format="png")
    plt.imsave("board.png", img)

    # Update the canvas with the new board image
    board_image = tk.PhotoImage(file="board.png")
    canvas.image = board_image
    canvas.create_image(0, 0, anchor=tk.NW, image=board_image)

# Function to go to the previous board
# bagla lih 
def show_previous_board():
    global current_index
    if current_index > 0:
        current_index -= 1
        show_board()

# Function to go to the next board
def show_next_board():
    global current_index
    if current_index < len(fen_list) - 1:
        current_index += 1
        show_board()

# Function to set up the tkinter application
def setup_tkinter_app():
    global canvas

    root = tk.Tk()
    root.title("Chess Board Navigator")

    # Frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack()

    # Next and Previous buttons
    prev_button = tk.Button(button_frame, text="Previous", command=show_previous_board)
    prev_button.grid(row=0, column=0, padx=10, pady=10)

    next_button = tk.Button(button_frame, text="Next", command=show_next_board)
    next_button.grid(row=0, column=1, padx=10, pady=10)

    # Canvas for board image
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    # Show the first board
    show_board()

    # Run the application
    root.mainloop()

# Run the application
setup_tkinter_app()
