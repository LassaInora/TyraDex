import Tyradex

pokemon = Tyradex.Pokemon.get(801)
print(f"{pokemon.name} :\n\tFrench: {pokemon.name.fr}\n\tJapan : {pokemon.name.jp}")

# Get the Pokémon N°801.
pokemon = Tyradex.Pokemon.get(801)
# Show its French name and its Japan name.
print("The French name and Japan name of Pokémon number 801 :", pokemon.name.fr, '->', pokemon.name.jp)

# Get the Pokémon N°0.
pokemon = Tyradex.Pokemon.get(0)
# Show its shiny sprite.
print("The shiny sprite of Pokemon number 0 (MissingNo.) :", pokemon.sprites.shiny)

# Get the 6th Gen.
gen = Tyradex.Generation.get(6)
# Show the 42th new Pokémon.
print("The 42th Pokémon of Gen 6 :", gen.pokemons[42].name)

# Get the type N°5.
type_ = Tyradex.Type.get(5)
# Show its 7th Pokémon.
print("The 7th Pokémon of type 5 :", type_.pokemons[7].name)

# Get the double type N°5 and N°7.
type__ = Tyradex.Type.get(5, 7)
# Show its 1st Pokémon.
print("The 1st Pokémon of type 5 and 7 :", type_.pokemons[0].name)

# Get Pikachu
pika = Tyradex.Pokemon.get('Pikachu')
# Show the Pokedex ID of Pikachu.
print("The Pokedex ID of Pikachu :", pika.pokedex_id)

# Get the 8th Gen.
gen8 = Tyradex.Generation.get(8)
# Show how many new Pokémon this gen have.
print(gen8.to_ - gen8.from_, "new Pokemon in Gen 8.")
