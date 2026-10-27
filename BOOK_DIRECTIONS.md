# Book directions — Dice Roller

**Catalog #456** · Al Sweigart, *The Big Book of Small Python Projects*, **Project #18** — Dice Roller

- Invent with Python: [project18.html](https://inventwithpython.com/bigbookpython/project18.html)
- Upstream: [diceroller.py](https://github.com/asweigart/the-big-book-of-small-python-projects/blob/main/diceroller.py)
- Local reference: [`reference/diceroller.py`](./reference/diceroller.py)
- Shared logic: [`dice_roller_core.py`](./dice_roller_core.py)

## What the book asks you to build

A loop that reads **D&D-style dice notation**:

- `<count>d<sides>` — roll `count` dice with `sides` faces each.
- Optional `+N` or `-N` modifier applied after summing dice.
- Print **total**, individual die results, and modifier when present.
- Re-prompt on invalid input; **QUIT** exits.

## Web version (`web/` — FastAPI, port **3022**)

| Book step | Web equivalent |
|-----------|----------------|
| Parse `3d6+1` | `dice_roller_core.parse_dice_notation` |
| `random.randint(1, sides)` per die | `roll_dice` |
| Display total + each die + mod | Result card + die chips |
| Example strings | Quick-fill chips + `/help` |

CLI: [`reference/run_cli.py`](./reference/run_cli.py)
