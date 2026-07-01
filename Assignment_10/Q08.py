class Player:
    def __init__(self, name, score, level):
        self.name = name
        self.score = score
        self.level = level

    def increase_score(self, points):
        self.score += points
        print("Score increased by", points, "→ New Score:", self.score)

    def level_up(self):
        self.level += 1
        print("Level Up! Current Level:", self.level)

    def show_progress(self):
        print("Player:", self.name)
        print("Score:", self.score)
        print("Level:", self.level)
        print("-------------------")

player1 = Player("Vedant", 0, 1)

player1.show_progress()
player1.increase_score(50)
player1.show_progress()
player1.level_up()
player1.show_progress()
player1.increase_score(100)
player1.level_up()
player1.show_progress()


