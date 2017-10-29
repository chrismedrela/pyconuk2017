import unittest

from bowling_game import BowlingGame

class BowlingGameTests(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    # def tearDown(self):
    #     del self.game

    def roll_many(self, pins, rolls):
        for _ in range(rolls):
            self.game.roll(pins)

    def roll_spare(self):
        self.game.roll(5)
        self.game.roll(5)

    def roll_strike(self):
        self.game.roll(10)

    def test_when_all_throws_in_gutter_then_score_should_be_zero(self):
        self.roll_many(pins=0, rolls=20)
        self.assertEqual(self.game.score(), 0)

    def test_when_no_bonus_then_score_should_be_sum_of_pins(self):
        self.roll_many(pins=2, rolls=20)
        self.assertEqual(self.game.score(), 20*2)

    def test_when_spare_then_next_roll_is_counted_twice(self):
        self.roll_spare()
        self.roll_many(pins=2, rolls=18)
        self.assertEqual(self.game.score(), 10 + 2 + 18*2)

    def test_when_strike_then_two_next_rolls_are_counted_twice(self):
        self.roll_strike()
        self.roll_many(pins=2, rolls=18)
        self.assertEqual(self.game.score(), 10 + 4 + 18*2)

    def test_perfect_game(self):
        self.roll_many(pins=10, rolls=12)
        self.assertEqual(self.game.score(), 300)
