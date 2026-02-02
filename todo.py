tasks = []

def add_task(text):
    tasks.append(text)
    print(f"Добавлено: {text}")

# Тест функции
add_task("Изучить Git")

def show_tasks():
    print("\nВаш список дел:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Тест
show_tasks()

def delete_task(number):
    if 0 < number <= len(tasks):
        removed = tasks.pop(number - 1)
        print(f"Удалено: {removed}")
    else:
        print("Ошибка: задачи с таким номером нет.")

# Тест
delete_task(1)
show_tasks()

def mark_complete(number):
    if 0 < number <= len(tasks):
        tasks[number-1] = f"[V] {tasks[number-1]}"
        print(f"Задача №{number} отмечена как выполненная!")
    else:
        print("Ошибка: задачи с таким номером не существует.")