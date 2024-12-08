class Game:
    __score = 0

    def roll(self, pins):
        self.__score += pins

    def score(self):
        return self.__score
