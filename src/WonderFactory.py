# pyright: basic

from src.Wonder import Wonder


class WonderFactory:
    @staticmethod
    def palace() -> Wonder:
        return Wonder(1, 2.5, 3, 3, 3, 1)