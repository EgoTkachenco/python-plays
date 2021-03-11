import os
import json
os.system('cls')

class TODO:
    def __init__(self):
        self.tasks = []

    def getTasksFromFile(self):
        with open('data.json') as json_file:
            data = json.load(json_file)
            self.tasks = data
            print('tasks loaded')
    
    def saveTasksToFile(self):
        with open('data.json', 'w') as json_file:
            json.dump(self.tasks, json_file)
            print('tasks loaded')
    
    def showTodoList(self):
        os.system('cls')
        for i in range(len(self.tasks)):
            print(str(i + 1) + '. ' + self.tasks[i])
        key = input('')
        self.printMenu()       

    def printError(msg):
        print(msg)
        key = input()
        self.printMenu()

    def addTodo(self):
        os.system('cls')
        newTask = input('Enter new task: ')
        self.tasks.append(newTask)
        self.saveTasksToFile()
        os.system('cls')
        print('Task Saved')
        key = input('')
        self.printMenu()

    def removeTodo(self):
        os.system('cls')
        for i in range(len(self.tasks)):
            print(str(i + 1) + '. ' + self.tasks[i])
        try:
            key = int(input('Enter task number: '))
        except:
            self.printError('Invalid number')

        if key < 1 or key > len(self.tasks) + 1:
            self.printError('Invalid number')
        else:
            self.tasks.pop(key - 1)
            self.saveTasksToFile()
            os.system('cls')
            print('Task removed')
            key = input('')
            self.printMenu()

    def todoAction(self, key):
        if key == 1:
            self.showTodoList()
        elif key == 2:
            self.addTodo()
        elif key == 3:
            self.removeTodo()
        elif key == 4:
            print('Close Program')
            return

    def printMenu(self):
        os.system('cls')
        print('---MENU---')
        print('1. Show Todo List')
        print('2. Add Task')
        print('3. Remove Task')
        print('4. Exit')
        try:
            key = int(input());
        except:
            self.printMenu()
        if key < 1 or key > 4:
            self.printMenu();
        else:
            self.todoAction(key)



todo = TODO()
todo.getTasksFromFile()
todo.printMenu()
