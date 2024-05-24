# Pokémon Data Scraper (Generation 1)
### Overview
- In this demonstration project, Python and the Selenium package were used to collect data on Generation 1 Pokémon from the [National Pokédex](https://pokemondb.net/pokedex/national). The Python script collected various details about each Pokémon, including their name, national number, type, species, height, weight, base stats, minimum stats, maximum stats, and entry. Then, the data was saved in CSV. 

### Requirements
- Required Python package
	- selenium
	- pandas
- A web driver compatible with Selenium e.g. `geckodriver` for FireFox

### Data Field
#### Characteristics of Pokémon
The following fields are saved in `pokemon_demo.csv`
- `name`: The name of the Pokémon
- `national_number`: The official Pokédex number for the Pokémon
- `type1` & `type2`: The elemental type(s) of the Pokémon (e.g., Fire, Water, Grass)
- `species`: The category or species of the Pokemon.
- `height`: The height of the Pokémon in meters.
- `weight`: The weight of the Pokémon in kilograms.
- `base_hp`, `base_attack`, `base_defense`, `base_sp_attack`, `base_sp_defence`, `base_speed`: Base stats
- `min_hp`, `min_attack`, `min_defense`, `min_sp_attack`, `min_sp_defence`, `min_speed`: Minimum stats
- `max_hp`, `max_attack`, `max_defense`, `max_sp_attack`, `max_sp_defence`, `max_speed`: Maximum stats
- `image_url`: URL of the image of the Pokémon
- `url`: Webpage of the data 
#### Description of Pokémon
The following fields are saved in the file `pokemon_pokedox_entry.csv`
- `national_number`: The official Pokédex number for the Pokémon
- `version`: Version of game
- `description`: Description of the Pokémon

