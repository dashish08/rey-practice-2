__version__ = "1.0.0"


# хранит список задач в памяти и позволяет им управлять
class TaskManager:

    def __init__(self):
        self._tasks = []
        self._next_id = 1

    # добавляет задачу и возвращает её номер (id)
    def add_task(self, title):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Название задачи не может быть пустым")
        task = {"id": self._next_id, "title": title.strip(), "done": False}
        self._tasks.append(task)
        self._next_id += 1
        return task["id"]

    # удаляет задачу по номеру
    def remove_task(self, task_id):
        self._tasks.remove(self._find(task_id))

    # отмечает задачу выполненной
    def complete_task(self, task_id):
        self._find(task_id)["done"] = True

    # возвращает задачи: все, только выполненные (True) или невыполненные (False)
    def get_tasks(self, done=None):
        return [dict(t) for t in self._tasks if done is None or t["done"] == done]

    def _find(self, task_id):
        for task in self._tasks:
            if task["id"] == task_id:
                return task
        raise KeyError(f"Задача с id={task_id} не найдена")
