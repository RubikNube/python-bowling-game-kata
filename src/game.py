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
            if self.is_strike(frame_index):
                score += 10 + self.strike_bonus(frame_index)
                frame_index += 1
            elif self.is_spare(frame_index):
                score += 10 + self.spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self.__rolls[frame_index] + self.__rolls[frame_index + 1]
                frame_index += 2
        return score

    def is_strike(self, frame_index: int) -> bool:
        return self.__rolls[frame_index] == 10

    def strike_bonus(self, frame_index: int) -> int:
        return self.__rolls[frame_index + 1] + self.__rolls[frame_index + 2]

    def is_spare(self, frame_index: int) -> bool:
        return self.__rolls[frame_index] + self.__rolls[frame_index + 1] == 10

    def spare_bonus(self, frame_index: int) -> int:
        return self.__rolls[frame_index + 2]
