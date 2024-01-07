import time

while True:
    with open("game.log", "r") as file:
        print(file.read())
    time.sleep(1)
