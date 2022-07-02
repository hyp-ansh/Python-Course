import requests
pokemon = input("Name the Pokemon -> ")
move = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
status = move.ok
if status == True:
    rw = f"https://some-random-api.ml/pokedex?pokemon={pokemon}"
    img = requests.get(f"https://api.pokemontcg.io/v1/cards?name={pokemon}")
    lol = img.json()
    #print(lol)
    img_url = lol["cards"][0]["imageUrlHiRes"]
    r = requests.get(rw)
    a = r.json()
    name = a["name"].upper()
    typ = a["type"]
    species = a["species"]
    abilities = a["abilities"]
    height = a["height"]
    weight = a["weight"]
    esatge = r.json()["family"]["evolutionStage"]
    try:
        weaknesses = lol["cards"][0]["weaknesses"][0]["type"]
    except BaseException:
        weaknesses = None
    l = r.json()["family"]["evolutionLine"]
    # ambiguous variable name 'l' flake8(E741)
    if not l:
        line = "None"
    else:
        line = ", ".join(map(str, l))
    gen = a["generation"]
    try:
        move1 = move.json()["moves"][0]["move"]["name"]
    except IndexError:
        move1 = None
    try:
        move2 = move.json()["moves"][1]["move"]["name"]
    except IndexError:
        move2 = None
    try:
        move3 = move.json()["moves"][2]["move"]["name"]
    except IndexError:
        move3 = None
    try:
        move4 = move.json()["moves"][3]["move"]["name"]
    except IndexError:
        move4 = None
    try:
        move5 = move.json()["moves"][4]["move"]["name"]
    except IndexError:
        move5 = None
    try:
        move6 = move.json()["moves"][5]["move"]["name"]
    except IndexError:
        move6 = None
    try:
        move7 = move.json()["moves"][6]["move"]["name"]
    except IndexError:
        move7 = None
    description = a["description"]
    typ = ", ".join(map(str, typ))
    Stats = a["stats"]
    species = ", ".join(map(str, species))
    abilities = ", ".join(map(str, abilities))
    cap = f"""\n\n
NAME : {name}
TYPE : {typ}
SPECIES : {species}
Evolution Line : {line}
Evolution Stage : {esatge}
Generation : {gen}

ABILITIES : {abilities}
WEAKNESSES :{weaknesses}
HEIGHT : {height}
WEIGHT : {weight}

    Stats                               Moves
Hp      : {Stats['hp']}               (1){move1}
Attack  : {Stats['attack']}           (2){move2}
Defense : {Stats['defense']}          (3){move3}
Sp_atk  : {Stats['sp_atk']}           (4){move4}
Sp_def  : {Stats['sp_def']}           (5){move5}
Speed   : {Stats['speed']}            (6){move6}
Total   : {Stats['total']}            (7){move7}

DESCRIPTION : {description}
"""
    print(cap)
else:
    print("\n\n                  [Name of pokemon is invalid]\n\n")
