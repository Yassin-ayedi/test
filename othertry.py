import tkinter as tk
import chess
import chess.svg
import matplotlib.pyplot as plt
import cairosvg
import io

class ChessBoardViewer:
    def __init__(self, fens):
        self.fens = fens  # List of FEN strings
        self.current_index = 0  # Start at the first board

        # Tkinter window setup
        self.root = tk.Tk()
        self.root.title("Chess Board Viewer")
        self.root.geometry("600x700")

        # Chessboard display
        self.board_canvas = tk.Canvas(self.root, width=600, height=600)
        self.board_canvas.pack()

        # Navigation buttons
        self.controls_frame = tk.Frame(self.root)
        self.controls_frame.pack(pady=10)

        self.prev_button = tk.Button(self.controls_frame, text="Previous", command=self.show_previous_board)
        self.prev_button.grid(row=0, column=0, padx=5)

        self.next_button = tk.Button(self.controls_frame, text="Next", command=self.show_next_board)
        self.next_button.grid(row=0, column=1, padx=5)

        # Display the first board
        self.display_board(self.fens[self.current_index])

        # Start the Tkinter main loop
        self.root.mainloop()

    def display_board(self, fen):
        """Display the chessboard for the given FEN string."""
        board = chess.Board(fen)
        svg = chess.svg.board(board)
        png = cairosvg.svg2png(bytestring=svg)

        image_stream = io.BytesIO(png)
        img = tk.PhotoImage(data=image_stream.getvalue())

        # Clear previous content and display the new board
        self.board_canvas.delete("all")
        self.board_canvas.image = img  # Prevent garbage collection
        self.board_canvas.create_image(300, 300, image=img)

    def show_next_board(self):
        """Show the next board if available."""
        if self.current_index < len(self.fens) - 1:
            self.current_index += 1
            self.display_board(self.fens[self.current_index])

    def show_previous_board(self):
        """Show the previous board if available."""
        if self.current_index > 0:
            self.current_index -= 1
            self.display_board(self.fens[self.current_index])

# Example usage
if __name__ == "__main__":
    # List of FEN strings to display
    fens = [
        chess.STARTING_FEN,
  # Initial position
        "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1",  # After e2-e4
        "rnbqkbnr/pppppp1p/8/6p1/4P3/8/PPPP1PPP/RNBQKBNR w KQkq g6 0 2"  # After g7-g5
    ]

    viewer = ChessBoardViewer(fens)
