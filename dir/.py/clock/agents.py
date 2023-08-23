import valorant

client = valorant.Client('RGAPI-ee17db31-4711-4fc6-8697-3a896bc4ed98')

skins = client.get_chromas()

weapon_skins = []

for skin in skins:
   weapon_skins.append(skin.name)

print("All Valorant weapon skins:")
print(str(weapon_skins).replace("'", '"'))