import unittest
from src.main.timer import Timer

class TestTimer(unittest.TestCase):
    def setUp(self):
        self.timer = Timer()

    def test_tick(self):
        self.timer.set_pomodoros(1)
        self.assertEqual(self.timer.get_time_remaining(), "25:00")
        self.timer.tick()
        self.assertEqual(self.timer.get_time_remaining(), "24:59")

    def test_state_transition(self):
        self.timer.set_pomodoros(2)
        self.assertEqual(self.timer.get_current_state(), "pomodoro")
        self.timer.time_remaining = 0
        self.timer.tick()
        self.assertEqual(self.timer.get_current_state(), "short_break")
        self.timer.time_remaining = 0
        self.timer.tick()
        self.assertEqual(self.timer.get_current_state(), "pomodoro")

if __name__ == "__main__":
    unittest.main()