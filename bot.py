import json

def showStats():
  # Checks userID and matches it to their account, then loops to print all the information
  with open("source.json", "r") as file:
    source = json.load(file)
  Players = source["Players"]["Registered"]
  response = []
  for number, players in Players.items():
    for stats, values in players.items():
      response.append(f"{stats}: {values}")
      format_response = '\n'.join(response)
  return format_response

print(showStats())