from enum import Enum, auto

class UnitActionType(Enum):
    WAIT = auto()
    SETTLE = auto()
    BUILD_FARM = auto()
    BUILD_MINE = auto()
    MOVE = auto()