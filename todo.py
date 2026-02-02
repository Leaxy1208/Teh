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

