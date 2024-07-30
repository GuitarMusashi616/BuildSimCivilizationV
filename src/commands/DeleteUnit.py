# pyright: strict

from dataclasses import dataclass


@dataclass
class DeleteUnit:
    civ_id: int
    unit_id: int