# pyright: strict

from typing import List
from core.Coord import Coord
from map.IMap import IMap
from tile.ITile import ITile
from tile.ResourceType import ResourceType


class MapHelper:
    city_tiles_offset = [
        (0, 0),
        (0, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, 1),

        (-1, 2),
        (0, 2),
        (1, 1),
        (2, 0),
        (2, -1),
        (2, -2),
        (1, -2),
        (0, -2),
        (-1, -1),
        (-2, 0),
        (-2, 1),
        (-2, 2),

        (-1, 3),
        (0, 3),
        (1, 2),
        (2, 1),
        (3, 0),
        (3, -1),
        (3, -2),
        (3, -3),
        (2, -3),
        (1, -3),
        (0, -3),
        (-1, -2),
        (-2, -1),
        (-3, 0),
        (-3, 1),
        (-3, 2),
        (-3, 3),
        (-2, 3),
    ]

    @staticmethod
    def get_city_tiles(map: IMap, center: Coord) -> List[ITile]:
        """Returns the clockwise order of tiles from the map starting from the middle"""
        output: List[ITile] = []
        for xoff,yoff in MapHelper.city_tiles_offset:
            coord = center + Coord(xoff, yoff)
            output.append(map.get_tile(coord))
        return output

    @staticmethod
    def find_coord(map: IMap, hitlist: List[ResourceType]):
        """Returns where you are on the map given the neighboring tiles"""
        width, height = map.get_width_height()
        found_so_far = 0
        # hitlist = [ResourceType.RESOURCE_MARBLE, ResourceType.NONE, ResourceType.RESOURCE_BANANA, ResourceType.NONE, ResourceType.NONE]
        finds: List[ITile] = []


        for h in range(height):
            for w in range(width):
                # needle = tile(w, h)
                needle = map.get_tile(Coord(w, h))
                # assert isinstance(needle, TileFeature)
                if needle.resource == hitlist[found_so_far]:
                    found_so_far += 1
                    print(f"Found {found_so_far} so far: {needle}")
                    finds.append(needle)
                    if found_so_far >= len(hitlist):
                        print("FOUND ALL 5")
                        for find in finds:
                            print(find)
                            found_so_far = 0
                            finds = []
                else:
                    found_so_far = 0
                    finds = []
        
                

        