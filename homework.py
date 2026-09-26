game = {

    "title": "Minecraft",

    "players": 2,

    "genre": "adventure",

}

print(game)

print(game.keys())

print(game.values())

print(game["genre"])

print(game["title"])

for key in game.keys():

    print(key,":",game[key])

if "score" in game:

    print("yes")

else:

    print("no")

game["difficulty"] = "hard"

del(game["players"])

print(game)

difficulty = input("What is your favorite difficulty?")

game["difficulty"] = difficulty

print(game)

game["scores"] = [100, 250, 175, 300, 225]

print(game)

print(game["scores"][4])