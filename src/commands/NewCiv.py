# pyright: strict

from dataclasses import dataclass

from enums.Nation import Nation


@dataclass
class NewCiv:
    civ_id: int
    nation: Nation
    settler_id: int
