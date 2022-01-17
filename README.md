# Chess Engine

## Install dependencies

Tested on `Python 3.6`

- [Python-chess](https://python-chess.readthedocs.io/en/latest/)

Run `pip install -r requirements.txt`

## How to run?

Run `python play.py`

## Strategies

- Greedy
  - It'll scan two levels of the search tree (i.e. only look forward two positions and optimized based on that).

## How is the codebase structured?

After running `play.py`, the chess engine gets created `engine.py`.

It initializes the chess board and provides an interface to make moves.

The main logic of the code is in `get_next_move()`. This is where the initial strategy is implemented.

For now, only a greedy strategy is implemented. In `play`, whenever the `engine` is asked to make the next move, it uses the greedy strategy implemented in `greedy.py`.

## How to use your own strategy?

In `engine.py`, you can replace the `get_next_move()` function with your own strategy.

Also feel free to make a PR with the strategy you want to add :)
