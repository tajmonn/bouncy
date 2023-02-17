import json

f = open("configs/settings.json")
data = json.load(f)
ball_settings = data["BALL"]
frame_settings = data["FRAME"]
game_settings = data["GAME"]
print(ball_settings, frame_settings, game_settings)
