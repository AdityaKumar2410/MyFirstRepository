import pygame
import chess
import chess.engine
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
DIMENSION = 8  # Chessboard is 8x8
SQ_SIZE = WIDTH // DIMENSION
MAX_FPS = 15
IMAGES = {}


# Load images
def load_images():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))


# Initialize the game state
board = chess.Board()


# Draw the game state
def draw_board(screen):
    colors = [pygame.Color("white"), pygame.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, board):
    for sq in chess.SQUARES:
        piece = board.piece_at(sq)
        if piece:
            piece_image = IMAGES[piece.symbol().lower() if piece.color else piece.symbol().upper()]
            screen.blit(piece_image,
                        pygame.Rect(chess.square_file(sq) * SQ_SIZE, chess.square_rank(sq) * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_game_state(screen, board):
    draw_board(screen)
    draw_pieces(screen, board)


# Random move bot
def get_random_move(board):
    return random.choice(list(board.legal_moves))


# Main function
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess Bot")
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))
    load_images()

    running = True
    player_turn = True  # True if player's turn, False if bot's turn
    move_made = False

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if player_turn:
                    location = pygame.mouse.get_pos()
                    col = location[0] // SQ_SIZE
                    row = location[1] // SQ_SIZE
                    move = chess.Move.from_uci(
                        f'{chess.square_name(chess.square(col, row))}{chess.square_name(chess.square(col, row))}')
                    if move in board.legal_moves:
                        board.push(move)
                        move_made = True
                        player_turn = False

        if not player_turn and not move_made:
            move = get_random_move(board)
            board.push(move)
            move_made = True
            player_turn = True

        if move_made:
            draw_game_state(screen, board)
            move_made = False

        clock.tick(MAX_FPS)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
