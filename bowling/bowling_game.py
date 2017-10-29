# Test Driven Development - iterations:

# 1. Write the simplest failing test
# 2. Write the simplest production code that passes all tests
# 3. Refactor both production code and tests, if necessary.

class BowlingGame(object):
    FRAMES_IN_GAME = 10
    NUMBER_OF_PINS = 10

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total = 0
        frame_start_index = 0
        for _ in range(self.FRAMES_IN_GAME):
            first_roll = self.rolls[frame_start_index]
            is_strike = first_roll == self.NUMBER_OF_PINS
            if is_strike:
                rolls_in_frame = 1
                frame_sum = first_roll
                next_roll = self.rolls[frame_start_index+1]
                next_next_roll = self.rolls[frame_start_index+2]
                bonus = next_roll + next_next_roll 
            else:
                rolls_in_frame = 2
                second_roll = self.rolls[frame_start_index+1]
                frame_sum = first_roll + second_roll
                is_spare = frame_sum == self.NUMBER_OF_PINS
                if is_spare:
                    next_roll = self.rolls[frame_start_index+2]
                    bonus = next_roll
                else:
                    bonus = 0
            total += frame_sum + bonus
            frame_start_index += rolls_in_frame
        return total