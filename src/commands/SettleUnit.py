# pyright: strict

from dataclasses import dataclass


@dataclass
class SettleUnit:
    civ_id: int
    unit_id: int
    new_city_id: int
