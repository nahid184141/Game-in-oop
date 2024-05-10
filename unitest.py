import unittest
from snakegame import GameManager, Snake, Food  

class TestGameManager(unittest.TestCase):
    def test_singleton_instance(self):
        instance1 = GameManager.get_instance()
        instance2 = GameManager.get_instance()
        self.assertIs(instance1, instance2)

    def test_game_initialization(self):
        manager = GameManager.get_instance()
        self.assertEqual(len(manager.objects), 2)
        self.assertIsInstance(manager.objects[0], Snake)
        self.assertIsInstance(manager.objects[1], Food)

    def test_score_increment(self):
        manager = GameManager.get_instance()
        initial_score = manager.score
        manager.score += 10  # Assume food is worth 10 point
        self.assertEqual(manager.score, initial_score + 10)

if __name__ == '__main__':
    unittest.main()

# unittest