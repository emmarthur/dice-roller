"""Terminal dice roller — uses shared dice_roller_core logic."""

from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from dice_roller_core import roll_notation  # noqa: E402

print(
    """Dice Roller

Enter dice notation: count + "d" + sides, optional + or - modifier.
Examples: 3d6   1d10+2   2d38-1
Type QUIT to exit.
"""
)

while True:
    dice_str = input("> ")
    if dice_str.strip().upper() == "QUIT":
        print("Thanks for playing!")
        break
    try:
        result = roll_notation(dice_str)
    except ValueError as exc:
        print('Invalid input. Enter something like "3d6" or "1d10+2".')
        print(f"Input was invalid because: {exc}")
        continue

    rolls_display = ", ".join(str(r) for r in result["rolls"])
    mod = result["modifier"]
    mod_part = ""
    if mod > 0:
        mod_part = f", +{mod}"
    elif mod < 0:
        mod_part = f", {mod}"
    print(
        f"Total: {result['total']} (Each die: {rolls_display}{mod_part})"
    )
