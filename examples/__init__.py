import Tyradex

print(Tyradex)

# Get the Pokémon N°801.
pokemon = Tyradex.Pokemon.get(801)
# Show its French name and its Japan name.
print(pokemon.name.fr, '->', pokemon.name.jp)

# # Get the 6th Gen.
# gen = Tyradex.Generation.get(6)
# # Show the 42th new Pokémon.
# print(gen.pokemons[42].name)
#
# # Get the type n°5.
# type_ = Tyradex.Type.get(5)
# # Show its 7th Pokémon.
# print(gen.pokemons[7].name)
#
# # Get the double type 5 and 7.
# type__ = Tyradex.Type.get(5, 7)
# # Show its 1st Pokémon.
# print(gen.pokemons[0].name)
#
# # Get Pikachu
# pika = Tyradex.Pokemon.get('Pikachu')
# # Show the Pokedex ID of Pikachu.
# print(pika.pokedex_id)
#
# # Get the 8th Gen.
# gen8 = Tyradex.Generation.get(8)
# # Show how many new Pokémon this gen have.
# print(gen8.to_ - gen8.from_)