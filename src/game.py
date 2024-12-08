class Game:
    __rolls = [0] * 21
    __current_roll = 0

    def roll(self, pins: int) -> None:
        self.__rolls[self.__current_roll] = pins
        self.__current_roll += 1

    def score(self) -> int:
        score = 0
        frame_index = 0
        for frame in range(0, 10):
            if self.__rolls[frame_index] + self.__rolls[frame_index + 1] == 10:  # spare
                score += 10 + self.__rolls[frame_index + 2]
                frame_index += 2
            else:
                score += self.__rolls[frame_index] + self.__rolls[frame_index + 1]
                frame_index += 2
        return score
