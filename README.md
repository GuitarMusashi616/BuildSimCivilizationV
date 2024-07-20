# civ 5 sim to plan early game


## settling on hill
- 2 prod 2 food

## tile types
- 1 prod 1 food (normal)
- 2 food into 3 food (farmland)
- 2 prod into 3 prod (hill)

## there's a bunch of stuff that cost hammers
- scout 25 hammers
- warrior 45 hammers
- etc

## there's religions that help with hammers


## there's social policies that help with hammers

# Simulator

## Test and configure that babylon early science strat

## Test and configure the zulu impi rush strat

## Test and configure like huns rush strat

## Test and configure like my general 4 city tradition opener


# How to make it work


- Use real maps as an example, predecide what the tiles of the city are in order ie [hill, hill, plains, plains hill, jungle, jungle, oasis, jungle river]
- Then set how many tile benefits for each tile
- Then we got a build order for the city
  - Build order for expansions, and expansion happens a certain number of turns after settler is created
- Social policy build order
- Religion build order?? Can we predict when pantheon will hit? Maybe just the average with x players, although there is a chance you won't get one
  - Hugely affects like if desert panth is used for example
- Choose leader

## What affects what

- Religion affects everything, cities or tiles
- Social policy affects everything, cities
- Leader affects everything
- Just have one config object that has like all the info about the civilization
- If there's a world instance just share it among the civilization objects as a reference


## Running it
- Choose 4 city locations, each with a river and ideally like 2 luxury resources



## Mechanics
- Settling a city gives the tile at least 2 food 1 prod
  - 2 prod hill becomes 2 food 2 prod

- 3 food tile becomes 3 food 1 prod

- Capital City starts with palace

### Happiness
- 3 unhappiness per city
- 1 unhappiness per citizen
- 9 happiness for difficulty level (KING)


## Minimum Viable Product
- Just how long to predict when something will be made

- How long to make 3 composite bowmen?
- How long to test babylon strategy?