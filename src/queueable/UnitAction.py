from enum import Enum, auto

class UnitAction(Enum):
    WAIT = auto()
    SETTLE = auto()
    BUILD_FARM = auto()
    BUILD_MINE = auto()