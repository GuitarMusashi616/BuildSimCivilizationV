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

## Game Speed
- Quick is 150% faster
  - requires 10 pop to grow rather than 15 (divide by 1.5)

## Damage mechanics unaccounted for
- How do cities take damage?
- Do they regenerate 20 HP/turn for a 200 HP town and 22 HP/turn for a 250 HP town?
- CS gets boosted by flat 0.5 for every population?
- How does garrisoned unit affect city combat strength
- If 3 catapults roll up to a city with a garrison, how many turns until the city goes down or does the city wipe out the catapults?
  - In the above scenario assume that their army has been defeated first
  - or see what it would take to slow them down with melee fortify units, how long would you have to stall their army to take the city?

## City seige use
- How many turns*catapults needed, eg 3 means 3 turns with 1 catapult or 3 catapults 1 turn
- How long does a catapult last, eg 2 means each catapult with last 2 volleys when focused by the city (need to include garrison of soldier vs archer and if within melee range)


## How caravans work

### Domestic trade routes
- 4 food / prod for land route
- 8 food / prod for sea route
- + 0.5 food for each age advancement starting at renaissance



## Try all paths through social policies and technologies?


## Try all paths to get fastest army up ancient era

### Given the following
- a single settler
- sets of tiles where civilization will grow
- ability to produce settlers (past pop 1)
- ability to produce workers and improve tiles

### determine
- how fast you can grow a population to max happiness
- fastest way to get max hammers for an amount of civ tiles


## Using id, repo, command_handler patterns
- can have any objects interacting with each other
- SettleUnit -> DeleteUnit and SpawnCity
- what commands to min max

- make builds and test them
- test options every step of the way
- maybe limit build orders so that build has to finish

- tradeoff between settle distance and resources (hard to brute force settling options)

- tradeoff between buying army or training an army?
- what about getting the AI to war with enemy?



