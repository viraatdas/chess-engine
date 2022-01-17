# Chess Engine

## Install dependencies

Tested on `Python 3.6`

- `pip install -r requirements.txt`

## How to run?

`python play.py`

## Strategies

- Greedy [need to fix]
  - It'll scan two levels of the search tree (i.e. only look forward two positions and optimized based on that).

## How to use your own strategy?

In `engine.py`, you can replace the `get_next_move` function with your own strategy.
