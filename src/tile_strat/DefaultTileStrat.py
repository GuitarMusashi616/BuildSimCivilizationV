# pyright: strict

from typing import List
from tile.Tile import Tile
from tile_strat.IPickTileStrat import IPickTileStrat


class DefaultTileStrat(IPickTileStrat):
    def pick_tiles(self, tiles: List[Tile], how_many: int) -> List[int]:
        """Given the tiles that make up the city and how many citizens to work, return the indices of the tiles to work"""
        assert how_many <= len(tiles), "not enough tiles to pick that many"
        assert len(tiles) > 1, "must pick between at least 2 tiles"

        tile_copy = [(i+1, x) for i,x in enumerate(tiles[1:])]
        tile_copy.sort(key=lambda ix: ix[1].output.food + ix[1].output.prod, reverse=True)

        return [0] + [i for i,_ in tile_copy[:how_many]]

