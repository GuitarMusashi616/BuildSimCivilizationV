# pyright: basic

import abc

class IQueue(abc.ABC):
    def get_name(self) -> str: # type: ignore
        """Gets the name of what is being queued up"""

    def get_hammers_req(self) -> int: # type: ignore
        """Returns how many production hammers total to produce this"""

