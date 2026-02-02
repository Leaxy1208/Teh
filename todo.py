tasks = []

# 1. Функция добавления (add: приоритет)
def add_task(text, priority="средний"):
    task = {
        "text": text, 
        "priority": priority, 
        "is_done": False
    }
    tasks.append(task)
    print(f"Добавлено: {text} (Приоритет: {priority})")

# 2. Функция отображения (refresh)
def show_tasks():
    print("\nВаш список дел:")
    for i, task in enumerate(tasks, 1):
        status = "[V]" if task["is_done"] else "[ ]"
        print(f"{i}. {status} {task['text']} | Приоритет: {task['priority']}")

# 3. Функция отметки выполненной задачи (add)
def mark_complete(number):
    if 0 < number <= len(tasks):
        tasks[number - 1]["is_done"] = True
        print(f"Задача №{number} выполнена!")
    else:
        print("Ошибка: задачи с таким номером нет.")

# 4. Функция удаления
def delete_task(number):
    if 0 < number <= len(tasks):
        removed = tasks.pop(number - 1)
        print(f"Удалено: {removed['text']}")
    else:
        print("Ошибка: задачи с таким номером нет.")

# Тесты
add_task("Изучить Git", "высокий")
add_task("Сходить в магазин", "низкий")
show_tasks()

mark_complete(1) # Отмечаем первую задачу
show_tasks()

delete_task(2)   # Удаляем вторую задачу
show_tasks()
