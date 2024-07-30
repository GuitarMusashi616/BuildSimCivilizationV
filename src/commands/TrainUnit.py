from dataclasses import dataclass

from queueable.UnitType import UnitType


@dataclass
class TrainUnit:
    civ_id: int
    city_id: int
    unit_type: UnitType