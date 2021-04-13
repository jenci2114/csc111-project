"""CSC111 Final Project: AI Player in Chinese Chess

Module Description
===============================

This Python module contains functions to run games.

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Junru Lin, Zixiu Meng, Krystal Miao and Jenci Wei
"""

from __future__ import annotations
from chess_game import ChessGame
import player


def run_games(n: int, red: player.Player, black: player.Player, visualize: bool = False) -> None:
    """Run n games using the given Players.

    visualize: print the board after each move

    Preconditions:
        - n >= 1
    """
    stats = {'Red': 0, 'Black': 0, 'Draw': 0}
    results = []
    for i in range(1, n + 1):
        red.reload_tree()
        black.reload_tree()

        winner, _ = run_game(red, black, visualize)
        stats[winner] += 1
        results.append(winner)

        print(f'Game {i} winner: {winner}')

    for outcome in stats:
        print(f'{outcome}: {stats[outcome]}/{n} ({100.0 * stats[outcome] / n:.2f}%)')


def run_game(red: player.Player, black: player.Player, visualize: bool = False) \
        -> tuple[str, list[str]]:
    """Run a Chinese Chess game between the two given players.

    Return the winner and list of moves made in the game.
    """
    game = ChessGame()

    move_sequence = []
    previous_move = None
    current_player = red
    while game.get_winner() is None:
        previous_move = current_player.make_move(game, previous_move)
        game.make_move(previous_move)
        move_sequence.append(previous_move)

        if visualize:
            print(game)

        if current_player is red:
            current_player = black
        else:  # if current_player is black
            current_player = red

    return game.get_winner(), move_sequence


# if __name__ == '__main__':
    # import python_ta.contracts
    # python_ta.contracts.check_all_contracts()

    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 100,
    #     'disable': ['E1136', 'E9998'],
    #     'extra-imports': ['chess_game', 'player']
    # })
