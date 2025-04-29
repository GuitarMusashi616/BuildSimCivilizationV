# pyright: strict

from typing import Tuple
from core.Coord import Coord
from tile.FeatureType import FeatureType
from tile.ITile import ITile
from tile.ImprovementType import ImprovementType
from tile.ResourceType import ResourceType
from tile.TerrainType import TerrainType
from tile.TileOutput import TileOutput

class TileFeature(ITile):
    def __init__(self, coord: Coord, terrain: TerrainType, resource: ResourceType = ResourceType.NONE, feature: FeatureType = FeatureType.NONE, improvement: ImprovementType = ImprovementType.NONE, is_worked: bool = False, has_city: bool = False):
        self.terrain = terrain
        self._resource = resource
        self.feature = feature
        self._improvement = improvement

        self._coord = coord
        self._is_worked = is_worked
        self._has_city = has_city
        self.yield_change = TileOutput(0, 0, 0, 0, 0, 0)

    @property
    def is_worked(self) -> bool:
        return self._is_worked

    @is_worked.setter
    def is_worked(self, value: bool):
        self._is_worked = value

    @property
    def has_city(self) -> bool:
        return self._has_city

    @has_city.setter
    def has_city(self, value: bool):
        self._has_city = value

    @property
    def coord(self) -> Coord:
        return self._coord
    
    @property
    def output(self) -> TileOutput:
        output = self.get_base_stats()

        if self.resource != ResourceType.NONE:
            output += self.get_resource_stats()

        if self.improvement != ImprovementType.NONE:
            output += self.get_improvement_stats()

        if self.has_city:
            output = output.set_minimum(TileOutput.minimum_if_tile_has_city())

        return output
    
    @property
    def resource(self) -> ResourceType:
        return self._resource
    
    @property
    def improvement(self) -> ImprovementType:
        return self._improvement
    
    @improvement.setter
    def improvement(self, value: ImprovementType):
        self._improvement = value
    
    def add_yield_change(self, output: TileOutput):
        self.yield_change += output
    
    def get_base_stats(self) -> TileOutput:
        """Base tile stats"""
        tup = self._get_base_stats_tuple()
        return TileOutput(tup[0], tup[1], tup[2], 0, 0, 0)
    
    def get_resource_stats(self) -> TileOutput:
        output = TileOutput(0, 0, 0, 0, 0, 0)
        if self.resource in {ResourceType.RESOURCE_IRON, ResourceType.RESOURCE_HORSE, ResourceType.RESOURCE_COAL, ResourceType.RESOURCE_OIL, ResourceType.RESOURCE_ALUMINUM, ResourceType.RESOURCE_URANIUM, ResourceType.RESOURCE_STONE}:
            output += TileOutput(0, 1, 0, 0, 0, 0)
        
        if self.resource in {ResourceType.RESOURCE_WHEAT, ResourceType.RESOURCE_COW, ResourceType.RESOURCE_SHEEP, ResourceType.RESOURCE_DEER, ResourceType.RESOURCE_BANANA, ResourceType.RESOURCE_FISH, ResourceType.RESOURCE_WHALE}:
            output += TileOutput(1, 0, 0, 0, 0, 0)

        if self.resource in {ResourceType.RESOURCE_PEARLS, ResourceType.RESOURCE_GOLD, ResourceType.RESOURCE_SILVER, ResourceType.RESOURCE_MARBLE, ResourceType.RESOURCE_IVORY, ResourceType.RESOURCE_FUR, ResourceType.RESOURCE_DYE, ResourceType.RESOURCE_SPICES, ResourceType.RESOURCE_SILK, ResourceType.RESOURCE_SUGAR, ResourceType.RESOURCE_COTTON, ResourceType.RESOURCE_WINE, ResourceType.RESOURCE_INCENSE}:
            output += TileOutput(0, 0, 2, 0, 0, 0)
        
        if self.resource == ResourceType.RESOURCE_WHALE:
            output += TileOutput(0, 0, 1, 0, 0, 0)

        if self.resource == ResourceType.RESOURCE_GEMS:
            output += TileOutput(0, 0, 3, 0, 0, 0)

        return output
    
    def get_improvement_stats(self) -> TileOutput:
        output = TileOutput(0, 0, 0, 0, 0, 0)
        if self.improvement in {ImprovementType.IMPROVEMENT_MINE, ImprovementType.IMPROVEMENT_LUMBERMILL}:
            output += TileOutput(0, 1, 0, 0, 0, 0)
        
        if self.improvement == ImprovementType.IMPROVEMENT_FARM:
            output += TileOutput(1, 0, 0, 0, 0, 0)
        
        if self.improvement == ImprovementType.IMPROVEMENT_TRADING_POST:
            output += TileOutput(0, 0, 1, 0, 0, 0)

        if self.improvement == ImprovementType.IMPROVEMENT_ACADEMY:
            output += TileOutput(0, 0, 0, 0, 8, 0)

        if self.improvement == ImprovementType.IMPROVEMENT_CUSTOMS_HOUSE:
            output += TileOutput(0, 0, 4, 0, 0, 0)

        if self.improvement == ImprovementType.IMPROVEMENT_MANUFACTORY:
            output += TileOutput(0, 4, 0, 0, 0, 0)
        
        return output
    
    def _get_base_stats_tuple(self) -> Tuple[int, int, int]:
        # feature
        if self.feature == FeatureType.FEATURE_ICE:
            return (0, 0, 0)
        
        if self.feature == FeatureType.FEATURE_MARSH:
            return (1, 0, 0)
        
        if self.feature == FeatureType.FEATURE_FOREST:
            return (1, 1, 0)

        if self.feature == FeatureType.FEATURE_JUNGLE:
            return (2, 0, 0)

        if self.feature == FeatureType.FEATURE_ATOLL:
            return (2, 1, 0)

        if self.feature == FeatureType.FEATURE_FLOOD_PLAINS:
            return (2, 0, 0)

        if self.feature == FeatureType.FEATURE_OASIS:
            return (3, 0, 1)
        
        # aquatic
        if self.terrain == TerrainType.TERRAIN_COAST:
            return (1, 0, 0)
        
        if self.terrain == TerrainType.TERRAIN_OCEAN:
            return (1, 0, 0)

        if self.terrain == TerrainType.TERRAIN_DESERT:
            return (0, 0, 0)

        if self.terrain == TerrainType.TERRAIN_MOUNTAIN:
            return (0, 0, 0)

        if self.terrain == TerrainType.TERRAIN_HILL:
            return (0, 2, 0)

        if self.terrain == TerrainType.TERRAIN_GRASS:
            return (2, 0, 0)

        if self.terrain == TerrainType.TERRAIN_PLAINS:
            return (1, 1, 0)

        if self.terrain == TerrainType.TERRAIN_TUNDRA:
            return (1, 0, 0)

        if self.terrain == TerrainType.TERRAIN_SNOW:
            return (0, 0, 0)

        return (0, 0, 0)
        
    
    def __repr__(self):
        out =  f"{self.terrain} @ {self.coord}"
        if self.resource != ResourceType.NONE:
            out += f" with {self.resource}"
        if self.feature != FeatureType.NONE:
            out += f" and {self.feature}"
        if self.improvement != ImprovementType.NONE:
            out += f" and {self.improvement}"
        return out

    