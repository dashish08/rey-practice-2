import unittest
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # setUp запускается перед каждым тестом
        self.manager = TaskManager()

    def test_add_task_returns_id(self):
        self.assertEqual(self.manager.add_task("Запустить процессор"), 1)
        self.assertEqual(self.manager.add_task("Включить монитор"), 2)

    def test_add_empty_task_raises(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")

    def test_complete_task(self):
        task_id = self.manager.add_task("Открыть вкладку")
        self.manager.complete_task(task_id)
        self.assertTrue(self.manager.get_tasks()[0]["done"])

    def test_remove_task(self):
        task_id = self.manager.add_task("Лишняя задача")
        self.manager.remove_task(task_id)
        self.assertEqual(self.manager.get_tasks(), [])

    def test_remove_unknown_task_raises(self):
        with self.assertRaises(KeyError):
            self.manager.remove_task(999)

    def test_get_tasks_filter(self):
        first = self.manager.add_task("Первая")
        self.manager.add_task("Вторая")
        self.manager.complete_task(first)
        self.assertEqual(len(self.manager.get_tasks()), 2)
        self.assertEqual(len(self.manager.get_tasks(done=True)), 1)
        self.assertEqual(len(self.manager.get_tasks(done=False)), 1)

    """def test_deliberately_failing(self):
        # специально неверный тест(ожидание 3 задач)
        self.manager.add_task("Первая")
        self.manager.add_task("Вторая")
        self.assertEqual(len(self.manager.get_tasks()), 2)"""


if __name__ == "__main__":
    unittest.main()
