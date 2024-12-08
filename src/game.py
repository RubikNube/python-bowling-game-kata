class Game:
    __score = 0

    def roll(self, pins: int) -> None:
        self.__score += pins

    def score(self) -> int:
        return self.__score
