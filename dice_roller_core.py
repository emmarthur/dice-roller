"""
Dice roller — parse D&D-style notation and simulate rolls.

Format: <count>d<sides>[+|-<modifier>]  (e.g. 3d6, 1d10+2, 2d38-1)
"""

from __future__ import annotations

import random
import re
from dataclasses import dataclass
from typing import Any

MAX_DICE = 100
MAX_SIDES = 10_000

_DICE_RE = re.compile(
    r"^(?P<count>\d+)d(?P<sides>\d+)(?P<mod>[+-]\d+)?$",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class DiceSpec:
    count: int
    sides: int
    modifier: int

    @property
    def notation(self) -> str:
        base = f"{self.count}d{self.sides}"
        if self.modifier > 0:
            return f"{base}+{self.modifier}"
        if self.modifier < 0:
            return f"{base}{self.modifier}"
        return base


def parse_dice_notation(raw: str) -> DiceSpec:
    cleaned = raw.strip().lower().replace(" ", "")
    if not cleaned:
        raise ValueError('Enter a dice string like "3d6" or "1d10+2".')

    match = _DICE_RE.match(cleaned)
    if not match:
        raise ValueError('Use the format count + "d" + sides, optional + or - modifier.')

    count = int(match.group("count"))
    sides = int(match.group("sides"))
    mod_text = match.group("mod")
    modifier = int(mod_text) if mod_text else 0

    if count < 1:
        raise ValueError("Roll at least one die.")
    if count > MAX_DICE:
        raise ValueError(f"At most {MAX_DICE} dice per roll.")
    if sides < 2:
        raise ValueError("Dice need at least 2 sides.")
    if sides > MAX_SIDES:
        raise ValueError(f"At most {MAX_SIDES} sides per die.")

    return DiceSpec(count=count, sides=sides, modifier=modifier)


def roll_dice(spec: DiceSpec) -> list[int]:
    return [random.randint(1, spec.sides) for _ in range(spec.count)]


def roll_notation(raw: str) -> dict[str, Any]:
    spec = parse_dice_notation(raw)
    rolls = roll_dice(spec)
    subtotal = sum(rolls)
    total = subtotal + spec.modifier
    return {
        "notation": spec.notation,
        "rolls": rolls,
        "subtotal": subtotal,
        "modifier": spec.modifier,
        "total": total,
        "count": spec.count,
        "sides": spec.sides,
    }


def example_notations() -> list[str]:
    return ["1d6", "3d6", "1d20", "2d10+3", "4d6-1"]
