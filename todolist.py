todos = []
while True:
    choice = input("Type add, show or exit: ")
    match choice:
        case 'add':
            todo = input("Entera todo: ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
