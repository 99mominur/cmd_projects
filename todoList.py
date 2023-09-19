import uuid
from datetime import datetime, date


class Task:
    tasks = {}

    def update_task(self, name, task_no, updated_time):
        self.name = name
        self.task_no = task_no
        self.update_time = updated_time
        for key, value in self.tasks.items():
            self.task_no -= 1
            if self.task_no == 0:
                self.tasks[key][0] = self.name
                self.tasks[key][2] = self.update_time
                print("Task Updated Succesfully")
                break

    def complete_task(self, task_no, completed_time):
        self.task_no = task_no
        self.completed_time = completed_time
        for key, value in self.tasks.items():
            self.task_no -= 1
            if self.task_no == 0:
                self.tasks[key][3] = True
                self.tasks[key][4] = self.completed_time
                print("Task Completed Succesfully")
                break


fields = {
    1: "Add New Task",
    2: "Show All Task",
    3: "Show Incomplete Tasks",
    4: "Show Complete Tasks",
    5: "Update Task",
    6: "Mark A Task Completed"
}

todo = Task()

def new_task():
    print()
    id = uuid.uuid1()
    name = input("Enter New Task: ")
    now_time = datetime.now().strftime("%H:%M:%S")
    now_date = date.today().strftime("%d/%m/%Y")
    created_time = f"{now_date} {now_time}"
    updated_time = "NA"
    completed = False
    completed_time = "NA"
    task = [name, created_time, updated_time, completed, completed_time]
    todo.tasks[id] = task
    print()
    print("Task Created Successfully")


def all_task():
    print()
    flag = False
    for key, value in todo.tasks.items():
        flag = True
        print()
        print(f"ID - {key}")
        print(f"Task - {value[0]}")
        print(f"Created time - {value[1]}")
        print(f"Updated time - {value[2]}")
        print(f"Completed - {value[3]}")
        print(f"Completed time - {value[4]}")

    if flag == False:
        print("No Task Added Yet")


def incomplete_tasks():
    print()
    flag = False
    for key, value in todo.tasks.items():
        if value[3] == False:
            flag = True
            print()
            print(f"ID - {key}")
            print(f"Task - {value[0]}")
            print(f"Created time - {value[1]}")
            print(f"Updated time - {value[2]}")
            print(f"Completed - {value[3]}")
            print(f"Completed time - {value[4]}")
    if flag == False:
        print("No Incompleted Task")


def complete_tasks():
    print()
    flag = False
    for key, value in todo.tasks.items():
        if value[3] == True:
            flag = True
            print()
            print(f"ID - {key}")
            print(f"Task - {value[0]}")
            print(f"Created time - {value[1]}")
            print(f"Updated time - {value[2]}")
            print(f"Completed - {value[3]}")
            print(f"Completed time - {value[4]}")
    if flag == False:
        print("No Completed Task")


def update_task():
    print()
    print("Select Which Task To Update")
    serial_no = 1
    flag = False
    for key, value in todo.tasks.items():
        if value[2] == "NA":
            flag = True
            print()
            print("Task NO - ", serial_no)
            serial_no += 1
            print(f"ID - {key}")
            print(f"Task - {value[0]}")
            print(f"Created time - {value[1]}")
            print(f"Updated time - {value[2]}")
            print(f"Completed - {value[3]}")
            print(f"Completed time - {value[4]}")
    if flag == False:
        print()
        print("No Task To Update")
        return
    print()
    task_no = int(input("Enter Task No: "))
    name = input("Enter New Task: ")
    now_time = datetime.now().strftime("%H:%M:%S")
    now_date = date.today().strftime("%d/%m/%Y")
    updated_time = f"{now_date} {now_time}"
    todo.update_task(name, task_no, updated_time)


def mark_completed():
    print()
    print("Select Which Task To Complete")
    serial_no = 1
    flag = False
    for key, value in todo.tasks.items():
        if value[3] == False:
            flag = True
            print()
            print("Task NO - ", serial_no)
            serial_no += 1
            print(f"ID - {key}")
            print(f"Task - {value[0]}")
            print(f"Created time - {value[1]}")
            print(f"Updated time - {value[2]}")
            print(f"Completed - {value[3]}")
            print(f"Completed time - {value[4]}")
    if flag == False:
        print()
        print("No Task To Complete")
        return
    print()
    task_no = int(input("Enter Task No: "))
    now_time = datetime.now().strftime("%H:%M:%S")
    now_date = date.today().strftime("%d/%m/%Y")
    completed_time = f"{now_date} {now_time}"
    todo.complete_task(task_no, completed_time)


if __name__ == "__main__":
    while True:
        print()
        for key, value in fields.items():
            print(f"{key}. {value}")
        data = input("Enter Option: ")
        if data == '1':
            new_task()
        elif data == '2':
            all_task()
        elif data == '3':
            incomplete_tasks()
        elif data == '4':
            complete_tasks()
        elif data == '5':
            update_task()
        elif data == '6':
            mark_completed()
